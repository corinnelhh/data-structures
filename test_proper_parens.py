import pytest
from proper_parens import paren_checker


def test_paren_checker():
    assert paren_checker("()") == 0
    assert paren_checker(")(") == -1
    assert paren_checker("(()") == 1
    assert paren_checker("((x)(x)(x))") == 0
    assert paren_checker("))))))") == -1
