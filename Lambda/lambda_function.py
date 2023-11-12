from datetime import datetime
import json
import os
import requests


def handler(event, context):
    webhook_status = set_telegram_webhook()
    instruction_dict = receive_parse_telegram(event)
    send_telegram(instruction_dict)
    return f'{datetime.now()}: function end'


def set_telegram_webhook():
    webhook_url = (
            'https://api.telegram.org/bot'
            + os.environ['telegram_token']
            + '/setWebhook?url='
            + os.environ['function_url']
    )
    webhook_response = requests.post(webhook_url).json()
    webhook_response = webhook_response['ok']
    print(f'set_telegram_webhook(): webhook set? {webhook_response}')
    return webhook_response


def receive_parse_telegram(event):
    """event e.g.
    {'version': '2.0', 'routeKey': '$default', 'rawPath': '/', 'rawQueryString': '',
    'headers': {'content-length': '350', 'x-amzn-tls-cipher-suite': 'ECDHE-RSA-AES128-GCM-SHA256', 'x-amzn-tls-version': 'TLSv1.2', 'x-amzn-trace-id': 'Root=1-6550f12a-1eaaba6d413b64a14f72d5ee', 'x-forwarded-proto': 'https', 'host': 'cw6w3detxaixc4g5624c5xa4nq0yrmby.lambda-url.eu-west-1.on.aws', 'x-forwarded-port': '443', 'content-type': 'application/json', 'x-forwarded-for': '91.108.6.32', 'accept-encoding': 'gzip, deflate'},
    'requestContext': {'accountId': 'anonymous', 'apiId': 'cw6w3detxaixc4g5624c5xa4nq0yrmby', 'domainName': 'cw6w3detxaixc4g5624c5xa4nq0yrmby.lambda-url.eu-west-1.on.aws', 'domainPrefix': 'cw6w3detxaixc4g5624c5xa4nq0yrmby', 'http': {'method': 'POST', 'path': '/', 'protocol': 'HTTP/1.1', 'sourceIp': '91.108.6.32', 'userAgent': None}, 'requestId': '1e708d6f-2ceb-4f65-9a06-58d8625a2429', 'routeKey': '$default', 'stage': '$default', 'time': '12/Nov/2023:15:37:14 +0000', 'timeEpoch': 1699803434540},
     'body': '{"update_id":251885733,\n"message":{"message_id":59,"from":{"id":140379965,"is_bot":false,"first_name":"(ARTHUR) Chionh Hwai Teck \\u848b\\u6000\\u5fb7","username":"artc95","language_code":"nl"}, "chat":{"id":140379965,"first_name":"(ARTHUR) Chionh Hwai Teck \\u848b\\u6000\\u5fb7","username":"artc95","type":"private"},"date":1699803434,"text":"abundance"}}', 'isBase64Encoded': False}
    """
    print(f'receive_parse_telegram() event - {event}')
    telegram_body = json.loads(event["body"])
    telegram_text = telegram_body["message"]["text"]
    print(f'receive_parse_telegram(): telegram_text = {telegram_text}')
    return telegram_text
    # try:
    #     if 'basic' in ast.literal_eval(telegram_text):
    #         # ast.literal_eval() converts dict/list in str, to actual dict/list
    #         print(f'receive_parse_telegram() telegram text parsed as "basic" instruction dict')
    #         return ast.literal_eval(telegram_text)
    # except Exception as e:
    #     print(f'receive_parse_telegram() exception: {e}')
    #     return telegram_text


def send_telegram(message):
    chat_ids = ["140379965"]
    message = str(message)
    for id in chat_ids:
        notification_url = ("https://api.telegram.org/bot" + os.environ['telegram_token']
                            + "/sendMessage?parse_mode=markdown&chat_id=" + id
                            + "&text=" + message)
        requests.get(notification_url)
    return message
