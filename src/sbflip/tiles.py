"""module for managing tiles."""
import collections
import dataclasses
from typing import Dict


@dataclasses.dataclass
class TileState:
    """Simple class for storing a tile's state."""

    current_char_index: int = 0
    remaining_flips_to_target: int = 0


def get_num_flips_until(
    tile_state: TileState, char_to_index_dict: Dict, char: str
) -> int:
    """Calculate how many flips are needed until a tile shows the target letter."""
    target_index = char_to_index_dict[char]
    if target_index > tile_state.current_char_index:
        return target_index - tile_state.current_char_index
    else:
        return (target_index - tile_state.current_char_index) % len(char_to_index_dict)


def attempt_flip(tile_state: TileState, num_chars) -> None:
    """Attempt to flip the tile.

    If a tile has reached its target, then this function won't change the state
    """
    if tile_state.remaining_flips_to_target > 0:
        tile_state.current_char_index += 1
        tile_state.current_char_index %= num_chars
        tile_state.remaining_flips_to_target -= 1


class Flipboard:
    """A board whose tiles flip around to display messages."""

    def __init__(self, line_length, chars):
        self._tiles = [TileState() for _ in range(line_length)]
        self._available_chars = chars
        self._message_queue = collections.deque()
        self._message_is_in_progress = False
        self._char_to_index_dict = {char: index for index, char in enumerate(chars)}

    @property
    def text(self) -> str:
        """Display the current text on the tiles."""
        chars = [
            self._available_chars[tile_state.current_char_index]
            for tile_state in self._tiles
        ]
        return "".join(chars)

    def set_message(self, message: str) -> None:
        """Set the message that will be displayed next."""
        if len(message) > len(self._tiles):
            raise RuntimeError("This message is too long for this board")

        unwriteable_chars = set(message) - set(self._available_chars)
        if unwriteable_chars:
            raise RuntimeError(
                f"Couldn't write message. These chars are unavailable: {unwriteable_chars}"
            )

        self._message_queue.append(message)
        if not self._message_is_in_progress:
            self._load_next_message()

    def _load_next_message(self) -> None:
        next_message = self._message_queue.popleft()
        for target_char, tile in zip(next_message, self._tiles):
            num_flips_to_target = get_num_flips_until(
                tile, self._char_to_index_dict, target_char
            )
            tile.remaining_flips_to_target = num_flips_to_target
        self._message_is_in_progress = True

    def tick(self) -> None:
        """Move forward one tick in time.

        Tiles that can be flipped will be flipped. If it's time to start on the next message, then
        begin doing that.
        """
        for tile in self._tiles:
            attempt_flip(tile, len(self._available_chars))
