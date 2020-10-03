# -*- coding: utf-8 -*-
# Copyright (c) 2020, Sameer and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Certificate(Document):
	pass

# @frappe.whitelist()
# def get_products(name=None)
# 	if name:
# 		product=[]
		# for i in :
		# product[] = frappe.get_list('Product',filter={'parent':name}, as_list=True )
