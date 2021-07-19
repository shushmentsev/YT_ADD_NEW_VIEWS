# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sys import platform
from os import system

#Путь к драйверу:
from conf import PTH_CHROMIUM_DRV_LIN, PTH_CHROME_DRV_WIN


# Настройка переменной окружения:
from sys import path
path.append(str(PTH_CHROMIUM_DRV_LIN))
path.append(str(PTH_CHROME_DRV_WIN))


def set_opt():

    # Опции для драйвера:
    options = Options()

    # Отключение загрузки изображений:
    #prefs = {"profile.managed_default_content_settings.images": 2}
    #options.add_experimental_option("prefs", prefs)

    # Размер окна:
    # options.add_argument("--start-maximized")
    options.add_argument("--window-size=1240x720")

    # Экспериментальная опция для подхвата уже запущенного браузера:
    options.add_experimental_option('debuggerAddress', 'localhost:9014')

    # Безголовый режим:
    #options.add_argument("headless")

    return options


def set_proxy(options, host, port, user, pwrd):

    import os
    import zipfile

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
              },
              bypassList: ["localhost"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (host, port, user, pwrd)

    pluginfile = 'proxy_auth_plugin.zip'

    with zipfile.ZipFile(pluginfile, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    
    options.add_extension(pluginfile)

    return options


def get_drv():

    # Настройка драйвера:
    options = set_opt()
    # options = set_proxy(options, "194.67.221.142", "9749", "f6a7ks", "FyWHou")    

    driver = None

    # Конфигурация в зависимости от платформы:
    if platform == "linux":
        driver = webdriver.Chrome(
            options=options,
            executable_path=str(PTH_CHROMIUM_DRV_LIN)
        )
    elif platform == "win32" or platform == "cygwin":
        driver = webdriver.Chrome(
            options=options,
            executable_path=str(PTH_CHROME_DRV_WIN)
        )
    else:
        exit(1)

    return driver    


if __name__ == "__main__":

    # Запуск браузера:
    system('start chrome.exe -remote-debugging-port=9014 --user-data-dir="D:\Selenium\Test"')

    # Получение драйвера:
    drv = get_drv()    

    # Переход на сайт:
    drv.get("https://myip.ru/")
