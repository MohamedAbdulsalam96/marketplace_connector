# -*- coding: utf-8 -*-
# Copyright (c) 2021, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

from marketplace_connector.marketplace_connector.doctype.frappeclient import FrappeClient
from marketplace_connector.marketplace_connector.doctype.shopee_shop_setting.shopee_connector.client import Client

import json
import os
import requests
import subprocess
from frappe.utils.background_jobs import enqueue
from frappe.utils import get_site_name

from frappe import utils
from frappe.utils import nowdate, add_days, random_string, get_url

import time
import datetime

from frappe import utils

import hmac
import time
import hashlib
import requests

class ShopeeShopSetting(Document):

	def generate_url_for_shop_id(self):
		if not self.partner_id :
			frappe.throw("Partner ID harus diisi")

		if not self.partner_key :
			frappe.throw("Partner Key harus diisi")

		if not self.redirect_url :
			frappe.throw("Redirect URL harus diisi")

		# # def api1 generator url
		timest = int(time.time())
		path = "/api/v1/shop/auth_partner"
		host = "https://partner.shopeemobile.com"
		partner_id = self.partner_id
		# partner_id = 3863
		redirect= self.redirect_url
		partner_key = self.partner_key
		token = partner_key+redirect
		hash_token = hashlib.sha256(token.encode()).hexdigest()
		url = host+path+"?id={}&redirect={}&token={}".format(partner_id,redirect,hash_token)

		# test_host = "https://partner.uat.shopeemobile.com/api/v1/shop/auth_partner"
		# test_id = 100958
		# test_key = "27fc6a405e1443e4853f9915ef65babb3c60b0dec6cab25450757405e1abb1bf"
		# test_token = hashlib.sha256((test_key+redirect).encode("utf-8")).hexdigest()
		# url = test_host+"?id={}&token={}&redirect={}".format(test_id,test_token,redirect)
		self.url_shop_id = url
		# resp = requests.get(url)
		# print(resp.content)
	
	def validate(self):

		if self.enable_sync :
			if self.shop_id and self.partner_id and self.partner_key :
				shopid = int(self.shop_id)
				partnerid = int(self.partner_id)
				api_key = str(self.partner_key)
				shopeeclient = Client(shopid, partnerid, api_key)

				result = shopeeclient.shop.get_shop_info()

				# frappe.throw(str(result))
				if result :

					self.shop_name = result["shop_name"]
					self.shop_region = result["country"]
					self.shop_status = result["status"]







