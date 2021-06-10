from odoo import models, fields


class CustomerDetails(models.TransientModel):
    _name = 'customer.details'
    address = fields.Text(string="Address")
    state = fields.Char(string='State')
    city = fields.Char(string='City')
    gst = fields.Char('GST Number:')

    def customer_details(self):
        active_id = self.env.context.get('active_id', False)
        active_ids = self.env.context.get('active_ids', False)
        active_model = self.env.context.get('active_model', False)
        cust_details = self.env['market.order'].browse(active_ids)
        number = self.gst
        add = self.address
        states = self.state
        citys = self.city

        cust_details.write({'gst_number': number})
        cust_details.write({'address_info': add})
        cust_details.write({'state_info': states})
        cust_details.write({'city_info': citys})



