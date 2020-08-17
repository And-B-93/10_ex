import requests
import json
token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
version = 5.21
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f'https://vk.com/id{self.user_id}'

    def list_users(self):
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'user_id': self.user_id,
                'fields': 'friends',
                'access_token': token,
                'v': version
            }
        )
        return f"{response.json()['response'][0]['first_name']} {response.json()['response'][0]['last_name']}"

    def friends_list(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': token,
                'v': version,
                'user_id': self.user_id,
                'fields': 'friends',
            }
        )
        list_id_1 = json.loads(response.text)['response']['count']
        return list_id_1

    def intersection_friends_list(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': token,
                'v': version,
                'user_id': self.user_id,
                'fields': 'friends',
            }
        )
        list_id_2 = set([user_id['id'] for user_id in json.loads(response.text)['response']['items']])
        return list_id_2

    def __and__(self, other):
        other.user_id = user_id
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': token,
                'v': version,
                'user_id': self.user_id,
                'fields': 'friends',
            }
        )
        list_id_2 = set([user_id['id'] for user_id in json.loads(response.text)['response']['items']])
        return list_id_2

user_1 = User(86780228)
user_2 = User(26205261)
#user_1 & user_2
print(f'{user_1.list_users()} {user_1} и {user_2.list_users()} {user_2} имеют {user_1.friends_list()} и {user_2.friends_list()} друзей соответсвено')
print('=====')
print(user_1.intersection_friends_list())
print(user_2.intersection_friends_list())
print('=====')
print()