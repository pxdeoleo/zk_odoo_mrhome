from odoo import api, fields, models, _
import logging
import urllib.parse as urlparse
import requests, json
from random import choice
from string import digits

_logger = logging.getLogger(__name__)

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def generate_random_barcode(self):
        for record in self:
            record.barcode = ''.join([choice(digits) for i in range(9)])

    @api.model
    def create(self, vals):
        res = super(HrEmployee, self).create(vals)

        if not res.barcode or len(res.barcode) > 9:
            res.generate_random_barcode()
        
        # res._post_to_biotime()
        return res
    
    def write(self, vals):
        res = super(HrEmployee, self).write(vals)

        if not self.barcode or len(self.barcode) > 9:
            self.generate_random_barcode()
            
        return res
    
