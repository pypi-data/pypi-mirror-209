import random
import math
import sys
sys.path.insert(0, '..')

from streamsketchlib.distinct_count import DistinctCount

m = 1000000
eps = 0.05
delta = 0.05

def test_f0_estimate_small():
    """ test case when F0 is large """
    l = 0
    u = 500000
    stream = []
    f_0 = DistinctCount(epsilon = eps, delta = delta)

    for i in range(m):
        x = random.randrange(l,u)
        stream.append(x)
        f_0.insert(str(x))

    ans = len(set(stream))
    assert (1-eps) * ans <= f_0.estimator() and  f_0.estimator() <= (1+eps) * ans

def test_f0_estimate_medium():
    """ test case when F0 is medium """
    l = 0
    u = 2000000
    stream = []
    f_0 = DistinctCount(epsilon = eps, delta = delta)

    for i in range(m):
        x = random.randrange(l,u)
        stream.append(x)
        f_0.insert(str(x))

    ans = len(set(stream))
    assert (1-eps) * ans <= f_0.estimator() and  f_0.estimator() <= (1+eps) * ans

def test_f0_estimate_large():
    """ test case when F0 is large """
    l = 0
    u = 1000000
    stream = []
    f_0 = DistinctCount(epsilon = eps, delta = delta)

    for i in range(m):
        x = random.randrange(l,u)
        stream.append(x)
        f_0.insert(str(x))

    ans = len(set(stream))
    assert (1-eps) * ans <= f_0.estimator() and  f_0.estimator() <= (1+eps) * ans

def test_f0_estimate_merge():
    """ test case when F0 is large """
    l = 0
    u = 1000000
    l2 = int(1000000/2)
    u2 = int(l2*2)

    stream = []
    f_0 = DistinctCount(epsilon = eps, delta = delta)
    f_0_new = DistinctCount.from_existing(f_0)

    for i in range(m):
        x = random.randrange(l,u)
        stream.append(x)
        f_0.insert(str(x))
    for i in range(m):
        x = random.randrange(l2,u2)
        stream.append(x)
        f_0_new.insert(str(x))

    f_0.merge(f_0_new)
    ans = len(set(stream))
    assert (1-eps) * ans <= f_0.estimator() and  f_0.estimator() <= (1+eps) * ans

def test_f0_estimate_add_operator():
    """ test case when F0 is large """
    l = 0
    u = 1000000
    l2 = int(1000000/2)
    u2 = int(l2*2)

    stream = []
    f_0 = DistinctCount(epsilon = eps, delta = delta)
    f_0_new = DistinctCount.from_existing(f_0)

    for i in range(m):
        x = random.randrange(l,u)
        stream.append(x)
        f_0.insert(str(x))
    for i in range(m):
        x = random.randrange(l2,u2)
        stream.append(x)
        f_0_new.insert(str(x))

    merged_f_0 = f_0 + f_0_new
    ans = len(set(stream))
    assert (1-eps) * ans <= merged_f_0.estimator() and  merged_f_0.estimator() <= (1+eps) * ans
    f_0 = f_0 + f_0_new
    assert (1-eps) * ans <= f_0.estimator() and  f_0.estimator() <= (1+eps) * ans




if __name__ == '__main__':
    test_f0_estimate_small()
    test_f0_estimate_medium()
    test_f0_estimate_large()
    test_f0_estimate_merge()
    test_f0_estimate_add_operator()
