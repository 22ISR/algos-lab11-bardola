import requests
import json

while True:
    user_input = input(
        "Введите название фильма (или напишите 'выход' чтобы завершить работу): "
    )
    if user_input == 'выход' or user_input == 'q':
        break

    response = requests.get(f'http://www.omdbapi.com/?apikey=505480d7&s={user_input}')
    if response.status_code == 200:
        answer = response.json()

        for i in answer.get('Search', [None]):
            if i == None:
                print('I\'m don\'t find it')
                continue
            print(f'Название: {i['Title']}, Год: {i['Year']}, Тип: {i['Type']}')
    else:
        print('Why do you do it?')