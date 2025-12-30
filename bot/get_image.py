import os
import requests
from PIL import Image

def get_image(prompt) :
    headers = {
        'Authorization': 'Bearer api_key',
        # TODO Add api key
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = '{ "prompt": "create a profitional image for an instagram post talking about '+prompt+'" }'

    response = requests.post(
        # TODO Add account_id
        'https://api.cloudflare.com/client/v4/accounts/account_id/ai/run/@cf/bytedance/stable-diffusion-xl-lightning',
        headers=headers,
        data=data,
    )


    f = open('image.png','wb')

    f.write(response.content)
    f.close()

    return response.content