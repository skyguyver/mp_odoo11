# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)

class customers(models.Model):
    _name = 'mp.customer'

    def test_func(self):
        obj_sequence = self.pool.get('ir.sequence')
        _logger.warning('XXXXXXX:' + str(obj_sequence));

    name = fields.Char()
    # address_ids = fields.One2many(comodel_name='mp.customer_address', inverse_name='customer_id', string='Customer address')
    street1 = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one(comodel_name='res.country.state', string='State', ondelete='restrict')
    zip = fields.Char()
    country_id = fields.Many2one(comodel_name='res.country', string='Country', ondelete='restrict')
    date_of_birth = fields.Date()
    phone = fields.Char(size=20, string="Phone")
    mobile = fields.Char(size=20, string="Mobile")
    email = fields.Char(size=40, string="Email")
    acct_ids = fields.One2many(comodel_name='mp.customer_acct', inverse_name='customer_id', string="Accounts")

class customer_acct(models.Model):
    _name = 'mp.customer_acct'

    @api.model
    def create(self, vals):
        if vals.get('acct_no', _('New')) == _('New'):
            vals['acct_no'] = self.env['ir.sequence'].next_by_code('customer_acct.acctno.sequence') or _('New')
        result = super(customer_acct, self).create(vals)
        return result

    name = fields.Char(related='customer_id.name', string='Customer')
    acct_no = fields.Char(size=20, string='Account number', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    passport = fields.Char(size=20, string='Passport')
    passport_expiry = fields.Date(string='Expiry')
    date_activated = fields.Date(string='Date activated')
    customer_id = fields.Many2one(comodel_name='mp.customer', string='Customer', ondelete='restrict')
    comments = fields.Char()
    state = fields.Selection([
        ('New', 'New'),
        ('Active', 'Active')
        ], string="Status", default="New")
