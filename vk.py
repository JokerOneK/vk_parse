import requests
import csv


def take_posts():
    token = '6aeb7ac86aeb7ac86aeb7ac8106a9856f166aeb6aeb7ac835f1fa93f2ac34a5f90667f4'
    version = '5.120'
    domain = 'yvkurse'
    count = 100
    offset = 0
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                })

        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)

    return all_posts


def write_file(data):

    with open('yvkurse.csv', 'w', encoding="utf-8") as file:
        table = csv.writer(file)
        table.writerow(('text', 'images_urls'))
        for post in data:
            try:
                if post['attachments'][0]['type'] == 'link':
                    img_url = post['attachments'][0]['link']['photo']['sizes'][-1]['url']

                elif post['attachments'].__len__() > 1:
                    img_url_list = []
                    for i in range(0, post['attachments'].__len__()):
                        img_url_list.append(str(post['attachments'][i]['photo']['sizes'][-1]['url']))
                    img_url = (", ".join(img_url_list))
                else:
                    img_url = 'not an image'
            except:
                pass
            table.writerow((post['text'], img_url))


all_posts = take_posts()
write_file(all_posts)

