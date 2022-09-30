import glob
import os
from aiogram import types
import youtube_dl


async def send_post(bot, tg_channel, text, photos, videos):
    if len(photos) == 0:
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
    # elif len(videos) == 1:
    #     ydl_opts = {}
    # video_url = videos[0]
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([video_url])
    # os.chdir(".")
    # for file in glob.glob("*.mp4"):
    #     print(file)
    #
    # with open("file.mp4", "rb") as video:
    #     await bot.send_chat_action(tg_channel, "upload_video")
    #     await bot.send_video(tg_channel, video=video, caption=text, parse_mode=types.ParseMode.HTML,supports_streaming=True)
    # media = types.MediaGroup()
    # media.attach_video(types.InputFile('file1.mp4'))
    # await bot.send_media_group(tg_channel, media)
    # print("ok")
    # os.remove(file)
    # await bot.send_video(tg_channel, videos[0], caption=text, parse_mode=types.ParseMode.HTML)
