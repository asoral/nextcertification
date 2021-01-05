// Copyright (c) 2020, Sameer and contributors
// For license information, please see license.txt

frappe.ui.form.on('SCHEDULE OF CERTIFICATION', {

    onload: function(frm){
         frm.set_query('test_report', function(frm){
                return {
                    filters: {
                    'application':frm.doc.application,
                    }

                };
            });
    },

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
                    'application':frm.doc.application
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

//  "test_report":  function(frm, cdt, cdn) {
//     frm.doc.product = []
//     frappe.call({
//        method: "frappe.client.get",
//        args: {
//            name: frm.doc.test_report,
//            doctype: "Product Test Report"
//        },
//        callback(r) {
//            if (r.message) {
//                for (var row in r.message.products) {
//                    var child = frm.add_child("product_test");
//                    frappe.model.set_value(child.doctype, child.name, "brand_name", r.message.products[row].p_brand_name);
//                    frappe.model.set_value(child.doctype, child.name, "model_no", r.message.products[row].model_number);
//                    frappe.model.set_value(child.doctype, child.name, "country", r.message.products[row].country_of_origin);
//                    frappe.model.set_value(child.doctype, child.name, "description", r.message.products[row].description);
//                    frm.refresh_field("product_test");
//                }
//            }
//        }
//     })
//  },

  click_to: function(frm, cdt, cdn) {
        if(frm.doc.docstatus != 1) {
               frm.doc.product = []
                  frappe.call({
                     method: "nextcertification.nextcertification.doctype.schedule_of_certification.schedule_of_certification.fetch_product",
                     args: {
                        application: frm.doc.application,
                        test_reports: frm.doc.test_report_child,
                        test_report: frm.doc.test_report
                     },
                     callback(r) {
                        if (r.message)
                        {
                            var array = r.message;
                            var array_len = array.length;
                            frm.set_value('product_test', []);
                            for (var i=0; i< array_len; i++)
                            {
                                var child = frm.add_child("product_test");
                                child.brand_name=array[i]['brand_name'];
                                child.manufacturer=array[i]['manufacturer'];
                                child.product_test_eport=array[i]['product_test_eport'];
                                child.product_test_report_2=array[i]['product_test_report_2'];
                                child.product_test_report_3=array[i]['product_test_report_3'];
                                child.annual_energy_consumption=array[i]['annual_energy_consumption'];
                                child.rating=array[i]['rating'];
                                child.model_number=array[i]['model_number'];
                                child.country_of_origin=array[i]['country_of_origin'];
                                child.description=array[i]['description'];
                                child.soc_print=array[i]['soc_print'];
                                child.coc_print=array[i]['coc_print'];
                                child.applicable_standards_1=array[i]['applicable_standards_1'];
                                child.applicable_standards_3=array[i]['applicable_standards_3'];
                                child.applicable_standards_5=array[i]['applicable_standards_5'];
                                child.applicable_standards_7=array[i]['applicable_standards_7'];
                                child.applicable_standards_9=array[i]['applicable_standards_9'];
                                child.applicable_standards_11=array[i]['applicable_standards_11'];
                                child.applicable_standards_13=array[i]['applicable_standards_13'];
                                child.applicable_standards_15=array[i]['applicable_standards_15'];
                                child.applicable_standards_17=array[i]['applicable_standards_17'];
                                child.applicable_standards_19=array[i]['applicable_standards_19'];
                                child.applicable_standards_21=array[i]['applicable_standards_21'];
                                child.applicable_standards_23=array[i]['applicable_standards_23'];
                                child.applicable_standards_25=array[i]['applicable_standards_25'];
                                child.applicable_standards_27=array[i]['applicable_standards_27'];
                                child.applicable_standards_29=array[i]['applicable_standards_29'];
                                child.applicable_standards_31=array[i]['applicable_standards_31'];
                                child.applicable_standards_33=array[i]['applicable_standards_33'];
                                child.applicable_standards_35=array[i]['applicable_standards_35'];
                                child.applicable_standards_37=array[i]['applicable_standards_37'];
                                child.applicable_standards_39=array[i]['applicable_standards_39'];
                                child.applicable_standards_41=array[i]['applicable_standards_41'];
                                child.applicable_standards_43=array[i]['applicable_standards_43'];
                                child.applicable_standards_45=array[i]['applicable_standards_45'];
                                child.applicable_standards_47=array[i]['applicable_standards_47'];
                                child.applicable_standards_49=array[i]['applicable_standards_49'];
                                child.applicable_standards_2=array[i]['applicable_standards_2'];
                                child.applicable_standards_4=array[i]['applicable_standards_4'];
                                child.applicable_standards_6=array[i]['applicable_standards_6'];
                                child.applicable_standards_8=array[i]['applicable_standards_8'];
                                child.applicable_standards_10=array[i]['applicable_standards_10'];
                                child.applicable_standards_12=array[i]['applicable_standards_12'];
                                child.applicable_standards_14=array[i]['applicable_standards_14'];
                                child.applicable_standards_16=array[i]['applicable_standards_16'];
                                child.applicable_standards_18=array[i]['applicable_standards_18'];
                                child.applicable_standards_20=array[i]['applicable_standards_20'];
                                child.applicable_standards_22=array[i]['applicable_standards_22'];
                                child.applicable_standards_24=array[i]['applicable_standards_24'];
                                child.applicable_standards_26=array[i]['applicable_standards_26'];
                                child.applicable_standards_28=array[i]['applicable_standards_28'];
                                child.applicable_standards_30=array[i]['applicable_standards_30'];
                                child.applicable_standards_32=array[i]['applicable_standards_32'];
                                child.applicable_standards_34=array[i]['applicable_standards_34'];
                                child.applicable_standards_36=array[i]['applicable_standards_36'];
                                child.applicable_standards_38=array[i]['applicable_standards_38'];
                                child.applicable_standards_40=array[i]['applicable_standards_40'];
                                child.applicable_standards_42=array[i]['applicable_standards_42'];
                                child.applicable_standards_44=array[i]['applicable_standards_44'];
                                child.applicable_standards_46=array[i]['applicable_standards_46'];
                                child.applicable_standards_48=array[i]['applicable_standards_48'];
                                child.applicable_standards_50=array[i]['applicable_standards_50'];
                            }
                            frm.refresh_field('product_test');
                        }
                     }
                  })
            }
  },

});
