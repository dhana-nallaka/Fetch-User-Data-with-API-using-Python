###printing the fetched data###

import requests
import json

headers_app = {'app-id': '6262317b43db6360bc82e35a'}
url="https://dummyapi.io/data/v1/user"
url_requests=requests.get(url,headers=headers_app)
url_data=json.loads(url_requests.content)
d=url_data['data']#to get the data from the dictionary with key 'data'
for i in range(len(d)):
    title_list=d[i]['title']
    first_name_list=d[i]['firstName']
    id_list=d[i]['id']
    last_name_list=d[i]['lastName']
    name=title_list+" "+first_name_list+" "+last_name_list
    print(f'''id: {id_list}     Name:  {name}''')#printing name and id
    url_posts=f'''{url}/{id_list}/post'''
    url_posts_requests=requests.get(url_posts,headers=headers_app)
    url_posts_data=json.loads(url_posts_requests.content)
    #print(url_posts_data)#for checking json
    for i in range(len(url_posts_data['data'])):
         owner_id=url_posts_data['data'][i]['owner']['id']
         post_id=url_posts_data['data'][i]['id']
         post_text=url_posts_data['data'][i]['text']
         print(owner_id+" "+post_id+" "+post_text)#printing corresponding names
