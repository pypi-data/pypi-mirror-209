from pyro.infer import Predictive

from ._decorators import auto_move_data


class AutoMoveDataPredictive(Predictive):
    """Auto move data."""

    @auto_move_data
    def forward(self, *args, **kwargs):
        return super().forward(*args, **kwargs)
