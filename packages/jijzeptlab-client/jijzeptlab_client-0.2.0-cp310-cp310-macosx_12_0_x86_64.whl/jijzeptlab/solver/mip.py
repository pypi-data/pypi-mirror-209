from __future__ import annotations
from enum import Enum
from typing import Dict, List, Optional

import jijmodeling as jm
import mip

from jijzeptlab.compile import CompiledInstance
from jijzeptlab.utils.baseclass import Option, ResultWithDualVariables
from pydantic import Field


class MipModelOption(Option):
    ignore_constraint_names: List[str] = Field(default_factory=list)
    relaxed_variable_names: List[str] = Field(default_factory=list)
    relax_all_variables: bool = False
    ignore_constraint_indices: Dict[str, List[List[int]]] = Field(default_factory=dict)


class MipModelStatus(Enum):
    SUCCESS: str
    TRIVIALLY_INFEASIBLE: str


class MipModel:
    mip_model: mip.Model | None
    model_status: MipModelStatus

    def __init__(self, mip_model, mip_decoder, model_status) -> None:
        raise NotImplementedError("MipModel is not implemented yet.")


class MipResultStatus(Enum):
    SUCCESS: str
    TRIVIALLY_INFEASIBLE: str


class MipResult(ResultWithDualVariables):
    mip_model: mip.Model | None
    status: MipResultStatus

    def to_sample_set(self) -> jm.SampleSet | None:
        """Convert to SampleSet"""
        raise NotImplementedError("MipResult is not implemented yet.")

    def __init__(self, mip_model, mip_decoder, status) -> None:
        raise NotImplementedError("MipResult is not implemented yet.")


def create_model(
    compiled_instance: CompiledInstance, option: Optional[MipModelOption] = None
) -> MipModel:
    raise NotImplementedError("create_model is not implemented yet.")


def solve(mip_model: MipModel) -> MipResult:
    raise NotImplementedError("solve is not implemented yet.")
