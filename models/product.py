from odoo import models, fields, api


class Product(models.Model):
    _name = 'market.product'
    name = fields.Char(string="Product List")
    quantity = fields.Integer(string='Quantity')
    price = fields.Integer(string='Price')
    location = fields.Char(string='Location')
    # orderline = fields.One2many('order.line', 'orderlines_id', string='Orderline')

