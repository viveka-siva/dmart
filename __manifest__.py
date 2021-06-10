# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'D-Mart',
    'version': '0.1',
    'summary': 'D Mart - SuperMarket',
    'description': """ Second test Customer Bills
    """,
    'depends': ['base'],
    'data': [
        'wizard/customer_details.xml',
        'security/ir.model.access.csv',
        'views/orderlines.xml',
        'views/product.xml',
        'views/orders.xml',
    ],
    'installable': True,
    'auto_install': False
}