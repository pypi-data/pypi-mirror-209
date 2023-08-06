import os, sys
import requests
import time
from typing import Optional, Sequence, Dict
from .utils import generate_uuid


class HTTPClient:
    """The base client for communicating with an overwatch server and it's model registry.

    The client is used to register, patch, delete and infer on models with the overwatch server.

    Attributes:
        ow_server_url (str): The url of the overwatch server.
        model_registry_url (str): The url of the model registry.
        header_payload (Dict[str, str]): The headers for the request.
        inference_timer (List[float]): A list of inference times.
        inference_counter (List[int]): A list of inference counts (number of inputs per inference call).
    """


    def __init__(
        self,
        overwatch_server_url: str = "https://overwatch.distributive.network",
        model_registry_url: str = "https://models.overwatch.distributive.network",
        header_key: str = "ovwatch-secret-key",
    ):
        """
        Initializes the client with the overwatch server url and model registry url.

        Args:
            overwatch_server_url (str): The url of the overwatch server.
            model_registry_url (str): The url of the model registry.
            header_key (str): The header key for the request.
        """
        self.ow_server_url = overwatch_server_url
        self.model_registry_url = model_registry_url
        self.header_payload = {"key": header_key}
        self.inference_timer = []
        self.inference_counter = []

    def check_overwatch_server_connection(self) -> bool:
        """
        Checks if the Overwatch server is reachable.

        Returns:
            Bool: True if the Overwatch server is reachable.
        """
        try:
            response = requests.get(f"{self.ow_server_url}/status", headers=self.header_payload)
            response.raise_for_status()
            return True
        except requests.exceptions.ConnectionError:
            return False

    def __get_file__(self, file_path: str) -> bytes:
        """
        Retrieves the contents of a file from disk and returns it as bytes. 

        Args:
            file_path (str): The path to the file.

        Returns:
            bytes: The contents of the file as bytes.
        """
        with open(file_path, "rb") as f:
            ret_bytes: bytes = f.read()
        return ret_bytes

    def register_model_with_bytes(
        self,
        model_name: str,
        model_bytes: bytes,
        preprocess_bytes: bytes,
        postprocess_bytes: bytes,
        password: str = "DefaultPassword",
        language: Optional[str] = None,
        packages: Optional[Sequence[str]] = None,
    ) -> requests.Response:
        """
        Registers a new model with the model registry. Will throw if the model already exists.

        Args:
            model_name (str): The name of the model to register.
            model_bytes (bytes): The bytes of the model.
            preprocess_bytes (bytes): The bytes of the preprocess file for this model.
            postprocess_bytes (bytes): The bytes of the postprocess file for this model.
            password (str): The password for this model.
            language (str): The language for this model. Can be either javascript or python.
            packages (Sequence[str]): A list of packages required for this model.

        Returns:
            requests.Resposne: The response from the model registry.
        """

        url = f"{self.model_registry_url}/models"
        data_payload = {
            "modelID": model_name,
            "password": password,
            "reqPackages": packages if packages is not None else [],
            "language": "javascript" if language is None else language,
        }

        files_payload = {
            "model": model_bytes,
            "preprocess": preprocess_bytes,
            "postprocess": postprocess_bytes,
        }

        response = requests.post(
            url,
            headers=self.header_payload,
            data=data_payload,
            files=files_payload,
        )
        return response 

    def register_model(
        self,
        model_name: str,
        model_path: str,
        preprocess_path: str,
        postprocess_path: str,
        password: str = "DefaultPassword",
        language: Optional[str] = None,
        packages: Optional[Sequence[str]] = None,
    ) -> requests.Response:
        """
        Registers a new model with the model registry. Will throw if the model already exists.

        Args:
            model_name (str): The name of the model to register.
            model_path (str): The path to the model.
            preprocess_path (str): The path to the preprocess file for this model.
            postprocess_path (str): The path to the postprocess file for this model.
            password (str): The password for this model.
            language (str): The language for this model. Can be either javascript or python.
            packages (Sequence[str]): A list of packages required for this model.

        Returns:
            requests.Resposne: The response from the model registry.
        """

        return self.register_model_with_bytes(
            model_name, 
            self.__get_file__(model_path),
            self.__get_file__(preprocess_path),
            self.__get_file__(postprocess_path),
            password,
            language,
            packages
        )

    def patch_model(
        self,
        model_name: str,
        model_path: str,
        preprocess_path: str,
        postprocess_path: str,
        password: str = "DefaultPassword",
        language: Optional[str] = None,
        packages: Optional[Sequence[str]] = None,
    ) -> requests.Response:
        """
        Patches a specified model from the model registry with provided information.

        Args:
            model_name(str): The name of the model to patch.
            model_path(str): The path to the model.
            preprocess_path(str): The path to the preprocess file for this model.
            postprocess_path(str): The path to the postprocess file for this model.
            password(str): The password for this model.
            language(str): The language for this model. Can be either javascript or python.
            packages(Sequence[str]): A list of packages required for this model.

        Returns:
            requests.Response: The response from the model registry.
        """
        url = f"{self.model_registry_url}/models/{model_name}"
        data_payload = {
            "modelID": model_name,
            "password": password,
            "reqPackages": packages if packages is not None else [],
            "language": "javascript" if language is None else language,
        }

        files_payload = {
            "model": self.__get_file__(model_path),
            "preprocess": self.__get_file__(preprocess_path),
            "postprocess": self.__get_file__(postprocess_path),
        }

        response = requests.patch(
            url,
            headers=self.header_payload,
            data=data_payload,
            files=files_payload,
        )

        response.raise_for_status()

        return response

    def delete_model(
        self, model_name: str, password: str = "DefaultPassword"
    ) -> requests.Response:
        """
        Deletes the specified model from the model registry.

        Args:
            model_name (str): The name of the model to delete.
            password (str): The associated password for the modelself.

        Returns:
            requests.Response: The response object from the model registry after deleting the model.
        """
        url = f"{self.model_registry_url}/models/{model_name}"

        header_payload = {
            "key": self.header_payload["key"],
            "password": password,
        }

        response = requests.delete(
            url,
            headers=header_payload,
        )

        response.raise_for_status()

        return response

    def get_model(self, model_name: str) -> requests.Response:
        """
        Retrieves a model from the model registry.
        
        Args:
            model_name (str): The name of the model to retrieve.

        Returns:
            requests.Response: The response object from the model registry.
        """
        url = f"{self.model_registry_url}/models/{model_name}"

        response = requests.get(url, headers=self.header_payload)

        response.raise_for_status()

        return response

    def infer(
        self,
        inputs: Sequence[bytes],
        model_name: str,
        slice_batch: int = 1,
        inference_id: Optional[str] = None,
        compute_group_info: Optional[str] = None,
    ) -> Dict:
        """
        Performs an inference on the provided inputs using the model specified. Returns 
        the inference results as a dictionary.

        Args:
            inputs(Sequence[bytes]): A list of inputs in byte format.
            model_name(str): The model name we will be inferencing on.
            slice_batch(int): The number of inputs to run per slice.
            inference_id(Optional[str]): A special ID for this inference instance (Optional).
            compute_group_info(Optional[str]): Compute group information in the form of "<joinKey>/<joinSecret>".

        Returns:
            Dict: The inference results as a dictionary.
        """
        inference_id = (
            inference_id
            if inference_id is not None
            else f"{model_name}_{generate_uuid()}"
        )
        url = f"{self.ow_server_url}/Prediction/{inference_id}/detect/iterations/{model_name}/{slice_batch}"
        if compute_group_info is not None:
            url = f"{url}/{compute_group_info}"

        files = {}
        for ind, elem in enumerate(inputs):
            files[f"{ind}"] = elem

        start_time = time.time()

        response = requests.post(
            url,
            headers= { "prediction-key": self.header_payload["key"] },
            files=files,
        )

        response.raise_for_status()

        end_time = time.time()

        self.inference_timer.append(end_time - start_time)
        self.inference_counter.append(len(inputs))

        return response.json()
