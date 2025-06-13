import base64
from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

base64_string = "aHR0cHM6Ly9raWNrLmNvbS9icnV0YWxsZXM="

# Decoding
decoded_bytes = base64.b64decode(base64_string)
decoded_string = decoded_bytes.decode("utf-8")
with SB(uc=True, test=True) as sb:
    sb.uc_open_with_reconnect(decoded_string, 2)
    sb.uc_gui_click_captcha()
    sb.sleep(1)
    sb.uc_gui_handle_captcha()
    sb.sleep(1)
    if sb.is_element_present('button:contains("Accept")'):
        sb.uc_click('button:contains("Accept")', reconnect_time=4)
    if sb.is_element_visible('#injected-channel-player'):
        dd2 = sb.get_new_driver(undetectable=True)
        dd2.uc_open_with_reconnect(url, 2)
        dd2.uc_gui_click_captcha()
        sb.sleep(1)
        dd2.uc_gui_handle_captcha()
        sb.sleep(10)
        if dd2.is_element_present('button:contains("Accept")'):
            dd2.uc_click('button:contains("Accept")', reconnect_time=4)
        while sb.is_element_visible('#injected-channel-player'):
            sb.sleep(20)
        sb.quit_extra_driver()
sb.sleep(1)
