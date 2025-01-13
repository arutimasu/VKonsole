import vk

#api = vk.API(access_token='vk1.a.JN_pxpqHHKc2vVCYbPy8EhvUYIsWnYKjURde5et77ArRokya0hQP1vZe8e-Nwq506XmdrnZcRrXrVeM5gQoYVHr1n2uHWOwDVvBzAQoqIYiGHXt-1dRkgHixC_w2FpLhOuuKocAjNk0A1I4YreCURLcD0K4biH4aoz9J3utwpaVkpBjKaYpAmtDiP44U1DV1PKqcLunAWpjGCo2-ofbepw',v='5.131')
api = vk.API(access_token='ee08e73aee08e73aee08e73a11ed2c9c78eee08ee08e73a893444840e4240ed446fcb09',v='5.199')
##def show_history(id):
##    response = api.messages.getHistory(peer_id=history[0])
##    for i in reversed(response['items']):
##        if realname:
##            print(get_username(i['from_id']),'\t',i['text'])
##        elif fullname:
##            print(f"{get_username(i['from_id'])} ({get_domain(i['from_id'])})\t{i['text']}")
##        else:
##            print(get_domain(i['from_id']),'\t',i['text'])
##def show_friends(id):
## response = api.friends.get(user_id=id)
## if response:
##     #print(response)
##     for i in response['items']:
##         if realname:
##             print(get_username(i))
##         elif fullname:
##             print(get_domain(i))
##         else:      
##             print(f'{get_username(i)} ({get_domain(i)})')
def get_username(id):
 response = api.users.get(user_ids=id) # Используем метод users.get
 if response!=None:
     return '{0} {1}'.format(response[0]['first_name'],response[0]['last_name'])
     #print(f"{response[0]['first_name']} {response[0]['last_name']}")
##     if response[0]['is_closed']:
##      print("Профиль закрыт");

##def show_wall(id):
##    response = api.wall.get(domain=id, extended=True) # Используем метод wall.get
##    #print(response)
##    if response['items']:
##        #vk.groups.getById(group_ids=str(response['items'][1]['owner_id'])[1:])[0]['screen_name'] 
##        #root.title(f"fooxy [{get_domain(response['items'][1]['owner_id'])}]")
##        if realname:
##            name = get_username(id)
##        elif fullname:
##            name = f'{get_username(i)} ({get_domain(i)})'
##        else:
##            name = id
##        print('===================== ', name,  '=====================')   
##        for i in response['items']: 
##            print('--------------------------------------------')
##            print("[{0}] {1}:\n {2}".format(datetime.utcfromtimestamp(int(i['date'])).strftime('%Y-%m-%d %H:%M:%S'),name,i['text']))
##            if "copy_history" in i:       
##                print("|[{0}] {1}:\n|{2}".format(datetime.utcfromtimestamp(int(i["copy_history"][0]['date'])).strftime('%Y-%m-%d %H:%M:%S'),get_domain(i["copy_history"][0]['owner_id']),i["copy_history"][0]['text']))   
##                print(f"likes: {i['likes']['count']} | reposts: {i['reposts']['count']} | comments: {i['comments']['count']} | views: {i['views']['count']}")
##            if comments:
##                show_comments(i["owner_id"],i["id"])
##def show_comments(id, post):
####    if gui:
####     response = vk.wall.getComments(owner_id=id, post_id=post)
####     #print(response)
####     for i in response['items']: 
####        Label(text="[{0}] {1}: {2}".format(datetime.utcfromtimestamp(int(i['date'])).strftime('%Y-%m-%d %H:%M:%S'),get_domain(i['from_id']),i['text'])).pack()
####
####    else:
##     response = api.wall.getComments(owner_id=id, post_id=post)
##     #print(response)
##     for i in response['items']:
##        if realname:
##            name = get_username(i['from_id'])
##        elif fullname:
##            name = f"{get_username(i['from_id'])} ({get_domain(i['from_id'])})"
##        else:
##            name = get_domain(i['from_id'])
##        print("[{0}] {1}: {2}".format(datetime.utcfromtimestamp(int(i['date'])).strftime('%Y-%m-%d %H:%M:%S'),name,i['text']))
def get_domain(id):
   if str(id)[0] == '-':
      return api.groups.getById(group_ids=str(id)[1:])[0]['screen_name']
   else:
      return api.users.get(user_ids=id, fields='domain')[0]['domain']
