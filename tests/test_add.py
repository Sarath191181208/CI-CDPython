from logic_ops import add
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 2),
    (2, 2, 4),
    (3, 3, 6),
    (0, 0, 0),
])
def test_add(x, y, expected):
    assert add(x, y) == expected

def test_set_add():
    with pytest.raises(TypeError):
        add({1, 2}, {3, 4})