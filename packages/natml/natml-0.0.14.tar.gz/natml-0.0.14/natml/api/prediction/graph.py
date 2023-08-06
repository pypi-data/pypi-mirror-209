# 
#   NatML
#   Copyright © 2023 NatML Inc. All Rights Reserved.
#

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class GraphPrediction: # INCOMPLETE
    """
    Graph prediction.

    Members:
        id (str): Prediction ID.
        tag (str): Graph tag.
        graph (str): Prediction graph URL.
        code (str): Prediction code URL.
        created (str): Date created.
    """
    id: str
    tag: str
    graph: str
    code: str
    created: str

    @classmethod
    def create (
        cls,
        tag: str,
        device: str=None,
        access_key: str=None
    ) -> GraphPrediction:
        """
        Create a graph prediction.

        Parameters:
            tag (str): Graph tag.
            device (str): Device model identifier. This is used to optimize the graph prediction based on known hardware optimizations.
            access_key (str): NatML access key.

        Returns:
            GraphPrediction: Graph prediction.
        """
        pass