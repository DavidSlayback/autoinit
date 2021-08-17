
# Copyright (C) 2019-2021 Cognizant Digital Business, Evolutionary AI.
# All Rights Reserved.
# Issued under the Academic Public License.
#
# You can be released from the terms, and requirements of the Academic Public
# License by purchasing a commercial license.
# Purchase of a commercial license is mandatory for any use of the
# AutoInit Software in commercial settings.
#
# END COPYRIGHT
from typing import List

from framework.enn.autoinit.estimators.estimate_layer_output_distribution \
    import LayerOutputDistributionEstimator


class SubtractOutputDistributionEstimator(LayerOutputDistributionEstimator):
    """
    This class is responsible for estimating the output distribution of Subtract layers.
    """

    def estimate(self, means_in: List, vars_in: List):
        """
        By linearity of expectation:
        E[X1 - X2] = E[X1] + E[-X2]
                   = E[X1] - E[X2].

        If we assume the inputs are independent, we also have:
        Var(X1 - X2) = Var(X1) + Var(-X2)
                     = Var(X1) + (-1)²Var(X2)
                     = Var(X1) + Var(X2).

        :param means_in: List containing the means of the input distributions of
        the incoming layers
        :param vars_in: List containing the variances of the input distributions of
        the incoming layers

        :return mean_out: Mean of the output distribution
        :return var_out: Variance of the output distribution
        """

        mean_out = means_in[0] - means_in[1]
        var_out = vars_in[0] + vars_in[1]

        return mean_out, var_out
