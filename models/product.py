from odoo import fields,models,api
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name="inventory.product"
    _description = "product in inventory"

    name = fields.Char(string="name")
    description = fields.Text(string="description")
    price = fields.Integer(string="price")
    color = fields.Char(string="color")
    creation_date = fields.Datetime(string="creation date",default=fields.Datetime.now)
    weight = fields.Integer(string="weight")
    shape = fields.Char(string="shape")
    quality = fields.Text(string="quality")
    details = fields.Text(string="details")
    postcode = fields.Char(string="postcode")
    tax = fields.Integer(string="tax")

    # def compute_stock_level(self):
    #     for rec in self:
            
    # stock_level = fields.Integer(string="stock Level",compute=compute_stock_level)

    @api.constrains('stock_level')
    def check_stock_level(self):
        if(self.stock_level >10):
            raise ValidationError (" stock level must be under 10")
        
    
    @api.depends('price','tax')
    def compute_price_notax(self):
        for rec in self:
            rec.final_price = rec.price - ((rec.price * rec.tax)/100 )
    final_price = fields.Integer(string="price_without_tax",compute=compute_price_notax)
    
    @api.depends_context()
    def write(self,vals):
        print(f" ======================================================/n context = {self.env.context}")
        return super(Product,self).write(vals)


    supplier_ids = fields.Many2many('inventory.supplier',string="suppliers")
    category_id = fields.Many2one('inventory.category',string="category", domain=[('postcode',">=",1000)])
    category_code = fields.Integer(string="category code",related="category_id.postcode")

    
