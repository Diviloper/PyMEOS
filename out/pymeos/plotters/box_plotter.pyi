from ..boxes import STBox as STBox, TBox as TBox
from .range_plotter import SpanPlotter as SpanPlotter
from .time_plotter import TimePlotter as TimePlotter
from matplotlib import pyplot as plt

class BoxPlotter:
    @staticmethod
    def plot_tbox(tbox: TBox, *args, axes: plt.axes.Axes | None = None, **kwargs): ...
    @staticmethod
    def plot_stbox_xy(
        stbox: STBox, *args, axes: plt.axes.Axes | None = None, **kwargs
    ): ...
    @staticmethod
    def plot_stbox_xt(
        stbox: STBox, *args, axes: plt.axes.Axes | None = None, **kwargs
    ): ...
    @staticmethod
    def plot_stbox_yt(
        stbox: STBox, *args, axes: plt.axes.Axes | None = None, **kwargs
    ): ...
