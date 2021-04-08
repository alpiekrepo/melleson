# -*- coding: utf-8 -*-
{
    'name' : 'Sale Order Delivery Note',
    'author' : 'Softhealer Technologies',
    'website': 'http://www.softhealer.com',
    "support": "support@softhealer.com",        
    'category': 'Sales',
	'summary': """sale order delivery note odoo, quotation delivery note app, print quotation delivery slip, delivery note of picking, print so delivery note module, print quote delivery note odoo
	""",    
    'description': """Useful to define Delivery Note in quotation and print in Picking Operations and Delivery Slip
""",    
    'version':'13.0.1',
    'depends' : ['sale_management','stock'],
    'application' : True,
    'data' : ['views/so_delivernote_view.xml',
              'reports/sale_report.xml',
              ],
    'images': ['static/description/background.jpg',],              
    'auto_install':False,
    'installable' : True,
    "price": 15,
    "currency": "EUR"      
}
