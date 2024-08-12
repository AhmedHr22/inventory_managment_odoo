from odoo import models,api,fields
import logging

_logger = logging.getLogger(__name__)

class Supplier(models.Model):
    _name = "inventory.supplier"
    _description = "a Supplier of the product"

    name = fields.Char(string="name")
    contact_info = fields.Integer(string="Telephone")
    is_stock_available = fields.Boolean(string="is stock available")
    supply_category = fields.Selection([('poor','Poor'),('medium','Medium'),('expensive','Expensive')])
    product_id  = fields.Many2many('inventory.product',string="products")
    
    # @api.model
    # def retreive_product_by_supplier(self):
    #     _logger.info('Entering retreive_product_by_supplier method')
    #     for rec in self:
    #         _logger.debug('Processing record: %s', rec)
    #     _logger.info('Exiting retreive_product_by_supplier method')
    #     return self
