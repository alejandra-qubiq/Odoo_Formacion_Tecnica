from odoo import fields,models

class LibraryBookGenre(models.Model):
    _name = "library.book.genre"
    _description = "Model that registers book's genres"
    
    #Genre name
    genre = fields.Char(string="Genre")
    
    