"""module for managing tiles."""
import dataclasses
from typing import Dict


@dataclasses.dataclass
class TileState:
    """Simple class for storing a tile's state."""

    current_char_index: int = 0


def get_num_flips_until(
    tile_state: TileState, char_to_index_dict: Dict, char: str
) -> int:
    """Calculate how many flips are needed until a tile shows the target letter."""
    target_index = char_to_index_dict[char]
    if target_index > tile_state.current_char_index:
        return target_index - tile_state.current_char_index
    else:
        return (target_index - tile_state.current_char_index) % len(char_to_index_dict)
