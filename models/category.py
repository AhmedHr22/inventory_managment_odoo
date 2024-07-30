from odoo import fields,api,models


class Category(models.Model):
    _name="inventory.category"
    _description = "a category for the product"

    name = fields.Char(string="name")
    product_ids = fields.One2many('inventory.product','category_id',string="product_id")
    postcode = fields.Integer(string="postcode")
    