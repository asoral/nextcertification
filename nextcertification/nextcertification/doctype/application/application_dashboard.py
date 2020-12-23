from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'application',
		'transactions': [
			{
				'label': _('Fulfillment'),
				'items': ['Sales Invoice','Payment Entry']
			},
			{
				'label': _('Selling'),
				'items': ['Sales Order']
			},
			{
				'label': _('Certificate'),
				'items': ['SCHEDULE OF CERTIFICATION','CERTIFICATE OF CONFORMITY']
			},
			{
				'label': _('Reports'),
				'items': ['Product Test Report']
			},

		]
	}
