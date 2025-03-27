from dataclasses import dataclass
from typing import Sequence, TypeAlias

from rlbot import flat

Slice: TypeAlias = flat.PredictionSlice


@dataclass(frozen=True, slots=True)
class BallPrediction:
    slices: Sequence[Slice]
    num_slices: int
