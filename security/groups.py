# -*- coding: utf-8 -*-
"""
Security groups for academia_extension module

This file defines all security groups for the academia_extension module.
Groups are synced to the database using the sync_groups management command.
"""

GROUPS = [
    {
        'name': 'Academia_extension Users',
        'technical_name': 'academia_extension.users',
        'category': 'Academia_extension',
        'description': 'Access academia_extension module',
    },
    {
        'name': 'Academia_extension Admins',
        'technical_name': 'academia_extension.admins',
        'category': 'Academia_extension',
        'implied_groups': ['academia_extension.users'],
        'description': 'Manage all academia_extension module',
    }
]
