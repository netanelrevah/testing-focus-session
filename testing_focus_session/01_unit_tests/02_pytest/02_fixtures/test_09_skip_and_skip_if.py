import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    pass


def test_1():
    if True:
        pytest.skip("unsupported configuration")


@pytest.mark.skipif(
    "sys.version_info > (2,7)", reason="requires python2.7 or lower"
)
def test_2(): pass


@pytest.mark.skipif('os.environ.get("TEST_LEVEL") != "unit"')
def test_3(): pass
