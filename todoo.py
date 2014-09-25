#!/usr/bin/env python

"""
Simple TODO tracker.

Words starting with # are tags.
Words starting with @ indicates places

"""

"""
Things to do:
* Global sync
 * unique identifier (uuid) to every todo item
* modify time to todos
* reorder support
* proper priority support
"""

import argparse
import os
import logging
from datetime import datetime

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

TODODIR=os.path.abspath(os.path.expanduser("~/.todoo"))
TODOFILE=os.path.join(TODODIR, 'todoo.txt')

COLORS=True

if not os.path.exists(TODODIR):
    os.mkdir(TODODIR)

class Colors:
    WHITE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED  = '\033[91m'
    END = '\033[0m'

class Item(object):
    def __init__(self, created, content, number, modified=None, priority=0):
        self.created = created
        self.content = content
        self.number = number

        self.modified = modified
        self.priority = priority

    def __str__(self):
        content = []
        replaces = {'#': Colors.BLUE, '@': Colors.GREEN}
        if COLORS:
            for i in self.content.split():
                for key, value in replaces.items():
                    if i.startswith(key) and len(i) > 1:
                        i = "%s%s%s" % (value, i[1:], Colors.END)
                content.append(i)
            content = ' '.join(content)
        else:
            content = self.content
        return "%d) %s [%s]" % (self.number, content, self.created.strftime("%Y.%m.%d %H:%M"))

class FileDB(object):
    def __init__(self):
        self._dbfile = TODOFILE
        self._changed = False
        self._opened = False
        self._content = []
        self._items = []

    def open(self):
        if self._opened:
            return
        self._opened = True
        if os.path.isfile(self._dbfile):
            with open(self._dbfile, 'r') as f:
                self._content = f.readlines()

    def add(self, item):
        self._content.append("%s %d %s\n" % (item.created.strftime("%Y-%m-%dT%H:%M:%S"), item.priority, item.content))
        item.number = len(self._content)
        self._changed = True

    def all(self):
        if not self._items:
            _id = 1
            for item in self._content:
                try:
                    (created, priority, content) = item.split(None, 2)
                    itime = datetime.strptime(created, "%Y-%m-%dT%H:%M:%S")
                    priority = int(priority)
                    content = content.strip()
                except Exception as e:
                    print(e)
                    print("Invalid line on database, skipping")
                    continue
                self._items.append(Item(itime, content, _id, priority=priority))
                _id += 1
        return [x for x in self._items]

    def remove(self, item_id):
        if item_id < 0 or len(self._content) > item_id:
            print("Invalid id")
        else:
            self._changed = True
            self._content = self._content[:item_id-1] + self._content[item_id:]
            self._items = self._items[:item_id-1] + self._items[item_id:]

    def close(self):
        if self._changed:
            with open(self._dbfile, 'w') as f:
                for line in self._content:
                    f.write(line)

class Todoo(object):
    def __init__(self):
        self.db = FileDB()
        self.db.open()

    def list(self):
        _id = 1
        for item in self.db.all():
            print("%s" % item)
            _id += 1

    def add(self, item):
        if not item.strip():
            print("Not adding empty todo")
            return
        i = Item(datetime.now(), item, number=None)
        self.db.add(i)

    def remove(self, item_id):
        self.db.remove(item_id)
        return
        if item_id < 0 or len(self.content) > item_id:
            print("Invalid id")
        else:
            self.content = self.content[:item_id-1] + self.content[item_id:]

    def search(self, pattern):
        for item in self.db.all():
            if pattern in item.content:
                print("%s" % item)

    def write(self):
        self.db.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ToDoo')
    parser.add_argument('-n', '--no-color', help="No colors", action="store_true", default=False)
    subparsers = parser.add_subparsers(dest="action")
    
    ls_parser = subparsers.add_parser('ls', help="List items")
    ls_parser = subparsers.add_parser('l', help="List items, alias for ls")

    add_parser = subparsers.add_parser('add', help="Add item")
    add_parser.add_argument('item', metavar='item', type=str, nargs='+', help="todo item")

    a_parser = subparsers.add_parser('a', help="Add item, alias for add")
    a_parser.add_argument('item', metavar='item', type=str, nargs='+', help="todo item")

    done_parser = subparsers.add_parser('do',help="Mark item done")
    done_parser.add_argument('id', metavar='ID', type=int, nargs=1, help="Item id")

    filter_parser = subparsers.add_parser('filter', help="filter")
    filter_parser.add_argument('pattern', metavar='PATTERN', type=str, nargs='+', help="Search pattern")

    filter_parser = subparsers.add_parser('f', help="filter, alias for filter")
    filter_parser.add_argument('pattern', metavar='PATTERN', type=str, nargs='+', help="Search pattern")


    args = parser.parse_args()


    t = Todoo()
    if args.no_color:
        COLORS=False
    if args.action in ['ls', 'l']:
        t.list()
    elif args.action in ['do', 'done']:
        t.remove(args.id[0])
    elif args.action in ['add', 'a']:
        t.add(' '.join(args.item))
    elif args.action in ['filter']:
        t.search(' '.join(args.pattern))
    else:
        print("FOO")
    t.write()
