// Copyright (c) 2020, Sameer and contributors
// For license information, please see license.txt

frappe.ui.form.on('CERTIFICATE OF CONFORMITY', {
	refresh: function(frm) {
        if( frm.doc.docstatus === 1){
            frm.set_df_property("application", "readonly", 1),
            frm.refresh_field("application")
        };
    },
	"application" : function(frm){
       // console.log('-------- frm status doc ------',frm.doc.docstatus);
        frm.set_query('test_report_child', function(doc){
                return {
                    filters: {
                    'application':frm.doc.application,
                     'docstatus': 1
                    }
                };
            });

          frappe.call({
                method: "nextcertification.nextcertification.doctype.certificate_of_conformity.certificate_of_conformity.check_section_certificate",
                args: {
                    doctype: "Service Types",
                    name: frm.doc.service_type
                    },
                callback:function(r) {
                    if(r.message.certificate == 1)
                    {
                    frm.set_df_property("sb1", "hidden", 0);
                    frm.refresh_field("sb1")
                    frm.set_df_property("sb", "hidden", 0);
                    frm.refresh_field("sb")
                    frm.set_df_property("sb_no_certificate", "hidden", 1);
                    frm.refresh_field("sb_no_certificate")

                    }
                    else
                    {
                    frm.set_df_property("sb1", "hidden", 1);
                    frm.refresh_field("sb1")
                    frm.set_df_property("sb", "hidden", 1);
                    frm.refresh_field("sb")
                    frm.set_df_property("sb_no_certificate", "hidden", 0);
                    frm.refresh_field("sb_no_certificate")

                     }
                }
            })
        }

});
