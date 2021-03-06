#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
Configuration file.
"""

import logging
import argparse

# Set cli arguments
OPTIONS = argparse.ArgumentParser(prog='run.py',
                                  description='A Telegram Bot who answers to all of your questions')
OPTIONS.add_argument('--TELEGRAM_TOKEN', help='Insert Telegram Token', required=True)
OPTIONS.add_argument('--ADMIN_CHAT_ID', help='Insert Telegram ChatID', default='')
OPTIONS.add_argument('--DIALOGFLOW_TOKEN', help='Specify Dialogflow Token', required=True)
OPTIONS.add_argument('--WIT_TOKEN', help='Specify Wit Token', default='')
OPTIONS.add_argument('--log', help='Set logging value', default='DEBUG')
ARGUMENTS = OPTIONS.parse_args()

# Logging configs
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s.',
                    level=ARGUMENTS.log)

# Telegram configs
TELEGRAM_TOKEN = ARGUMENTS.TELEGRAM_TOKEN
ADMIN_CHAT_ID = ARGUMENTS.ADMIN_CHAT_ID

# Dialogflow configs
DIALOGFLOW_TOKEN = ARGUMENTS.DIALOGFLOW_TOKEN

# WIT configs
WIT_TOKEN = ARGUMENTS.WIT_TOKEN
