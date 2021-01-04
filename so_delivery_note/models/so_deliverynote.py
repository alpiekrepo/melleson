# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import api , models ,fields


class SoDelivernote(models.Model):
    _inherit = "sale.order"

    delivernote = fields.Text("Delivery Note")

class DoDelivernote(models.Model):
    _inherit = "stock.picking"
    
    do_delivernote = fields.Text("Delivery Note")

    @api.model
    def create(self, vals):
        sale_obj = self.env['sale.order']
        if vals.get('origin',False):           
            sale_id = vals.get('origin')
            sale_order =sale_obj.search([('name','=',sale_id)],limit=1)
            if sale_order.delivernote:
                vals.update({'do_delivernote':sale_order.delivernote})
        return super(DoDelivernote, self).create(vals)
    

