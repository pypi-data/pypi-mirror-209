from typing import Any
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from material_zui.fake import random_sleep
from material_zui.selenium.common import safe_find_element


class Zui_Selenium_Chrome:
    def __init__(self) -> None:
        self.is_mac = False
        if not any(os_name in platform.platform() for os_name in ["Windows", "Linux"]):
            self.is_mac = True

    def connect(self) -> None:
        self.driver = webdriver.Chrome()

    def connect_debug(self, port: int = 9000) -> None:
        '''
        @port: port number, default `9000`
        - Use for case need authorization, you just need to start `chrome beta` -> login account -> close browswer then
            - start `chrome` on debug mode -> call this method to connect to browser opened
        1. Install `chrome beta` for better automation: https://www.google.com/chrome/beta
        2. Start `chrome` by command: `google-chrome-beta --remote-debugging-port={port}`
                - `port` must the same with input parameter of this method
        '''
        self.options = Options()
        self.options.add_experimental_option(
            "debuggerAddress", f"localhost:{port}")
        self.driver = webdriver.Chrome(options=self.options)

    def delay(self, sec: float = 0) -> None:
        random_sleep(1, 5, sec)

    def find_element(
            self, by: str = By.ID,
            value: str | None = None,
            parent: Any = None):
        '''
        This is safe find element method
        @return `None` incase not found
        '''
        return safe_find_element(parent if parent else self.driver, by, value)
