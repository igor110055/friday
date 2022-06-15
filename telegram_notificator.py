import requests
import config
#from logger import get_logger


# singleton pattern implementation
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TelegramNotificator(metaclass=Singleton):

    # constructor
    def __init__(self):

        # telegram group with the traders:
        self.notifications_url = config.TELEGRAM_NOTIFICATIONS_URL
        # telegram group with the devs but no the traders:
        self.exception_url = config.TELEGRAM_EXCEPTION_URL

        # set the logging object to be what we get as a parameter, which should be the same used by
        # the rest of the bot
        #self.logging = get_logger()


    # sends a message in telegram to the traders group and also to our logger
    def notification(self, message):
        # log in our logger:
        #self.logging.exception(message)

        # send message to the jarvis positions group where the traders are:
        requests.get(f'{self.notifications_url}{message}')


    # sends a message in telegram to the devs (not to the traders) group and also to our logger to help dev
    def exception(self, message):

        # log in our logger:
        #self.logging.exception(message)

        # send message to jarvis exceptions telegram group where the developers are:
        requests.get(f'{self.exception_url}{message}')


    # sends a message in telegram to all the groups and also to our logger
    def emergency(self, message):

        # log in our logger:
        #self.logging.exception(message)

        # send message to jarvis exceptions telegram group where the developers are:
        requests.get(f'{self.exception_url}{message}')

        # send message to the jarvis positions group where the traders are:
        requests.get(f'{self.notifications_url}{message}')
