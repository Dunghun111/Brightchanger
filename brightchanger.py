#!/usr/bin/env python3
from platform import python_version
import os
import sys

if os.getuid() == 0:
    if '3.' in python_version():
        bright_in_usr = 0
        print('This programme only support linux, MacOS.')
        dir_check = os.listdir('/usr/bin/')
        for i in dir_check:
            brightchanger_test = i
            if brightchanger_test == 'brightchanger':
                bright_in_usr = 1
            else:
                pass

        if bright_in_usr != 1:
            ask = input('Wanna run this script with just it name (linux only)?: ')
            if ask == 'yes':
                if sys.platform.startswith('linux'):
                    cmd = os.system('cp brightchanger.py /usr/bin/brightchanger')
                    cmd_2 = os.system('chmod +x /usr/bin/brightchanger')
                else:
                    print('It\'s not linux :(.')
        else:
            pass

        if sys.platform.startswith('darwin'):
            print('W: You\'re starting with MacOS, this programme may not fully support.')
            print('''CN: Make sure you have install \'brightness\' package from Homebrew
If not, then install here: \'https://brew.sh/\'.
Then run: \'brew install brightness\'.''')  # Critical Note
            brightness_level = int(input('Set brightness to (1 - 100): '))
            brightness_level = float(brightness_level / 100)
            cmd = os.system('brightness ' + str(brightness_level))

        elif sys.platform.startswith('linux'):
            brightness_level = input('Set brightness level to: ')
            check_backlight = os.listdir('/sys/class/backlight/')
            for driver in check_backlight:
                brightness_driver = driver
            cmd = os.system('echo ' + brightness_level + ' > /sys/class/backlight/' + brightness_driver + '/brightness')
        else:
            print('Not a supported os.')
    elif '2.' in python_version():
        print('This programme is not support python2.')
else:
    print('Please run this programme in root!')
