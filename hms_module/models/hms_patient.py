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
    age = fields.Integer(store=True)
    department_id = fields.Many2one('hms.department')
    doctor_ids = fields.Many2many('hms.doctor')
    state = fields.Selection([('undetermined', 'Undetermined'),
                              ('good', 'Good'),
                              ('fair', 'Fair'),
                              ('serious', 'Serious')])

    @api.depends('birth_date')
    def _compute_age(self):
        for patient in self:
            if patient.birth_date:
                patient.age = (fields.Date.today() - fields.Date.from_string(patient.birth_date)).days // 365

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
