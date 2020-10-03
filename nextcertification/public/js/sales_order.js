
frappe.ui.form.on("Sales Order", {
     setup: function(frm) {
		frm.add_fetch("application", "registration_no", "registration_no");
	},

    refresh:function(frm){
        if(frm.doc.docstatus ==1){
            frm.add_custom_button(__('Application'),function() {
                return frappe.call({
                    method: 'nextcertification.sales_order.make_application',
                    args:{
                     doc_name:frm.doc.name
                    },
                    callback: function(r) {
                        var doc = frappe.model.sync(r.message);
                        frappe.set_route("Form", doc[0].doctype, doc[0].name);
                    }
                });
            }, __("Create"));
        }
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
                method: "nextcertification.sales_order.check_registration_req",
                args: {
                    doctype: "Service Types",
                    name: frm.doc.service_type
                    },
                callback:function(r) {
                    if(r.message.registration == 1)
                    {
                    frm.set_df_property("registration_no", "hidden", 0);
                    frm.set_df_property("registration_no", "reqd", 1);

                    frm.refresh_field("registration_no")
                    }
                    else
                    {
                    frm.set_df_property("registration_no", "hidden", 1);
                    frm.refresh_field("registration_no")
                    }
                }
            })
        }


});
