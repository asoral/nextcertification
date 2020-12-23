# -*- coding: utf-8 -*-
# Copyright (c) 2020, Sameer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
import json
from datetime import datetime

class SCHEDULEOFCERTIFICATION(Document):
	def get_options(self, arg=None):
		pass

	def before_insert(self):
		self.append("timer",{
			'start_time': datetime.now()
		})
		self.resume_time = 1

	def before_submit(self):
		for res in self.timer:
			if not res.end_time:
				res.end_time = datetime.now()
		self.resume_time = 0

		query = frappe.db.sql("""select start_time from `tabCertificte Schedule Time` where parent = %s order by start_time limit 1""",(self.name), as_list=True)
		if query:
			total_seconds = (datetime.now() - query[0][0]).total_seconds()
			if total_seconds:
				self.total_time = total_seconds/60
		self.db_update()

@frappe.whitelist()
def start_time(doc_name):
	doc = frappe.get_doc("SCHEDULE OF CERTIFICATION",doc_name)
	doc.append("timer", {
		'start_time': datetime.now()
	})
	doc.resume_time = 1
	doc.save(ignore_permissions=True)

@frappe.whitelist()
def resume_time(doc_name):
	doc = frappe.get_doc("SCHEDULE OF CERTIFICATION", doc_name)
	query = frappe.db.sql("""select name from `tabCertificte Schedule Time` where parent = %s order by start_time desc limit 1""",(doc.name),as_list=True)
	if query:
		doc_child = frappe.get_doc("Certificte Schedule Time",query[0][0])
		doc_child.end_time = datetime.now()
		doc_child.db_update()
	doc.resume_time = 0
	doc.db_update()


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
def fetch_product(application, test_reports=None,test_report=None):
	report_lst =[]
	if test_reports:
		json_data = json.loads(test_reports)
		for j in json_data:
			report_lst.append(j['test_report_child'])
	if test_report:
		report_lst.append(test_report)
	products = frappe.db.sql(""" select brand_name, manufacturer, product_test_eport, product_test_report_2, 
				product_test_report_3, annual_energy_consumption, rating, model_number, 
				country_of_origin, description, soc_print, coc_print, applicable_standards_1, 
				applicable_standards_3, applicable_standards_5, applicable_standards_7, applicable_standards_9, 
				applicable_standards_11, applicable_standards_13, applicable_standards_15, applicable_standards_17, 
				applicable_standards_19, applicable_standards_21, applicable_standards_23, applicable_standards_25, 
				applicable_standards_27, applicable_standards_29, applicable_standards_31, applicable_standards_33, 
				applicable_standards_35, applicable_standards_37, applicable_standards_39, applicable_standards_41, 
				applicable_standards_43, applicable_standards_45, applicable_standards_47, applicable_standards_49, 
				applicable_standards_2, applicable_standards_4, applicable_standards_6, applicable_standards_8,
				applicable_standards_10, applicable_standards_12, applicable_standards_14, 
				applicable_standards_16, applicable_standards_18, applicable_standards_20, 
				applicable_standards_22, applicable_standards_24, applicable_standards_26, 
				applicable_standards_28, applicable_standards_30, applicable_standards_32, 
				applicable_standards_34, applicable_standards_36, applicable_standards_38, 
				applicable_standards_40, applicable_standards_42, applicable_standards_44, 
				applicable_standards_46, applicable_standards_48, applicable_standards_50 from `tabProduct` where parent= %(parent)s
				and product_test_eport in %(tp)s or product_test_report_2 in %(tp)s or product_test_report_3 in %(tp)s""",
				{'parent':application,'tp':report_lst},as_dict=1)
	return products