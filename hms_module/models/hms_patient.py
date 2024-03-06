from odoo import models, fields, api, exceptions


class HMSPatient(models.Model):
    _name = 'hms.patient'
    _description = 'Hospital Patient'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(
        [
            ('a', 'A'),
            ('b', 'B'),
            ('o', 'O'),
        ]
    )
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(store=True, compute='_compute_age')
    department_id = fields.Many2one('hms.department')
    doctor_ids = fields.Many2many('hms.doctor')
    state = fields.Selection([('undetermined', 'Undetermined'),
                              ('good', 'Good'),
                              ('fair', 'Fair'),
                              ('serious', 'Serious')])
    email = fields.Char(string='Email', unique=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                delta = relativedelta(fields.Date.today(), fields.Date.from_string(patient.birth_date))
                patient.age = delta.years

    @api.constrains('pcr', 'cr_ratio')
    def _check_pcr_cr_ratio(self):
        for patient in self:
            if patient.pcr and not patient.cr_ratio:
                raise exceptions.ValidationError('CR Ratio must be specified if PCR is checked.')

    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 30:
            self.pcr = True

    @api.onchange('department_id')
    def _onchange_department_id(self):
        if self.department_id:
            self.doctor_ids = self.department_id.doctor_ids

    @api.constrains('email')
    def _check_unique_email(self):
        for patient in self:
            if patient.email and self.search([('email', '=', patient.email), ('id', '!=', patient.id)]):
                raise exceptions.ValidationError('Email address must be unique.')
