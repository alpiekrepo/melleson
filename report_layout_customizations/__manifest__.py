# -*- coding: utf-8 -*-
{
    'name': 'Report layout customizations',
    'version': '13.0.1.0.0',
    'description': """
    Delivery Slip and Invoice modifications - separating 'Internal reference' and 'Product' in two columns
    """,
    'author': "Alpiek",
    'website': "https://alpiek.nl/",
    'depends': [
        'account',
        'stock',
    ],
    'data': [
        'report/account_report_templates.xml',
        'report/stock_report_templates.xml',
    ],
    'application': False,
    'license': u'OPL-1',
}
