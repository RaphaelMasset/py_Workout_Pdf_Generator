from project import max_potent, lbs_convert, how_heavy
from unittest.mock import patch
from io import StringIO


#def test_Program_table_create():
    #assert


def test_max_potent():
    assert max_potent(100, "kg", 200, 20) == (18.7, 123.4, 124)


def test_lbs_convert():
    assert lbs_convert(100, "lbs") == (45.4, "lbs")

def test_how_heavy():
    with patch("sys.stdin", StringIO("80 kg\n")):
        assert how_heavy("bench") == (92.0, "kg")

