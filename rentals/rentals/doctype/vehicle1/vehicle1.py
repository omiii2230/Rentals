# Copyright (c) 2025, BWh and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class vehicle1(WebsiteGenerator):
	def before_save(self):
		self.set_title()
		pass

	def set_title(self):
		self.title = f"{self.make} {self.model},{self.year}"
