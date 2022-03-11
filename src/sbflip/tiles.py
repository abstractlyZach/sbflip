"""module for managing tiles."""
from typing import Dict


class TileState:
    """Simple class for storing a tile's state."""

    def __init__(self, current_char_index=0):
        self._current_char_index = current_char_index

    @property
    def current_char_index(self) -> int:  # noqa: D102
        return self._current_char_index


def get_num_flips_until(
    tile_state: TileState, char_to_index_dict: Dict, char: str
) -> int:
    """Calculate how many flips are needed until a tile shows the target letter."""
    target_index = char_to_index_dict[char]
    if target_index > tile_state.current_char_index:
        return target_index - tile_state.current_char_index
    else:
        return (target_index - tile_state.current_char_index) % len(char_to_index_dict)
