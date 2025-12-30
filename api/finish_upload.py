import json
import os
import requests , random , time
from colorama import Fore

def finish(pk,upload_id,session,caption):
    headers = {
    'Host': 'i.instagram.com',
    'X-Ig-Eu-Configure-Disabled': 'true',
    'X-Ig-App-Locale': 'en_US',
    'X-Ig-Device-Locale': 'en_US',
    'X-Ig-Mapped-Locale': 'en_US',
    'X-Pigeon-Session-Id': 'UFS-c3cf95cc-a918-4848-8da2-c5fbb6af0995-0',
    'X-Pigeon-Rawclienttime': '1762618201.887',
    'X-Ig-Bandwidth-Speed-Kbps': '2190.000',
    'X-Ig-Bandwidth-Totalbytes-B': '140223',
    'X-Ig-Bandwidth-Totaltime-Ms': '64',
    'X-Bloks-Version-Id': '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf',
    'X-Ig-Www-Claim': 'hmac.AR1t5viLZHk-fPfvnIwFP2G9EcXB-uSUBBBwBDh2PvrUp2AU',
    'X-Bloks-Prism-Button-Version': 'CONTROL',
    'X-Bloks-Prism-Colors-Enabled': 'true',
    'X-Bloks-Prism-Ax-Base-Colors-Enabled': 'false',
    'X-Bloks-Prism-Font-Enabled': 'false',
    'X-Bloks-Is-Layout-Rtl': 'false',
    'X-Ig-Device-Id': 'ca4dd24f-c663-4add-8a41-71ba9e84eb01',
    'X-Ig-Family-Device-Id': 'e3e38729-5a92-4783-94b1-ffe5356ea212',
    'X-Ig-Android-Id': 'android-990cd84386ee9b4f',
    'X-Ig-Timezone-Offset': '0',
    'X-Ig-Nav-Chain': 'SelfFragment:self_profile:5:main_profile:1762616465.501:::1762616465.501,ProfileMediaTabFragment:self_profile:6:button:1762616465.583:::1762617197.572,ProfileMediaTabFragment:self_profile:10:button:1762617313.257:::1762617313.257,QuickCaptureFragment:stories_precapture_camera:11:camera_tab_bar:1762618060.856:::1762618077.870,QuickCaptureFragment:feed_precapture_camera:21:button:1762618077.872:::1762618108.294,PhotoFilterFragment:photo_filter:25:button:1762618110.224:::1762618110.224,FollowersShareFragment:media_broadcast_share:26:next:1762618132.330:::1762618199.62',
    'X-Ig-Client-Endpoint': 'FollowersShareFragment:media_broadcast_share',
    'Retry_context': '{"num_reupload":0,"num_step_manual_retry":0,"num_step_auto_retry":0}',
    'X-Fb-Session-Id': 'nid=qp5+EELspMzd;nc=1;fc=1;bc=0;',
    'X-Fb-Session-Private': 'PwjfDVeVVRsD',
    'X-Fb-Connection-Type': 'WIFI',
    'X-Ig-Connection-Type': 'WIFI',
    'X-Fb-Network-Properties': 'Validated;dhcpServerAddr=10.0.3.2;LocalAddrs=/fe80::4ba7:85f8:7c64:dbfb,/10.0.3.16,;',
    'X-Ig-Capabilities': '3brTv10=',
    'X-Ig-App-Id': '567067343352427',
    'User-Agent': 'Instagram 361.0.0.46.88 Android (34/14; 418dpi; 1080x2215; Genymobile/Samsung; Galaxy S24; vbox86p; vbox86; en_US; 674675155)',
    'Accept-Language': 'en-US',
    'Cookie':'sessionid='+str(session),
    'X-Mid': 'aQzw4AABAAHMJ-vyxmgdfNaXWNug',
    'Ig-U-Ds-User-Id': str(pk),
    'Ig-U-Rur': 'CLN,2241055671,1794154133:01fe1f8d731bf404b135410da5e04a8c2d9d37bc29b5f02433cf295adbcb530b0f739889',
    'Ig-Intended-User-Id': str(pk),
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }

    data = {
        'signed_body': 'SIGNATURE.{"app_attribution_android_namespace":"","camera_entry_point":"360","camera_session_id":"8b1584f2-001f-458f-83a4-4ad991d3e034","original_height":"720","camera_model":"Galaxy S24","include_e2ee_mentioned_user_list":"1","hide_from_profile_grid":"false","scene_capture_type":"","timezone_offset":"0","source_type":"3","_uid":"2241055671","device_id":"android-990cd84386ee9b4f","_uuid":"ca4dd24f-c663-4add-8a41-71ba9e84eb01","creation_tool_info":"[]","creation_logger_session_id":"8b1584f2-001f-458f-83a4-4ad991d3e034","date_time_digitized":"2025:11:08 16:08:29","nav_chain":"SelfFragment:self_profile:5:main_profile:1762616465.501:::1762616465.501,ProfileMediaTabFragment:self_profile:6:button:1762616465.583:::1762617197.572,ProfileMediaTabFragment:self_profile:10:button:1762617313.257:::1762617313.257,QuickCaptureFragment:stories_precapture_camera:11:camera_tab_bar:1762618060.856:::1762618077.870,QuickCaptureFragment:feed_precapture_camera:21:button:1762618077.872:::1762618108.294,PhotoFilterFragment:photo_filter:25:button:1762618110.224:::1762618110.224","caption":"'+str(caption)+'","audience":"default","upload_id":"'+str(upload_id)+'","bottom_camera_dial_selected":"11","publish_id":"1","original_width":"1280","camera_make":"Genymobile","edits":{"filter_type":0,"filter_strength":1.0,"crop_original_size":[1280.0,720.0],"crop_center":[0.0,-0.0],"crop_zoom":1.7777778},"extra":{"source_width":1280,"source_height":720},"device":{"manufacturer":"Genymobile","model":"Galaxy S24","android_version":34,"android_release":"14"},"overlay_data":[]}',
    }

    response = requests.post('https://i.instagram.com/api/v1/media/configure/', headers=headers, data=data, verify=False)
    print(response.text)