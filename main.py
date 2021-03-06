import os
import config
import telebot
from bot import bot
from flask import Flask, request

bot.remove_webhook()
bot.set_webhook(f'https://<app_name>.herokuapp.com/{config.token}')
server = Flask(__name__)

@server.route("/", methods=['GET'])
def keepAlive():
    # Just to not let the server on the free Heroku account go to sleep
    # http://kaffeine.herokuapp.com/
    print('Keep alive: OK.')
    return '!', 200

@server.route(f"/{config.token}", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', '5000')))
