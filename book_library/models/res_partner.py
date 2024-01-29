# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(
        compute='_compute_full_name',
        readonly=False, store=True
    )
    last_name = fields.Char(
        compute='_compute_full_name',
        readonly=False, store=True
    )
    partner = fields.Boolean(
        string='Library partner'
    )
    author = fields.Boolean(
        string="Author"
    )
    partner_number = fields.Char(
        string='Membership number: '
    )
    genre_ids = fields.Many2many(
        comodel_name='library.book.genre',
        relation='res_partner_book_genre_rel',
        column1='partner_id',
        column2='genre_id',
        string='Genres',
    )
    _sql_constraints = [
        ('partner_number_unique', 'unique (partner_number,company_id)', 'The Library Partner Code of contact must be unique per company !')
    ]

    def singup(self):
        self.write({'partner': True})

    def signout(self):
        self.write({'partner': False,
                    'partner_number': False})

    def unlink(self):
        for rec in self:
            if rec.partner:
                if self.env['book.borrowing'].search(
                    [('partner_id', '=', rec.id),
                     ('state', '=', 'borrowed')]):
                    raise UserError(
                        "The partner %s still has books to return" % rec.name)
        return super().unlink()

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

    def get_books(self):
        self.ensure_one()
        return self.env['book.borrowing'].search([('partner_id', '=', self.id),
                                              ('state', '=', 'borrowed')])