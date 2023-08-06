import numpy as np


def generate_axis(start, stop, step):
    return np.arange(start, stop - step / 2, step) + step / 2


def get_pyfai_range_npts(start, stop, step):
    rnge = (start, stop)
    npts = int((stop - start) / step)
    return rnge, npts


def get_ai_params(start, stop, step):
    q = generate_axis(start, stop, step)
    r, n = get_pyfai_range_npts(start, stop, step)
    return q, r, n
