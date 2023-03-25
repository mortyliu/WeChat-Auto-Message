# -*- coding: utf-8 -*-
# created by Morty Liu on 2022/7/8

import win32api
import win32con
import time

pause_time = 0.6

def ctrl_f():
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(70, 0, 0, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(70, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(pause_time)


def ctrl_v():
    win32api.keybd_event(17, 0, 0, 0)
    win32api.keybd_event(86, 0, 0, 0)
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(pause_time)


def enter():
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(pause_time)

