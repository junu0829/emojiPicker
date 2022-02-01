
import json
from googletrans import Translator

with open("C:/Users/wnsn0/emojiPicker/src/emojis.json", "r", encoding='UTF-8') as json_file:
     emoji_json= json.load(json_file)


p = emoji_json["People & Body"]

trans = Translator()


for e in p:
    e.update(name = trans.translate(e["name"], dest='ko').text)


print (json.dumps(p, ensure_ascii=False))
    


    





# result = trans.translate("word", dest='ko')


# print(result.text)