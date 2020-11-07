// Copyright (c) 2020, Sameer and contributors
// For license information, please see license.txt

frappe.ui.form.on('Product Test Report', {
	 refresh: function(frm) {
		    if (frm.doc.docstatus === 0 ){
                frm.add_custom_button(__('Application'),function() {
                    erpnext.utils.map_current_doc({
                        method: "nextcertification.nextcertification.doctype.product_test_report.product_test_report.get_products",
                        source_doctype: "Application",
                       // date_field: "date",
                        target: frm,
                        setters: {
                            customer: frm.doc.customer || undefined,
                            status: frm.doc.status || undefined,

                        },
                        get_query_filters: {
//                            docstatus : 1,
                            name: frm.doc.application || undefined,
                        //   status: ["not in", ["Approved", "Rejected","Draft"]]
                           // company: frm.doc.company
                        }
                    })
                }, __("Get items from"));
        }
     }
});
