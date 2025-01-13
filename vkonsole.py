#import vk
import random
import argparse
from datetime import datetime
from client import *

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("-s", "--send", nargs=2, help="Send message")
parser.add_argument("-m", "--messages", nargs="?", type=int, help="Show messages")
parser.add_argument("--history", nargs=2, help="Show message history")
#parser.add_argument("id", nargs='?', default=None, help="resource id")
parser.add_argument("--comments", action='store_true', help="shows comments on a post")
parser.add_argument("--realname", action='store_true', help="shows users real names instead nicks")
parser.add_argument("--fullname", action='store_true', help="shows users real names with nicks")
parser.add_argument("--noname", action='store_true', help="shows users activity without their names")
parser.add_argument("-l", "--log", action='store_true', help="logging")

parser.add_argument("-f", "--friends", action='store_true', help="show your friends list")

args = parser.parse_args()
send = args.send
messages = args.messages
history = args.history

#id = args.id
comments = args.comments
realname = args.realname
fullname = args.fullname
noname = args.noname
log = args.log
friends = args.friends

print(messages)
#parser.print_help()
#Сгенерировать свой токен по этому адресу https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&2fa_supported=1&username=[логин]&password=[пароль]&v=5.131
#P.S. Автоматическая генерация токена будет реализована позже.

api = vk.API(access_token=,v='5.199')
#print(api.users.get(user_ids=1))
#msg = input('Введите текст сообщения: ')
#recipient = input('Введите получателя: ')
#print(random.randint(0, 10000))

if friends:
    response = api.friends.get(user_id=id)
    if response:
         #print(response)
         for i in response['items']:
             if realname:
                 print(get_username(i))
             elif fullname:
                 print(get_domain(i))
             else:      
                 print(f'{get_username(i)} ({get_domain(i)})')
# if id:
    # response = api.wall.get(domain=id, extended=True) # Используем метод wall.get
    # #print(response)
    # if response['items']:
        # #vk.groups.getById(group_ids=str(response['items'][1]['owner_id'])[1:])[0]['screen_name'] 
        # #root.title(f"fooxy [{get_domain(response['items'][1]['owner_id'])}]")
        # if realname:
            # name = get_username(id)
        # elif fullname:
            # name = f'{get_username(i)} ({get_domain(i)})'
        # else:
            # name = id
        # print('===================== ', name,  '=====================')   
        # for i in response['items']: 
            # print('--------------------------------------------')
            # print("[{0}] {1}:\n {2}".format(datetime.utcfromtimestamp(int(i['date'])).strftime('%Y-%m-%d %H:%M:%S'),name,i['text']))
            # if "copy_history" in i:       
                # print("|[{0}] {1}:\n|{2}".format(datetime.utcfromtimestamp(int(i["copy_history"][0]['date'])).strftime('%Y-%m-%d %H:%M:%S'),get_domain(i["copy_history"][0]['owner_id']),i["copy_history"][0]['text']))   
                # print(f"likes: {i['likes']['count']} | reposts: {i['reposts']['count']} | comments: {i['comments']['count']} | views: {i['views']['count']}")
            # if comments:
                # show_comments(i["owner_id"],i["id"])
if history:
    #show_history(id)
    response = api.messages.getHistory(peer_id=history[0], count=history[1])

    if log:
        with open(r"archive.log", "w", encoding='utf-8') as file:
            for i in reversed(response['items']):
                file.write(i['text'] + '\n')
##                if realname:
##                    print(get_username(i['from_id']),'\t',i['text'], file=file)
##                elif fullname:
##                    print(f"{get_username(i['from_id'])} ({get_domain(i['from_id'])})\t{i['text']}", file=file)
##                elif noname:
##                    print(i['text'], file=file)    
##            else:
##                print(get_domain(i['from_id']),'\t',i['text'], file=file)
    else:   
        for i in reversed(response['items']):
            if realname:
                print(get_username(i['from_id']),'\t',i['text'])
            elif fullname:
                print(f"{get_username(i['from_id'])} ({get_domain(i['from_id'])})\t{i['text']}")
            elif noname:
                print(i['text'])
        
            else:
                print(get_domain(i['from_id']),'\t',i['text'])
    
if messages:
    response = api.messages.getConversations(count=messages)
    #print(response)
    
    for i in response['items']:
        if 'chat_settings' not in i['conversation']:
            print(i['conversation']['peer']['id'], '\t', i['last_message']['text'])
        else:
            print(i['conversation']['peer']['id'],'\t',i['conversation']['chat_settings']['title'], '\t', i['last_message']['text'])
##else:
##    response = api.messages.getConversations()
##    #print(response)
##    
##    for i in response['items']:
##        if 'chat_settings' not in i['conversation']:
##            print(i['conversation']['peer']['id'], '\t', i['last_message']['text'])
##        else:
##            print(i['conversation']['peer']['id'],'\t',i['conversation']['chat_settings']['title'], '\t', i['last_message']['text'])
if send:
    if not send[0].isdigit():
        response = api.messages.send(domain=send[0],message=send[1],random_id=random.randint(0, 10000) )
    else:
        response = api.messages.send(peer_id=send[0],message=send[1],random_id=random.randint(0, 10000) )
#print(response)
def show_comments(id, post):
##    if gui:
##     response = vk.wall.getComments(owner_id=id, post_id=post)
##     #print(response)
##     for i in response['items']: 
##        Label(text="[{0}] {1}: {2}".format(datetime.utcfromtimestamp(int(i['date'])).strftime('%Y-%m-%d %H:%M:%S'),get_domain(i['from_id']),i['text'])).pack()
##
##    else:
     response = api.wall.getComments(owner_id=id, post_id=post)
     #print(response)
     for i in response['items']:
        if realname:
            name = get_username(i['from_id'])
        elif fullname:
            name = f"{get_username(i['from_id'])} ({get_domain(i['from_id'])})"
        else:
            name = get_domain(i['from_id'])
        print("[{0}] {1}: {2}".format(datetime.utcfromtimestamp(int(i['date'])).strftime('%Y-%m-%d %H:%M:%S'),name,i['text']))
