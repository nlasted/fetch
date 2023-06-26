#!/bin/python3

import platform
import os

data = platform.freedesktop_os_release()

name = data['NAME']
version = data['VERSION']

kernel = platform.system()
kernel_version = platform.release()
shell = os.environ['SHELL']
username = os.environ['USER']

architecture = platform.machine()
print(" ┏━━")
print(f" ┃  {kernel} {kernel_version}")
print(f" ┃  {name} {version} {architecture}")
print(f" ┃  {shell}")
print(f" ┃  {username}")
print(" ┗━━")