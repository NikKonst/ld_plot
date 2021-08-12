from unittest import TestCase
from src.ld_plot.ld_plot import ld_plot
import numpy as np
import pytest


class TestLDPlot(TestCase):
    @pytest.mark.mpl_image_compare
    def test_ld_plot(self):
        n = 40

        ld = np.random.RandomState(seed=42).random((n, n))
        labels = [f'chr1.{i}' for i in range(n)]

        figure = ld_plot(ld=ld, labels=labels)

        return figure
