from __future__ import annotations

from enum import Enum
import json
from typing import NewType

from attrs import define


def rawtext(text: str) -> str:
    """Wraps text inside a rawtext JSON object.
    
    .. seealso:: https://wiki.bedrock.dev/commands/tellraw.html
    """
    return json.dumps({
        "rawtext": [{"text": text}]
    })

class TargetSelector(str, Enum):
    """
    A collection of target selectors that can be used within commands.
    
    .. seealso:: https://minecraft.fandom.com/wiki/Target_selectors
    """

    NEAREST_PLAYER = "@p"
    RANDOM_PLAYER  = "@r"
    ALL_PLAYERS    = "@a"
    ALL_ENTITIES   = "@e"
    SELF           = "@s"
    PLAYER_AGENT   = "@c"
    ALL_AGENTS     = "@v"
    INITIATOR      = "@initiator"

@define
class WorldCoordinate:
    """
    A class representing a world coordinate.
    """
    coord: float
    is_relative: bool = False

    def __str__(self) -> str:
        return f"{'~' if self.is_relative else ''}{self.coord}"

    @classmethod
    def from_string(cls, value: str) -> WorldCoordinate:
        n = value.removeprefix("~")
        return cls(numeric(n), is_relative=len(n) != len(value))


@define
class LocalCoordinate:
    """
    A class representing a local coordinate.
    """
    coord: float

    def __str__(self) -> str:
        return f"^{self.coord}"

    @classmethod
    def from_string(cls, value: str) -> LocalCoordinate:
        n = value.removeprefix("^")
        if len(n) != len(value):
            raise ValueError("coordinate must start with a caret (^)")
        return cls(numeric(n))


WorldCoordinates = NewType(
    "WorldCoordinates", tuple[WorldCoordinate, WorldCoordinate, WorldCoordinate]
)
LocalCoordinates = NewType(
    "LocalCoordinates", tuple[LocalCoordinate, LocalCoordinate, LocalCoordinate]
)


def numeric(value: str) -> float:
    """
    Converts a string into an integer or if that fails into a floating
    point.

    Parameters
    ----------
    value
        The string to converr into a numeric.

    Raises
    ------
    ValueError
        The string cannot be converted into a boolean.
    """
    try:
        return int(value)
    except ValueError:
        return float(value)
