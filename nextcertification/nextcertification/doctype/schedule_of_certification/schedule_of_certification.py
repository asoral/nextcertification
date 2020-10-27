# -*- coding: utf-8 -*-
# Copyright (c) 2020, Sameer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class SCHEDULEOFCERTIFICATION(Document):
	def get_options(self, arg=None):
		pass

	def validate(self):
		pass

@frappe.whitelist()
def get_test_products(source_name, target_doc=None):
	def set_item_in_product_test_report(source,target):
		soc = frappe.get_doc(target)
		test_report = frappe.get_doc(source)

	doclist = get_mapped_doc("Product Test Report", source_name, {
		"Application": {
			"doctype": "SCHEDULE OF CERTIFICATION",
			  "validation": {
			  	#"docstatus": ["=", 0]
				  "status": "To Verify"
			  }
		},
		"Product Test Report": {
			"doctype": "SCO Test Report",
			"field_map": {
				"name": "name",
				"p_brand_name":"brand_name",
				"manufacturer":"manufacturer",
				"model_no":"model_no",

			},
		},

	}, target_doc,set_item_in_product_test_report)
	return doclist

@frappe.whitelist()
def check_section_certificate(name=None):
	if name:
		dic={}
		service = frappe.get_doc("Service Types",name)
		dic['certificate'] = service.is_certificate_req
		dic['audit'] = service.is_audit
		return dic
	return False

@frappe.whitelist()
def check_is_for_all_report(name=None):
	if name:
		dic={}
		service = frappe.get_doc("Product Category",name)
		dic['certificate'] = service.is_one_certificate
		return dic
	return False

@frappe.whitelist()
def fetch_product(application, test_report):
	products = frappe.db.sql(""" select brand_name, model_number, description, country_of_origin from `tabProduct` where parent= %(parent)s 
				and product_test_eport = %(tp)s or product_test_report_2 = %(tp)s or product_test_report_3 = %(tp)s""",
				  {'parent':application,'tp':test_report},as_dict=1)
	return products