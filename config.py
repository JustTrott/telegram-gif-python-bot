import os
import yaml
import configparser as cp

class Config():
    def __init__(self, file_name='config.yml'):
        self.cp = cp.ConfigParser()
        self.telegramGroup = 'Telegram'
        self.exceptionsKey = 'exceptions'
        self.cfg = self.get_config(file_name)
        self.get_exceptions()

    def get_config(self, file_name):
        try:
            with open(file_name, 'r') as yamlfile:
                config = yaml.load(yamlfile, Loader=yaml.BaseLoader)
        except:
            config_dict = {}
            config_dict['config'] = {}
            config_dict['config']['connection'] = {
                'bot_token': None
            }
            with open(file_name, 'w') as yamlfile:
                yaml.dump(config_dict, yamlfile, default_flow_style=False)
                print('No config.yml file was not found. Succesfully created empty config.yml file')
            with open(file_name, 'r') as yamlfile:
                config = yaml.load(yamlfile, Loader=yaml.BaseLoader)
        return config

    def get_exceptions(self):
        if os.path.isfile('exceptions.cfg'):
            self.cp.read('exceptions.cfg')
        else:
            self.cp['Telegram'] = {}
            self.cp['Telegram']['exceptions'] = ''
            with open('exceptions.cfg', 'w') as file:
                self.cp.write(file)

    def add_exception(self, exception):
        if self.cp['Telegram']['exceptions'].find(exception) > -1:
            return False
        self.cp['Telegram']['exceptions'] += f'\n{exception}'
        with open('exceptions.cfg', 'w') as file:
            self.cp.write(file)
        return True

    def remove_exception(self, exception):
        exceptions = self.cp['Telegram']['exceptions'][1:].split('\n')
        try:
            exceptions.remove(exception)
        except:
            return False
        self.cp['Telegram']['exceptions'] = '\n' + '\n'.join(exceptions)
        with open('exceptions.cfg', 'w') as file:
            self.cp.write(file)
        return True

    @property
    def bot_token(self):
        return self.cfg['config']['connection']['bot_token']

    @property
    def exceptions(self):
        return self.cp['Telegram']['exceptions'][1:].split('\n')

if __name__ == '__main__':
    config = Config('config.yml')
    config.remove_exception('lulbw')
    print(config.exceptions)
