{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','mail','contacts', 'project'],

    # always loaded
    'data': [
        'security/security.xml',
        'data/mail_reminder.xml',
        'data/ir_cron_reminder.xml',
        'data/mail_templates.xml',
        'data/update_validation.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/templates.xml',
        'views/sessions_templates.xml',
        'views/validate_template.xml',
        'views/registration_views.xml',
        'views/project_task_views.xml',

        'views/partner.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}