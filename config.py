import yaml

class Config():
    def __init__(self, fileName='config.yml'):
        try:
            with open(fileName, 'r') as yamlfile:
                self.cfg = yaml.load(yamlfile, Loader=yaml.BaseLoader)
        except:
            config_dict = {}
            config_dict['config'] = {}
            config_dict['config']['connection'] = {
                'bot_token': None
            }
            config_dict['config']['telegram'] = {}
            config_dict['config']['telegram']['prefix'] = None
            with open(fileName, 'w') as yamlfile:
                yaml.dump(config_dict, yamlfile, default_flow_style=False)
                print('No config.yml file was not found. Succesfully created empty config.yml file')
            with open(fileName, 'r') as yamlfile:
                self.cfg = yaml.load(yamlfile, Loader=yaml.BaseLoader)
    @property
    def bot_token(self):
        return self.cfg['config']['connection']['bot_token']

if __name__ == '__main__':
    config = Config('config.yml')
    print(str(config.bot_token))
