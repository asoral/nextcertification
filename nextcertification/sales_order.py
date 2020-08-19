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
        application.registration_no = doc.registration_no
        application.sales_order_id = doc.name
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


def add_sales_to_application(doc, method):
    if doc.application:
        app = frappe.get_doc('Application', doc.application)
        print("*************",app)
        if(app):
            app.sales_order_id = doc.name
            app.flags.ignore_validate_update_after_submit = True
            app.save(ignore_permissions=True)
