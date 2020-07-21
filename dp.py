#!/usr/bin/python3

import configparser as cfg
import requests


def sensitive_info():
    conf = cfg.ConfigParser()
    conf.read("sensitive.ini")

    print(conf["Secret Key"]["secret"])

def main():
    sensitive_info()

if __name__ == "__main__":
    main()