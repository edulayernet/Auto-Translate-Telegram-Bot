import pyrogram
import tgcrypto
from pyrogram.types import *
from pyrogram import Client, filters
from googletrans import Translator
from googletrans.constants import LANGUAGES, LANGCODES
from config import *

# arkadaşlar izliyorsanız, pes etmeyin sonunda bunu da çözdük :DD

app = Client(name=session_name, bot_token=bot_token, api_id=api_id, api_hash=api_hash)

def translate(text, des, src='auto'):
    translator = Translator()
    result = translator.translate(text, dest=des, src=src)
    return result
translator = Translator()
@app.on_message(filters.group)
async def tr(client, message):
    current_language = "tr"
    t = translate(message.text, des=current_language).text
    pattern = f'Bir yabancı mesaj tespit edildi!\n\nMetnin çevirisi: {t}\n ```{message.chat.title}```'
    print(type(translator.detect(message.text).confidence))
    if type(translator.detect(message.text)) != list and "tr" not in translator.detect(message.text).lang and translator.detect(message.text).confidence >= 0.70 :

      await app.send_message(message.chat.id, text=f"{pattern}",reply_to_message_id=message.id)


app.run()
