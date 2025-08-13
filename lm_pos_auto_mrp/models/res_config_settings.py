# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api

class PosConfig(models.Model):
    _inherit = 'pos.config'

    automation_mo_state = fields.Selection([
        ('draft', 'Create in draft'),
        ('confirmed', 'Create in confirmed'),
        ('done', 'Create and validate'),
    ], string='Automation Manufacturing Order',
        default='draft',
        required=True,
    )


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    automation_mo_state = fields.Selection([
        ('draft', 'Create in draft'),
        ('confirmed', 'Create in confirmed'),
        ('done', 'Create and validate'),
    ], string='Automation Manufacturing Order',
        related='pos_config_id.automation_mo_state',
        readonly=False)
