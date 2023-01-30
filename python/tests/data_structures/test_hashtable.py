import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_return_null():
    hashtable = Hashtable()
    actual = hashtable.keys()
    expected = []
    assert actual == expected


def test_has_matt():
    hashtable = Hashtable()
    hashtable.set("matt", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.has("matt")
    expected = True
    assert actual == expected

def test_return_unique_keys():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    expected = ['listen', 'silent', 'ahmad']
    actual = hashtable.keys()
    print(f'actual is {actual}')
    assert actual == expected


def test_handle_collision():
    hashtable = Hashtable(1)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    print(hashtable)

    actual = hashtable.get('silent')
    expected = True

    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
