import aiohttp
import re
import os
import json

async def right_name(key: str):
    url = f"https://ygocdb.com/?search={key}"
    headers = {
        'user-agent': 'Passerby_D',
        'referer': 'https://ygocdb.com/',
    }
    async with aiohttp.ClientSession() as session:
        c = await session.get(url=url, headers=headers)
        text = (await c.content.read()).decode()

        #print(text)

        cn_name=re.findall('<strong class="name"><span>(.*?)</span><br></strong>', text)
        return cn_name
    

async def name2id(name: str,main_deck=None):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    with open("{}/data/cards.json".format(cur_dir), "r", encoding="utf-8") as f:
        cards = json.load(f)

    names=await right_name(name)

    if main_deck:
        for i in cards.keys():
            if cards[i]['cn_name'] in names and cards[i]['data']['level']>0:
                if i in main_deck:
                    return i

    for i in cards.keys():
        if cards[i]['cn_name'] in names and cards[i]['data']['level']>0:
            return i
        
    return None
