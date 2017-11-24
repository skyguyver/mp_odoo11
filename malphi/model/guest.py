# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import Warning

_logger = logging.getLogger(__name__)

class GuestCustomer(models.Model):
    _inherit = 'gunit.customer'

    passport = fields.Char('Passport')
    # def test_func(self):
    #     obj_sequence = self.pool.get('ir.sequence')
    #     _logger.warning('XXXXXXX:' + str(obj_sequence));


# class customer_acct(models.Model):
#     _name = 'mp.customer_acct'

    # @api.model
    # def create(self, vals):
    #     if vals.get('acct_no', _('New')) == _('New'):
    #         vals['acct_no'] = self.env['ir.sequence'].next_by_code('customer_acct.acctno.sequence') or _('New')
    #     result = super(customer_acct, self).create(vals)
    #     return result

    # name = fields.Char(related='customer_id.name', string='Customer')
    # acct_no = fields.Char(size=20, string='Account number', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    # passport = fields.Char(size=20, string='Passport')
    # passport_expiry = fields.Date(string='Expiry')
    # date_activated = fields.Date(string='Date activated')
    # customer_id = fields.Many2one(comodel_name='dc.customer', string='Customer', ondelete='restrict')
    # comments = fields.Char()
    # state = fields.Selection([
    #     ('New', 'New'),
    #     ('Active', 'Active')
    #     ], string="Status", default="New")