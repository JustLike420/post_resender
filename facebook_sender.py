import facebook


group = '3071372716522115'
token=''
msg = 'test text'
image_url = 'https://sun9-6.userapi.com/impg/mixite2huffOMRRfpWsAlEZbfwxtVydii_aJzA/MCPTBqakNXA.jpg?size=827x990&quality=96&sign=c27f062a8a33429b4804a5e541a6c9c1&c_uniq_tag=oNnVXAI6J4z-kqzPxMp4G1D_DG_vcVOppqqrVv1pwVU&type=album'
graph = facebook.GraphAPI(access_token=token)
video_url = 'https://vk.com/video-211099549_456239031'

x = graph.put_object(group, 'feed', message=msg)
x = graph.put_object(group, 'photos',  message=msg, url=image_url)
x = graph.put_object(group, 'feed', message=msg, link=video_url)
# print(x)