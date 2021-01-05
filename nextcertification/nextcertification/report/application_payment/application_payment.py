# Copyright (c) 2013, Sameer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{
			"fieldname": "application",
			"fieldtype": "Link",
			"label": "Application",
			"options": "Application",
			"width": 200
		},
		{
			"fieldname": "sales_invoice",
			"fieldtype": "Link",
			"label": "Sales Invoice",
			"options": "Sales Invoice",
			"width": 200
		},
		{
			"fieldname": "invoice_status",
			"fieldtype": "Data",
			"label": "Invoice Status",
			"width": 150
		},
		{
			"fieldname": "payment_entry",
			"fieldtype": "Link",
			"label": "Payment Entry",
			"options": "Payment Entry",
			"width": 200
		},
		{
			"fieldname": "payment_status",
			"fieldtype": "Data",
			"label": "Payment Status",
			"width": 150
		},
		{
			"fieldname": "bill_amt",
			"fieldtype": "Float",
			"label": "Billed Amount",
			"width": 150
		},
		{
			"fieldname": "pending_amt",
			"fieldtype": "Float",
			"label": "Pending Amount",
			"width": 150
		}
	]
	return columns

def get_data(filters =None):

	query = """select TP.name as application,
			TSI.name as sales_invoice,
			TSI.status as invoice_status,
			pe.name as payment_entry,
			CASE
				WHEN pe.docstatus = 0 THEN 'draft'
				WHEN pe.docstatus = 1 THEN 'Submitted'
				WHEN pe.docstatus = 2 THEN 'Cancelled'
				ELSE Null
			END as payment_status,
			TSI.rounded_total as bill_amt,
			TSI.outstanding_amount as pending_amt
			from `tabApplication` as TP
			left join `tabSales Invoice` as TSI on TP.name = TSI.application 
			left join `tabPayment Entry Reference` as per on TSI.name = per.reference_name and per.reference_doctype = 'Sales Invoice'
			left join `tabPayment Entry` as pe on pe.name = per.parent
			where TP.docstatus = 1 and TP.date between '{0}' and '{1}'""".format(filters.get('from_date'),filters.get('to_date'))

	if filters.get('application'):
		query += " and TP.name = '{0}'".format(filters.get('application'))
	result = frappe.db.sql(query ,as_dict=True)
	return result