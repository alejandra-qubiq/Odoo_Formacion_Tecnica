from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    partner = fields.Boolean(string='Library partner')
    author = fields.Boolean (string="Author")
    partner_number = fields.Integer(string='Membership number: ')
    genre_ids = fields.Many2many(
        comodel_name='library.book.genre',
    )
