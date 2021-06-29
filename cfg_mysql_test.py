#!/usr/bin/env python3

import os

from cltests import TestSet, T, IsSuccessful
from cfg.mysql import FindConfig, ParseConfig

def getKeys(obj):
    keys = []
    for key in obj:
        keys.append(key)
    return keys
    

def testFindConfig():
    # write out test conf file.
    home = os.getenv("HOME")
    os.mkdir
    with open('testdata/my1.cnf', 'w') as f:
        f.write('''
[client]
localhost = Lisbon
database = Cyucos
user = Maz
password = Ocean
''')
    expect = 'testdata/my1.cnf'
    got = FindConfig(names = ['my1.cnf'], search_path = ['testdata', '.', home])
    t = T()
    t.Expected(expect, got, "should find testdata location")
    return t.Results()

def testParse():
    t = T()
    my_cnf = FindConfig(names = ['my1.cnf'], search_path = ['testdata'])
    conf = ParseConfig(my_cnf)
    t.Expected(False, conf == None, f"{my_cnf}, conf should not be None")
    expect = {
        "localhost": "Lisbon", "database": "Cyucos",
        "user": "Maz", "password": "Ocean"
        }
    t.ExpectedList(getKeys(expect), getKeys(conf), "checking my1.cnf keys");
    for key in conf:
        t.Expected(expect[key], conf[key], "checking values my1.cnf")

    conf = ParseConfig(my_cnf, Ada = "Lovelace", Blaise = "Pascal", Niklaus = "Wirth")
    pairs = { "Ada": "Lovelace", "Blaise": "Pascal", "Niklaus": "Wirth"}
    for key in pairs:
        t.Expected(True, key in conf, "checking for {key} in {conf}")
        if key in conf:
            t.Expected(pairs[key], conf[key], "checking values for {key}")
    return t.Results()


if __name__ == '__main__':
    ts = TestSet('cfg.mysql tests')
    ts.add(testFindConfig)
    ts.add(testParse)
    IsSuccessful(ts.run())
