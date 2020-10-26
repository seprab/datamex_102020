from googletrans import Translator
translator = Translator()
print(translator.translate('swimming', src='en').extra_data())
print(translator.detect('swimming'))
