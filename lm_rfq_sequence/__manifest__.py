# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
{
    'name': "RFQ and Purchase Order Sequence | Custom Sequence for RFQ",
    'summary': "Custom Sequence for RFQs on Purchase Orders.",
    'description': "This module customizes the sequence for Request for Quotations (RFQs) in Purchase Orders, allowing for a more organized and traceable procurement process.",
    'author': "Lema Core Technologies",
    'company': "Lema Core Technologies",
    'maintainer': "Lema Core Technologies",
    'website': "https://www.lemacore.com",
    'category': 'Custom Modules/Purchase',
    'version': '1.0',
    'depends': ['purchase'],
    'data': [
        'data/purchase_data.xml',

        'views/purchase_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
