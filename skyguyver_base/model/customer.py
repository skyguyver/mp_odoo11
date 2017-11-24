# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, tools, models, _
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)

class Customer(models.Model):
    _name = 'gunit.customer'
    _description = 'Customer'

    # This function will reduce the size of any attached picture to 128x128px suitable for Kanban views
    @api.depends('picture')
    def _reduce_customer_picture(self):
        for rec in self:
            rec.picture = tools.image_resize_image_medium(rec.picture)

    # customer picture portrait
    picture = fields.Binary('Picture', help='Attached picture will automatically be re-sized to 128x128px')

    name = fields.Char(index=True)
    date = fields.Date(index=True)
    title = fields.Many2one('res.partner.title')
    # address_ids = fields.One2many(comodel_name='mp.customer_address', inverse_name='customer_id', string='Customer address')
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(comodel_name='res.country.state', string='State', ondelete='restrict')
    zip = fields.Char()
    country_id = fields.Many2one(comodel_name='res.country', string='Country', ondelete='restrict')
    date_of_birth = fields.Date()
    phone = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    website = fields.Char(help="Website of Partner or Company")