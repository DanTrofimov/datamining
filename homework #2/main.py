from pprint import pprint
import vk_api
import re

import pandas as pd
import matplotlib.pyplot as plt
import vk_api

# remove symbols: " ) ( # & << » [ ] «
# remove words with: digits / length==0or 1 club
removingChars = ["(", ")", "[", "]", "«", "»", "&", "!", "\""]
banningSubs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "/", "club", "\\", ";", "#", "@"]


def remove_char(input_word, char):
    resultWord = input_word.replace(char, "")
    return resultWord


def clear_word(word_clear):  # Убираем ненужные символы
    for char in removingChars:
        word_clear = remove_char(word_clear, char)
    return word_clear


def filter_word(filtering_word):  # Удаляем неподходящие слова
    if len(filtering_word) == 1 or len(filtering_word) == 0:
        return False
    for sub in banningSubs:
        if sub in filtering_word:
            return False
    return True


def get_words(text):  # Рaзбиваем на слова данные
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):  # Подсчет слов
    words_filtered = []
    clear_words = []
    words_dictionary = dict()

    for word_item in words:
        if filter_word(word_item):
            words_filtered.append(word_item)

    for word_item in words_filtered:
        clear_words.append(clear_word(word_item))

    for word_item in clear_words:
        if word_item in words_dictionary:
            words_dictionary[word_item] = words_dictionary[word_item] + 1
        else:
            words_dictionary[word_item] = 1
    return words_dictionary


vk_session = vk_api.VkApi("+79053749485", "ila09202000")  # Проводим авторизацию(логин и пароль от вк)
vk_session.auth()
id = 'id641678009'  # Вводим свой айдишник
api = vk_session.get_api()

groups = api.groups.get()
pprint(groups)

walls = api.wall.get(domain='itis_kfu', count=200)  # Получили все посты

resultText = ""

# fixme: Добавление текстовых полей, если возможно, то добавить еще
for item in walls['items']:
    resultText = resultText + item['text']
    if ('title' in item):
        resultText += item['title']

words_dict = get_words_dict(get_words(resultText))  # Итоговый словарь (слово - кол-во вхождений)

words_dict = dict(sorted(words_dict.items(), key=lambda dict_item: dict_item[1]))

# df = pd.DataFrame.from_dict(words_dict, orient='index').transpose()

plt.title('Words statistics')

words_top = 20

bars = list(words_dict.values())[len(words_dict)-words_top:]
xticks = list(words_dict.keys())[len(words_dict)-words_top:]

plt.bar(range(words_top), bars, align='center')
plt.xticks(range(words_top), xticks, rotation='vertical')
plt.tight_layout()

plt.savefig('words-top.png')

plt.show()

# logs
for word in words_dict:
    print(word.ljust(20), words_dict[word])
