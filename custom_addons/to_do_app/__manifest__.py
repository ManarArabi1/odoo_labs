# -- coding: utf-8 --

{
    'name': 'ToDo App',
    'version': '17.0.0.0',
    'category': 'Productivity',
    'summary': 'Manage your daily tasks',
    'description': """ This module allows users to manage their daily tasks in Odoo. """,
    'author': 'Manar Arabi',

    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/base_menus.xml',
        'views/todo_ticket.xml',
        # 'views/todo_kanban.xml',
        # 'views/todo_tree.xml',
        # 'views/todo_actions.xml',

        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
