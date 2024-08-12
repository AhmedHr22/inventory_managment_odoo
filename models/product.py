from odoo import fields,models,api
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name="inventory.product"
    _description = "product in inventory"

    name = fields.Char(string="name")
    description = fields.Text(string="description")
    state = fields.Selection([('accept','Accept'),('decline','Decline'),('in progress','In Prgress'),('terminate','Terminate')])
    price = fields.Integer(string="price")
    color = fields.Char(string="color")
    creation_date = fields.Datetime(string="creation date",default=fields.Datetime.now)
    weight = fields.Integer(string="weight")
    shape = fields.Char(string="shape")
    quality = fields.Text(string="quality")
    details = fields.Text(string="details")
    postcode = fields.Char(string="postcode")
    tax = fields.Integer(string="tax")        
    stock_level = fields.Integer(string="stock Level")

    @api.constrains('stock_level')
    def check_stock_level(self):
        if(self.stock_level >10):
            raise ValidationError (" stock level must be under 10")
    
    @api.depends('price','tax')
    def compute_price_notax(self):
        for rec in self:
            rec.final_price = rec.price - ((rec.price * rec.tax)/100 )
    final_price = fields.Integer(string="price_without_tax",compute=compute_price_notax)
    
    def accept_action(self):
        self.state = 'accept'

    def decline_action(self):
        self.state = 'decline'

    def terminate_action(self):
        self.state = 'terminate'

    reorder_levels = fields.Integer(string='reorder levels')
    inventory_ids = fields.One2many("inventory.inventory", "product_id", string="Inventory")
    supplier_ids = fields.Many2many('inventory.supplier',string="suppliers")
    category_id = fields.Many2one('inventory.category',string="category", domain=[('postcode',">=",1000)])
    category_code = fields.Integer(string="category code",related="category_id.postcode")

    @api.model
    def check_reorder_levels(self):
        products = self.search([('stock_level', '<', 'reorder_levels')])  # corrected typo here
        for product in products:
            self.env['inventory.inventory'].create({
                'product_id': product.id,
                'quality': product.quality,
                'quantity': product.reorder_levels - product.stock_level  # corrected typo here
            })

    # @api.depends_context()
    # def write(self,vals):
    #     print(f" ======================================================/n context = {self.env.context}")
    #     return super(Product,self).write(vals)