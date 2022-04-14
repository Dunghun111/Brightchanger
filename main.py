import os
import random
import sys
import time
import ChangeBrighter


# ========================================================================================================================================================= #
random_tips = ['''Tip: look for something like eDP or DVI-0 in "maximum <resolution>, <your display> connected to" after run command "xrandr --verbose"!''',
'''Tip: search your display backlight file that have "brightness" file in it to change Hardware backlight!''',
'''Tip: Use gamma correctly or else your display will like it get drunk!''',
'''Tip: Set software brightness from 0 to 1 or else your display will not output correctly!''',
'''Tip: Don't set Hardware brightness to 0 because it will bright as the display after it is turned off!''']
random_typo_warn = ['Hey! You make a typo!', 'Check what you type, there is a typo!', 'Typo Detected!']

end_loop1 = False
end_loop2 = False
r_light = '0'
b_light = '0'
g_light = '0'
curr_display = 'eDP'
monitor_file = 'radeon_bl0'
gamma = '1'
brightness = '1'

try:
    while not end_loop1:
        new_to_software = input('Are you new to this software?: ')

        if new_to_software.lower() == 'no':
            print('pro')
            break

        if new_to_software.lower() == 'yes':
            man_ask = input('Want me to run "man xrandr": ')

            if man_ask.lower() == 'yes':
                print('Running "man xrandr"...')
                time.sleep(1)
                os.system('man xrandr')
                print('''Go to /sys/class/backlight/ and check and any folders that contain "brightness" file in it because this software need "brightness" file to change Hardware backlight brightness.''')
                time.sleep(1)
                print('Now, good luck and have fun ;)')
                time.sleep(1)
                end_loop1 = True

            elif man_ask.lower() == 'no':
                print('''Go to /sys/class/backlight/ and check and any directories that contain "brightness" file in it because this software need "brightness" file to change Hardware backlight brightness.''')
                time.sleep(1)
                print('Ok! Good luck and have fun ;)')
                time.sleep(1)
                end_loop1 = True

            else:
                print(random.choice(random_typo_warn))

        else:
            print(random.choice(random_typo_warn))

    print('''             
    //   ) )                                       //   ) )                                                        
   //___/ /   __     ( )  ___     / __    __  ___ //        / __      ___       __      ___      ___      __    
  / __  (   //  ) ) / / //   ) ) //   ) )  / /   //        //   ) ) //   ) ) //   ) ) //   ) ) //___) ) //  ) )   
 //    ) ) //      / / ((___/ / //   / /  / /   //        //   / / //   / / //   / / ((___/ / //       //         
//____/ / //      / /   //__   //   / /  / /   ((____/ / //   / / ((___( ( //   / /   //__   ((____   //             

''')
    print(random.choice(random_tips))
    print(f'''Current:
    Monitor file: {monitor_file}
    Brightness: {brightness}
    Display: {curr_display}
    Gamma: {gamma} 
    Red: {r_light}
    Green: {g_light}
    Blue: {b_light}''')
    print('Type \'help\' for more info!')
    choice = False
    command_list = ['help', 'hw', 'gamma', 'rgb', 'import', 'export', 'execute', 'current', 'quit']

    while not choice:
        usr_input = input('Input: ')

        if usr_input.lower() not in command_list:
            print('WRONG COMMAND! Type \'help\' for help')

        if usr_input.lower() in command_list:

            if usr_input.lower() == 'help':
                print('''
[Option]   [Explain]
HW       : Change brightness in hardware level (change display brightness).
GAMMA    : Change gamma. (I mean brightness)
RGB      : Change RGB light (like the light change when use "Night mode" in Windows) when output.
IMPORT   : Import a save file.
EXPORT   : Export settings to a save file.
EXECUTE  : Execute current setup
CURRENT  : Display current status
QUIT     : Exit this software
''')

            if usr_input.lower() == 'hw':
                monitor_file = input('Monitor driver folder (in /sys/class/backlight): ')
                brightness = input('Brightness level: ')
                ChangeBrighter.Change_Bright_HW(brightness_value=brightness, monitor_driver=monitor_file)

            if usr_input.lower() == 'gamma':
                curr_display = input('Current Display: ')
                gamma = input('Brightness level: ')
                ChangeBrighter.Change_Bright_Gamma(display=curr_display, brigntness_level=gamma)

            if usr_input.lower() == 'rgb':
                r_light = input("Red value: ")
                g_light = input("Green value: ")
                b_light = input('Blue value: ')
                curr_display = input("Current display: ")
                ChangeBrighter.Change_RGB_Color(display=curr_display, r=r_light, g=g_light, b=b_light)

            if usr_input.lower() == 'import':
                location = input('File location = ')

                if location[0] == '~':
                    print('Please use /home/<username> instead!')
                    continue

                try:
                    get_saved_file = open(f'{location}', 'r')

                except FileNotFoundError as File_not_found:
                    print('Fatal Error: File not found')
                    continue

                except IsADirectoryError as a_directoy:
                    print('Fatal Error: Is a directory')
                    continue

                for i in get_saved_file:
                    e = i.split()
                    try:
                        e.pop(e.index('='))
                    except ValueError as no_equal:
                        pass

                    try:
                        if e[0] == 'rgb':
                            r_light = e[1]
                            g_light = e[2]
                            b_light = e[3]
                    except IndexError as cant_find:
                        pass

                    try:
                        if e[0] == 'gamma':
                            gamma = e[1]
                    except IndexError as cant_find:
                        pass

                    try:
                        if e[0] == 'brighness':
                            brightness = e[1]
                    except IndexError as cant_find:
                        pass

                    try:
                        if e[0] == 'display':
                            curr_display = e[1]
                    except IndexError as cant_find:
                        pass

                    try:
                        if e[0] == 'monitor':
                            monitor_file = e[1]
                    except IndexError as cant_find:
                        pass

            if usr_input.lower() == 'export':
                saved_name = input('File name = ')
                make_saved_file = open(f'{saved_name}', 'w')
                make_saved_file.write(f'''rgb = {r_light} {g_light} {b_light}
brightness = {brightness}
gamma = {gamma}
display = {curr_display}
monitor = {monitor_file}''')
                make_saved_file.close()

            if usr_input.lower() == 'execute':
                try:
                    ChangeBrighter.Special_layout(display=curr_display, r= r_light, g= g_light, b= b_light, brigntness_level=gamma)
                    ChangeBrighter.Change_Bright_HW(monitor_driver=monitor_file, brightness_value=brightness)
                except PermissionError as some_error:
                    pass
                    
            if usr_input.lower() == 'current':
                print(f'''Current:

    Monitor file: {monitor_file}
    Brightness: {brightness}
    Display: {curr_display}
    Gamma: {gamma} 
    Red: {r_light}
    Green: {g_light}
    Blue: {b_light}
''')


            if usr_input.lower() == 'quit':
                print("Goodbye~!")
                sys.exit()

except KeyboardInterrupt as CtrlC:
    print('\nGoodbye~!')
# ========================================================================================================================================================= #
