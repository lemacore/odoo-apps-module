# -*- coding: utf-8 -*-
# from odoo import http


# class LmSalesQuotationSequence(http.Controller):
#     @http.route('/lm_sales_quotation_sequence/lm_sales_quotation_sequence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lm_sales_quotation_sequence/lm_sales_quotation_sequence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lm_sales_quotation_sequence.listing', {
#             'root': '/lm_sales_quotation_sequence/lm_sales_quotation_sequence',
#             'objects': http.request.env['lm_sales_quotation_sequence.lm_sales_quotation_sequence'].search([]),
#         })

#     @http.route('/lm_sales_quotation_sequence/lm_sales_quotation_sequence/objects/<model("lm_sales_quotation_sequence.lm_sales_quotation_sequence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lm_sales_quotation_sequence.object', {
#             'object': obj
#         })

