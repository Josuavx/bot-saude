
from google_auth_oauthlib.flow import Flow
import requests
from utils import CONST
import json
import time


def Conversa(credencial, txt):
    payload = payload = {
        "queryParams": {
            "source": "DIALOGFLOW_CONSOLE",
            "timeZone": "America/Fortaleza",
            "sentimentAnalysisRequestConfig": {
                "analyzeQueryTextSentiment": True
            }
        },
        "queryInput": {
            "text": {"text": txt, "languageCode": "pt-br"}
        }
    }

    headers = {
        'accept': 'application/json text/plain, */*',
        'content-type': 'application/json; charset=UTF-8',
        'authorization': 'Bearer ' + credencial
    }

    res = requests.post(CONST.URL, headers=headers, json=payload)
    if(res.status_code == 200):
        resp = json.loads(res.text)
        resp_message = resp['queryResult']['fulfillmentMessages']
 
        if len(resp_message) > 1:
            c = 0
            re = []
            for i in resp_message:
                contagem = resp_message[c]['text']['text'][0]
                re.append(contagem)
                c += 1
        else:
            re = contagem = resp_message[0]['text']['text'][0]
         
        return re

