# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _


class PosOrder(models.Model):
    _inherit = 'pos.order'

    mrp_production_ids = fields.One2many('mrp.production', 'pos_order_id', string='Manufacturing Orders')
    mrp_production_count = fields.Integer(compute='_compute_mrp_production_count', string='Manufacturing Orders Count')

    # create MO when order is paid
    def action_pos_order_paid(self):
        res = super(PosOrder, self).action_pos_order_paid()
        for order in self:
            order._create_manufacturing_order()
        return res

    def _create_manufacturing_order(self):
        for order in self:
            company_id = order.config_id.company_id or order.env.company
            productions = self.env['mrp.production']
            for line in order.lines:
                productions |= line._prepare_manufacturing_order(company_id)
            if productions:
                order.mrp_production_ids |= productions

    def _compute_mrp_production_count(self):
        for order in self:
            if order.mrp_production_ids:
                order.mrp_production_count = len(order.mrp_production_ids)
            else:
                order.mrp_production_count = 0

    def action_open_production(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Manufacturing Orders'),
            'res_model': 'mrp.production',
            'view_mode': 'list,kanban,form',
            'domain': [('id', 'in', self.mrp_production_ids.ids)],
            'context': {
                'create': False,
                'delete': False,
            },
            'target': 'current',
        }