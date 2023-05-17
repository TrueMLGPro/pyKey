import subprocess
import time
from pyKey.key_dict import linux_keys as key_dict

def press_key(key=None):
    """
    Presses a key and holds it until explicitly called the `release_key()` function.

    Parameters:
    - key: [str] A key to press
    """
    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exist! Please check for any spelling errors.".format(key)

    subprocess.call(['xdotool', 'keydown', key_dict[key]])

def release_key(key=None):
    """
    Releases a key that was pressed using `press_key()`.

    NEVER forget to use this after using `press_key()` function.

    Parameters:
    - key: [str] A key to release
    """
    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exist! Please check for any spelling errors.".format(key)

    subprocess.call(['xdotool', 'keyup', key_dict[key]])

def press(key=None, sec=0):
    """
    Presses a key and releases it.

    If `sec` argument is given, this function will press and hold a key for that many seconds.

    Parameters:
    - key: [str] A key to press
    - sec: [int, float] An interval to hold a key down for
    """
    assert key is not None, "No keys are given (key=None). Please check your code"
    assert key in key_dict, "The key({}) you're trying to press does not exist! Please check for any spelling errors.".format(key)
    assert sec >= 0, 'Seconds cannot be negative'

    if sec == 0:
        subprocess.call(['xdotool', 'key', key_dict[key]])
    else:
        subprocess.call(['xdotool', 'keydown', key_dict[key]])
        time.sleep(sec)
        subprocess.call(['xdotool', 'keyup', key_dict[key]])

def send_sequence(seq=None, interval=None):
    """
    Send a sequence of key presses.

    If `seq` is a string, it'll be simulated.

    If `seq` is a list of keys, it'll be simulated.

    If `seq` is a dict, it will be interpreted as a key value pair, whose key is the key that is going to be pressed and the value as how long to hold the key for (in seconds).

    You can also set an `interval` inbetween key presses (optional, defaults to None).

    Parameters:
    - seq: [str, list, dict] A sequence of keys to press
    - interval: [int, float] A time interval between key presses (in seconds, the argument may be a floating point number for subsecond precision)
    """
    assert seq is not None, "No sequence is given (seq=None). Please check your code"
    assert interval >= 0, "Interval cannot be negative"

    if isinstance(seq, str):
        subprocess.call(['xdotool', 'type', '{}'.format(seq), '--delay', ''.format(interval*1000)])

    elif isinstance(seq, list):
        for key in seq:
            if interval is not None:
                time.sleep(interval)
            press(key)

    elif isinstance(seq, dict):
        for key, sec in seq.items():
            if interval is not None:
                time.sleep(interval)
            press(key, sec)

def show_keys():
    """
    Show the list of available keys and their scancodes.
    """
    print('These are the available keys and their corresponding xdotool names')
    print('{:20}'.format('Key'), 'Xdotool Name')
    print('')
    for key, name in key_dict.items():
        print('{:20}'.format(key), name)
