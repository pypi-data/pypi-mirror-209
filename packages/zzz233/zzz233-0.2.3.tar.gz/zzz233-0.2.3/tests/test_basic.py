# TODO test to_pickle and from_pickle
import zzz233
from zzz233 import to_pickle, from_pickle

def test_to_pickle_from_pickle():
    a = 233
    b = 0.233
    to_pickle(a=a, b=b)
    assert from_pickle('a')==a
    assert from_pickle('b')==b


def test_version():
    assert hasattr(zzz233, '__version__')
    assert hasattr(zzz233, '__version_tuple__')
