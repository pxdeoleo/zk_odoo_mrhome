from odoo import models, fields, api, _
import logging
import urllib.parse as urlparse
import requests, json
from random import choice
from string import digits


_logger = logging.getLogger(__name__)

class HrJob(models.Model):
    _inherit = "hr.job"

    barcode = fields.Char(string="Code", groups="hr.group_hr_user", copy=False)

    def generate_random_barcode(self):
        for record in self:
            record.barcode = ''.join([choice(digits) for i in range(9)])

    @api.model
    def create(self, vals):
        res = super(HrJob, self).create(vals)

        if not res.barcode or len(res.barcode) > 9:
            res.generate_random_barcode()
        
        return res
    
    def write(self, vals):
        res = super(HrJob, self).write(vals)

        if not self.barcode or len(self.barcode) > 9:
            self.generate_random_barcode()
        return res

