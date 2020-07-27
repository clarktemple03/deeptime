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



def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration('sktime', parent_package, top_path)

    config.add_subpackage('clustering')
    config.add_subpackage('covariance')
    config.add_subpackage('data')
    config.add_subpackage('decomposition')
    config.add_subpackage('markov')
    config.add_subpackage('numeric')

    from Cython.Build import cythonize
    config.ext_modules = cythonize(
        config.ext_modules,
        compiler_directives={'language_level': '3'})

    return config