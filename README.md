# DiscordOauth2

Discord Oauth2認証を使用して自動でユーザーをサーバーに招待します。

### ソースコードの使用について

このソースコードは自由に使ってください。ただし再配布や悪用は厳禁です。

# Discord Developer Portal設定

※先にDiscord Developer PortalでアプリケーションおよびBotを作成しておく必要があります  

- Bot：PUBLIC BOTを有効にする
- OAuth2/General：RedirectsにリダイレクトURLを設定する(http://ドメイン/callback / ローカル環境の場合はlocalhost:8000)
- OAuth2/General：Default Authorization Link/AUTHORIZATION METHODでIn-app Authorizationを選択する
- OAuth2/General：Default Authorization Link/SCOPESはbotとapplications.commandsにチェックを入れる
- OAuth2/General：Default Authorization Link/BOT PERMISSIONSはAdministratorにチェックを入れる
- OAuth2/URL Generator：SCOPESはidentify, guilds, guilds.joinにチェックを入れる
- OAuth2/URL Generator：SELECT REDIRECT URLは最初に設定したリダイレクトURLを選択する
- OAuth2/URL Generator：GENERATED URLに表示されるURLを開いて認証を押す

# ソースコードに必要な情報

ソースコードの6行目から9行目の定数に各環境に合わせた値を代入する必要があります。それらの値は全てDiscord Developer Portalに記載されています。

- CLIENT_ID(str)：OAuth2/General
- CLIENT_SECRET(str)：OAuth2/General
- REDIRECT_URI(str)：OAuth2/General(Redirectsに設定した値)
- BOT_TOKEN(str)：Bot(Build-A-Bot/TOKEN)

10行目のGUILD_ID(int)はDiscordのサーバー設定のウィジェットから取得できます。

# 補足

58行目のresponseにはjson形式でDiscordユーザー情報が格納されています。response.text['key']で情報を取得できます。
