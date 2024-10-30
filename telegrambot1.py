import requests

# Replace these with your bot token and chat ID
BOT_TOKEN = '7613413804:AAFS9CQ0gNVguHEH0OBtQ398R98O1dnjP6w'
CHAT_ID = '7839184160'
MESSAGE = 'Hello from Polize Doge bot!'

def send_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.text)

# Send the message
send_message(BOT_TOKEN, CHAT_ID, MESSAGE)
