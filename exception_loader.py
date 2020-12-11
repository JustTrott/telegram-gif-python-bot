import os
import configparser as cp

exceptionsFile = 'config.ini'
telegramGroup = 'Telegram'
exceptionsKey = 'exceptions'

class ExceptionLoader:
    def __init__(self):
        self.cp = cp.ConfigParser()
        self.check_config()

    def check_config(self):
        if os.path.isfile(exceptionsFile):
            self.cp.read(exceptionsFile)
            return
        self.create_config()

    def create_config(self):
        self.cp[telegramGroup] = {}
        self.cp[telegramGroup][exceptionsKey] = ''
        with open(exceptionsFile, 'w') as file:
            self.cp.write(file)

    def add_exception(self, exception):
        if self.cp[telegramGroup][exceptionsKey].find(exception) > -1:
            return False
        self.cp[youtubeGroup][exceptionsKey] += f'\n{exception}'
        with open(configFile, 'w') as file:
            self.cp.write(file)
        return True

    def remove_exception(self, exception):
        exceptions = self.cp[telegramGroup][exceptionsKey][1:].split('\n')
        exceptions.remove(exception)
        self.cp[telegramGroup][exceptionsKey] = '\n' + '\n'.join(exceptions)
        with open(configFile, 'w') as file:
            self.cp.write(file)

    @property
    def exceptions(self):
        return self.cp[telegramGroup][exceptionsKey][1:].split('\n')

