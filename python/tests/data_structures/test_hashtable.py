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
    actual = hashtable.has("listen")
    expected = True
    assert actual == expected

def test_return_unique_keys():
    pass

def test_handle_collision():
    pass

def test_retrieve_value_bucket():
    pass

def test_hash_a_key():
    pass


# @pytest.mark.skip("TODO")
# def test_internals():
#     hashtable = Hashtable(1024)
#     hashtable.set("ahmad", 30)
#     hashtable.set("silent", True)
#     hashtable.set("listen", "to me")
#
#     actual = []
#
#     # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
#     for item in hashtable._buckets:
#         if item:
#             actual.append(item.display())
#
#     expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
#
#     assert actual == expected
