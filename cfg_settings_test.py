#!/usr/bin/env python3

import os

from cltests import TestSet, T, IsSuccessful
from cfg.settings import FindConfig, ParseConfig

def getKeys(obj):
    keys = []
    for key in obj:
        keys.append(key)
    return keys
    

def testFindConfig():
    # write out test conf file.
    home = os.getenv("HOME")
    os.mkdir
    with open('testdata/settings.ini', 'w') as f:
        f.write('''
[app]
localhost = Lisbon
database = Cyucos
user = Maz
password = Ocean
''')
    expect = 'testdata/settings.ini'
    got = FindConfig(names = ['settings.ini'], search_path = ['testdata', '.', home])
    t = T()
    t.Expected(expect, got, "should find testdata location")
    return t.Results()

def testParse():
    t = T()
    my_cnf = FindConfig(names = ['settings.ini'], search_path = ['testdata'])
    conf = ParseConfig(my_cnf, section = 'app')
    expect = {
        "localhost": "Lisbon", "database": "Cyucos",
        "user": "Maz", "password": "Ocean"
        }
    t.Expected(False, conf == None, "conf should not be None")
    t.ExpectedList(getKeys(expect), getKeys(conf), "checking settings.ini keys");
    for key in conf:
        t.Expected(expect[key], conf[key], "checking values settings.ini")

    conf = ParseConfig(my_cnf, section = 'app', Ada = "Lovelace", Blaise = "Pascal", Niklaus = "Wirth")
    pairs = { "Ada": "Lovelace", "Blaise": "Pascal", "Niklaus": "Wirth"}
    for key in pairs:
        t.Expected(True, key in conf, "checking for {key} in {conf}")
        if key in conf:
            t.Expected(pairs[key], conf[key], "checking values for {key}")
    return t.Results()


if __name__ == '__main__':
    ts = TestSet('cfg.settings tests')
    ts.add(testFindConfig)
    ts.add(testParse)
    IsSuccessful(ts.run())
