from odoo import models, fields


class HMSDepartment(models.Model):
    _name = 'hms.department'
    _description = 'Hospital Department'

    name = fields.Char(required=True)
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    location = fields.Char(string='Location')
    hod_id = fields.Many2one('hms.doctor', string='Head of Department')
    contact_number = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    services_offered = fields.Text(string='Services Offered')
    patient_ids = fields.One2many('hms.patient', 'department_id')
    doctor_ids = fields.Many2many('hms.doctor')
