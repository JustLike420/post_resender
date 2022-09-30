import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

vk_token = config["settings"]["vk_token"]
tg_token = config["settings"]["tg_token"]
