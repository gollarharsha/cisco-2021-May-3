from firstlast import firstlast
import pytest


@pytest.mark.parametrize('seq,result',
                         [('abcde', 'ae'),
                          ([10, 20, 30, 40, 50, 60], [10, 60]),
                          ((100, 200), (100, 200))])
def test_firstlast(seq, result):
    assert firstlast(seq) == result
