# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    rfq_ref = fields.Char(string='RFQ', required=True, copy=False, readonly=True, index='trigram',
                          default=lambda self: _('New'), tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            company_id = vals.get('company_id', self.default_get(['company_id'])['company_id'])
            self_comp = self.with_company(company_id)
            if vals.get('rfq_ref', 'New') == 'New':
                vals['rfq_ref'] = self_comp.env['ir.sequence'].next_by_code('purchase.order.rfq')
        return super(PurchaseOrder, self).create(vals_list)

    @api.depends('rfq_ref', 'name', 'partner_ref', 'amount_total', 'currency_id')
    @api.depends_context('show_total_amount')
    def _compute_display_name(self):
        for order in self:
            po_name = order.name
            rfq_name = order.rfq_ref
            if order.partner_ref and order.state in ['draft', 'state']:
                rfq_name += ' (' + order.partner_ref + ')'  # (ref)
            elif order.partner_ref and order.state not in ['draft', 'state']:
                po_name += ' (' + order.partner_ref + ')'  # (ref)
            if self.env.context.get('show_total_amount') and order.amount_total:
                po_name += ': ' + formatLang(self.env, order.amount_total, currency_obj=order.currency_id)

            if order.state in ['draft', 'sent']:
                order.display_name = rfq_name
            else:
                order.display_name = po_name