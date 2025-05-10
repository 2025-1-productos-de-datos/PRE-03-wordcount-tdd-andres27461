import sys

from ...wordcount import parse_args
from ...wordcount import read_all_lines

def test_parse_args():

    test_args = ["homework", "data/input/", "data/output/"]
    sys.argv = test_args
    input_folder, output_folder = parse_args()
    assert input_folder == test_args[1]
    assert output_folder == test_args[2]

def test_read_all_lines():
    input_folder = "data/input/"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational "
    )
 