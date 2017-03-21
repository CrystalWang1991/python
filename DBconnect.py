# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 15:33:29 2017

@author: 98002
"""

import cx_Oracle as ora
import numpy

dbcenter_dsn = ora.makedsn(host= "172.16.8.20", port="1521", sid= "dbcenter")
dbcenter_conn_Ora = ora.connect('READER', 'reader', dbcenter_dsn)