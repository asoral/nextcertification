import frappe

def set_aplication(purchase, method):
    # print("---------------purchase", purchase)
    if not purchase.application:
        for res in purchase.references:
            if res.reference_doctype == 'Sales Invoice' and res.reference_name:
                doc = frappe.get_doc("Sales Invoice",res.reference_name)
                if doc.application:
                    purchase.application = doc.application
                    purchase.service_type = doc.service_type
                    purchase.application_type = doc.application_type
                    break
