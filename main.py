import requests
from urllib.parse import urlencode
from flask import Flask, request

API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '1104942716305027123'
CLIENT_SECRET = 'yiUppztLyAKb4D1Y1qyc0hkWGxOKBu6n'
REDIRECT_URI = 'http://localhost:8000/callback'

app = Flask(__name__)

def get_authorization_url():
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': 'identify guilds guilds.join',
    }
    url = f'{API_ENDPOINT}/oauth2/authorize?{urlencode(params)}'
    return url

def exchange_code(code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    r = requests.post(f'{API_ENDPOINT}/oauth2/token', data=data, headers=headers)
    r.raise_for_status()
    return r.json()

def get_user_id(access_token):
    url = f'{API_ENDPOINT}/users/@me'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    return response.json()['id']

def add_to_guild(access_token, guild_id):
    user_id = get_user_id(access_token)
    url = f'{API_ENDPOINT}/guilds/{guild_id}/members/{user_id}'
    bot_token = 'MTEwNDk0MjcxNjMwNTAyNzEyMw.GLMge4.OzEwe24cUF9zmfseF8Meb7HR0mJjIem4M5_6Mw'
    data = {
        'access_token': access_token,
    }
    headers = {
        'Authorization': f'Bot {bot_token}',
        'Content-Type': 'application/json',
    }
    response = requests.put(url=url, headers=headers, json=data)
    print(response.text)

@app.route('/')
def index():
    authorization_url = get_authorization_url()
    return f'<a href="{authorization_url}">以下のURLにアクセスして認証を完了させてください:</a>'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    access_token = exchange_code(code)['access_token']
    add_to_guild(access_token, 1068175810864877579)
    return "認証が完了しました。このページを閉じてください。"

if __name__ == "__main__":
    app.run(debug=True,port=8000)
