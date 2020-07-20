import frappe
from frappe.model.document import Document

@frappe.whitelist()
def make_application(doc_name =None):
    if doc_name:
        doc = frappe.get_doc("Sales Order",doc_name)
        application =frappe.new_doc("Application")
        application.customer = doc.customer
       # application.status = doc.status
        return application

