
from reverso_api.context import ReversoContextAPI

english_word = ReversoContextAPI("swim","","en","es")
english_gen = english_word.get_translations()
spanish_translation = next(english_gen).translation
spanish_word = ReversoContextAPI(spanish_translation,"","es","en")
spanish_gen = spanish_word.get_translations()
english_verb = next(spanish_gen).translation
print(english_verb)

