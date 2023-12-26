from odoo import fields,models

class BookLibrary(models.Model):
    _name = "book.library"
    _description = "Model that registers books"
    _inherits = {'product.template': 'product_tmpl_id'}

    product_tmpl_id = fields.Many2one(
        comodel_name='product.template',
        string='Product Template'
    )
    
    # #Book name - Lo quitamos porque estamos heredando de product.template
    # name = fields.Char(string="Name", 
    # required=True, defaul="Book")
    
    
    # Book price
    price = fields.Float(string="Price")
    #Volume
    volume = fields.Integer(string='Volume')
    #Printed/Digital
    type = fields.Selection(
        string='Digital/Printed',
        selection=[('printed', 'Printed'), ('digital', 'Digital')])
    #URL to purchase
    url = fields.Char(string="Purchase from")
    #Check to see if the book was bought already
    is_bought = fields.Boolean(string='Bought')
    #Purchase date
    purchase_date = fields.Datetime(
        string='Date of purchase',
        default=fields.Datetime.now,
    )
     # Agrega el campo Many2one para la relación con el autor
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
    
    pack_ids = fields.Many2one('library.book.component.line', string='Packs',)