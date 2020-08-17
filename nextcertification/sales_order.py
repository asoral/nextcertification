import frappe
from frappe.model.document import Document

@frappe.whitelist()
def make_application(doc_name =None):
    if doc_name:
        doc = frappe.get_doc("Sales Order",doc_name)
        application =frappe.new_doc("Application")
        application.customer = doc.customer
        application.service_type = doc.service_type
        application.section = doc.section
        application.product_category = doc.product_category
        application.sub_category = doc.sub_category
        application.customer_name = doc.customer_name
        application.registration_no = doc.registration_no
        application.address_html = doc.address_display
        return application

@frappe.whitelist()
def check_registration_req(name=None):
	if name:
		dic={}
		service = frappe.get_doc("Service Types",name)
		dic['certificate'] = service.is_certificate_req
		dic['registration'] = service.is_registration_req
		return dic
	return False