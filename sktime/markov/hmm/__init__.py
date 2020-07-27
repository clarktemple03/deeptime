# This file is part of scikit-time
#
# Copyright (c) 2020 AI4Science Group, Freie Universitaet Berlin (GER)
#
# scikit-time is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


r"""
.. currentmodule: sktime.markov.hmm

The implementations that can be found in this subpackage are based on the `BHMM <https://github.com/bhmm/bhmm>`_
software package.

Output models
-------------

.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    OutputModel
    DiscreteOutputModel
    GaussianOutputModel


Maximum-likelihood estimation of HMMs
-------------------------------------

Since the maximum-likelihood estimation (via Baum-Welch :cite:`hmminit-baum1967inequality`) of
:class:`HMMs <sktime.markov.hmm.HiddenMarkovStateModel>` is likely to
get stuck in local maxima, a good initial guess is important for a high-quality model. The following methods aim to
provide heuristics which can yield such an initial guess and can be found in :cite:`hmminit-noe2013projected`.

For a HMM with a :class:`discrete output model <sktime.markov.hmm.DiscreteOutputModel>`, the following main
steps are involved:

1. A :class:`markov state model <sktime.markov.msm.MarkovStateModel>` is estimated from given discrete
   trajectories. This step is optional if the markov model already exists.
2. The estimated MSM transition matrix :math:`P\in\mathbb{R}^{n\times n}` is coarse-grained with PCCA+ into the
   desired number of hidden states :math:`m` and memberships :math:`M\in\mathbb{R}^{n \times m}`. The transition
   matrix is projected into the hidden state space by

   .. math::
        P_\mathrm{coarse} = (M^\top M)^{-1} M^\top P M.

.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    init.discrete.metastable_from_data
    init.discrete.metastable_from_msm

A non data-driven way to initialize a HMM is implemented by setting the transition matrix and initial distribution to
uniform, and drawing a random row-stochastic emission probability matrix:

.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    init.discrete.random_guess

For a HMM with a :class:`gaussian output model <sktime.markov.hmm.GaussianOutputModel>`, a Gaussian mixture
model is estimated. This particular heuristic requires an installation of `scikit-learn <https://scikit-learn.org/>`_.

.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    init.gaussian.from_data

Estimation and resulting model:

.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    MaximumLikelihoodHMSM
    HiddenMarkovStateModel

Bayesian hidden markov state models
-----------------------------------
Bayesian HMMs can provide confidence estimates. They are estimated by starting from a reference HMM and then use
Gibbs sampling.

See :cite:`hmminit-chodera2011bayesian` for a manuscript describing the theory behind using Gibbs 
sampling to sample from Bayesian hidden Markov model posteriors.

.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    BayesianHMSM
    BayesianHMMPosterior

References
----------
.. bibliography:: /references.bib
    :style: unsrt
    :filter: docname in docnames
    :keyprefix: hmminit-
"""

from .hidden_markov_model import HiddenMarkovStateModel
from .maximum_likelihood_hmm import MaximumLikelihoodHMSM
from .bayesian_hmm import BayesianHMSM, BayesianHMMPosterior
from .output_model import OutputModel, DiscreteOutputModel, GaussianOutputModel

from . import init