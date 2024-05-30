import sys


def assert_equal(expected, actual):
    assert expected == actual


def assert_is(expected, actual):
    assert expected is actual


def assert_raises(expected, callable_, *args, **kwargs):
    actual = None
    try:
        callable_(*args, **kwargs)
    except:
        actual, _, _ = sys.exc_info()
    assert actual == expected, \
        "No exception raised" if actual is None \
        else "Expected {}, got {}".format(
            expected.__name__, actual.__name__
        )
