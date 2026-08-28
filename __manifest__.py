# -*- coding: utf-8 -*-
{
    'name': 'Academia Extension',
    'technical_name': 'academia_extension',
    'type': 'app',
    'summary': 'Academia customizations: deliver WhatsApp templates about a student to the linked parent',
    'description': """
Customer-specific academia customizations.

Redirects WhatsApp template delivery from a student partner to the parent
partner linked through ``parent_id`` (falls back to the student's own number
when no usable parent is linked). Template variables still render from the
student record; only the delivery target changes.
""",
    'author': "Genie ERP",
    'website': "https://www.aigeniecrm.com",
    'category': 'Academia',
    'version': '0.0.1',
    'depends': ['whatsapp'],
    'application': False,
    'installable': True,
    'auto_install': False,
}
