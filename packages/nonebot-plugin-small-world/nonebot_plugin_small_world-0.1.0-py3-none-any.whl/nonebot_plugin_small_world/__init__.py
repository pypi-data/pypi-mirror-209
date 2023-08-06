from os import path,makedirs
import os
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event,Message,MessageSegment,Bot,GroupMessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg,ArgPlainText
from nonebot.matcher import Matcher
import json

from .name2id import name2id


if path.exists("data/small_world")==False:
   makedirs("data/small_world")



small_world=on_command('small_world',aliases={'sw','小世界','小世界现象'})

@small_world.handle()
async def _(event:Event,matcher:Matcher,args:Message = CommandArg()):
    if path.exists("data/small_world/{}".format(event.get_user_id()))==False:
        await small_world.finish('您还没有保存过您的卡组码！')
    if args:
        matcher.set_arg('name',args)

@small_world.got('name',prompt='请输入您想查询的卡组名')
async def _(event:Event,matcher:Matcher,content:str=ArgPlainText('name')):
    if str(matcher.get_arg('name'))+'.txt' not in os.listdir("data/small_world/{}".format(event.get_user_id())):
        await small_world.finish('您没有保存这个名字的卡组！')

@small_world.got('start',prompt='请输入您想里侧除外的手牌')
async def _(bot:Bot,event:Event,matcher:Matcher,content:str=ArgPlainText('start')):
    start_id=str(matcher.get_arg('start'))
    try:
        int(start_id)
    except:
        start_id=await name2id(start_id)

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    with open("{}/data/cards.json".format(cur_dir), "r", encoding="utf-8") as f:
        cards = json.load(f)

    

    with open("data/small_world/{}/{}.txt".format(event.get_user_id(),str(matcher.get_arg('name'))), "r", encoding="utf-8") as f:
        deck = f.readlines()
        start=deck.index('#main\n')+1
        end=deck.index('#extra\n')
        main_deck=[]
        for i in range(start,end):
            temp_card=deck[i].strip()
            if temp_card not in main_deck:
                if temp_card in cards.keys():
                    main_deck.append(temp_card)

    if start_id not in main_deck:
        await small_world.finish('请输入正确的卡名或id！')


    path=[]
    end=[]

    for j in main_deck:
        same_times=0
        if cards[j]['data']['attribute']==cards[start_id]['data']['attribute']:same_times+=1
        if cards[j]['data']['atk']==cards[start_id]['data']['atk']:same_times+=1
        if cards[j]['data']['def']==cards[start_id]['data']['def']:same_times+=1
        if cards[j]['data']['level']==cards[start_id]['data']['level']:same_times+=1
        if cards[j]['data']['race']==cards[start_id]['data']['race']:same_times+=1
        if same_times==1:
            for k in main_deck:
                same_times=0
                if cards[k]['data']['attribute']==cards[j]['data']['attribute']:same_times+=1
                if cards[k]['data']['atk']==cards[j]['data']['atk']:same_times+=1
                if cards[k]['data']['def']==cards[j]['data']['def']:same_times+=1
                if cards[k]['data']['level']==cards[j]['data']['level']:same_times+=1
                if cards[k]['data']['race']==cards[j]['data']['race']:same_times+=1
                if same_times==1 and int(cards[j]['data']['level'])*int(cards[k]['data']['level'])>0:
                    path.append([cards[j]['cn_name'],cards[k]['cn_name']])
                    if cards[k]['cn_name'] not in end:
                        end.append(cards[k]['cn_name'])

    temp_str=''
    for i in end:
        temp_str+=i+' | '
    await small_world.send('可以检索到 | {}'.format(temp_str))

    temp_str=''
    msgs=[]
    end_count=[]
    for i in path:
        if i[1] not in end_count:
            temp_str='*'+i[1]+'*'
            end_count.append(i[1])
            for j in path:
                if j[1]==i[1]:
                    temp_str+='\n'+cards[start_id]['cn_name']+'-->'+j[0]+'-->'+j[1]
            msgs.append(temp_str)

    if isinstance(event,GroupMessageEvent):
        await send_forward_msg_group(bot, event, "小世界助手", msgs if msgs else ["没有任何路径！"])
    elif isinstance(event,PrivateMessageEvent):
        if not msgs:
            await small_world.finish("没有任何路径！")
        for msg in msgs:
            await small_world.send(msg)



        


ydk_input=on_command('ydk_input',aliases={'yi','ydk','卡组码'})

@ydk_input.handle()
async def _(matcher:Matcher,args:Message = CommandArg()):
    pass

@ydk_input.got('name',prompt='请输入您的卡组名')
async def _(event:Event,matcher:Matcher,content:str=ArgPlainText('name')):
    if path.exists("data/small_world/{}".format(event.get_user_id())):
        if matcher.get_arg('name') in os.listdir("data/small_world/{}".format(event.get_user_id())):
            await ydk_input.finish('已经有这个卡组名了！')

@ydk_input.got('ydk',prompt='请输入您的卡组码')
async def _(event:Event,matcher:Matcher,content:str=ArgPlainText('ydk')):
    if path.exists("data/small_world/{}".format(event.get_user_id()))==False:
        makedirs("data/small_world/{}".format(event.get_user_id()))
    with open("data/small_world/{}/{}.txt".format(event.get_user_id(),matcher.get_arg('name')),'w') as f:
        f.write(str(matcher.get_arg('ydk')))
    await ydk_input.finish("保存卡组码成功！")




small_world_search=on_command('small_world_search',aliases={'sws','小世界搜索','小世界现象搜索'})

@small_world_search.handle()
async def _(matcher:Matcher,args:Message = CommandArg()):
    if args:
        arglist=args.extract_plain_text().split()
        matcher.set_arg('start',arglist[0])
        matcher.set_arg('end',arglist[1])

@small_world_search.got('start',prompt='请输入您想里侧除外的手牌')
async def _(bot:Bot,event:Event,matcher:Matcher,content:str=ArgPlainText('start')):
    pass

@small_world_search.got('end',prompt='请输入您想检索的卡牌')
async def _(bot:Bot,event:Event,matcher:Matcher,content:str=ArgPlainText('end')):
    start_id=str(matcher.get_arg('start'))
    end_id=str(matcher.get_arg('end'))

    try:
        int(start_id)
    except:
        start_id=await name2id(start_id)

    try:
        int(end_id)
    except:
        end_id=await name2id(end_id)
    
    if start_id==None or end_id==None:
        await small_world_search.finish('请输入正确的卡名或id！')

    cur_dir = os.path.dirname(os.path.abspath(__file__))
    with open("{}/data/cards.json".format(cur_dir), "r", encoding="utf-8") as f:
        cards = json.load(f)
    

    temp_dict=[]
    temp_str='可以当中介的卡有：\n'
    for i in cards.keys():
        same_times=0
        #print(cards[i]['cid'])
        if cards[start_id]['data']['attribute']==cards[i]['data']['attribute']:same_times+=1
        if cards[start_id]['data']['atk']==cards[i]['data']['atk']:same_times+=1
        if cards[start_id]['data']['def']==cards[i]['data']['def']:same_times+=1
        if cards[start_id]['data']['level']==cards[i]['data']['level']:same_times+=1
        if cards[start_id]['data']['race']==cards[i]['data']['race']:same_times+=1
        if same_times==1:
            if cards[end_id]['data']['attribute']==cards[i]['data']['attribute']:same_times+=1
            if cards[end_id]['data']['atk']==cards[i]['data']['atk']:same_times+=1
            if cards[end_id]['data']['def']==cards[i]['data']['def']:same_times+=1
            if cards[end_id]['data']['level']==cards[i]['data']['level']:same_times+=1
            if cards[end_id]['data']['race']==cards[i]['data']['race']:same_times+=1
            if same_times==2:
                temp_dict.append(cards[i]['cn_name'])

    count=0
    msgs=[]
    for i in temp_dict:
        temp_str+=' | '+i
        count+=1
        if count==100:
            temp_str+=' |'
            msgs.append(temp_str)
            count=0
            temp_str=''
    temp_str+=' |'
    msgs.append(temp_str)
    if isinstance(event,GroupMessageEvent):
        await send_forward_msg_group(bot, event, "小世界助手", msgs if msgs else ["没有任何中介卡！"])
    elif isinstance(event,PrivateMessageEvent):
        if not msgs:
            await small_world.finish("没有任何中介卡！")
        for msg in msgs:
            await small_world.send(msg)

    


# 合并消息
async def send_forward_msg_group(
        bot: Bot,
        event: GroupMessageEvent,
        name: str,
        msgs: list
):
    def to_json(msg):
        return {"type": "node", "data": {"name": name, "uin": bot.self_id, "content": msg}}

    messages = [to_json(msg) for msg in msgs]
    await bot.call_api(
        "send_group_forward_msg", group_id=event.group_id, messages=messages
    )