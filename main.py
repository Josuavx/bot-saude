
from google_auth_oauthlib.flow import Flow
import requests
from utils import CONST
import json
from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

appflow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['openid', 'https://www.googleapis.com/auth/dialogflow',
            'https://www.googleapis.com/auth/cloud-platform'],
    redirect_uri='http://localhost:5000')

auth_uri = appflow.authorization_url()
print(auth_uri)

"""
driver = webdriver.Firefox()
driver.get(auth_uri[0])
##print(auth_uri)
time.sleep(3)
username = driver.find_element(By.NAME, CONST.id_username)
username.send_keys(CONST.USERNAME)
username.send_keys(Keys.RETURN)
time.sleep(3)
password = driver.find_element(By.NAME, CONST.id_password)
password.send_keys(CONST.PASSWORD)
password.send_keys(Keys.RETURN)
time.sleep(40)
"""
"""btn = driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d') 
btn.click()
"""
#driver.quit()

code = input('digite: ')
appflow.fetch_token(code=code)
credencial = appflow.credentials


while(True):
    txt = input("Mensagem: ")
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
        'authorization': 'Bearer ' + credencial.token
    }

    res = requests.post(CONST.URL, headers=headers, json=payload)
    if(res.status_code==200):
        resp = json.loads(res.text)
        resp_message = resp['queryResult']['fulfillmentMessages']
        print(resp_message)


#identifier
#password
#VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe P62QJc qfvgSe xYnMae TrZEUc lw1w4b