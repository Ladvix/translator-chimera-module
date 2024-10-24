from pyrogram import Client, filters
from googletrans import Translator
translator = Translator()

def init(app):

    @app.on_message(filters.command('translate', prefixes = '.') & filters.me)
    def _(client, message):

        text = message.text.split(' ', maxsplit = 2)[2]
        dest = message.text.split(' ', maxsplit = 2)[1]

        translation = translator.translate(text, dest = dest)

        message.edit(translation.text)