from fairbench.forks.fork import parallel
from eagerpy import Tensor
from typing import Optional


@parallel
def prule(
    predictions: Tensor,
    sensitive: Tensor,
    non_sensitive: Optional[Tensor] = None,
    max_sensitive: float = 1,
):
    if non_sensitive is None:
        non_sensitive = max_sensitive - sensitive
    sum_sensitive = sensitive.sum()
    sum_non_sensitive = non_sensitive.sum()
    if sum_sensitive == 0:
        return sum_sensitive
    if sum_non_sensitive == 0:
        return sum_non_sensitive
    r1 = (predictions * sensitive).sum() / sum_sensitive
    r2 = (predictions * non_sensitive).sum() / sum_non_sensitive
    max_r = r1.maximum(r2)
    if max_r == 0:
        return max_r
    return r1.minimum(r2) / max_r


@parallel
def cvdisparity(
    predictions: Tensor,
    sensitive: Tensor,
    non_sensitive: Optional[Tensor] = None,
    max_sensitive: float = 1,
):
    if non_sensitive is None:
        non_sensitive = max_sensitive - sensitive
    sum_sensitive = sensitive.sum()
    sum_non_sensitive = non_sensitive.sum()
    if sum_sensitive == 0:
        return sum_sensitive
    if sum_non_sensitive == 0:
        return sum_non_sensitive
    r1 = (predictions * sensitive).sum() / sum_sensitive
    r2 = (predictions * non_sensitive).sum() / sum_non_sensitive
    return r1 - r2


@parallel
def eqrep(
    predictions: Tensor,
    sensitive: Tensor,
    non_sensitive: Optional[Tensor] = None,
    max_sensitive: float = 1,
):
    if non_sensitive is None:
        non_sensitive = max_sensitive - sensitive
    sum_sensitive = sensitive.sum()
    sum_non_sensitive = non_sensitive.sum()
    if sum_sensitive == 0:
        return sum_sensitive
    if sum_non_sensitive == 0:
        return sum_non_sensitive
    r1 = (predictions * sensitive).sum()
    r2 = (predictions * non_sensitive).sum()
    max_r = r1.maximum(r2)
    if max_r == 0:
        return max_r
    return r1.minimum(r2) / max_r
