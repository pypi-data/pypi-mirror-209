import os
from typing import Any, List, Optional

import pandas as pd
import requests

from eigenrules.exceptions import raise_empty_datapoint, raise_missing_argument
from eigenrules.schemas import (
    AnomalyData,
    Prediction,
    PredictRequest,
    SegmentationData,
    decode_data,
    encode_data,
)


class AnomalyEngine:
    def __init__(self, api_token: str, api_url: Optional[str] = "https://api.eigendata.ai", api_version="v1") -> None:
        self.token = os.getenv("EIGEN_API_TOKEN", api_token)
        self.api_url = api_url
        self.api_version = api_version
        self.dataset: pd.DataFrame = None
        self.data: SegmentationData = None
        self.model_id: int = None

    def _load_data(self, path: Optional[str], data: Optional[pd.DataFrame]):
        if data is not None:
            self.dataset = data
        elif path is not None:
            self.dataset = pd.read_csv(path)
        else:
            raise_missing_argument()

    def train(
        self,
        name: str,
        data_path: Optional[str],
        features: Optional[List[str]],
        data: Optional[pd.DataFrame] = None,
        split: Optional[float] = 0.25,
        contamination: Optional[float] = None,
    ) -> int:
        """
        Returns the trained model id. Sets this model as default for the RulesEngine class.

        Parameters
        ----------
        name : str
            Name identifier for the model..
        data_path : str
            Path to dataset (CSV). Required unless `data` argument is provided.
        data : pd.DataFrame, Optional
            pandas DataFrame object containing the dataset.
        split : float, Optional
            Which percentage of the dataset to be used for testing. > 0 and < 1.
        balance : float, Optional
            Value between 0 and 1 that balances the dataset classes during training sampling.
        contamination : float || string, Optional
            if left empty, the model will do contamination auto detection.
            This value represents expected percentage of outliers in data.


        Returns
        -------
        model_id : int
            Trained model id for future use. This gets set as default use within the class instance.
        """
        train_url = f"{self.api_url}/{self.api_version}/models/anomaly/train"
        headers = {"Authorization": f"Bearer {self.token}"}

        self._load_data(data_path, data)

        data = AnomalyData(
            name=name, dataset=encode_data(self.dataset), features=features, split=split, contamination=contamination
        )

        self.data = data

        response = requests.post(url=train_url, headers=headers, json=data.dict())
        self.model_id = response.json()["id"]
        return response.json()["id"]

    def authenticate(self, username: str, password: str):
        auth_url = f"{self.api_url}/token"
        form_data = {"username": username, "password": password}
        res = requests.post(auth_url, data=form_data)
        self.token = res.json()["access_token"]

    def list_models(self) -> pd.DataFrame:
        list_models = f"{self.api_url}/{self.api_version}/models"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        res = requests.get(url=list_models, headers=headers)
        models = res.json()
        return pd.DataFrame.from_dict(models)

    def predict(
        self,
        df_datapoint: Optional[pd.DataFrame] = None,
        columns: Optional[List[str]] = [],
        values: Optional[List[Any]] = [],
        model_id: Optional[int] = None,
    ) -> Prediction:
        if df_datapoint is not None:
            datapoint = df_datapoint
        else:
            datapoint = pd.DataFrame(values, columns=columns)
        if len(datapoint.index) == 0:
            raise_empty_datapoint()

        mid = model_id or self.model_id
        predict_url = f"{self.api_url}/{self.api_version}/models/anomaly/{mid}/predict"
        req = PredictRequest(datapoint=encode_data(datapoint), model_id=mid)
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        res = requests.post(predict_url, headers=headers, json=req.dict())
        res_json = res.json()
        prediction = Prediction(
            datapoint=datapoint,
            result=decode_data(res_json["result"]),
            confidence=decode_data(res_json["confidence"]),
        )
        return prediction
