import time
from googletrans import Translator
translator = Translator()

translated_text = []
count = 0
grams = ["hello my name is Olivia."]

for g in grams:
    time.sleep(10)
    translated_text.append(
        translator.translate(g, dest='es', src='en')
    )

for t in translated_text:
    print(
        'English: ', t.origin, ' -----> ',
        'French: ', t.text
    )