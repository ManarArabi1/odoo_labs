from odoo import models, fields


class HMSDoctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Hospital Doctor'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    image = fields.Binary()

    # Additional fields
    specialty = fields.Selection([
        ('pediatrician', 'Pediatrician'),
        ('cardiologist', 'Cardiologist'),
        ('dermatologist', 'Dermatologist'),
        ('neurologist', 'Neurologist'),
        ('orthopedic_surgeon', 'Orthopedic Surgeon'),
        ('oncologist', 'Oncologist'),
        ('psychiatrist', 'Psychiatrist'),
        ('urologist', 'Urologist'),
        ('gynecologist', 'Gynecologist'),
        ('ophthalmologist', 'Ophthalmologist'),
        ('dentist', 'Dentist'),
        ('general_practitioner', 'General Practitioner'),
        ('other', 'Other'),
    ], string='Specialty')

    contact_number = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    qualifications = fields.Text(string='Qualifications')
    schedule = fields.Text(string='Schedule')
