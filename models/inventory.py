from odoo import api,fields,models

class Inventory(models.Model):
    _name= "inventory.inventory"
    _description=" an inventory module"

    name= fields.Char(string="name")
    quantity= fields.Integer(string="quantity")
    product_id = fields.Many2one('inventory.product', string="Product")
    mouvement_type = fields.Selection([('incoming','Incoming'),('outgoing','Outgoing')])

    