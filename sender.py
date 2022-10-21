import glob
import os
from aiogram import types
import youtube_dl


async def send_post(bot, tg_channel, text, photos, videos):
    if len(photos) == 0 and len(videos) == 0:
        await bot.send_message(tg_channel, text, parse_mode=types.ParseMode.HTML)
    elif len(photos) == 1:
        await bot.send_photo(tg_channel, photos[0], caption=text, parse_mode=types.ParseMode.HTML)
    elif 1 < len(photos) <= 10:
        media = types.MediaGroup()

        for photo in photos:
            media.attach_photo(types.InputMediaPhoto(photo))
            media.media[0].caption = text
            media.media[0].parse_mode = types.ParseMode.HTML
        await bot.send_media_group(tg_channel, media)
    elif len(videos) == 1:
        text += f'\n\n <a href="{videos[0]}">👉 Смотреть видео</a>'
        await bot.send_message(tg_channel, text, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
