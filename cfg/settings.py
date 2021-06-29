import os
from configparser import ConfigParser

_home = os.getenv('HOME')
ini_name = 'settings.ini'

def FindConfig(names = [ini_name], search_path = ['.']): 
    '''FindConfig checks each of the expected names in the search path
       returning None if none are found, otherwise the first one found.
       The defaults roughly mimic the MySQL search behavoir.
    '''
    my_cnf = None
    for name in names:
        for p in search_path:
            if os.path.exists(os.path.join(p, name)):
                my_cnf = os.path.join(p, name)
                break
        if my_cnf != None:
            break
    return my_cnf

def ParseConfig(fname, section = "defaults", **kwargs):
    '''ParseConfig takes a configuration filename and any
       key/value pairs you with to use as defaults. It parses
       the config file and overwrites the defaults'''
    settings = None
    config = ConfigParser()
    if (config != None) and (fname != None) :
        config.read(fname)
        # Set up our handly defaults
        settings = {}
        for key in kwargs:
            settings[key] = kwargs[key]
        if section in config:
            for key in config[section]:
                if key == 'port':
                    settings[key] = int(config[section][key])
                else:
                    settings[key] = config[section][key]
        else:
            return None
    return settings 

