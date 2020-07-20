
frappe.ui.form.on("Sales Order", {
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
});
