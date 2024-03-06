# -- coding: utf-8 --

{
    'name': 'Hospital Management System',
    'version': '17.0.0.0',
    'category': 'Services',
    'summary': 'Hospital Management System for managing departments, doctors, and patients.',
    'author': 'Manar Arabi',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/hms_security.xml',
        'views/res_partner.xml',
        'views/hms_department_views.xml',
        'views/hms_doctors_views.xml',
        'views/hms_patient_views.xml',
    ],
    'installable': True,
    'application': True,
}
