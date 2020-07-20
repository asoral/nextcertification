
frappe.ui.form.on('Application', {
    // Get Item From (sales order) in Application
	refresh: function(frm) {
		    if (frm.doc.docstatus === 0 ){
            frm.add_custom_button(__('Sales Order'),function() {
                erpnext.utils.map_current_doc({
                    method: "nextcertification.nextcertification.doctype.application.application.make_sales_order",
                    source_doctype: "Sales Order",
                    date_field: "transaction_date",
                    target: frm,
                    setters: {
                        customer: frm.doc.customer || undefined,
                        status: frm.doc.status || undefined,
                         },
                    get_query_filters: {
                        docstatus: 1,
                        status: ["not in", ["Closed", "On Hold"]],
//                        company: frm.doc.company
                    }
                })
            }, __("Get items from"));
        };

        if(frm.doc.docstatus === 1){
	        frm.page.add_inner_button(__("Print"), function() {
		    frm.print_doc();
	        });
        }

	},

        //Evaluation Check List
        "checklist_tc" : function(frm) {
            frappe.call({
                "method": "frappe.client.get",
                args: {
                    doctype: "Terms and Conditions",
                    name: frm.doc.checklist_tc
                },
                callback: function (data) {
                    frappe.model.set_value(frm.doctype,
                        frm.docname, "conditions_tc",
                        data.message.terms
                        )
                }
            })
        },
        "section" : function(frm) {
            frm.set_query('product_category', function(doc) {
                return {
                    filters: {'section': frm.doc.section}
                };
            });
        },
        "product_category" : function(frm) {
            frm.set_query('sub_category', function(doc) {
                return {
                    filters: {'product_category': frm.doc.product_category}
                };
            });
        },
        "service_type" : function(frm){
       // console.log('-------- frm status doc ------',frm.doc.docstatus);
          frappe.call({
                method: "nextcertification.nextcertification.doctype.application.application.check_section_certificate",
                args: {
                    doctype: "Service Types",
                    name: frm.doc.service_type
                    },
                callback:function(r) {
                    if(r.message.certificate == 1)
                    {
                    frm.set_df_property("section_break_certificates", "hidden", 0);
                    frm.refresh_field("section_break_certificates")
                    }
                    else
                    {
                    frm.set_df_property("section_break_certificates", "hidden", 1);
                    frm.refresh_field("section_break_certificates")
                    }
                    if(r.message.audit == 1){
                    frm.set_df_property("section_break_ap", "hidden", 0);
                    frm.refresh_field("section_break_ap")
                    }
                    else
                    {
                    frm.set_df_property("section_break_ap", "hidden", 1);
                    frm.refresh_field("section_break_ap")
                    }
                }
            })
        }

//    refresh:function(frm){
//        if(frm.doc.docstatus === 1){
//	        frm.page.add_inner_button(__("Print"), function() {
//		    frm.print_doc();
//	        });
//        }
//    }

});

