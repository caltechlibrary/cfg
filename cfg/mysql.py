import os
from configparser import ConfigParser

def FindConfig(name = 'my.cnf'): 
    # check the current directory first, then check the home directory
    home = os.getenv('HOME')
    my_cnf = None
    if os.path.exists(name):
        my_cnf = name
    elif os.path.exists(os.path.join(home, '.my.cnf')):
        my_cnf = os.path.join(home,'.my.cnf')
    return my_cnf

def ParseConfig(name, database = None, host = 'localhost', port = '3306', socket = '/tmp/mysql.sock'):
    client = None
    config = ConfigParser()
    if config != None:
        config.read(name)
        # Set our handly defaults
        client = { 
            'host': host,
            'port': port,
            'socket': socket,
            'database': database,
            'user': None,
            'password': None
        } 
        if 'client' in config:
            for key in config['client']:
                client[key] = config['client'][key]
        else:
            return None
    return client 
