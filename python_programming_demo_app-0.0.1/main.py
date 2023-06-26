import os
import sys

import flask

import roboter.controller.conversation

import setting

def main():
    roboter.controller.conversation.talk_about_restaurant()

if __name__ == '__main__':
    main()