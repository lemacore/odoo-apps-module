# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    pos_order_id = fields.Many2one('pos.order', string='Point of Sale Order', copy=False)