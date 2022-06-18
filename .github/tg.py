import telegram
from tgconfig import *
from json import load
import multiprocessing
import os
from time import sleep as wait

def deploy():
    os.system(f'~/bot-api --local --api-id={TG_API_ID} --api-hash={TG_API_HASH}')

def bot():
    wait(10)
    f = open('commit.json')
    data = load(f)
    f.close()

    bot = telegram.Bot(TG_TOKEN, base_url="http://0.0.0.0:8081/bot")
    bot.send_photo(TG_POST_ID, open('alpha.png', 'rb'), f'''*Libretube {data['sha'][0:7]} // Alpha*

{data['commit']['message']}

Signed-off-by: {data['commit']['author']['name']}
''', parse_mode=telegram.ParseMode.MARKDOWN)
    bot.send_media_group(TG_POST_ID, [telegram.InputMediaDocument(open('app-x86-debug.apk', 'rb')), telegram.InputMediaDocument(open('app-x86_64-debug.apk', 'rb')), telegram.InputMediaDocument(open('app-armeabi-v7a-debug.apk', 'rb')), telegram.InputMediaDocument(open('app-arm64-v8a-debug.apk', 'rb'))])
    os.system('killall -9 python || true')
    
if __name__ == '__main__':
    multideploy = multiprocessing.Process(target=deploy)
    multibot = multiprocessing.Process(target=bot)
    multideploy.start()
    multibot.start()
    multideploy.join()
    multibot.join()
