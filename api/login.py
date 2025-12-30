import base64
import json
from colorama import Fore
import requests 

def login(username,password,uuid) -> dict :
    headers = {
            "Host": "i.instagram.com",
            "X-Ig-App-Locale": "en_US",
            "X-Ig-Device-Locale": "en_US",
            "X-Ig-Mapped-Locale": "en_US",
            "X-Pigeon-Session-Id": "UFS-39d3390f-f76a-4086-94bc-e9d6a0ef7de0-1",
            "X-Bloks-Version-Id": "9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a",
            "X-Ig-Www-Claim": "0",
            "X-Bloks-Is-Prism-Enabled": "false",
            "X-Bloks-Is-Layout-Rtl": "false",
            "X-Ig-Device-Id": uuid,
            "X-Ig-Family-Device-Id": uuid,
            "X-Ig-Android-Id": "android-9fa31f7eb19661f4",
            "X-Ig-Timezone-Offset": "0",
            "X-Fb-Connection-Type": "WIFI",
            "X-Ig-Connection-Type": "WIFI",
            "X-Ig-Capabilities": "3brTv10=",
            "Priority": "u=3",
            "User-Agent": "Instagram 309.1.0.41.113 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)",
            "Accept-Language": "en-US",
            "X-Mid": "Zl8PKgABAAGDZNC7T7f0Kd5n7gwZT",
            "Ig-Intended-User-Id": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True",
    } 
   
    data = {
            "jazoest": "22452",
            "phone_id": uuid,
            "enc_password": "#PWD_INSTAGRAM:0:0:" + password,
            "username": username,
            "adid": uuid,
            "guid": uuid,
            "device_id": uuid,
            "google_tokens": "[]",
            "login_attempt_count": "0",
    }

    req = requests.post(
            url="https://i.instagram.com/api/v1/accounts/login/",
            headers=headers,
            data=data,
    )

    if req.text.__contains__("logged_in_user"):
            pk = str(req.json()['logged_in_user']['pk'])
            fbid = str(req.json()['logged_in_user']['fbid_v2'])
            head = req.headers["ig-set-authorization"]
          
            base64Encoded = head.split(":")[2]
            decoded_json_string = base64.b64decode(base64Encoded).decode("utf-8")

            json_data = json.loads(decoded_json_string)
            session = json_data["sessionid"]

            return {
                   'logged_in':True,
                   'reason':'None',
                   'sessionid':session,
                   'pk':pk,
                   'fbid':fbid
            }
            

    elif req.text.__contains__("checkpoint"):
            print(Fore.LIGHTBLUE_EX + "Account needs Checkpoint\nPlease approve login and click enter.")
            input()
            login(username,password,uuid)

    else:
            print(Fore.RED + "Password or username is incorrect")
            input()
            return {
                   'logged_in':False,
                   'reason':'Bad Password',
                   'sessionid':'None'
            }

