cfg
===

A small package for access various types of configuration files, 
e.g. MySQL's my.cnf or other "ini" style configration. Wraps 
Python 3's standard configparser. 

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg?style=flat-square)](https://choosealicense.com/licenses/bsd-3-clause)
[![Latest release](https://img.shields.io/github/v/release/caltechlibrary/template.svg?style=flat-square&color=b44e88)](https://github.com/caltechlibrary/template/releases)


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Known issues and limitations](#known-issues-and-limitations)
* [Getting help](#getting-help)
* [Contributing](#contributing)
* [License](#license)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#authors-and-acknowledgments)


Introduction
------------

This is a small simple configuration file utlity that wrap's Python 3's
own configparser. Support initialization files are assumed to be in
"ini" format and are associated with a support system like MySQL. Each
support configuration file provides two functions, FindConfig() and
ParseConfig(). FindConfig checks a series of path location for configuration
and returns the first one found or None if no config file is discovered.
ParseConfig takes the path from FindConfig and any additional optional
parameters associated with the  resource (e.g. a database name in MySQL)
and returns a dictionary of key/value parse.


Installation
------------

cfg is installable with Python setup.py. 

```
git clone git@github.com:caltechlibrary/cfg
cd cfg
python3 setup.py install
```

Usage
-----

Once installed this Python 3 package can be included using 
the standard `from cfg import ...` pattern. Here's an example
of installing it to return a configuration needed for a MySQL
connection.

```
import sys
from cfg import FindConfig, ParseConfig

my_cnf = FindConfig()
if my_cnf == None:
    print('Can't find my.cnf')
    sys.exit(1)
conf = ParseConfig(my_cnf, database = 'mydb')
if conf == None:
    print(f'''Can't parse {my_cnf}''')
    sys.exit(1)


```

Known issues and limitations
----------------------------

Currently supports searching in the current directory for a
"my.cnf" file or the user's home directory for ".my.cnf". Assumes
a Unix style file system (using path separate and dot prefix).
Does not current support looking for other types of configuration files.


Getting help
------------

File an issues on GitHub, see https://github.com/caltechlibrary/cfg/issues

Contributing
------------

This section is optional; if your repository is for a project that accepts open-source contributions, then this section is where you can mention how people can offer contributions, and point them to your guidelines for contributing.  (If you delete this section, don't forget to remove the corresponding entry in the [Table of Contents](#table-of-contents) too.)


License
-------

Software produced by the Caltech Library is Copyright © 2021 California Institute of Technology.  This software is freely distributed under a BSD/MIT type license.  Please see the [LICENSE](LICENSE) file for more information.


Authors and history
---------------------------

In this section, list the authors and contributors to your software project.  Adding additional notes here about the history of the project can make it more interesting and compelling.  This is also a place where you can acknowledge other contributions to the work and the use of other people's software or tools.


Acknowledgments
---------------

This work was funded by the California Institute of Technology Library.

(If this work was also supported by other organizations, acknowledge them here.  In addition, if your work relies on software libraries, or was inspired by looking at other work, it is appropriate to acknowledge this intellectual debt too.)

<div align="center">
  <br>
  <a href="https://www.caltech.edu">
    <img width="100" height="100" src="https://raw.githubusercontent.com/caltechlibrary/template/main/.graphics/caltech-round.png">
  </a>
</div>
