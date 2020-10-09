# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nextcertification"
app_title = "Nextcertification"
app_publisher = "Sameer"
app_description = "NextCertification"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sshaikh@dexciss.com"
app_license = "MIT"

# Includes in <head>
# ------------------
doctype_js = {
    "Sales Order" : "public/js/sales_order.js",
    "Sales Invoice" : "public/js/sales_invoice.js"
}

# include js, css files in header of desk.html
# app_include_css = "/assets/nextcertification/css/nextcertification.css"
# app_include_js = "/assets/nextcertification/js/nextcertification.js"

# include js, css files in header of web template
# web_include_css = "/assets/nextcertification/css/nextcertification.css"
# web_include_js = "/assets/nextcertification/js/nextcertification.js"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "nextcertification.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nextcertification.install.before_install"
# after_install = "nextcertification.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nextcertification.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"nextcertification.tasks.all"
# 	],
# 	"daily": [
# 		"nextcertification.tasks.daily"
# 	],
# 	"hourly": [
# 		"nextcertification.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nextcertification.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nextcertification.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nextcertification.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nextcertification.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nextcertification.task.get_dashboard_data"
# }
override_doctype_dashboards = {
    "Sales Order" :"nextcertification.sales_order_dashboard.get_data",
    "Customer" :"nextcertification.customer_dashboard.get_data"
}
# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

doc_events = {
    "Sales Order" : {
        "after_insert" : "nextcertification.sales_order.add_sales_to_application",
    },
    "Application" : {
        "after_insert" : "nextcertification.nextcertification.doctype.application.application.add_app_to_sales",
    }
}

standard_portal_menu_items = [
	{"title": "Certificate Application", "route": "/certificate-application", "reference_doctype": "Application", "role": "ALL"},
]