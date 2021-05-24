# -*- coding: utf-8 -*-
# Copyright (c) 2021, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import os
import requests
import json
import subprocess


class SyncManual(Document):
	
	def sync_manual(self):
		if not self.tanggal_sync :
			frappe.throw("Tanggal Sync belum dipilih")

		if not self.marketplace :
			frappe.throw("Marketplace belum dipilih")

		if not self.store_name :
			frappe.throw("Store Name belum dipilih")

		sitename = str(frappe.utils.get_url()).replace("https://", "").replace("http://", "").replace("/","")

		# frappe.throw(sitename)

		os.chdir("/home/frappe/ahok-bench")
		os.system(""" bench --site {} execute marketplace_connector.marketplace_connector.doctype.sync_method.enqueue_marketplace_orders --kwargs '{{"date":"{}", "shop_setting":"{}"}}' """.format(sitename, self.tanggal_sync, self.store_name))

		