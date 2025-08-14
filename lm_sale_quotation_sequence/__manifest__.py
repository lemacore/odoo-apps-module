# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
{
    'name': "Quotation Order Sequence | Custom Sequence for Quotation Order",
    'summary': "Quotation Sequence, Custom Sequence for Quotation Order, Difference Sequence Quotation, Sale Order Sequence Separator, Quotation Number, Quotation Order Number, Quotation Reference",
    'description': """
This module customizes the sequence for Sales Quotation Orders, allowing for a more organized and traceable sales process.
It modifies the sequence of sales orders to include a unique reference number for each quotation, enhancing tracking and management capabilities.
    """,
    'author': "Lema Core Technologies",
    'company': "Lema Core Technologies",
    'maintainer': "Lema Core Technologies",
    'website': "https://www.lemacore.com",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['sale_management'],
    'data': [
        'data/sale_data.xml',
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
