from config_reader import *
import random
import gui
import browser

whatsapp_cookie = ''
telegram_cookie = ''
yandex_disk_cookie = ''

def generate_random_string(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def init():
    os.system('open whatsapp-desktop')
    os.system('open telegram')


def main():
    main_config = ConfigMain('../../cofnig/main_config.json')
    http_requests = HttpRequestsCollection('../../cofnig/' + main_config.http_config)
    payload_config = PayloadConfig('../../cofnig/' + main_config.payload_config)
    telegram_config = TelegramDataConfig('../../cofnig/' + main_config.telegram_config)
    whatsapp_config = WhatsAppMessageConfig('../../cofnig/' + main_config.whatsapp_config)
    yandexdisk_config = YandexDiskConfig('../../cofnig/' + main_config.yandex_disk_config)

    init()

    while True:
        rand_selection = random.randint(1, 5)
        if rand_selection == 1:
           WhatsAppGen(whatsapp_config)
        elif rand_selection == 2:
            PayloadGen(payload_config)
        elif rand_selection == 3:
            YandexDiskGen(yandexdisk_config)
        elif rand_selection == 4:
            TelegramGen(telegram_config)
        elif rand_selection == 5:
            HttpGen(http_requests)


    

    
