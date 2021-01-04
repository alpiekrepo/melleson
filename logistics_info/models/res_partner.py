from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    alpiek_aanmelding_nodig = fields.Boolean(required=False, string='Aanmelding nodig')
    alpiek_alleen_europallets = fields.Boolean(required=False, string='Alleen op europallets leveren')
    alpiek_fsc_code = fields.Boolean(required=False, string='FSC code op pallets')
    alpiek_sscc_nodig = fields.Boolean(required=False, string='SSCC code nodig')
    alpiek_heftruck = fields.Boolean(required=False, string='Heftruck aanwezig')
    alpiek_hoeksteunen = fields.Boolean(required=False, string='Hoeksteunen gebruiken')
    alpiek_laadklep = fields.Boolean(required=False, string='Leveren met laadklep')
    alpiek_levering_dinsdag = fields.Boolean(required=False, string='Dinsdag')
    alpiek_levering_donderdag = fields.Boolean(required=False, string='Donderdag')
    alpiek_levering_maandag = fields.Boolean(required=False, string='Maandag')
    alpiek_levering_vrijdag = fields.Boolean(required=False, string='Vrijdag')
    alpiek_levering_woensdag = fields.Boolean(required=False, string='Woensdag')
    alpiek_levering_zaterdag = fields.Boolean(required=False, string='Zaterdag')
    alpiek_levering_zondag = fields.Boolean(required=False, string='Zondag')
    alpiek_levertijd_window = fields.Char(required=False, string='Levertijd window')
    alpiek_logistieke_notes = fields.Text(
        required=False,
        string='Overige notities',
        help='Overige notities, die niet in bovenstaande velden opgenomen kunnen worden'
    )
    alpiek_pallets_ruilen = fields.Boolean(required=False, string='Europallets worden geruild')
    alpiek_palletwagen = fields.Boolean(required=False, string='Palletwagen bij levering')
    alpiek_sticker_lotnummer = fields.Boolean(required=False, string='Sticker op display met lotnummer')
    alpiek_van_lotnummer_voorzien = fields.Boolean(required=False, string='Produten voorzien van lotnummer')
    alpiek_vervoerder = fields.Many2one(
        'res.partner',
        required=False,
        string='Vervoerder'
    )
