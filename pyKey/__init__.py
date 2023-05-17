import sys

if sys.platform == 'linux':
    from pyKey.linux import press_key, release_key, press, show_keys, send_sequence
elif sys.platform == 'win32':
    from pyKey.windows import press_key, release_key, press, show_keys, send_sequence
