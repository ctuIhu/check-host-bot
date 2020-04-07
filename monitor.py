import requests
import json
session = requests.session()


domain = "https://mb.com.ph"
ch_url = "https://check-host.net:443/check-http?host=" + domain + "&max_nodes=24"
ch_headers = {"User-Agent": "curl/7.54.0", "Accept": "application/json", "Connection": "close"}



result = session.get(ch_url, headers=ch_headers)
tangina = json.loads(result.text)

url = str(tangina['permanent_link'])


def monitor_url(url1):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&disable_web_page_preview=1&parse_mode=Markdown&text=' + url1

    response = requests.get(send_text)

    return response.json()

test = monitor_url("URL: " + url +"")

