# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from __future__ import annotations
from dataclasses import asdict, dataclass
from io import BytesIO
from numpy import frombuffer
from PIL import Image
from requests import get
from typing import Any, Dict, List, Union
from urllib.request import urlopen

from ..api import query
from ..dtype import Dtype
from ..feature import Feature
from .feature import FeatureInput

@dataclass
class EndpointPrediction:
    """
    Endpoint prediction.

    Members:
        id (str): Prediction ID.
        tag (str): Endpoint tag.
        created (str): Date created.
        results (list): Prediction results.
        latency (float): Prediction latency in milliseconds.
        error (str): Prediction error. This is `null` if the prediction completed successfully.
        logs (str): Prediction logs.
    """
    id: str
    tag: str
    created: str
    results: List[Feature]
    latency: float
    error: str
    logs: str

    @classmethod
    def create (
        cls,
        tag: str,
        *features: List[FeatureInput],
        raw_outputs: bool=False,
        access_key: str=None,
        **inputs: Dict[str, Any],
    ) -> EndpointPrediction:
        """
        Create an endpoint prediction.

        Parameters:
            tag (str): Endpoint tag.
            features (list): Input features.
            raw_outputs (bool): Skip parsing output features into Pythonic data types.
            access_key (str): NatML access key.
            inputs (dict): Input features.

        Returns:
            EndpointPrediction: Endpoint prediction.
        """
        # Collect input features
        input_features = list(features) + [FeatureInput.from_value(value, name) for name, value in inputs.items()]
        input_features = [asdict(feature) for feature in input_features]
        # Query
        parsed_fields = "" if raw_outputs else "\n".join(_FEATURE_KEYS)
        response = query(f"""
            mutation ($input: CreateEndpointPredictionInput!) {{
                createEndpointPrediction (input: $input) {{
                    id
                    tag
                    created
                    results {{
                        data
                        type
                        shape
                        {parsed_fields}
                    }}
                    latency
                    error
                    logs
                }}
            }}""",
            { "input": { "tag": tag, "inputs": input_features, "client": "python" } },
            access_key=access_key
        )
        # Check prediction
        prediction = response["createEndpointPrediction"]
        if not prediction:
            return None
        # Parse outputs
        prediction["results"] = [_parse_output_feature(feature) for feature in prediction["results"]] if prediction["results"] and not raw_outputs else prediction["results"]
        prediction = EndpointPrediction(**prediction)
        # Return
        return prediction

def _parse_output_feature (feature: dict) -> Union[Feature, str, float, int, bool, Image.Image, list, dict]:
    data, type, shape = feature["data"], feature["type"], feature["shape"]
    # Handle image
    if type == Dtype.image:
        return Image.open(_download_feature_data(data))
    # Handle non-numeric scalars
    values = [feature.get(key, None) for key in _FEATURE_KEYS]
    scalar = next((value for value in values if value is not None), None)
    if scalar is not None:
        return scalar
    # Handle ndarray
    ARRAY_TYPES = [
        Dtype.int8, Dtype.int16, Dtype.int32, Dtype.int64,
        Dtype.uint8, Dtype.uint16, Dtype.uint32, Dtype.uint64,
        Dtype.float16, Dtype.float32, Dtype.float64, Dtype.bool
    ]
    if type in ARRAY_TYPES:
        # Create array
        array = frombuffer(_download_feature_data(data).getbuffer(), dtype=type).reshape(shape)
        return array if len(shape) > 0 else array.item()
    # Handle generic feature
    feature = Feature(**feature)
    return feature

def _download_feature_data (url: str) -> BytesIO:
    # Check if data URL
    if url.startswith("data:"):
        with urlopen(url) as response:
            return BytesIO(response.read())
    # Download
    response = get(url)
    result = BytesIO(response.content)
    return result

_FEATURE_KEYS = ["stringValue", "listValue", "dictValue"]