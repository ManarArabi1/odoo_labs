from odoo import models, fields, api, exceptions


class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient', string='Related Patient', groups='hms.group_user')
    vat = fields.Char(string='Tax ID', required=True)

    @api.constrains('email')
    def _check_unique_email(self):
        for partner in self:
            if partner.email and self.env['hms.patient'].search_count([('email', '=', partner.email)]):
                raise exceptions.ValidationError('Email address already exists in patient records.')

    @api.constrains('related_patient_id')
    def _check_related_patient(self):
        for partner in self:
            if partner.related_patient_id:
                raise exceptions.ValidationError('Cannot delete customer linked to a patient.')
