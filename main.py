import requests , time , threading , random, string , uuid
from colorama import Fore , init
from api.login import login
from bot.get_caption import get_caption
from bot.get_image import get_image
from api.upload_post import get_photo
from api.finish_upload import finish
import os , textwrap
class Bot:
    def __init__(self):
        init(autoreset=True)

        self.shared = 0
        self.error = 0
        self.hours = 0

        self.start()

    def start(self):
        print(
f"""
{Fore.LIGHTGREEN_EX}Welcome to automatic instagram post using ai,
{Fore.LIGHTGREEN_EX}This bot was made by strngprogrammer
{Fore.LIGHTCYAN_EX}Have fun.
"""
        )
        print(Fore.YELLOW+"\nPlease login with your instagram account")
        print(Fore.LIGHTYELLOW_EX+'Use session id ? Y/y')

        inp = str(input('>'))
        if inp == "y":
            self.sessionid = str(input(Fore.LIGHTYELLOW_EX+'Session id >'))
            self.pk =  self.sessionid.split('%3')[0] 
            self.get_info()
        else:
            username = str(input(Fore.LIGHTYELLOW_EX+'Username >'))
            password = str(input(Fore.LIGHTYELLOW_EX+'Password >'))

            muuid = str(uuid.uuid4())

            result = login(username,password,muuid)

            if result['logged_in'] == True:

                self.sessionid = result['sessionid']
                print(self.sessionid)
                self.pk = result['pk']
                print(Fore.LIGHTGREEN_EX+f'Logged in to @{username}.')
                self.get_info()
        
            
        
            else:
                exit(0)

    def get_info(self):
        
        self.prompt = open('caption.txt','r').read()

        self.timesleep = int(input(Fore.YELLOW + 'Time sleep in hours : '))

        self.start_posting()


    def start_posting(self):
        
        threads = []

        t1 = threading.Thread(target=self.posting)
        threads.append(t1)
        t1.start()

        t2 = threading.Thread(target=self.monitoring)
        threads.append(t2)
        t2.start()

    def posting(self):

        while True:

            caption = get_caption(self.prompt)
          

            geti = get_image(textwrap.dedent(caption).replace('\n',' '))
            upload_id = get_photo(image=geti,width='1280',height='720',image_file='image.png',pk=self.pk,session=self.sessionid)

            finish(pk=self.pk,session=self.sessionid,upload_id=upload_id,caption=textwrap.dedent(caption).replace('\n',' '))

            self.shared += 1

            time.sleep(self.timesleep * 3600)


    def monitoring(self):

        while True:
            os.system('clear||cls')
            print(
                f'''
{Fore.LIGHTGREEN_EX} Shared : {Fore.WHITE} {str(self.shared)} 
{Fore.LIGHTRED_EX} Error : {Fore.WHITE} {str(self.error)} 

'''
            )
            time.sleep(5)

        
        
            
  



if __name__ == "__main__":
    Bot()

