# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    quotation_ref = fields.Char(string='Quotation', required=True, copy=False, readonly=True, index='trigram',
                          default=lambda self: _('New'), tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            company_id = vals.get('company_id', self.default_get(['company_id'])['company_id'])
            self_comp = self.with_company(company_id)
            if vals.get('quotation_ref', 'New') == 'New':
                vals['quotation_ref'] = self_comp.env['ir.sequence'].next_by_code('sale.order.quotation')
        return super(SaleOrder, self).create(vals_list)

    @api.depends('quotation_ref', 'name', 'partner_id')
    @api.depends_context('sale_show_partner_name')
    def _compute_display_name(self):
        if not self._context.get('sale_show_partner_name'):
            return super()._compute_display_name()
        for order in self:
            sales_name = order.name
            quote_name = order.quotation_ref
            if order.partner_id.name and order.state not in ['draft', 'sent']:
                sales_name += ' - ' + order.partner_id.name  # (partner name)
            elif order.partner_id.name and order.state in ['draft', 'sent']:
                quote_name += ' - ' + order.partner_id.name

            if order.state in ['draft', 'sent']:
                order.display_name = quote_name
            else:
                order.display_name = sales_name