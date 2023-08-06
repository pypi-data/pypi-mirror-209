import pytest


def test_binary_gets_diffed(golden):
    with pytest.raises(AssertionError):
        golden.test(b"\xCA\xFE\xBA\xBE")


def test_text_gets_diffed(golden):
    with pytest.raises(AssertionError):
        golden.test("BAR")


def test_dicts_get_diffed(golden):
    test_data = {"foo": "bar"}
    with pytest.raises(AssertionError):
        golden.test(test_data)


def test_fails_if_golden_is_missing(golden):
    # pytest throws Failed when we call pytest.fail which is unexported, so we catch the base one.
    with pytest.raises(BaseException):
        golden.test("")
