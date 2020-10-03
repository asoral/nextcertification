# -*- coding: utf-8 -*-
# Copyright (c) 2020, Sameer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.model.utils import get_fetch_values
from frappe.contacts.doctype.address.address import get_company_address
from erpnext.stock.doctype.item.item import get_item_defaults
from erpnext.setup.doctype.item_group.item_group import get_item_group_defaults

class ProductTestReport(Document):
	def get_options(self, arg=None):
		pass

	def validate(self):
		pass


@frappe.whitelist()

def get_products(source_name, target_doc=None):
	def set_item_in_product_test_report(source,target):
		pt_report = frappe.get_doc(target)
		application = frappe.get_doc(source)

	doclist = get_mapped_doc("Application", source_name, {
		"Application": {
			"doctype": "Product Test Report",
			  "validation": {
			#  	"docstatus": ["=", 1]
			#	  "status": "to verify"
			  }
		},
		"Product": {
			"doctype": "Test Report Product Child",
			"field_map": {
				"name": "t_brand_name",
				"brand_name":"p_brand_name",
				"manufacturer":"manufacturer",
				"model_no":"model_no",
				"parent": "application",
			},

		},

	}, target_doc,set_item_in_product_test_report)
	return doclist

