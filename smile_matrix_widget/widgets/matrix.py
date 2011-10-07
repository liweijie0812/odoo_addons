# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Smile. All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import random

from openerp.widgets import TinyInputWidget, register_widget
from openerp import validators

from openobject.widgets import JSSource, JSLink
from openobject.validators import BaseValidator


class MatrixValidator(BaseValidator):
    def _to_python(self, value, state):
        import pdb; set_trace()

    def _from_python(self, value, state):
        import pdb; set_trace()




class Matrix(TinyInputWidget):

    template = "/smile_matrix_widget/widgets/templates/matrix.mako"

    javascript = [
        JSLink("smile_matrix_widget", "javascript/matrix.js"),
        ]

    params = ['widget']


    def __init__(self, **attrs):
        name = 'matrix_%s' % (random.randint(0, 10000))
        super(Matrix, self).__init__(**attrs)
        self.validator = MatrixValidator()


    def set_value(self, value):
        self.default = value

    def save(self, **kw):
        import pdb; pdb.set_trace()
        return



register_widget(Matrix, ["matrix"])
