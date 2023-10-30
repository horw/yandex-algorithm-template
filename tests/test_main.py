from pathlib import Path

import pytest

from algorithm import main

TEST_DATA_DIR = Path(__file__).resolve().parent / 'data'


@pytest.mark.parametrize('if_name, ef_name', [
    ('in_1', 'ex_1'),
    ('in_2', 'ex_2')
])
def test_algorithm(if_name, ef_name, capsys):
    expect: str
    with open(TEST_DATA_DIR / 'expect' / ef_name) as f:
        expect = f.read()

    main(TEST_DATA_DIR / 'input' / if_name)

    out, err = capsys.readouterr()
    assert out == expect
