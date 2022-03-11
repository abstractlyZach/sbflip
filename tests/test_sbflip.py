from sbflip import tiles
import pytest
import collections



def test_default_tile_state():
    tile_state = tiles.TileState()
    assert tile_state.current_char_index == 0


def test_tile_state_init_with_args():
    tile_state = tiles.TileState(current_char_index=5)
    assert tile_state.current_char_index == 5


FlipCountTest = collections.namedtuple(
    "FlipCountTest",
    ["starting_index", "char_to_index_dict", "target_char", "expected_flip_count"],
)


flip_count_tests = [
    FlipCountTest(
        starting_index=2,
        char_to_index_dict={"f": 7},
        target_char="f",
        expected_flip_count=5,
    ),
    FlipCountTest(
        starting_index=2,
        char_to_index_dict={"f": 10},
        target_char="f",
        expected_flip_count=8,
    ),
    FlipCountTest(
        starting_index=3,
        char_to_index_dict={"f": 10, "g": 11, "h": 12},
        target_char="f",
        expected_flip_count=7,
    ),
    # make sure we can wrap around the loop
    FlipCountTest(
        starting_index=3,
        char_to_index_dict={"a": 0, "b": 1, "c": 2, "d": 3, "e": 4},
        target_char="a",
        expected_flip_count=2,
    ),
    FlipCountTest(
        starting_index=1,
        char_to_index_dict={"a": 0, "b": 1, "c": 2, "d": 3, "e": 4},
        target_char="a",
        expected_flip_count=4,
    ),
]


@pytest.mark.parametrize("test_case", flip_count_tests)
def test_count_flips(test_case):
    tile_state = tiles.TileState(current_char_index=test_case.starting_index)
    assert (
        tiles.get_num_flips_until(
            tile_state, test_case.char_to_index_dict, test_case.target_char
        )
        == test_case.expected_flip_count
    )


def test_flip():
    tile_state = tiles.TileState(current_char_index=5)
    assert tile_state.current_char_index == 5
