# Saygısızlar Filter Bot
#### With Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Neredeyse filtrelenmemiş filtrelere sahip gelişmiş bir Filtre Botu!

### Özellikler
* Neredeyse sınırsız filtreler
* Her türlü filtreyi destekler (Uyarı Düğmesi Filtresi Dahil).
* Düğme filtrelerini doğrudan kaydedebilir (Rose Bot Özelliği)
* Birden fazla PM bağlantısını destekler
* Ve filtre botunun diğer tüm özellikleri :D

#### Botu dağıtın ve filtrelerinizi :) eklemeye başlayın

## Bot nasıl kullanılır
* Yönetici haklarına sahip grubunuza bot ekleyin.

* Filtrelerinizi ekleyin :)


## Bot Commands

(You need to be an admin or Auth User in order to use these commands)

> Filter Commands
* `/add <filtername> <filtercontent>`  -  To add your filter. You can also reply to your content with /add command.

* `/del <filtername>`  -  Delete your filter.

* `/delall`  -  Delete all filters from group. (Group Owner Only!)

* `/viewfilters`  -  List all filters in chat.

> Connection Commands
* `/connect groupid`  -  Connects your group to PM. You can also simply use, `/connect` in groups.

* `/connections`  -  Manage your connections. (only in PM)

> Extras
* `/status`  -  Shows current status of your bot (Auth User Only)

* `/id`  -  Shows ID information

* `/info <userid>`  -  Shows User Information. Also use `/info` as reply to some message for their details!

## Configs

* TG_BOT_TOKEN  - Get bot token from @BotFather

* API_ID        - From my.telegram.org (or @UseTGXBot)

* API_HASH      - From my.telegram.org (or @UseTGXBot)

* AUTH_USERS  - ID of users that can use the bot commands. Get from [MissRose Bot](https://telegram.dog/MissRose_bot) by using /id command

* DATABASE_URI  - Mongo Database URL from https://cloud.mongodb.com/

* DATABASE_NAME  - Your database name from mongoDB. Default will be 'Cluster0'

* SAVE_USER  -  Give yes or no . Usefull for getting userinfo and total user counts. May reduce filter capacity :( .

* HEROKU_API_KEY  -  To check dyno status. Go to https://dashboard.heroku.com/account , scroll down and press Reveal API


### Optional - To set alternate Bot Commmands!
( *Add required field as heroku var and give desired command as value. You can edit it in sample_config.py also!*)

* ADD_FILTER_CMD  -  default will be 'add'

* DELETE_FILTER_CMD  -  default will be 'del'

* DELETE_ALL_CMD  -  default will be 'delall'

* CONNECT_COMMAND  -  default will be 'connect'

* DISCONNECT_COMMAND  -  default will be 'disconnect'
