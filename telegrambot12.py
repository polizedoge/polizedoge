import requests

BOT_TOKEN = '7613413804:AAFS9CQ0gNVguHEH0OBtQ398R98O1dnjP6w'
GROUP_CHAT_ID = '-1002360511110'  # Replace with the actual group chat ID, usually starts with -100

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': GROUP_CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()

# Example usage
message = "Hello, Polize Doge community! This is a test message."
send_message(message)
