# -*- coding: utf-8 -*-
# Copyright (c) 2020, Sameer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CERTIFICATEOFCONFORMITY(Document):
	pass

@frappe.whitelist()
def check_section_certificate(name=None):
	if name:
		dic={}
		service = frappe.get_doc("Service Types",name)
		dic['certificate'] = service.is_certificate_req
		dic['audit'] = service.is_audit
		return dic
	return False
