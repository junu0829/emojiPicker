import os 




import json
from google.cloud import translate_v2 as translate
credential_path ="C:/Users/wnsn0/Documents/boreal-album-340112-defd948aaca6.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
with open("C:/Users/wnsn0/emojiPicker/src/emojis.json", "r", encoding='UTF-8') as json_file:
     emoji_json= json.load(json_file)


p = emoji_json["Symbols"]

trans = translate.Client()

trans.raise_Exception = True


for e in p:
    e.update(name = trans.translate(e["name"], target_language='ko')["translatedText"])


# print (json.dumps(p, ensure_ascii=False))

with open('data7.json', 'w', encoding='UTF-8') as make_file:
    json.dump(p, make_file, ensure_ascii=False, indent="\t")




    





# result = trans.translate("word", dest='ko')


# print(result.text)