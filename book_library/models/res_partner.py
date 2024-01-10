from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(
        compute='_compute_full_name',
        readonly=False,
    )
    last_name = fields.Char(
        compute='_compute_full_name',
        readonly=False,
    )
    partner = fields.Boolean(
        string='Library partner'
    )
    author = fields.Boolean()
    partner_number = fields.Integer(
        string='Membership number: '
    )
    genre_ids = fields.Many2many(
        comodel_name='library.book.genre',
    )

    @api.depends('name')
    def _compute_full_name(self):
        for record in self:
            record.first_name = record.name.split(' ')[0]
            record.last_name = record.name.split(' ')[1]
            return record

    @api.onchange('first_name', 'last_name')
    def _onchange_first_last_name(self):
        if not self.first_name or not self.last_name:
            self.name = ''
        else:
            self.name = f'{self.first_name} {self.last_name}'
