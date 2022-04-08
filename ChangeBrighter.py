import os

# Monitor driver is the file in /sys/class/backlight that can affect monitor
def Change_Bright_HW(monitor_driver, brightness_value):
    b_file = open(f'/sys/class/backlight/{monitor_driver}/brightness', 'w')
    b_file.write(f'{brightness_value}')
    b_file.close()

# Use xrandr to change gamma (I mean brightness)
def Change_Bright_Gamma(brigntness_level, display):
    os.system(f'xrandr --output {display} --brightness {brigntness_level}')

# Use xrandr to change r,g,b color
def Change_RGB_Color(r, g, b, display):
    os.system(f'xrandr --output {display} --gamma {r}:{g}:{b}')

# Special layout
def Special_layout(brigntness_level, r, g, b, display):
    os.system(f'xrandr --output {display} --gamma {r}:{g}:{b} --brightness {brigntness_level}')
