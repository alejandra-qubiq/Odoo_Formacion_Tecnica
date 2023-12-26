from odoo import fields,models

class LibraryBookComponentLine(models.Model):
    _name = "library.book.component.line"
    _description = "Model that registers book's components"
    
    #Genre name
    name = fields.Char(string="Packs", 
    required=True
    )
    book_id = fields.One2many('book.library', string='Books', ondelete='cascade',inverse_name='pack_ids')
