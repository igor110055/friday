import pickle
import os
import traceback

#local imports
import config
#from telegram_notificator import TelegramNotificator

#class Disk(metaclass=singleton.Singleton):
class Disk():
    def __init__(self):

        #logging object
        #self.telegram_notificator = TelegramNotificator()

        pass


    #this method saves an inputted object into the disk, using the file name provided, it will overwrite the current file
    def save(self, filename, obj):
        try:
            with open(os.path.join(os.path.dirname(__file__), f"config/{filename}.pickle"), "wb") as file:
                pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)

        except Exception as e:
            self.telegram_notificator.exception(traceback.format_exc())


    #this methods loads a file written into the disk
    def load(self, filename):
        try:
            with open(os.path.join(os.path.dirname(__file__), f"config/{filename}.pickle"), "rb") as file:
                return pickle.load(file)

        except Exception as e:
            self.telegram_notificator.exception(traceback.format_exc())