import facebook

import json
import time
from vk_parser import VkParser

group = ''
token = ''


def send_post(text, photos, videos):
    graph = facebook.GraphAPI(access_token=token)
    if len(photos) == 0 and len(videos) == 0:
        x = graph.put_object(group, 'feed', message=text)
    elif len(photos) == 1:
        x = graph.put_object(group, 'photos', message=text, url=photos[0])
    elif len(photos) > 1:
        x = graph.put_object(group, 'photos', message=text, url=photos[0])
    elif 1 < len(photos) <= 10:
        pass
    elif len(videos) == 1:
        x = graph.put_object(group, 'feed', message=text, link=videos[0])
    print('sent post')


def main():
    with open("publics1.json", "r") as f:
        groups = json.load(f)
    for group in groups:

        vk = VkParser(vk_group=group["vk_id"])
        posts = vk.get_posts()
        new_last_id = posts[0]["id"]
        if new_last_id > group["last_post_id"]:
            post = posts[0]
            vk.parse_post(post)
            print(vk.photos)
            send_post(vk.text, vk.photos, vk.videos)
            group["last_post_id"] = new_last_id
            with open('publics1.json', 'w') as outfile:
                json.dump(groups, outfile)




if __name__ == "__main__":
    while True:
        main()
        time.sleep(60 * 5)
