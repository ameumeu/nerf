import torch

class IntergratorBase(object):
    def __init__(self, *arg, **kwargs):
        pass
    
    def integrate_along_rays(
        self,
        sigma: torch.Tensor,
        radiance: torch.Tensor,
        delta: torch.Tenseor,
    ):
        raise NotImplementedError()