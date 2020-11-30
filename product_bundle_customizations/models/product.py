from odoo import api, fields, models, _


class ProductProduct(models.Model):
	_inherit = 'product.template'

	max_packs = fields.Integer(
		string=_("Maximum amount of packs available"),
		compute="_compute_max_packs",
	)

	@api.depends('pack_ids')
	def _compute_max_packs(self):
		for r in self:
			if r.is_pack:
				r.max_packs = min([item.product_id.qty_available / item.qty_uom for item in r.pack_ids])
