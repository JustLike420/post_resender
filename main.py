import json
import time

from apscheduler.schedulers.background import BackgroundScheduler
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from vk_parser import VkParser
from sender import send_post
import config


def main():
    bot = Bot(token=config.tg_token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())
    with open("publics.json", "r") as f:
        groups = json.load(f)
    for group in groups:

        vk = VkParser(vk_group=group["vk_id"])
        posts = vk.get_posts()
        new_last_id = posts[0]["id"]
        if new_last_id > group["last_post_id"]:
            post = posts[0]
            vk.parse_post(post)
            executor.start(dp, send_post(bot, group['telegram_login'], vk.text, vk.photos, vk.videos))
            group["last_post_id"] = new_last_id
            with open('publics.json', 'w') as outfile:
                json.dump(groups, outfile)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(60*5)
