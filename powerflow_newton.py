#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:sw=8:ts=8:si:et
# To use the above modeline in vim you must have "set modeline" in your .vimrc
#
# Filename: powerflow_newton.py
#
# Created on: 06. des. 2014
#
# Author: Eirik Haustveit
#
# Copyright (c) Eirik Haustveit, 2014
#
#
# This file is part of powerflow.
#
# powerflow is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# powerflow is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with libXplained. If not, see <http://www.gnu.org/licenses/>.
##

__author__ = "Eirik Haustveit"
__copyright__ = "Copyright 2014, Eirik Haustveit"
__credits__ = ["various"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Eirik Haustveit"
__email__ = "eirik@la2kta.net"
__status__ = "Development"


import numpy as np
"""
Implements a powerflow computation algorithm based on Newtons iterative method.

"""
a = np.arange(16).reshape((4,4))
b = np.arange(4)

print np.dot(a,b)


iteration = 1
maximum_iterations = 20
converged = False

while (not converged):
   if iteration >= maximum_iterations:
      print 'Failed to converge in ', iteration, ' iterations.'
      break
  
   print 'Performing iteration: ', iteration
  
   iteration = iteration + 1