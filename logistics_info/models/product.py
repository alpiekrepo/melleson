from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    alpiek_length = fields.Integer(
        string=_('Length (mm)'),
        required=False
    )
    alpiek_width = fields.Integer(
        string=_('Width (mm)'),
        required=False
    )
    alpiek_height = fields.Integer(
        string=_('Height (mm)'),
        required=False
    )
    alpiek_amount_in_box = fields.Integer(
        string=_('Amount in a box'),
        required=False
    )
    alpiek_number_of_boxes_per_layer = fields.Integer(
        string=_('Number of boxes per layer'),
        required=False
    )
    alpiek_number_of_layers_per_pallet = fields.Integer(
        string=_('Number of layers per pallet'),
        required=False
    )
    alpiek_weight_package_plastic_new = fields.Float(
        string=_('Verpakkingsgewicht Plastic'),
        required=False
    )
    alpiek_weight_package_paper_new = fields.Float(
        string=_('Verpakkingsgewicht Karton'),
        required=False
    )
    alpiek_weight_package_al_new = fields.Float(
        string=_('Verpakkingsgewicht Aluminium'),
        required=False
    )

