
frappe.ui.form.on("Sales Invoice", {
//    refresh:function(frm){
//        if(frm.doc.docstatus ==1){
//            frm.add_custom_button(__('Application'),function() {
//                return frappe.call({
//                    method: 'nextcertification.sales_order.make_application',
//                    args:{
//                     doc_name:frm.doc.name
//                    },
//                    callback: function(r) {
//                        var doc = frappe.model.sync(r.message);
//                        frappe.set_route("Form", doc[0].doctype, doc[0].name);
//                    }
//                });
//            }, __("Create"));
//        }
//	},

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

});
