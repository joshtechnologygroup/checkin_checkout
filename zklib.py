#!/usr/bin/env python

import sys
from zklib import zklib

import time
from zklib import zkconst




zk = zklib.ZKLib("192.168.1.10", 4370)
ret = zk.connect()
print "connection:", ret