#!/usr/bin/env python

"""Tests for `addana` package."""


import sys

sys.path.append('..')
import  addanase

def test_addana():
    print(addanase.transform(["吉林：吉林"]))
test_addana()
