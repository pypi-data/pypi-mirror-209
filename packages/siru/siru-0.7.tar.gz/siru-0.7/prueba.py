#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################################################################
# Copyright (c) 2022-2023, Laboratorio de Microprocesadores
# Facultad de Ciencias Exactas y Tecnología, Universidad Nacional de Tucumán
# https://www.microprocesadores.unt.edu.ar/
#
# Copyright (c) 2022-2023, Esteban Volentini <evolentini@herrera.unt.edu.ar>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
# OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2023, Esteban Volentini <evolentini@herrera.unt.edu.ar>
##################################################################################################

from siru.preat import Preat, Result
from siru.gpio import Output, Input

port = "/dev/tty.usbserial-14430"
preat = Preat(port)

OUT_1 = Output(preat, 0)
OUT_2 = Output(preat, 1)
OUT_3 = Output(preat, 2)
OUT_4 = Output(preat, 3)
OUT_5 = Output(preat, 4)
OUT_6 = Output(preat, 5)

IN_1 = Input(preat, 0)
IN_2 = Input(preat, 1)
IN_3 = Input(preat, 2)
IN_4 = Input(preat, 4)
IN_5 = Input(preat, 5)
IN_6 = Input(preat, 3)

print("\r\nTesting input IN_1 by changing output OUT_1...")
assert OUT_1.clear() == Result.NO_ERROR
assert preat.wait(0, 50, [IN_1.has_falling], OUT_1.set) == Result.NO_ERROR
assert preat.wait(0, 50, [IN_1.has_rising], OUT_1.clear) == Result.NO_ERROR

print("\r\nTesting input IN_2 by changing output OUT_2...")
assert OUT_2.clear() == Result.NO_ERROR
assert preat.wait(0, 50, [IN_2.has_falling], OUT_2.set) == Result.NO_ERROR
assert preat.wait(0, 50, [IN_2.has_rising], OUT_2.clear) == Result.NO_ERROR

print("\r\nTesting input IN_3 by changing output OUT_3...")
assert OUT_3.clear() == Result.NO_ERROR
assert preat.wait(0, 50, [IN_3.has_falling], OUT_3.set) == Result.NO_ERROR
assert preat.wait(0, 50, [IN_3.has_rising], OUT_3.clear) == Result.NO_ERROR

print("\r\nTesting input IN_4 by changing output OUT_4...")
assert OUT_4.clear() == Result.NO_ERROR
assert preat.wait(0, 50, [IN_4.has_falling], OUT_4.set) == Result.NO_ERROR
assert preat.wait(0, 50, [IN_4.has_rising], OUT_4.clear) == Result.NO_ERROR

print("\r\nTesting input IN_5 by changing output OUT_5...")
assert OUT_5.clear() == Result.NO_ERROR
assert preat.wait(0, 50, [IN_5.has_falling], OUT_5.set) == Result.NO_ERROR
assert preat.wait(0, 50, [IN_5.has_rising], OUT_5.clear) == Result.NO_ERROR

print("\r\nTesting input IN_6 by changing output OUT_6...")
assert OUT_6.clear() == Result.NO_ERROR
assert preat.wait(0, 50, [IN_6.has_falling], OUT_6.set) == Result.NO_ERROR
assert preat.wait(0, 50, [IN_6.has_rising], OUT_6.clear) == Result.NO_ERROR
