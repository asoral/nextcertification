
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.model.utils import get_fetch_values
from frappe.contacts.doctype.address.address import get_company_address
from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.website.website_generator import WebsiteGenerator
STANDARD_USERS = ("Guest", "Administrator","All")
class Application(WebsiteGenerator):


	def get_list_context(self, context):
		# context.introduction = _('EOI')
		context.no_cache = 1
		context.show_sidebar = True
		context.get_list = frappe.get_doc(frappe.form_dict.doctype, frappe.form_dict.name)
		context.title = _("Application")
		context.get_list.update({
			'show_sidebar': True,
			'show_search': True,
			'title': _('Application')
		})

	def get_options(self, arg=None):
		pass

	def validate(self):
		pass

	def onload(self):
		load_address_and_contact(self)

def get_list_context(context=None):
	return {
		"title": _("Application"),
		"show_sidebar": True,
		"show_search": True,
		'no_breadcrumbs': True

	}

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

