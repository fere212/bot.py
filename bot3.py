import os
import telebot
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from chk import *#chk 
from otp import *
from st import * #stripe auth
from shopfy import * #10$ chk
from ba import *#1$ check
#from sa import *

from reg import reg
from dotenv import load_dotenv
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading


import threading
import time
from telebot import types



load_dotenv()  # .env dosyasını yükle
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Bot nesnesini tanımlayın
bot = telebot.TeleBot(BOT_TOKEN)

admin=7457947976

myid = ['7457947976']

admins = ['7457947976']




#تحديث جديد









command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='Free - Not Subscribed'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "Free - Not Subscribed",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == 'Free - Not Subscribed':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Programmer - FTX", url="https://t.me/iphonesahibi")
			keyboard.add(contact_button)
			random_number = random.randint(4, 17)
			photo_url = f'https://t.me/iphonesahibi/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>ϟ Welcome Dear -> {name} ϟ
ϟ Youre Not Subscribed in Check World Bot ❌

ϟ For Show Bot Prices Send -> /prices
ϟ Programmer ~ @F_TT_X </b>''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="ϟ Our Channel ϟ", url="https://t.me/Pythonln")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(4, 17)
		photo_url = f'https://t.me/animephotossea/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<strong>ϟ Welcome -> {name} ϟ
- Your Subscription is Active ✅

- For Show check commands Send -> /cmds
- For Check The Combo CC File Send The Combo And Choose The Gate ✅

ϟ - Programmer • @F_TT_X ϟ</strong>''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='Free - Not Subscribed'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"ϟ {BL} ϟ",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text='''<b> 
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Auth 1
[ϟ] Format: /chk card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Stripe Auth 2
[ϟ] Format: /st card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Otp Chekcer
[ϟ] Format: /vbv card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Shopify Charhe 10$ 
[ϟ] Format: /sp card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: Braintree Charge 1$
[ϟ] Format: /ba card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: BIN Info Lookup
[ϟ] Format: /bin BIN
[ϟ] Condition: ON! ✅
[ϟ] Type: Free For All ✅
━━━━━━━━━━━━━━━━━━━
 Name: Gen Generator
[ϟ] Format: /gen .gen 505662001674xxx
[ϟ] Condition: ON! ✅
[ϟ] Type: Free For All ✅
━━━━━━━━━━━━━━━━━━━
ϟ - We will adding More Gates....</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='Free - Not Subscribed'
		if BL == 'Free - Not Subscribed':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "Free - Not Subscribed",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Programmer - FTX", url="https://t.me/iphonesahibi")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>• Welcome Dear » {name}
- Youre Not Subscribed in BOT ❌

• For Show Bot Priced Send /prices
- Programmer ~ @F_TT_X - </b>''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Programmer - FTX", url="https://t.me/İphoneSahibi")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>• Welcome Dear » {name}
- Youre Not Subscribed in BOT ❌

• For Show Bot Priced Send /prices
- Programmer ~ @F_TT_X - </b>''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="ϟ Programmer - FTX ", url="https://t.me/iphonesahibi")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text='''<b>ϟ Your Subscription has Expired • لاتستطيع استخدام البوت لانه انتهى اشتراكك </b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = 'Free - Not Subscribed'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"ϟ Braintree Auth 1 ϟ",callback_data='br')
		sw = types.InlineKeyboardButton(text=f"ϟ Stripe Auth 2 ϟ️",callback_data='br2')
		b3 = types.InlineKeyboardButton(text=f"ϟ Otp ϟ️",callback_data='br3')
		sa = types.InlineKeyboardButton(text=f"ϟ 1$ Check ϟ️",callback_data='br4')
		m = types.InlineKeyboardButton(text=f"ϟ Moneris Cahrge 0.10$ ϟ️",callback_data='br4')
		d = types.InlineKeyboardButton(text=f"ϟ Moneris Cahrge 0.10$ ϟ️",callback_data='br4')
		keyboard.add(contact_button)
		keyboard.add(sw)
		keyboard.add(b3)
		keyboard.add(sa)
		keyboard.add(m)
		keyboard.add(d)
		bot.reply_to(message, text=f'ϟ Chose The Gateway You Want to use from Bellow ',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
			
			
			
			

	
	
	
	
def dato(zh):
 
 

 
 
	try:
		api_url = requests.get("https://bins.antipublic.cc/bins/"+zh).json()
		brand=api_url["brand"]
		card_type=api_url["type"]
		level=api_url["level"]
		bank=api_url["bank"]
		country_name=api_url["country_name"]
		country_flag=api_url["country_flag"]
		mn = f'''ϟ BIN Info -> {brand} - {card_type} - {level}
ϟ Bank -> {bank} - {country_flag}
ϟ Country -> {country_name} [ {country_flag} ]'''
		return mn
	except Exception as e:
		print(e)
		return 'No info'
	
	
	







import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  # لتعقب حالة كل مستخدم

# تعريف المتغيرات لتخزين حالة كل بوابة


# تعريف المتغيرات لحالة البوابات
check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True

check_enabled_ch1 = True






@bot.message_handler(commands=['onb1'])
def enable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 1 has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb1'])
def disable_br1(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 1 has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')








@bot.message_handler(commands=['onst1'])
def enable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 2 has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offst1'])
def disable_br2(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 2 has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')





@bot.message_handler(commands=['onb3'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Otp Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['offb3'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Otp Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
        
        
        

        
        
@bot.message_handler(commands=['onb4'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Charge 1$ Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
@bot.message_handler(commands=['offb4'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Charge 1$ Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
        
        
        
        
        
@bot.message_handler(commands=['onch1'])
def enable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been enabled. ✅')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
@bot.message_handler(commands=['offch1'])
def disable_br3(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Auth 4 Check has been disabled. 🔒')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')
        
        
        
        
        





from telebot import types

# تعريف المتغيرات لحالة البوابات
check_enabled_br1 = True
check_enabled_br2 = True
check_enabled_br3 = True
check_enabled_br4 = True
check_enabled_ch1 = True

MAX_LINES = 1000

@bot.message_handler(commands=['gate'])
def show_menu(message):
    if str(message.from_user.id) in admins:
        markup = types.InlineKeyboardMarkup(row_width=1)
        toggle_br1 = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        toggle_br2 = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        toggle_br3 = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        toggle_br4 = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        toggle_ch1 = 'Enable✅' if check_enabled_ch1 else 'Disable❌'
        
        br1_button = types.InlineKeyboardButton(f"Braintree Auth 1 ({toggle_br1})", callback_data='toggle_br1')
        br2_button = types.InlineKeyboardButton(f"Stripe Auth ({toggle_br2})", callback_data='toggle_br2')
        br3_button = types.InlineKeyboardButton(f"Otp  ({toggle_br3})", callback_data='toggle_br3')
        br4_button = types.InlineKeyboardButton(f"Braintree Charge 1$ ({toggle_br4})", callback_data='toggle_br4')
        ch1_button = types.InlineKeyboardButton(f"Braintree Charge 1 ({toggle_ch1})", callback_data='toggle_ch1')
        limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
        
        markup.add(br1_button, br2_button, br3_button, br4_button, ch1_button, limits_button)
        bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'You are not the owner 🤍')

@bot.callback_query_handler(func=lambda call: call.data.startswith('toggle_') or call.data == 'set_limits')
def handle_toggle(call):
    global check_enabled_br1, check_enabled_br2, check_enabled_br3, check_enabled_br4, check_enabled_ch1, MAX_LINES
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    if call.data == 'toggle_br1':
        check_enabled_br1 = not check_enabled_br1
        status = 'Enable✅' if check_enabled_br1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Auth 1 is now {status}.")
    elif call.data == 'toggle_br2':
        check_enabled_br2 = not check_enabled_br2
        status = 'Enable✅' if check_enabled_br2 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Stripe Auth 2 is now {status}.")
    elif call.data == 'toggle_br3':
        check_enabled_br3 = not check_enabled_br3
        status = 'Enable✅' if check_enabled_br3 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Otp Checker is now {status}.")
    elif call.data == 'toggle_br4':
        check_enabled_br4 = not check_enabled_br4
        status = 'Enable✅' if check_enabled_br4 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Charge 1$ {status}.")
    elif call.data == 'toggle_ch1':
        check_enabled_ch1 = not check_enabled_ch1
        status = 'Enable✅' if check_enabled_ch1 else 'Disable❌'
        bot.answer_callback_query(call.id, f"Braintree Charge 1 is now {status}.")
    elif call.data == 'set_limits':
        # إرسال رسالة للمستخدم لإدخال قيمة جديدة لـ MAX_LINES
        bot.send_message(chat_id, "Please enter the new limit value for Gate limits as /set_limit 1500")

    # تحديث الرسالة لعرض الحالة الجديدة
    markup = types.InlineKeyboardMarkup(row_width=1)
    br1_button = types.InlineKeyboardButton(f"Braintree Auth 1 ({'Enable✅' if check_enabled_br1 else 'Disable❌'})", callback_data='toggle_br1')
    br2_button = types.InlineKeyboardButton(f"Stripe Auth 2 ({'Enable✅' if check_enabled_br2 else 'Disable❌'})", callback_data='toggle_br2')
    br3_button = types.InlineKeyboardButton(f" Otp ({'Enable✅' if check_enabled_br3 else 'Disable❌'})", callback_data='toggle_br3')
    br4_button = types.InlineKeyboardButton(f"Braintree Charge 1$ ({'Enable✅' if check_enabled_br4 else 'Disable❌'})", callback_data='toggle_br4')
    ch1_button = types.InlineKeyboardButton(f"Braintree Charge 1 ({'Enable✅' if check_enabled_ch1 else 'Disable❌'})", callback_data='toggle_ch1')
    limits_button = types.InlineKeyboardButton(f"Gate limits ({MAX_LINES})", callback_data='set_limits')
    markup.add(br1_button, br2_button, br3_button, br4_button, ch1_button, limits_button)
    
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Choose an option:", reply_markup=markup)

@bot.message_handler(commands=['set_limit'])
def set_limit(message):
    global MAX_LINES
    try:
        # Extract the new limit value from the command
        if len(message.text.split()) == 2 and message.text.split()[1].isdigit():
            new_limit = int(message.text.split()[1])
            MAX_LINES = new_limit
            bot.reply_to(message, f"Gate limit has been set to {MAX_LINES}.")
            
            # تحديث قائمة الخيارات في الرسالة
            show_menu(message)
        else:
            bot.reply_to(message, "Please use the correct format: /set_limit 1500.")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")
        print(f"Error: {e}")











import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  # لتعقب حالة كل مستخدم
check_enabled = True  # لتتبع ما إذا كان الفحص مفعلًا أم لا

@bot.message_handler(commands=['offb1'])
def handle_admin_commands(message):
    global check_enabled
    if str(message.from_user.id) in admins:
        check_enabled = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb1'])
def handle_admin_commands(message):
    global check_enabled
    if str(message.from_user.id) in admins:
        check_enabled = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br1:  # تحقق من حالة بوابة رقم واحد
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    def my_function():
        gate = 'Braintree Auth 1'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                # تحقق من عدد الأسطر
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @F_TT_X </b>''', 
                        reply_markup=mes)

                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

                    if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(5)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص بعد الانتهاء
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @F_TT_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')
	
	
	
	
	
	



	

	
	
	
	
	
	
	


import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  # لتعقب حالة كل مستخدم
check_enabled_br2 = True  # لتتبع ما إذا كان فحص Braintree Auth 2 مفعلًا أم لا

@bot.message_handler(commands=['st2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = False
        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 2 Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['st1'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Stripe Auth 2 Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br2')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br2:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    def my_function():
        gate = 'Stripe Auth'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                # تحقق من عدد الأسطر
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                        return
                    start_time = time.time()
                    try:
                        last = str(Tele2(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @F_TT_X </b>''', 
                        reply_markup=mes)

                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

                    if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(5)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص بعد الانتهاء
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @F_TT_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')
	
	
	#_------------------------------------------------------------------------------------












	






















import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  # لتعقب حالة كل مستخدم
check_enabled_br3 = True  # لتتبع ما إذا كان فحص Braintree Auth 3 مفعلًا أم لا

@bot.message_handler(commands=['offb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.cohat.id, text='- Otp Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Otp Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br3')
def menu_callback(call):
    id = str(call.from_user.id)

    if not check_enabled_br3:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    def my_function():
        gate = 'Otp Check'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)

        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)

                # تحقق من عدد الأسطر
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                    return

                stopuser[id] = {'status': 'start'}

                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                        return
                    start_time = time.time()
                    try:
                        last = str(vbv(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"

                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)

                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @F_TT_X </b>''', 
                        reply_markup=mes)

                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

                    if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1

                    time.sleep(15)

        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')

        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص بعد الانتهاء
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @F_TT_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')
    







	
	
	
	
	
	
	
	
	
	
	
import threading
import time
from telebot import types

MAX_LINES = 1000
stopuser = {}  # لتعقب حالة كل مستخدم
check_enabled_br4 = True  # لتتبع ما إذا كان فحص Braintree Auth 4 مفعلًا أم لا

@bot.message_handler(commands=['offb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Charge 1$ Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='- Braintree Charge 1$ Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.callback_query_handler(func=lambda call: call.data == 'br4')
def menu_callbactok(call):
    id = str(call.from_user.id)

    if not check_enabled_br4:
        bot.send_message(chat_id=call.message.chat.id, text="- Gateway is under maintenance ❌.")
        return

    # تحقق مما إذا كان المستخدم لديه فحص جاري
    if id in stopuser and stopuser[id]['status'] == 'start':
        bot.send_message(
            chat_id=call.message.chat.id,
            text="- You Are Already Checking A Combo. 🔄 Please Wait Until It Finishes Or Stop It Manually."
        )
        return  # إذا كان هناك فحص جاري، نخرج من الدالة ولا نبدأ فحص جديد

    def my_function():
        gate = 'Braintree Charge 10$'
        dd = 0
        live = 0
        cm = 0
        mes = types.InlineKeyboardMarkup(row_width=1)
        cm1 = types.InlineKeyboardButton("- [ CARD ]", callback_data='u8')
        status = types.InlineKeyboardButton(f"- Status & Message ", callback_data='u8')
        cm3 = types.InlineKeyboardButton("- Approved ✅-> Number ", callback_data='x')
        ccn = types.InlineKeyboardButton("- CVV & CCN✅-> Number ", callback_data='x')
        cm4 = types.InlineKeyboardButton("- Declined ❌-> Number ", callback_data='x')
        cm5 = types.InlineKeyboardButton("- Total ⚡-> Number ", callback_data='x')
        stop = types.InlineKeyboardButton("- For Stop Check 🔍", callback_data='stop')
        mes.add(cm1, status, cm3, ccn, cm4, cm5, stop)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="- Please Wait Processing Your File ..", reply_markup=mes)
        
        try:
            with open("combo.txt", 'r') as file:
                lines = file.readlines()
                total_lines = len(lines)
                
                # تحقق من عدد الأسطر
                if total_lines > MAX_LINES:
                    bot.send_message(
                        chat_id=call.message.chat.id,
                        text=(
                            f"- 𝐁𝐀𝐃 𝐁𝐑𝐎 ❌\n\n"
                            f"• 𝐓𝐇𝐄 𝐌𝐀𝐗 𝐂𝐂 𝐋𝐈𝐌𝐈𝐓 𝐈𝐒 {MAX_LINES} ✅\n\n"
                            "• 𝐂𝐇𝐄𝐂𝐊 𝐘𝐎𝐔𝐑 𝐅𝐈𝐋𝐄 𝐀𝐍𝐃 𝐓𝐑𝐘 𝐀𝐆𝐀𝐈𝐍 📣"
                        )
                    )
                    stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                    return
                
                stopuser[id] = {'status': 'start'}
                
                for cc in lines:
                    if stopuser[id]['status'] == 'stop':
                        bot.send_message(chat_id=id, text='- Done Stop Check Cards 📣⚡')
                        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص
                        return
                    start_time = time.time()
                    try:
                        last = str(notauto(cc))
                        cm += 1
                    except Exception as e:
                        print(e)
                        last = "RISK: gateway_error"
                    
                    print(last)
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    cm1 = types.InlineKeyboardButton(f"- 𝘾𝘾 • {cc}", callback_data='u8')
                    status = types.InlineKeyboardButton(f"- 𝙎𝙩𝙖𝙩𝙪𝙨 • {last}", callback_data='u8')
                    cm3 = types.InlineKeyboardButton(f"- 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 !✅ • {live}", callback_data='x')
                    cm4 = types.InlineKeyboardButton(f"- 𝗗𝗘𝗖𝗜𝗡𝗘𝗗 !❌ • {dd}", callback_data='x')
                    cm5 = types.InlineKeyboardButton(f"• {total_lines} / {cm} •", callback_data='x')
                    stop = types.InlineKeyboardButton("- Stop Check 🚷", callback_data='stop')
                    mes.add(cm1, status, cm3, cm4, cm5, stop)
                    
                    end_time = time.time()
                    execution_time = end_time - start_time
                    bot.edit_message_text(chat_id=call.message.chat.id, 
                        message_id=call.message.message_id, 
                        text=f'''
<b>- Please Wait Checking Your Cards 💫
- Gate -> {gate} 💫
- Programmer -> @F_TT_X </b>''', 
                        reply_markup=mes)
                    
                    msg = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> {gate}

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''
                    
                    if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
                        live += 1
                        bot.send_message(call.from_user.id, msg)
                    else:
                        dd += 1
                    
                    time.sleep(5)
        except Exception as error:
            bot.send_message(admins[0], f'Error -> {error}')
        
        stopuser[id]['status'] = 'stopped'  # تحرير حالة الفحص بعد الانتهاء
        bot.send_message(chat_id=call.message.chat.id, text='- Done Check All Cards ✅\n - Programmer • @F_TT_X')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_check(call):
    id = str(call.from_user.id)
    if id in stopuser and stopuser[id]['status'] == 'start':
        stopuser[id]['status'] = 'stop'
        bot.send_message(chat_id=call.message.chat.id, text='- Stopping Check...')
    else:
        bot.send_message(chat_id=call.message.chat.id, text='- No ongoing check to stop.')
    


	






























import json
from datetime import datetime, timedelta

# دالة تحقق من خطة المستخدم
def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)]['plan']
        timer = json_data[str(user_id)]['timer']
        if user_plan != 'Free - Not Subscribed':
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  # قم بتعديل فترة الاشتراك حسب الحاجة
                    return True
            except Exception as e:
                return False
    return False










import time
from datetime import datetime, timedelta

# قم بتعريف قاموس لتخزين وقت آخر طلب لكل مستخدم
command_usage = {}

# الحالة الافتراضية لبوابة رقم 1 (مفعلة)
check_enabled_br1 = True

@bot.message_handler(commands=['offb1'])
def handle_admin_commands(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb1'])
def handle_admin_commands(message):
    global check_enabled_br1
    if str(message.from_user.id) in admins:
        check_enabled_br1 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.mvbv') or message.text.lower().startswith('/mvbv'))
def respond_to_mvbv(message):
    with open('data.json') as f:
    	data = json.load(f)
    	user_id = str(message.from_user.id)
    	if user_id not in data:
	       
	       bot.reply_to(message, "You need to be registered to use this command.")
	       return
    gate = '3D Lookup'
    name = message.from_user.first_name
    idt = message.from_user.id
    id = message.chat.id
    try:
        command_usage[idt]['last_time']
    except:
        command_usage[idt] = {
            'last_time': datetime.now()
        }
    if command_usage[idt]['last_time'] is not None:
        current_time = datetime.now()
        time_diff = (current_time - command_usage[idt]['last_time']).seconds
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {15 - time_diff} seconds.</b>", parse_mode="HTML")
            return

    ko = bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id

    try:
        cc = message.reply_to_message.text
    except:
        cc = message.text

    # تقسيم البطاقات باستخدام المسافة كفاصل
    cc_list = cc.split()  # هنا يتم تقسيم النص بناءً على المسافة
    if len(cc_list) > 5:
        cc_list = cc_list[:5]  # يقتصر على 5 بطاقات كحد أقصى

    results = []
    for card in cc_list:
        card = card.strip()
        card = str(reg(card))
        if card == 'None':
            results.append(f"<b>🚫 Oops! Card format is incorrect: {card}</b>")
            continue

        start_time = time.time()
        try:
            command_usage[idt]['last_time'] = datetime.now()
            last = str(vbv(card))
        except Exception as e:
            last = 'Error'

        try:
            data = requests.get(f'https://bins.antipublic.cc/bins/{card[:6]}').json()
        except:
            data = {}

        brand = data.get('brand', 'Unknown')
        card_type = data.get('type', 'Unknown')
        country = data.get('country_name', 'Unknown')
        country_flag = data.get('country_flag', 'Unknown')
        bank = data.get('bank', 'Unknown')

        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  OTP CHECK

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> OTP CHECK

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        cvc = f'''<b>• Approved ✅        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @F_TT_X</b>'''

        if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
            results.append(msg)
            bot.send_message(message.chat.id, text = msg, parse_mode="HTML")
        else:
            results.append(msgd)
            bot.send_message(message.chat.id, text = msgd, parse_mode="HTML")

    # إرسال الرسائل لكل بطاقة
    for result in results:
        bot.send_message(message.chat.id, result, parse_mode="HTML")
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vhk(message):
    global check_enabled_br1
    user_id = message.chat.id
    current_time = datetime.now()

    # تحقق من حالة بوابة رقم 1
    if not check_enabled_br1:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    # تحقق من وجود آخر وقت استخدام للأمر للمستخدم
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # تحقق مما إذا كان الوقت الفاصل أقل من 30 ثانية
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    # تحديث وقت آخر طلب
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.chk ', '').replace('/chk ', '')
        gate='Braintree Auth 1'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(Tele(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  Braintree Auth 1

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> Braintree Auth 1

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        cvc = f'''<b>• Approved ✅       
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @F_TT_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed FTXCHK BOT !❌

Your ID : {message.chat.id}
Programmer - @F_TT_X''')




















import time
from datetime import datetime, timedelta

# قم بتعريف قاموس لتخزين وقت آخر طلب لكل مستخدم
command_usage = {}

# الحالة الافتراضية لبوابة رقم 2 (مفعلة)
check_enabled_br2 = True

@bot.message_handler(commands=['offb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb2'])
def handle_admin_commands(message):
    global check_enabled_br2
    if str(message.from_user.id) in admins:
        check_enabled_br2 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 2 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.st') or message.text.lower().startswith('/st'))
def respond_to_vhk(message):
    global check_enabled_br2
    user_id = message.chat.id
    current_time = datetime.now()

    # تحقق من حالة بوابة رقم 2
    if not check_enabled_br2:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    # تحقق من وجود آخر وقت استخدام للأمر للمستخدم
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # تحقق مما إذا كان الوقت الفاصل أقل من 30 ثانية
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    # تحديث وقت آخر طلب
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.st ', '').replace('/st ', '')
        gate = 'Stripe Auth'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(Tele2(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  Stripe Auth

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> Stripe Auth

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        cvc = f'''<b>• Aprroved ✅        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @F_TT_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'CVV' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed FTXCHK BOT !❌

Your ID : {message.chat.id}
Programmer - @F_TT_X''')
		      









import time
from datetime import datetime, timedelta

# قم بتعريف قاموس لتخزين وقت آخر طلب لكل مستخدم
command_usage = {}

# الحالة الافتراضية لبوابة رقم 3 (مفعلة)
check_enabled_br3 = True

@bot.message_handler(commands=['offb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb3'])
def handle_admin_commands(message):
    global check_enabled_br3
    if str(message.from_user.id) in admins:
        check_enabled_br3 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 3 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vhk(message):
    global check_enabled_br3
    user_id = message.chat.id
    current_time = datetime.now()

    # تحقق من حالة بوابة رقم 3
    if not check_enabled_br3:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    # تحقق من وجود آخر وقت استخدام للأمر للمستخدم
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # تحقق مما إذا كان الوقت الفاصل أقل من 30 ثانية
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    # تحديث وقت آخر طلب
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.vbv ', '').replace('/vbv ', '')
        gate='Otp Check'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(vbv(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  OTP CHECK

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> OTP CHECK

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        cvc = f'''<b>• Approved ✅        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @F_TT_X</b>'''

        if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed FTXCHK BOT !❌

Your ID : {message.chat.id}
Programmer - @F_TT_X''')












import time
from datetime import datetime, timedelta

# قم بتعريف قاموس لتخزين وقت آخر طلب لكل مستخدم
command_usage = {}

# الحالة الافتراضية لبوابة رقم 4 (مفعلة)
check_enabled_br4 = True

@bot.message_handler(commands=['offb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(commands=['onb4'])
def handle_admin_commands(message):
    global check_enabled_br4
    if str(message.from_user.id) in admins:
        check_enabled_br4 = True
        bot.send_message(chat_id=message.chat.id, text='- Focusing Check for Gateway 4 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.sp') or message.text.lower().startswith('/sp'))
def respond_to_vhk(message):
    global check_enabled_br4
    user_id = message.chat.id
    current_time = datetime.now()
    
    # تحقق من حالة بوابة رقم 4
    if not check_enabled_br4:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    # تحقق من وجود آخر وقت استخدام للأمر للمستخدم
    if user_id in command_usage:
        last_time = command_usage[user_id]['last_time']
        time_diff = (current_time - last_time).seconds
        # تحقق مما إذا كان الوقت الفاصل أقل من 30 ثانية
        if time_diff < 30:
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return
    
    # تحديث وقت آخر طلب
    command_usage[user_id] = {'last_time': current_time}

    if check_user_plan(user_id):
        cc = message.text.replace('.sp ', '').replace('/sp ', '')
        gate='Braintree Charge 10$'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(notauto(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  Braintree Charge 10$

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> Braintree Charge 10$

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        cvc = f'''<b>• Approved ✅        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @F_TT_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed FTXCHK BOT !❌

Your ID : {message.chat.id}
Programmer - @F_TT_X''')






























































from datetime import datetime, timedelta

# قم بإنشاء قاموس لتتبع آخر وقت استخدم فيه كل مستخدم الأمر
last_command_usage = {}

# الحالة الافتراضية لبوابة رقم 1 (مفعلة)
check_enabled_ch1 = True

@bot.message_handler(commands=['offch1'])
def handle_admin_commands(message):
    global check_enabled_ch1
    if str(message.from_user.id) in admins:
        check_enabled_ch1 = True
        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been disabled. 🔒 No users can start the check until it is re-enabled.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

@bot.message_handler(commands=['onch1'])
def handle_admin_commands(message):
    global check_enabled_ch1
    if str(message.from_user.id) in admins:
        check_enabled_ch1 = True
        bot.send_message(chat_id=message.chat.id, text='- Charge Check for Gateway 1 has been re-enabled. ✅ Users can now start the check.')
    else:
        bot.send_message(chat_id=message.chat.id, text='- You are not the owner 🤍')

@bot.message_handler(func=lambda message: message.text.lower().startswith('.ba') or message.text.lower().startswith('/ba'))
def respond_to_vhk(message):
    global check_enabled_ch1
    user_id = message.chat.id
    current_time = datetime.now()

    # تحقق من حالة بوابة رقم 1
    if not check_enabled_ch1:
        bot.reply_to(message, "<b>- Gateway is under maintenance ❌.</b>", parse_mode="HTML")
        return

    # تحقق من آخر وقت استخدم فيه المستخدم الأمر
    if user_id in last_command_usage:
        time_diff = (current_time - last_command_usage[user_id]).seconds
        if time_diff < 30:  # إذا كانت المدة أقل من 30 ثانية
            bot.reply_to(message, f"<b>Try again after {30 - time_diff} seconds.</b>", parse_mode="HTML")
            return

    # تحديث وقت الاستخدام الأخير
    last_command_usage[user_id] = current_time

    if check_user_plan(user_id):
        cc = message.text.replace('.ba ', '').replace('/ba ', '')
        gate = 'BrainTree Charge 10$'
        ko = bot.reply_to(message, '- Please Wait Checking your Card...⌛').message_id
        start_time = time.time()
        try:
            last = str(Tele4(cc))
        except:
            last = 'Gateway Error ❌'
        end_time = time.time()
        execution_time = end_time - start_time

        dec = f'''<b>• Declined ❌

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate ->  Braintree Charge 1$

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        ok = f'''<b>• Approved ✅

ϟ Card ->  <code>{cc}</code>
ϟ Status -> {last}
ϟ Gate -> Braintree Charge 1$

{str(dato(cc[:6]))}

ϟ Time -> {"{:.1f}".format(execution_time)} Seconds. 
ϟ - Programmer -> @F_TT_X⚡</b>'''

        cvc = f'''<b>• Approved ✅        
--------------------------------------------
- Card -> <code>{cc}</code>
- Message -> {last}
- GateWay -> {gate}
--------------------------------------------
{str(dato(cc[:6]))}
- Process Time -> {"{:.1f}".format(execution_time)} Seconds. 
--------------------------------------------
- Programmer • @F_TT_X</b>'''

        if 'CVV' in last or 'CCN' in last:
            bot.edit_message_text(text=cvc, chat_id=message.chat.id, message_id=ko)
        elif "Funds" in last or 'Invalid postal' in last or 'Charge 0.50$ ✅' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
            bot.edit_message_text(text=ok, chat_id=message.chat.id, message_id=ko)
        else:
            bot.edit_message_text(text=dec, chat_id=message.chat.id, message_id=ko)
    else:
        bot.reply_to(message, f'''- Welcome Dear ♡!
You are Not Subscribed FTXCHK BOT !❌

Your ID : {message.chat.id}
Programmer - @F_TT_X''')


















@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def resgpond_to_vhk(message):
	cc = message.text.replace('.bin ', '').replace('/bin ', '')
	bot.reply_to(message,f'''<b>ϟ BIN Info Lookup  🔍
	
ϟ - BIN -></b> <code>{cc}</code>

<b>{str(dato(cc[:6]))}</b>''')










import json
import threading
from datetime import datetime
import time




def get_user_info(user_id):
    try:
        chat = bot.get_chat(user_id)
        user_name = chat.first_name
        user_username = chat.username
        return user_name, user_username
    except Exception as e:
        m = (f"Error retrieving user info for ID {user_id}: {e}")
        return 'Unknown', 'Unknown'

def notify_admins(user_id, user_data):
    user_name, user_username = get_user_info(user_id)
    message = f'''- Subscription Expired Notification 😢

• User ID: {user_id}
• User Name: {user_name}
• Username: @{user_username}
• Plan: {user_data.get('plan', 'Free - Not Subscribed')}
• Expiration Date: {user_data.get('timer', 'N/A')}
'''
    for admin_id in myid:
        bot.send_message(admin_id, message)

def notify_user(user_id):
    try:
        bot.send_message(user_id, "Your Subscription Has Expired.")
    except Exception as e:
        m = (f"Error notifying user {user_id}: {e}")

def update_subscription_status():
    try:
        # قراءة بيانات المستخدمين من ملف data.json
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        current_time = datetime.now()
        updated = False  # لنعرف إذا كانت هناك تحديثات

        for user_id, user_data in json_data.items():
            timer_str = user_data.get('timer', None)
            if timer_str:
                try:
                    expiration_time = datetime.strptime(timer_str, "%Y-%m-%d %H:%M")
                    
                    if current_time > expiration_time:
                        user_data['plan'] = 'Free - Not Subscribed'
                        del user_data['timer']  # حذف الوقت بعد التحديث
                        updated = True
                        # إرسال إشعار إلى الأدمن
                        notify_admins(user_id, user_data)
                        # إرسال إشعار إلى المستخدم
                        notify_user(user_id)
                except ValueError:
                    m = (f"Date format error for user {user_id} with date {timer_str}")
        
        if updated:
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = ("Subscription status updated.")
    
    except Exception as e:
        mm = (f"Error updating subscription status: {e}")

def schedule_check():
    while True:
        update_subscription_status()
        time.sleep(1)  # تحقق كل دقيقة

# بدء عملية التحقق من الاشتراكات في خيط منفصل
check_thread = threading.Thread(target=schedule_check)
check_thread.start()















import json
from datetime import datetime, timedelta

# دالة تحقق من خطة المستخدم
def check_user_plan(user_id):
    with open('data.json', 'r') as file:
        json_data = json.load(file)
    if str(user_id) in json_data:
        user_plan = json_data[str(user_id)].get('plan', 'Free - Not Subscribed')
        timer = json_data[str(user_id)].get('timer', None)
        if user_plan != 'Free - Not Subscribed' and timer:
            date_str = timer.split('.')[0]
            try:
                provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                current_time = datetime.now()
                if current_time - provided_time <= timedelta(hours=0):  # قم بتعديل فترة الاشتراك حسب الحاجة
                    return True
            except Exception as e:
                print(f"Error parsing date for user {user_id}: {e}")
                return False
    return False
    
    
    



@bot.message_handler(commands=['kil'])
def qwwe(message):
    if str(message.from_user.id) in myid:
        mp, erop = 0, 0
        try:
            idd = message.from_user.id
            mes = message.text.replace("/kil ", "")
            bot.send_message(idd, mes)

            # إرسال الرسائل للمشتركين من data.json
            with open('data.json', 'r') as file:
                json_data = json.load(file)

            for user_id, details in json_data.items():
                if check_user_plan(user_id):
                    try:
                        mp += 1
                        bot.send_message(user_id, text=mes)
                    except Exception as e:
                        erop += 1
                        print(f"Error sending message to user {user_id}: {e}")

            bot.reply_to(message, f'''- Hello Kilwa
• Done Send - {mp}
• Bad Send - {erop}''')
        except Exception as err:
            bot.reply_to(message, f'- Was An error : {err}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")












@bot.message_handler(commands=["tot"])
def adode(message):
    if str(message.from_user.id) in myid:
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        vip_count = 0
        for user_id, details in json_data.items():
            user_plan = details.get('plan', 'Free - Not Subscribed')
            timer = details.get('timer', None)
            if user_plan != 'Free - Not Subscribed' and timer:
                try:
                    date_str = timer.split('.')[0]
                    provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    current_time = datetime.now()
                    if current_time - provided_time <= timedelta(hours=0):  # قم بتعديل فترة الاشتراك حسب الحاجة
                        vip_count += 1
                except Exception as e:
                    print(f"Error parsing date for user {user_id}: {e}")

        bot.reply_to(message, f'- Total VIP Subscribers: {vip_count}')
    else:
        bot.reply_to(message, "You are not authorized to use this command.")











import json
from datetime import datetime

@bot.message_handler(commands=['sh'])
def show_vip_subscribers(message):
    if str(message.chat.id) in myid:
        try:
            with open('data.json', 'r') as file:
                json_data = json.load(file)
        except Exception as e:
            bot.send_message(message.chat.id, f'- Error reading data file: {e}')
            return

        total_subscribers = 0
        subscriber_details = []

        for user_id, user_data in json_data.items():
            plan = user_data.get('plan', 'NO PLAN')
            if plan == 'VIP Subscribed':
                timer = user_data.get('timer', 'NO EXPIRATION DATE')
                if timer != 'NO EXPIRATION DATE':
                    try:
                        expiration_date = datetime.strptime(timer, "%Y-%m-%d %H:%M")
                        expiration_date_str = expiration_date.strftime("%Y-%m-%d %H:%M")
                    except ValueError:
                        expiration_date_str = 'INVALID DATE FORMAT'
                else:
                    expiration_date_str = 'NO EXPIRATION DATE'
                
                # الحصول على تفاصيل المستخدم
                try:
                    chat = bot.get_chat(user_id)
                    user_name = chat.first_name
                    user_username = chat.username
                    if user_name:
                        user_display = f"Name: {user_name}\nUsername: @{user_username}" if user_username else f"Name: {user_name}\nUsername: Not Available"
                    else:
                        # Skip users with no valid name
                        continue
                except Exception as e:
                    # Skip users with errors retrieving data
                    continue
                
                subscriber_details.append(f'''• User ID: {user_id}
{user_display}
• Plan: {plan}
• Expiration Date: {expiration_date_str}
━━━━━━━━━━━━━━━━━━━━━━
''')

                total_subscribers += 1

        if subscriber_details:
            details_message = "\n".join(subscriber_details)
            bot.send_message(message.chat.id, f'''- VIP Subscriber Details ✅💫

{details_message} - Total VIP Subscribers -> {total_subscribers} ✅
''')
        else:
            bot.send_message(message.chat.id, '- No VIP subscribers found.')











import json
from datetime import datetime

def remove_subscription(user_id):
    try:
        # قراءة بيانات المستخدمين من ملف data.json
        with open('data.json', 'r') as file:
            json_data = json.load(file)
        
        if user_id in json_data:
            # تحويل الخطة إلى FREE
            json_data[user_id]['plan'] = 'Free - Not Subscribed'
            del json_data[user_id]['timer']  # حذف الوقت إن وجد
            
            # كتابة البيانات المعدلة إلى data.json
            with open('data.json', 'w') as file:
                json.dump(json_data, file, indent=2, ensure_ascii=False)
            p = (f"Subscription for user {user_id} has been set to FREE.")
        else:
            mm= (f"User ID {user_id} not found in data.json.")
    
    except Exception as e:
        m = (f"Error removing subscription for user {user_id}: {e}")

@bot.message_handler(commands=['dele'])
def qwwem(message):
    if str(message.chat.id) in admins:
        user_id = message.text.replace("/dele ", "")
        
        # تحويل اشتراك المستخدم إلى FREE
        remove_subscription(user_id)
        
        try:
            chat = bot.get_chat(user_id)
            frs = chat.first_name
            use = chat.username
            bot.send_message(message.chat.id, f'''- Done ✅💫 

• Name Subscriber -> <code>{frs}</code> 
• User Subscriber -> @{use}

- IS Removed From Subscribers ✅''')
        except Exception as e:
            bot.send_message(message.chat.id, f'''- UnSuccessful Removal ❌

• User might not have opened your bot.

- Error -> {e}''')
    else:
        bot.send_message(message.chat.id, "You do not have permission to execute this command.")















@bot.message_handler(commands=['id'])
def send_user_info(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_username = message.from_user.username or 'NoUsername'  # التعامل مع حالة عدم وجود اسم مستخدم
    
    response_message = f'''🌟 Welcome » {user_first_name}
🆔 ID » <code>{user_id}</code>
📛 Name » {user_first_name}
🧑 Username » @{user_username}'''
    
    bot.reply_to(message, response_message, parse_mode='HTML')








@bot.message_handler(commands=["/menu"])
def adodre(message):
	if str(message.chat.id) in myid:
		bot.reply_to(message,'''- Welcome My Boss ♡
- Start Check Bot ¦ /start
- Add New Subscriber ¦ /add + ID
- Total Bot Users ¦ /tot
- Send Msg Forr All ¦ /kil + msg
- Delete A Subsc ¦ /dele + ID
- Show Sub's ID's ¦ /sh
- Stop And Start The Gate's /gate
------------------------------------
• Programmer ¦ @F_TT_X
• Channel ¦ @FtxCard''')





	
	
	
@bot.message_handler(func=lambda message: message.text.lower().startswith('.prices') or message.text.lower().startswith('/prices'))
def respondn_to_vhk(message):
 bot.reply_to(message,'''• Bot Prices •
⬅️ - Combo CC Checker Bot 🛒👑

- (4 Gates ) ⭐️
- ( TELEGRAM STARTS ) ⭐️
20  💷Day -> 3 ⚡️
50  💷 Week -> 7 ⚡️
100 💷Half month -> 10 ⚡️
150 💷Month -> 17 ⚡️

• Buy Premium✅
• We Accept All Payment Methods in World ✅
• (💴💷🌐👛💀..........🌎🌎)

• For Subscribe & inquiry -Connect Owner • 🛩
🖱👼@F_TT_X👼''')












import json
import threading
from datetime import datetime, timedelta
import random
import string

# وظيفة توليد كود
@bot.message_handler(commands=["code"])
def generate_code(message):
    def my_function():
        id = message.from_user.id
        if not str(id) in myid:
            return
        try:
            h = float(message.text.split(' ')[1])
            with open('data.json', 'r') as json_file:
                existing_data = json.load(json_file)
            
            characters = string.ascii_uppercase + string.digits
            pas = 'FTXCHECKERVİP-' + '2025' +'-' + ''.join(random.choices(characters, k=4))
            current_time = datetime.now()
            expiration_time = current_time + timedelta(hours=h)
            plan = 'VIP Subscribed'
            expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
            
            new_data = {
                pas: {
                    "plan": plan,
                    "timer": expiration_time_str
                }
            }
            
            existing_data.update(new_data)
            
            with open('data.json', 'w') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
            
            msg = f'''<b>ϟ Check World Code
ϟ Expire in -> {expiration_time_str}
ϟ Code -> <code>{pas}</code>
            
ϟ For redeem The Code Use /redeem code</b>'''
            bot.reply_to(message, msg, parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, f'<b>ERROR : {e}</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()

    
def generate_credit_card(message, bot, ko):
    try:
        # البحث عن رقم البطاقة والبيانات الأخرى في الرسالة
        match = re.search(r'(\d{6,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
        if match:
            card_number = match.group(1)
            
            # التحقق من صحة BIN
            if len(card_number) < 6 or card_number[0] not in ['4', '5', '3', '6']:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>BIN not recognized. Please enter a valid BIN ❌</b>''', parse_mode="HTML")
                return

            bin = card_number[:6]
            response_message = ""

            # توليد 10 بطاقات ائتمان
            for _ in range(10):
                month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
                year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)

                # تحديد طول الـ CVV بناءً على نوع البطاقة
                if card_number[:1] == "3":
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(1000, 9999)
                else:
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)

                # توليد بطاقة ائتمان مع الشهر، السنة، والـ CVV
                credit_card_info = generate_credit_card_info(card_number, month, year, cvv)
                response_message += f"<code>{credit_card_info}</code>\n"

            # جلب معلومات الـ BIN
            try:
                data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country_name', 'Unknown')
                country_flag = data.get('country_flag', 'Unknown')
                bank = data.get('bank', 'Unknown')
            except:
                brand = 'Unknown'
                card_type = 'Unknown'
                country = 'Unknown'
                country_flag = 'Unknown'
                bank = 'Unknown'

            # إرسال النتيجة إلى المستخدم
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"𝐁𝐈𝐍 ➜  {bin}\n\n{response_message}\n𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {brand} - {card_type}\n𝐁𝐚𝐧𝐤 ➜  {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}", parse_mode="HTML")
        else:
            # في حالة الإدخال غير الصحيح
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Invalid input. Please provide a BIN (Bank Identification Number) that is at least 6 digits but not exceeding 16 digits. 
Example: <code>/gen 412236xxxx |xx|2023|xxx</code></b>''', parse_mode="HTML")
    
    except IndexError:
        # معالجة الخطأ إذا كانت القائمة فارغة أو بها مشكلة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text="<b>BIN not recognized. Please enter a valid BIN ❌</b>")
    
    except Exception as e:
        # معالجة أي أخطاء غير متوقعة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"An error occurred: {str(e)}")

def generate_credit_card_info(card_number, expiry_month, expiry_year, cvv):
    generated_num = str(card_number)
    if card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
        while len(generated_num) < 15:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
    elif card_number[:1] == "3":
        while len(generated_num) < 14:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"

def generate_check_digit(num):
    num_list = [int(x) for x in num]
    for i in range(len(num_list) - 1, -1, -2):
        num_list[i] *= 2
        if num_list[i] > 9:
            num_list[i] -= 9
    return (10 - sum(num_list) % 10) % 10

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    return checksum % 10



def gen(bin):
	remaining_digits = 16 - len(bin)
	card_number = bin + ''.join([str(random.randint(0, 9)) for _ in range(remaining_digits - 1)])
	digits = [int(digit) for digit in card_number]
	for i in range(len(digits)):
		if i % 2 == 0:
			digits[i] *= 2
			if digits[i] > 9:
				digits[i] -= 9
	
	checksum = sum(digits)
	checksum %= 10
	checksum = 10 - checksum
	if checksum == 10:
		checksum = 0
	card_number += str(checksum)
	return card_number        
                
    
    
@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def respond_to_vbv(message):
    try:
        # محاولة قراءة النص الذي تم الرد عليه إذا كان موجودًا
        bm = message.reply_to_message.text
    except:
        # إذا لم يكن هناك رسالة تم الرد عليها، استخدم النص الحالي
        bm = message.text
    
    # استخراج الأرقام من الرسالة
    regex = r'\d+'
    try:
        matches = re.findall(regex, bm)
    except:
        bot.reply_to(message, '<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>', parse_mode="HTML")
        return

    # الحصول على أول 6 أرقام من BIN
    bin = ''.join(matches)[:6]
    ko = bot.reply_to(message, "<b>Checking Your bin...⌛</b>", parse_mode="HTML").message_id

    # التحقق من أن الـ BIN يتكون من 6 أرقام على الأقل
    if len(bin) >= 6:
        try:
            # طلب معلومات الـ BIN من API
            data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            country = data.get('country_name', 'Unknown')
            country_flag = data.get('country_flag', '🏳️')
            bank = data.get('bank', 'Unknown')
            
            # تكوين الرسالة النهائية
            msg = f'''<b>
𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ✅
    
𝐁𝐈𝐍 ➜ <code>{bin}</code>
    
𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {card_type} - {brand}  
𝐁𝐚𝐧𝐤 ➜ {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}
</b> '''
        except:
            # في حال حدوث خطأ أثناء طلب البيانات
            msg = '<b>𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ❌</b>'
    else:
        msg = '<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>'
    
    # تعديل الرسالة الأصلية مع النتيجة
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")      
@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
	ko = (bot.reply_to(message, "<b>Generating cards...⌛</b>",parse_mode="HTML").message_id)
	generate_credit_card(message,bot,ko)        
    
    
     
    
    
    
    

# وظيفة استرداد كود
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
    def my_function():
        try:
            # استخراج الكود من الرسالة
            re = message.text.split(' ')[1]
            
            # قراءة البيانات من data.json
            with open('data.json', 'r') as file:
                json_data = json.load(file)
            
            # تحقق من وجود الكود في البيانات
            if re in json_data:
                timer = json_data[re].get('timer', 'Unknown')
                typ = json_data[re].get('plan', 'Free - Not Subscribed')

                # تحديث بيانات المستخدم الحالي
                json_data[str(message.from_user.id)] = {
                    'timer': timer,
                    'plan': typ
                }
                
                # حذف الكود القديم
                del json_data[re]
                
                # كتابة البيانات المعدلة إلى data.json
                with open('data.json', 'w') as file:
                    json.dump(json_data, file, indent=2, ensure_ascii=False)

                msg = f'''<b>ϟ Check World VIP Subscribtion Done ✅
ϟ Expires in -> {timer}</b>'''
                bot.reply_to(message, msg, parse_mode="HTML")
            else:
                bot.reply_to(message, '<b>Incorrect code or it has already been redeemed </b>', parse_mode="HTML")

        except KeyError as e:
            print(f'KeyError: {e}')
            bot.reply_to(message, '<b>Incorrect code or it has already been redeemed </b>', parse_mode="HTML")
        except Exception as e:
            print('ERROR : ', e)
            bot.reply_to(message, '<b>There was an error processing your request. Please try again later.</b>', parse_mode="HTML")

    my_thread = threading.Thread(target=my_function)
    my_thread.start()
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    

# وظيفة إضافة مستخدم جديد إلى خطة VIP
@bot.message_handler(commands=['add'])
def add_subscription(message):
    def my_function():
        try:
            chid = message.chat.id
            command_text = message.text.replace('/add ', '')
            user_id, duration_hours = command_text.split()
            duration_hours = int(duration_hours)
            
            if str(message.chat.id) in myid:
                current_time = datetime.now()
                expiration_time = current_time + timedelta(hours=duration_hours)
                expiration_time_str = expiration_time.strftime("%Y-%m-%d %H:%M")
                plan = 'VIP Subscribed'
                
                # قراءة البيانات من data.json
                with open('data.json', 'r') as json_file:
                    existing_data = json.load(json_file)
                
                # تحديث بيانات المستخدم الجديد
                existing_data[user_id] = {
                    'timer': expiration_time_str,
                    'plan': plan
                }
                
                # كتابة البيانات المعدلة إلى data.json
                with open('data.json', 'w') as json_file:
                    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
                
                # الحصول على تفاصيل المستخدم
                try:
                    chat = bot.get_chat(user_id)
                    frs = chat.first_name
                    use = chat.username
                    user_display = f"Name: {frs}\nUsername: @{use}" if use else f"Name: {frs}\nUsername: Not Available"
                except Exception as e:
                    user_display = f"Name: Unknown\nUsername: Unknown"
                
                bot.send_message(chid, f'''- Done Add -> <code>{user_id}</code> 

• Subscription Duration -> {duration_hours} hours
• {user_display}
- Added to Subscribers List ✅''')
            else:
                bot.send_message(chid, ' - Unauthorized Access !!!!')
        except Exception as e:
            bot.reply_to(message, f'- Was An Error -> {e}')

    my_thread = threading.Thread(target=my_function)
    my_thread.start()











def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")
		continue
