// Copyright (c) 2020, Sameer and contributors
// For license information, please see license.txt

frappe.ui.form.on('Certificate', {
//	 refresh: function(frm) {
//
//
//	 },

        "application" : function(frm) {
           doc = frappe.db.get_doc('Application',{ 'name':'application'})
                console.log('*********** doc ********',doc)

            frm.set_query('p_link', function(doc) {
                return {
                    filters: {'parent': frm.doc.application}
                };
            });
            frm.set_query('test_report', function(doc){
                return {
                    filters: {'application':frm.doc.application}
                };
            });
        },

});