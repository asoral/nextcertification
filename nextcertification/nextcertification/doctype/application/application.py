
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.model.utils import get_fetch_values
from frappe.contacts.doctype.address.address import get_company_address
from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils.user import is_website_user
from datetime import datetime

STANDARD_USERS = ("Guest", "Administrator","All")
class Application(WebsiteGenerator):

	def before_insert(self):
		self.append("timer",{
			'start_time': datetime.now()
		})
		self.resume_time = 1

	# def before_submit(self):
	# 	for res in self.timer:
	# 		if not res.end_time:
	# 			res.end_time = datetime.now()
	# 	self.resume_time = 0
	#
	# 	query = frappe.db.sql("""select start_time from `tabCertificte Schedule Time` where parent = %s order by start_time limit 1""",(self.name), as_list=True)
	# 	if query:
	# 		total_seconds = (datetime.now() - query[0][0]).total_seconds()
	# 		if total_seconds:
	# 			self.total_time = total_seconds/60
		# self.db_update()

	def get_options(self, arg=None):
		pass

	def validate(self):
		if self.workflow_state == "Sent For Senior Conformity Engineer Approval":
			if not self.checklist_tc:
				frappe.throw("Checklist Is Mandatory")
			if not self.eval_attachment:
				frappe.throw("Checklist Files Is Mandatory")
			for itm in self.product:
				if self.is_eesl_req != 0:
					if not itm.rating:
						frappe.throw("Rating Is Mandatory")
				if self.is_eesl_req != 0:
					if not itm.annual_energy_consumption:
						frappe.throw("Annual Energy Consumption Is Mandatory")
				if not itm.country_of_origin:
					frappe.throw("Country of Origin Is Mandatory")
				if not itm.model_number :
					frappe.throw("Model Number Is Mandatory")
				if not itm.description:
					frappe.throw("Description Is Mandatory")
				if not itm.manufacturer:
					frappe.throw("manufacturer Is Mandatory")
				if not itm.brand_name:
					frappe.throw("brand_name Is Mandatory")
				if not itm.applicable_standards_1:
					frappe.throw("Applicable Standards 1 Is Mandatory")

	def onload(self):
		load_address_and_contact(self)

	def create_prod_rep(self):
		for i in self.product_test_reports:
			if i.description and i.attach_document:
				if not frappe.db.exists("Product Test Report", i.description):
					pro_test = frappe.new_doc("Product Test Report")
					pro_test.application = self.name
					pro_test.test_report_no = i.description
					pro_test.save(ignore_permissions = True)
		for j in self.product:
			if j.product_test_eport or j.product_test_report_2 or j.product_test_report_3 and j.updated == 0:
				if j.product_test_eport:
					pro_test1 = frappe.get_doc("Product Test Report",j.product_test_eport)
					pro_test1.append('products', {
						"p_brand_name": j.brand_name,
						"manufacturer": j.manufacturer,
						"product_test_eport": j.product_test_eport,
						"annual_energy_consumption": j.annual_energy_consumption,
						"model_number" : j.model_number,
						"country_of_origin": j.country_of_origin,
						"description": j.description,
						"applicable_standards_1": j.applicable_standards_1,"applicable_standards_2": j.applicable_standards_2,
						"applicable_standards_3": j.applicable_standards_3,"applicable_standards_4": j.applicable_standards_4,
						"applicable_standards_5": j.applicable_standards_5,"applicable_standards_6": j.applicable_standards_6,
						"applicable_standards_7": j.applicable_standards_7,"applicable_standards_8": j.applicable_standards_8,
						"applicable_standards_9": j.applicable_standards_9,"applicable_standards_10": j.applicable_standards_10,
						"applicable_standards_11": j.applicable_standards_11,"applicable_standards_12": j.applicable_standards_12,
						"applicable_standards_13": j.applicable_standards_13,"applicable_standards_14": j.applicable_standards_14,
						"applicable_standards_15": j.applicable_standards_15,"applicable_standards_16": j.applicable_standards_16,
						"applicable_standards_17": j.applicable_standards_17,"applicable_standards_18": j.applicable_standards_18,
						"applicable_standards_19": j.applicable_standards_19,"applicable_standards_20": j.applicable_standards_20,
						"applicable_standards_21": j.applicable_standards_21,"applicable_standards_22": j.applicable_standards_22,
						"applicable_standards_23": j.applicable_standards_23,"applicable_standards_24": j.applicable_standards_24,
						"applicable_standards_25": j.applicable_standards_25,"applicable_standards_26": j.applicable_standards_26,
						"applicable_standards_27": j.applicable_standards_27,"applicable_standards_28": j.applicable_standards_28,
						"applicable_standards_29": j.applicable_standards_29,"applicable_standards_30": j.applicable_standards_30,
						"applicable_standards_31": j.applicable_standards_31,"applicable_standards_32": j.applicable_standards_32,
						"applicable_standards_33": j.applicable_standards_33,"applicable_standards_34": j.applicable_standards_34,
						"applicable_standards_35": j.applicable_standards_35,"applicable_standards_36": j.applicable_standards_36,
						"applicable_standards_37": j.applicable_standards_37,"applicable_standards_38": j.applicable_standards_38,
						"applicable_standards_39": j.applicable_standards_39,"applicable_standards_40": j.applicable_standards_40,
						"applicable_standards_41": j.applicable_standards_41,"applicable_standards_42": j.applicable_standards_42,
						"applicable_standards_43": j.applicable_standards_43,"applicable_standards_44": j.applicable_standards_44,
						"applicable_standards_45": j.applicable_standards_45,"applicable_standards_46": j.applicable_standards_46,
						"applicable_standards_47": j.applicable_standards_47,"applicable_standards_48": j.applicable_standards_48,
						"applicable_standards_49": j.applicable_standards_49,"applicable_standards_50": j.applicable_standards_50,
					})
					pro_test1.save(ignore_permissions = True)

				if j.product_test_report_2:
					pro_test2 = frappe.get_doc("Product Test Report", j.product_test_report_2)
					pro_test2.append('products', {
						"p_brand_name": j.brand_name,
						"manufacturer": j.manufacturer,
						"product_test_eport": j.product_test_eport,
						"annual_energy_consumption": j.annual_energy_consumption,
						"model_number": j.model_number,
						"country_of_origin": j.country_of_origin,
						"applicable_standards": j.applicable_standards_1,
						"description": j.description
					})
					pro_test2.save(ignore_permissions=True)
				if j.product_test_report_2:
					pro_test3 = frappe.get_doc("Product Test Report", j.product_test_report_2)
					pro_test3.append('products', {
						"p_brand_name": j.brand_name,
						"manufacturer": j.manufacturer,
						"product_test_eport": j.product_test_eport,
						"annual_energy_consumption": j.annual_energy_consumption,
						"model_number": j.model_number,
						"country_of_origin": j.country_of_origin,
						"applicable_standards": j.applicable_standards_1,
						"description": j.description
					})
					pro_test3.save(ignore_permissions=True)
				frappe.db.sql(""" update `tabProduct` set updated = 1 where name = %(name)s """,{'name':j.name})
				frappe.db.commit()
		self.reload()


def get_list_context(context=None):
	return {
		"title": _("Application"),
		"get_list": get_issue_list,
		"show_sidebar": True,
		"show_search": True,
		'no_breadcrumbs': True

	}

def get_issue_list(doctype, txt, filters, limit_start, limit_page_length=20, order_by=None):
	from frappe.www.list import get_list

	user = frappe.session.user
	contact = frappe.db.get_value("Contact", {"user": user}, "name")
	customer = frappe.db.get_value("Customer", {"email_id": user}, "name")

	# if contact:
	# 	contact_doc = frappe.get_doc("Contact", contact)
	# 	customer = contact_doc.get_link_for("Customer")
	# if customer:


	ignore_permissions = False
	if is_website_user():
		if not filters: filters = {}

		if customer:
			filters["customer"] = customer
		else:
			filters["mail_id"] = user

		ignore_permissions = True

	return get_list(doctype, txt, filters, limit_start, limit_page_length, ignore_permissions=ignore_permissions)

def has_website_permission(doc, ptype, user, verbose=False):
	from erpnext.controllers.website_list_for_contact import has_website_permission
	permission_based_on_customer = has_website_permission(doc, ptype, user, verbose)

	return permission_based_on_customer or doc.mail_id==user

@frappe.whitelist()
def make_sales_order(source_name, target_doc=None, ignore_permissions=False):
	def postprocess(source, target):
		set_missing_values(source, target)
		if target.get("allocate_advances_automatically"):
			target.set_advances()

	def set_missing_values(source, target):
		target.ignore_pricing_rule = 1
		target.flags.ignore_permissions = True
		target.run_method("set_missing_values")
		target.run_method("set_po_nos")
		target.run_method("calculate_taxes_and_totals")


		if source.company_address:
			target.update({'company_address': source.company_address})
		else:
			# set company address
			target.update(get_company_address(target.customer))

		if target.company_address:
			target.update(get_fetch_values("Sales Invoice", 'company_address', target.company_address))

		if source.loyalty_points and source.order_type == "Shopping Cart":
			target.redeem_loyalty_points = 1

	def update_item(source, target, source_parent):
		target.item_tax_template = source.item_tax_template


		if source_parent.customer:
			target.customer = source_parent.customer
			target.sales_order = source_parent.name
			target.service_type = source_parent.service_type
			target.section = source_parent.section
			target.product_category = source_parent.product_category
			target.sub_category = source_parent.sub_category


	doclist = get_mapped_doc("Sales Order", source_name, {
		"Sales Order": {
			"doctype": "Application",
			"validation": {
				"docstatus": ["=", 1]
			}
		},

	}, target_doc, postprocess, ignore_permissions=ignore_permissions)

	return doclist

@frappe.whitelist()
def create_application(source_name, target_doc=None):

	def set_item_in_application(source,target):
		sale_order = frappe.get_doc(source)
		application = frappe.get_doc(target)

	doc = get_mapped_doc('Sales Order', source_name, {
		'Sales Order': {
			'doctype': 'Application',
			'validation': {
				'docstatus': ['=', 1]
			}
		},
	}, target_doc,set_item_in_application)

@frappe.whitelist()
def check_section_certificate(name=None):
	if name:
		dic={}
		service = frappe.get_doc("Service Types",name)
		dic['certificate'] = service.is_certificate_req
		dic['audit'] = service.is_audit
		dic['registration'] = service.is_registration_req
		return dic
	return False

def add_app_to_sales(doc, method):
    if doc.sales_order_id:
        app = frappe.get_doc('Sales Order', doc.sales_order_id)
        if(app):
            app.application = doc.name
            app.flags.ignore_validate_update_after_submit = True
            app.save(ignore_permissions=True)

@frappe.whitelist()
def prod_cat_eesl(product_category):
	pc = frappe.get_doc("Product Category", product_category)
	if pc.is_eesl_req == 1:
		return 1

@frappe.whitelist()
def update_test_report_name(name):
	# print("****************************************************************")
	frappe.db.sql(""" update `tabCustomer Product Test Report` set description = %(name)s where name = %(name)s 
	 """,{'name':name})
	frappe.db.commit()


@frappe.whitelist()
def start_time(doc_name):
	doc = frappe.get_doc("Application",doc_name)
	doc.append("timer", {
		'start_time': datetime.now()
	})
	doc.resume_time = 1
	doc.save(ignore_permissions=True)

@frappe.whitelist()
def resume_time(doc_name):
	doc = frappe.get_doc("Application", doc_name)
	query = frappe.db.sql("""select name from `tabCertificte Schedule Time` where parent = %s order by start_time desc limit 1""",(doc.name),as_list=True)
	if query:
		doc_child = frappe.get_doc("Certificte Schedule Time",query[0][0])
		doc_child.end_time = datetime.now()
		doc_child.db_update()
	doc.resume_time = 0
	doc.db_update()

