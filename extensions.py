# -*- coding: utf-8 -*-
"""Academia-specific model extensions."""
from modules.base.model_inheritance import ModelExtension


class PartnerExtension(ModelExtension):
    """Redirect WhatsApp template delivery from a student to their parent."""

    _inherit = 'base.partner'
    _depends = ['whatsapp']

    def get_whatsapp_recipient(self):
        """Partner that should actually receive WhatsApp templates about this one.

        The student -> parent link is stored in ``parent_id``. NOTE: that field
        is also auto-written by the WhatsApp duplicate-partner linker
        (modules/whatsapp/services/partner_linking.py), so a duplicate-cluster
        link redirects to the cluster root as well — accepted trade-off.

        Never redirects to a company ('Related Company' is parent_id's base
        semantic) and falls back to the partner itself when the parent has no
        usable phone. Callers resolve this via
        modules.whatsapp.utils.phone.resolve_template_recipient, so the
        whatsapp module works unchanged when this module is not installed.
        """
        parent = self.parent_id
        if parent and not parent.is_company and (parent.phone or parent.mobile):
            return parent
        return self
