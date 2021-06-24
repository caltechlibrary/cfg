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

def ParseConfig(name, db_name = None):
    config = ConfigParser()
    config.read(name)
    # Handly defaults
    client = {
            'port': '3306', 
            'host': 'localhost', 
            'socket': '/tmp/mysql.sock',
            'database': db_name,
            'user': None,
            'password': None
            }
    if 'client' in config:
        for key in config['client']:
            client[key] = config['client'][key]
    else:
        print(f'ERROR: did not find client section in {my_cnf}')
        return None
    return client 
