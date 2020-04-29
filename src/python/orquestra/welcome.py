"""
This module saves a welcome message.
"""

import json
import numpy as np

def welcome():
    a = np.array(range(1000))
    b = np.array(range(1000))
    message = "Welcome to Orquestra!"

    message_dict = {}
    message_dict["message"] = calc_vals(a,b)
    message_dict["schema"] = "message"

    with open("welcome.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact

def calc_vals(a, b):
    return np.sin(a)*np.cos(b)