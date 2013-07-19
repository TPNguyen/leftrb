#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest
import random

from leftrb.test.test_bst import TestBST as Base
from leftrb.llrb import LeftRB


Tree = LeftRB


def fill_tree(items):
    tree = Tree()
    print len(tree)
    map(tree.insert, items)
    print len(tree)

    return tree


class TestLeftRB(Base):

    items = [5,1,3]

    def test_min(self):
        t = fill_tree(self.items)
        assert t.min() == min(self.items)

    def test_max(self):
        t = fill_tree(self.items)
        assert t.max() == max(self.items)

    def test_delete(self):
        t = fill_tree(random.sample(xrange(100), 90))

        key = random.randint(0, 999)
        value = str(key)
        t.insert(key, value)
        assert value == t.search(key)
        t.delete(key)
        assert None == t.search(key)
