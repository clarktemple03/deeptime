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
.. currentmodule: sktime.decomposition

.. rubric:: Koopman model
.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    KoopmanModel
    CovarianceKoopmanModel
    KoopmanBasisTransform
    IdentityKoopmanBasisTransform

.. rubric:: TICA
.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    TICA

.. rubric:: VAMP
.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    VAMP

.. rubric:: VAMPNets
.. autosummary::
    :toctree: generated/
    :template: class_nomodule.rst

    VAMPNet
    vampnet.MLPLobe
    vampnet.koopman_matrix
    vampnet.sym_inverse
    vampnet.covariances
    vampnet.score
    vampnet.loss
"""

from .tica import TICA
from .vamp import VAMP
from .koopman import KoopmanBasisTransform, IdentityKoopmanBasisTransform, KoopmanModel, CovarianceKoopmanModel
from ..util import module_available

if module_available("torch"):
    from .vampnet import VAMPNet
    from . import vampnet
del module_available
