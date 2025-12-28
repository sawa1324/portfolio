import requests

TOKEN = '8296280900:AAHBmKrsOCj80lNlT7L7a2mFG5VwaXJ4dgQ'

response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
print(response.json())