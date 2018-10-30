#!/usr/bin/env python3
# coding=utf-8

import json

PROXY_JSON = "proxy.list"
PROXY_LIST = "proxylist.txt"


def log(msg):
    # print(msg)
    with open(PROXY_LIST, "a+") as f:
        f.write(msg + "\r\n")


def main():
    with open(PROXY_JSON, "r") as f:
        for i in f:
            s = json.loads(i)
            log("%s://%s:%s" % (s["type"], s["host"], s["port"]))


if __name__ == '__main__':
    main()
