import pytest
from main import do_something


class TestDoSomething:
    @pytest.mark.parametrize(
        "given, want",
        [
            (0, "Something has been done 0 times"),
            (3, "Something has been done 3 times"),
        ],
    )
    def test_ok(self, given: int, want: str) -> None:
        actual = do_something(given)
        assert actual == want

    @pytest.mark.parametrize(
        "given, want",
        [
            (-1, "times must be >= 0"),
        ],
    )
    def test_error(self, given: int, want: str) -> None:
        with pytest.raises(ValueError):
            do_something(given)
