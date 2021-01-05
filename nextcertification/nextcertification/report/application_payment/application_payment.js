// Copyright (c) 2016, Sameer and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Application Payment"] = {
	"filters": [
        {
           "fieldname": "application",
           "fieldtype": "Link",
           "label": "Application",
           "options": "Application"
        },
        {
            "fieldname":"from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "width": "80",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            "reqd": 1
        },
	    {
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		}
	]
};
