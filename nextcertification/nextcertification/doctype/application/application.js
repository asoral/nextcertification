
frappe.ui.form.on('Application', {
    // Get Item From (sales order) in Application
    onload: function(frm) {

//        cur_frm.page.menu.find("a:contains("+__("Email")+")").on('click', function() {
//           setTimeout(() => {
//               $('*[data-fieldname="subject"]').val("Test subject")
//           },500);
//        });

        frm.fields_dict['product'].grid.get_field("product_test_eport").get_query =
                function(doc, cdt, cdn) {
                  var child = locals[cdt][cdn];
                    return {
                     filters: [
                     ['Product Test Report','application','=',frm.doc.name]
                 ]
              }
          }
          frm.fields_dict['product'].grid.get_field("product_test_report_2").get_query =
                function(doc, cdt, cdn) {
                  var child = locals[cdt][cdn];
                    return {
                     filters: [
                     ['Product Test Report','application','=',frm.doc.name]
                 ]
              }
          }
          frm.fields_dict['product'].grid.get_field("product_test_report_3").get_query =
                function(doc, cdt, cdn) {
                  var child = locals[cdt][cdn];
                    return {
                     filters: [
                     ['Product Test Report','application','=',frm.doc.name]
                 ]
              }
          }
    },

    setup: function(frm) {
		frm.add_fetch("sales_order", "registration_no", "registration_no");
	},
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
                        status: ["not in", ["Closed", "Draft"]],
                        company: frm.doc.company
                    }
                })
            }, __("Get items from"));
        };
        if (!frm.doc.__islocal && frm.doc.docstatus == 0 )
        {
            if(frm.doc.resume_time == 0 ){
                frm.add_custom_button(__('Start Time'), function () {
                    return frappe.call({
                        method: 'nextcertification.nextcertification.doctype.application.application.start_time',
                        args: {
                            doc_name: frm.doc.name
                        },
                        callback: function() {
                            frm.reload_doc();
                        }
                    });
                }).addClass("btn-primary");
            }
            else{
                frm.add_custom_button(__('Stop Time'), function () {
                    return frappe.call({
                        method: 'nextcertification.nextcertification.doctype.application.application.resume_time',
                        args: {
                            doc_name: frm.doc.name
                        },
                        callback: function() {
                            frm.reload_doc();
                        }
                    });
                }).addClass("btn-primary");
            }
        }
	},

	after_save: function(frm){

       frm.call('create_prod_rep').then(() => {
            frm.refresh();
        });



//         $.each(frm.doc["product_test_reports"],function(i, product_test_reports)
//            {
//                if(product_test_reports.attach_document){
//                    frm.call({
//                                method: "nextcertification.nextcertification.doctype.application.application.update_test_report_name",
//                                args: {
//                                    name: product_test_reports.description,
//
//                                   },
//                                callback: function(r) {
//                                    if(r.message) {
////                                        frm.refresh_field("product_test_reports");
//                                    }
//                                }
//                            });
//                }
//            });
//            frappe.ui.toolbar.clear_cache();
    },

        //Evaluation Check List
//        "checklist_tc" : function(frm) {
//            frappe.call({
//                "method": "frappe.client.get",
//                args: {
//                    doctype: "Terms and Conditions",
//                    name: frm.doc.checklist_tc
//                },
//                callback: function (data) {
//                    frappe.model.set_value(frm.doctype,
//                        frm.docname, "conditions_tc",
//                        data.message.terms
//                        )
//                }
//            })
//        },
//        "section" : function(frm) {
//            frm.set_query('product_category', function(doc) {
//                return {
//                    filters: {'section': frm.doc.section}
//                };
//            });
//        },
//        is_eesl_req : function(frm) {
//            if (frm.doc.is_eesl_req == 1 ){
//                console.log("****");
//                 frm.fields_dict.product.grid.toggle_reqd("rating", frm.doc.is_eesl_req == 1);
//                 frm.fields_dict.product.grid.toggle_reqd("model_number", frm.doc.is_eesl_req == 1);
//            }
//        },


});

//frappe.ui.form.on('Customer Product Test Report', {
//
//    description: function(frm, cdt, cdn) {
//            var arr = [];
//        var child = locals[cdt][cdn];
//        arr.push(child.description);
//        var df = frappe.meta.get_docfield("Product","parent", frm.doc.name);
//        df.product_test_eport = ["Tech M", "Wipro", "TCS"];
//    },
//});