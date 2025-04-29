from copy import deepcopy

import numpy as np

from .utils_scheduling import adaptive_binary_search

def gradient_numerical(
    loss_function,
    eo_d_type,
    params: list,
    loss_0,
    s_0,
    mode,
    delta: float = 1e-7,
):
    grad = np.zeros(len(params))
    for i in range(len(params)):
        params_new = deepcopy(params)
        params_new[i] += delta
        eo_d = eo_d_type.load(params_new)
        # find the increment of a very small step
        grad[i] = (loss_function(s_0, eo_d, mode) - loss_0) / delta

    # normalize gradient
    grad = grad / max(abs(grad))
    return grad


def choose_gd_params(
    gci,
    eo_d_type,
    params,
    loss_0,
    s_0,
    mode,
    s_min=1e-4,
    s_max=2e-2,
    lr_min=1e-4,
    lr_max=1,
    threshold=1e-4,
    max_eval=30,
    please_be_adaptive=True,
    please_be_verbose=False,
):
    pass
