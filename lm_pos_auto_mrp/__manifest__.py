# -*- coding: utf-8 -*-
# Copyright 2025 Lema Core Technologies
# Part of Lema Core Technologies. See LICENSE file for full copyright and licensing details.
{
    'name': "POS Auto MRP | Manufacturing Order Automation",
    'summary': "Automation of Manufacturing Orders from Point of Sale Orders",
    'description': """This module automates the creation of Manufacturing Orders (MO) from Point of Sale (POS) orders.""",
    'author': "Lema Core Technologies",
    'company': "Lema Core Technologies",
    'maintainer': "Lema Core Technologies",
    'website': "https://www.lemacore.com",
    'category': 'Manufacturing',
    'version': '1.0',
    'depends': ['point_of_sale', 'mrp'],
    'data': [
        'views/pos_order_views.xml',
        'views/mrp_bom_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
