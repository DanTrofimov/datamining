import vk_api
import itertools
import asyncio

import database
import settings as cfg



def get_top_words(vk, domain):
    top_words = {}

    for i in range(2):
        data = vk.wall.get(domain=domain, offset=i * 100, count=100)
        for item in data['items']:
            text = item['text']
            text: str
            words = text.lower().split(" ")
            for word in words:
                if word in top_words:
                    top_words[word] += 1
                else:
                    top_words[word] = 0
    # print(top_words)
    sorted_x = sorted(top_words.items(), key=lambda item: item[1])
    sorted_x.reverse()
    new_top = {k: v for k, v in sorted_x}

    new_top = dict(itertools.islice(new_top.items(), 100))
    return new_top


async def worker():
    await database.preapare_db()
    print('db ready')
    vk_session = vk_api.VkApi(token=cfg.APP_VK_TOKEN)
    vk = vk_session.get_api()
    domain = 'itis_kfu'

    top_words = get_top_words(vk, domain)
    print('all words got')
    await database.TopWords.clear_table()
    for k, v in top_words.items():
        await database.TopWords.create(k, v)
    print('finish')


asyncio.run(worker())
