from typing import Dict


class TileState(object):
    def __init__(self, current_char_index=0):
        self._current_char_index = current_char_index

    @property
    def current_char_index(self) -> int:
        return self._current_char_index

def get_num_flips_until(tile_state: TileState, char_to_index_dict: Dict, char: str) -> int:
    target_index = char_to_index_dict[char]
    if target_index > tile_state.current_char_index:
        return target_index - tile_state.current_char_index
    else:
        return (target_index - tile_state.current_char_index) % len(char_to_index_dict)
