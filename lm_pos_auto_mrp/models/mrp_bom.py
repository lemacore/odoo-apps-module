# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    is_auto_generate_mo = fields.Boolean(string='Auto Generate MO', default=False)

    @api.onchange('type')
    def _onchange_type(self):
        if self.type == 'phantom':
            self.is_auto_generate_mo = False
        self.is_auto_generate_mo = None
