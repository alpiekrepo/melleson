from odoo import api, fields, models, _


class ProductProduct(models.Model):
	_inherit = "product.template"

	max_packs = fields.Integer(
		string=_("Maximum amount of packs available"),
		compute="_compute_max_packs",
	)

	pack_components = fields.Many2one(
		comodel_name="product.product",
		default=None,
		compute="_compute_pack_components",
		store=True,
	)

	def _compute_pack_components(self):
		for r in self:
			if r.is_pack and r.pack_ids:
				r.pack_components = [item.product_id.id for item in r.pack_ids]

	@api.depends("pack_ids")
	def _compute_max_packs(self):
		for r in self:
			# The virtual inventory needs to be strictly more than 0 to be shown as non 0
			if r.is_pack and min(item.product_id.virtual_available for item in r.pack_ids) > 0: 
				r.max_packs = min([item.product_id.virtual_available / item.qty_uom for item in r.pack_ids])
			else:
				r.max_packs = 0
