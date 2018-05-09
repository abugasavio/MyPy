import pytest
from enum import Enum

RED = 1
BLUE = 2
GREEN = 3


class Color(Enum):
    red = 1
    green = 2
    blue = 3


def get_rgb(color):
    if color == Color.red:
        return 255, 0, 0
    elif color == Color.green:
        return 0, 255, 0
    elif color == Color.blue:
        return 0, 0, 255


def test_enum():
    # Create an enumeration, ``Color``, that
    # has ``red``, ``green``, and ``blue``
    # as the different members. Use the class
    # style by subclassing ``Enum``
    # (Normally these are created
    # at the global level)
    # ***************************************

    assert Color.red in Color
    with pytest.raises(AttributeError):
        Color.brown

    # Refactor ``get_rgb`` to use the Color
    # enumeration.
    # ***************************************
    assert get_rgb(Color.red) == (255, 0, 0)

    # Create an enumeration, ``Pet``, that
    # has ``dog``, ``cat``, and ``fish``
    # as the different members. Call the
    # ``Enum`` class to create it
    # ***************************************
 
    class Pet(Enum):
        dog = 'dog'
        cat = 'cat'
        fish = 'fish'
        
    assert {x.name for x in Pet} == \
        {'cat', 'dog', 'fish'} 

        
if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
