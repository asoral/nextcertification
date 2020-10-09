// Copyright (c) 2020, Sameer and contributors
// For license information, please see license.txt

frappe.ui.form.on('SCHEDULE OF CERTIFICATION', {

    refresh: function(frm) {
        if( frm.doc.docstatus === 1){
            frm.set_df_property("application", "readonly", 1),
            frm.refresh_field("application")
            frm.set_df_property("click_to", "hidden", 1);
            frm.refresh_field("click_to")
        };
    },
	  "application" : function(frm, cdt, cdn) {
            frm.set_query('test_report', function(doc){
                return {
                    filters: {
                    'application':frm.doc.application,
                     'docstatus': 1
                    }

                };
            });

            frm.set_query('test_report_child', function(doc){
                return {
                    filters: {
                    'application':frm.doc.application,
                     'docstatus': 1
                    }
                };
            });

            frappe.call({
                method: "nextcertification.nextcertification.doctype.schedule_of_certification.schedule_of_certification.check_section_certificate",
                args: {
                    doctype: "Service Types",
                    name: frm.doc.service_type
                    },
                callback:function(r) {
                    if(r.message.certificate == 1)
                    {
                    frm.set_df_property("sb_certificate", "hidden", 0);
                    frm.refresh_field("sb_certificate")
                    frm.set_df_property("sb_qrcode", "hidden", 0);
                    frm.refresh_field("sb_qrcode")
                    frm.set_df_property("sb_product", "hidden", 0);
                    frm.refresh_field("sb_product")
                    frm.set_df_property("sb_no_certifiate", "hidden", 1);
                    frm.refresh_field("sb_no_certifiate")
                    }
                    else
                    {
                    frm.set_df_property("sb_certificate", "hidden", 1);
                    frm.refresh_field("sb_certificate")
                    frm.set_df_property("sb_qrcode", "hidden", 1);
                    frm.refresh_field("sb_qrcode")
                    frm.set_df_property("sb_product", "hidden", 1);
                    frm.refresh_field("sb_product")
                    frm.set_df_property("sb_no_certifiate", "hidden", 0);
                    frm.refresh_field("sb_no_certifiate")
                     }
                }
            });

            frappe.call({
                method: "nextcertification.nextcertification.doctype.schedule_of_certification.schedule_of_certification.check_is_for_all_report",
                args: {
                    doctype: "Product Category",
                    name: frm.doc.product_category
                    },
                callback:function(r) {
                    if(r.message.certificate == 1)
                    {
                    frm.set_df_property("test_report", "hidden", 1);
                    frm.refresh_field("test_report")
                    frm.set_df_property("test_report_child", "hidden", 0);
                    frm.refresh_field("test_report_child")
//                    frm.set_df_property("click_to", "hidden", 0);
                    frm.refresh_field("click_to")
                    frm.set_value("is_one",1)
                    frm.refresh_field("is_one")
                    }
                    else
                    {
                    frm.set_df_property("test_report", "hidden", 0);
                    frm.refresh_field("test_report")
                    frm.set_df_property("test_report_child", "hidden", 1);
                    frm.refresh_field("test_report_child")
//                    frm.set_df_property("click_to", "hidden", 1);
                    frm.refresh_field("click_to")
                    frm.set_value("is_one",0)
                    frm.refresh_field("is_one")
                     }
                }
            });
      },

  "test_report":  function(frm, cdt, cdn) {
     frm.doc.product = []
     frappe.call({
        method: "frappe.client.get",
        args: {
            name: frm.doc.test_report,
            doctype: "Product Test Report"
        },
        callback(r) {
            if (r.message) {
                for (var row in r.message.products) {
                    var child = frm.add_child("product_test");
                    frappe.model.set_value(child.doctype, child.name, "brand_name", r.message.products[row].p_brand_name);
                    frappe.model.set_value(child.doctype, child.name, "model_no", r.message.products[row].model_number);
                    frappe.model.set_value(child.doctype, child.name, "country", r.message.products[row].country_of_origin);
                    frappe.model.set_value(child.doctype, child.name, "description", r.message.products[row].description);
                    frm.refresh_field("product_test");
                }
            }
        }
     })
  },

  click_to: function(frm, cdt, cdn) {
        if(frm.doc.docstatus != 1) {
               frm.doc.product = []
                  frappe.call({
                     method: "nextcertification.nextcertification.doctype.schedule_of_certification.schedule_of_certification.fetch_product",
                     args: {
                        application: frm.doc.application,
                     },
                     callback(r) {
                        if (r.message) {
                        console.log("product",r.message);
                        var array = r.message;
                        var array_len = array.length;
                        for (var i=0; i< array_len; i++){
                            console.log("array",array[i]['brand_name']);
                            var child = frm.add_child("product_test");
                            child.brand_name = array[i]['brand_name'];
                            child.model_no = array[i]['model_number'];
                            child.description = array[i]['description'];
                            child.country = array[i]["country_of_origin"];
                        }
                        frm.refresh_fields();
                        }
                     }
                  })
            }
  },

});
