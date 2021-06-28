import os
from configparser import ConfigParser

_home = os.getenv('HOME')

def FindConfig(names = ['my.cnf', '.my.cnf'], search_path = ['.', _home]): 
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

def ParseConfig(fname, **kwargs):
    '''ParseConfig takes a configuration filename and any
       key/value pairs you with to use as defaults. It parses
       the config file and overwrites the defaults'''
    client = None
    config = ConfigParser()
    if (config != None) and (fname != None) :
        config.read(fname)
        # Set up our handly defaults
        client = {}
        for key in kwargs:
            client[key] = kwargs[key]
        if 'client' in config:
            for key in config['client']:
                if key == 'port':
                    client[key] = int(config['client'][key])
                else:
                    client[key] = config['client'][key]
        else:
            return None
    return client 

