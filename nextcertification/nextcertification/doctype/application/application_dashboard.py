from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'application',
		'transactions': [
			{
				'label': _('Fulfillment'),
				'items': ['Sales Invoice']
			},
			{
				'label': _('Selling'),
				'items': ['Sales Order']
			},

		]
	}
