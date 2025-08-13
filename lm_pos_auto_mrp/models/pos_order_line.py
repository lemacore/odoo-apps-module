# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, SUPERUSER_ID


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    mrp_production_id = fields.Many2one('mrp.production', string='Manufacturing Order', copy=False)
    automation_mo_state = fields.Selection([
        ('draft', 'Create in draft'),
        ('confirmed', 'Create in confirmed'),
        ('done', 'Create and validate'),
    ], string='Automation Manufacturing Order', default='draft',
        related='order_id.config_id.automation_mo_state')

    def _prepare_manufacturing_order(self, company):
        productions = self.env['mrp.production']
        for line in self:
            # Skip lines without a configuration automation manufacturing order state
            if not line.automation_mo_state:
                print('Skipping line without automation MO state:', line.id)
                continue

            bom = self.env['mrp.bom']._bom_find(line.product_id, bom_type='normal', company_id=company.id)[
                line.product_id]
            print('Found BOM:', bom.id, 'for product:', line.product_id.id)
            if bom.is_auto_generate_mo and bom.picking_type_id:
                print('Creating production for line:', line.id)
                production = self.env['mrp.production'].with_user(SUPERUSER_ID).with_company(company).create({
                    'product_id': line.product_id.id,
                    'product_qty': line.qty,
                    'qty_producing': line.qty if self.automation_mo_state not in ['draft'] else False,
                    'bom_id': bom.id,
                    'picking_type_id': bom.picking_type_id.id,
                    'origin': f"Point of Sale: {line.order_id.session_id.name} - Order: {line.order_id.name}",
                    'pos_order_id': line.order_id.id,
                    'move_raw_ids': [],
                    'move_byproduct_ids': [],
                })
                move_lines = [
                    (0, 0, {
                        'product_id': bl.product_id.id,
                        'product_uom_qty': bl.product_qty * line.qty,
                        'quantity': bl.product_qty * line.qty if self.automation_mo_state != 'draft' else False,
                        'product_uom': bl.product_uom_id.id,
                        'picked': True if self.automation_mo_state != 'draft' else False,
                    })
                    for bl in bom.bom_line_ids
                ]
                move_byproduct_ids = [
                    (0, 0, {
                        'product_id': bp.product_id.id,
                        'product_uom_qty': bp.product_qty * line.qty,
                        'product_uom': bp.product_uom_id.id,
                    })
                    for bp in bom.byproduct_ids
                ]
                production.move_raw_ids = move_lines
                production.move_byproduct_ids = move_byproduct_ids

                line.mrp_production_id = production
                if self.automation_mo_state == 'done':
                    production.button_mark_done()
                elif self.automation_mo_state == 'confirmed':
                    production.action_confirm()
                elif self.automation_mo_state == 'draft':
                    continue
                productions |= production

        return productions
