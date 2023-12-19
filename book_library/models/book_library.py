from odoo import fields,models

class BookLibrary(models.Model):
    _name = "book.library"
    _description = "Model that registers books"
    
    #Book name
    name = fields.Char(string="Name")
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
    
    