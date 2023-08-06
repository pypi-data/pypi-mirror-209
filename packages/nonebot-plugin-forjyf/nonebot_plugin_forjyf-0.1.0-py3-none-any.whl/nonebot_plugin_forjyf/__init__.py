from nonebot import on_regex,on_keyword,on_startswith,on_message
from nonebot.adapters.onebot.v11 import Event,Message
import re

for_jyf = on_keyword({"酷","库","裤","哦哈哟","噢","cool","来点","这样","么","趣","(","xm"}, priority=1,block=False)
for_jyf2 = on_message(priority=1,block=False)

@for_jyf.handle()
async def _(event: Event):
    if event.get_user_id() != "1767818223":
        return
    await for_jyf.finish(event.get_message())

@for_jyf2.handle()
async def __(event: Event):
    if event.get_user_id() != "1767818223":
        return

    for msg_seg in event.message:
        if(msg_seg.type == "image"):
            await for_jyf2.finish(event.get_message())

    jap = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\uAC00-\uD7A3]')

    if jap.search(str(event.get_message())):
        await for_jyf2.finish(event.get_message())