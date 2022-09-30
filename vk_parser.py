import requests
import config


class VkParser:
    def __init__(self, vk_group):
        self.vk_token = config.vk_token
        self.vk_group = '-' + str(vk_group)
        self.text = ''
        self.photos = []
        self.videos = []

    def get_posts(self):
        api = 'https://api.vk.com/method/wall.get'
        req = requests.get(api,
                           params={
                               "access_token": self.vk_token,
                               "v": '5.131',
                               "owner_id": self.vk_group,
                               "count": 20,
                           },
                           )
        data = req.json()
        post_list = data['response']['items']
        # проверка на закреп posts_list[1].get('is_pinned')
        if "is_pinned" in post_list[0]:
            post_list = post_list[1:]
        return post_list

    def parse_post(self, post: dict):
        self.text = post['text'].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

        if 'attachments' in post:
            for attachment in post['attachments']:
                if attachment['type'] == 'photo':
                    photo_url = attachment['photo']['sizes'][-1]['url']
                    self.photos.append(photo_url)
                elif attachment['type'] == 'video':
                    owner_id = attachment["video"]["owner_id"]
                    video_id = attachment["video"]["id"]
                    response = requests.get(
                        "https://api.vk.com/method/video.get",
                        params={
                            "access_token": self.vk_token,
                            "v": '5.131',
                            "videos": f"{owner_id}_{video_id}",
                        },
                    )
                    data = response.json()
                    video_url = data["response"]['items'][0]['player']
                    self.videos.append(video_url)


# if __name__ == '__main__':
#     vk = VkParser(vk_group=45509461)
#     posts = vk.get_posts()
#     post = posts[0]
#     vk.parse_post(post)
#     print(vk.text, vk.photos)
