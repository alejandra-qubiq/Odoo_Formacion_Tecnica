# Copyright 2024 Alejandra García <alejandra.gracia@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import datetime


class BookLibrary(models.Model):
    _name = "book.library"
    _description = "Model that registers books"
    _inherits = {'product.template': 'product_tmpl_id'}

    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string='Product Template',
    )
    price = fields.Float()
    volume = fields.Integer()
    type = fields.Selection(
        string='Digital/Printed',
        selection=[
            ('printed', 'Printed'),
            ('digital', 'Digital')]
    )
    url = fields.Char(
        string="Purchase from"
    )
    is_bought = fields.Boolean(
        string='Bought'
    )
    purchase_date = fields.Datetime(
        string='Date of purchase',
        default=fields.Datetime.now,
    )
    author_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[('author', '=', True)],
        help="Select the author of the book."
    )
    genre_ids = fields.Many2many(
        comodel_name='library.book.genre',
    )
    is_pack = fields.Boolean(
        string='Pack',
    )
    pack_ids = fields.Many2one(
        'library.book.component.line',
        string='Packs',
    )
    record_id = fields.One2many(comodel_name='library.audit', inverse_name='book_id', string='Audit')

    @api.onchange('author_id')
    def _onchange_author_id(self):
        if self.author_id.genre_ids:
            self.genre_ids = self.author_id.genre_ids

    @api.constrains('price')
    def _check_price_is_not_zero(self):
        for record in self:
            if record.price <= 0:
                raise UserError("The price must be greater than 0")

    @api.model_create_multi
    def create(self, vals):
        current_user = self.env.user
        for rec in self:
            audit_vals = {
                'book_id': rec.id,
                'operation': 'create',
                'user_id': current_user.id,
                'date': datetime.now(),
            }
            self.env['library.audit'].create(audit_vals)
        result = super().create(vals)
        result.write({'detailed_type': 'product'})
        return result

    def write(self, vals):
        current_user = self.env.user
        for rec in self:
            audit_vals = {
                'book_id': rec.id,
                'operation': 'write',
                'user_id': current_user.id,
                'date': datetime.now(),
            }
            self.env['library.audit'].create(audit_vals)
        result = super().write(vals)
        return result

    def unlink(self):
        current_user = self.env.user
        for rec in self:
            audit_vals = {
                'book_id': rec.id,
                'operation': 'unlink',
                'user_id': current_user.id,
                'date': datetime.now(),
            }
            self.env['library.audit'].create(audit_vals)
        result = super().unlink()
        return result
