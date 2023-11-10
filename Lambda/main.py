import json
import requests
import os
import ast

"""
HOW-TO:
- deployed in AWS region 'London'
- in Telegram bot 'test': send message 'AWS'
- in Telegram bot 'test': receive message 'success', with order placed in crypto.com
"""


def set_telegram_webhook():
    webhook_url = ('https://api.telegram.org/bot'
                        + os.environ['telegram_token']
                        + '/setWebhook?url='
                        + os.environ['function_url'])
    webhook_response = requests.post(webhook_url).json()
    webhook_response = webhook_response['ok']
    print(f'set_telegram_webhook() webhook set: {webhook_response}')

def receive_parse_telegram(event):
    telegram_body = json.loads(event["body"])
    telegram_text = telegram_body["message"]["text"]
    print(f'receive_parse_telegram() telegram_text is {telegram_text}')
    try:
        if 'basic' in ast.literal_eval(telegram_text):
            # ast.literal_eval() converts dict/list in str, to actual dict/list
            print(f'receive_parse_telegram() telegram text parsed as "basic" instruction dict')
            return ast.literal_eval(telegram_text)
    except Exception as e:
        print(f'receive_parse_telegram() exception: {e}')
        return telegram_text