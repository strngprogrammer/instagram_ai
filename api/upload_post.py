import json
import os
import requests , random , time
from colorama import Fore

def generate_upload_id(somefile):
        upload_id = str(int(time.time()))  # e.g : 1524115561404
        milieu = '_0_'
        hashcode = str(hash(os.path.basename(somefile))) # e.g : 363954952
        final = upload_id + milieu + str(hashcode)  # e.g : # 1524115561404_0_363954952
        return upload_id, hashcode, final

def get_photo(image,width,height,image_file,session,pk):
    upload_idonly, hashcode, final = generate_upload_id(image_file)
    upload_id = int(time.time())
    rupload = json.dumps({"media_type":1,"upload_id":f"{upload_id}","session_id":f"{upload_id}","upload_media_height":width,"upload_media_width":height})
    headers = {
        'Host': 'i.instagram.com',
        'X_fb_photo_waterfall_id': '32b63383-64c2-449b-9530-e538d13839d5',
        'X-Entity-Length': str(len(image)),
        'X-Entity-Name': str(final),
        'X-Instagram-Rupload-Params': rupload,
        'X-Entity-Type': 'image/webp',
        'Offset': '0',
        'X-Ig-Salt-Ids': '332018011,332012435',
        'X-Fb-Session-Id': 'nid=qp5+EELspMzd;nc=1;fc=1;bc=0;',
        'X-Fb-Session-Private': 'PwjfDVeVVRsD',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Fb-Network-Properties': 'Validated;dhcpServerAddr=10.0.3.2;LocalAddrs=/fe80::4ba7:85f8:7c64:dbfb,/10.0.3.16,;',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 148.0.0.33.121 Android (34/14; 418dpi; 1080x2215; Genymobile/Samsung; Galaxy S24; vbox86p; vbox86; en_US; 674675155)',
        'Accept-Language': 'en-US',
        'Cookie':f'sessionid={session}',
        'X-Mid': 'aQzw4AABAAHMJ-vyxmgdfNaXWNug',
        'Ig-U-Ds-User-Id': str(pk),
        'Ig-U-Rur': 'CLN,2241055671,1794154110:01fe54cdfa9eb6cad83e53f74d82eeffd918e17adfeaccfa2ed1348a1c2528583087d700',
        'Ig-Intended-User-Id': str(pk),
        'Content-Type': 'application/octet-stream',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }
    response = requests.post(
        f'https://i.instagram.com/rupload_igphoto/{final}',
        headers=headers,
        data=image,  
    )

    new_upload_id = ''

    if 'upload_id' in response.text:
          new_upload_id = str(response.json()['upload_id'])
          return new_upload_id
    else:
          print(response.text)
          print(Fore.RED+'Error')
          exit()
    
    
