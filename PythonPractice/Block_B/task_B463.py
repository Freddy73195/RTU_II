"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""
import string
import re
def wiki_function(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    translator = str.maketrans('', '', string.digits + string.punctuation)
    lines = [line.translate(translator) for line in lines]
    text = ' '.join(lines)
    w = {}
    for word in text.split():
        if word not in w:
            w[word] = 0
        w[word] += 1
    sorted_words = sorted(w.items(), key=lambda x: x[1], reverse=True)
    popular_words = [w[0] for w in sorted_words[:10]]
    for w in popular_words:
        pattern = r"\b" + re.escape(w) + r"\b"
        text = re.sub(pattern, "PYTHON", text)
    # sorted_words = sorted(w.items(),key=lambda x: x[1], reverse=True)
    # p = [word[0] for word in sorted_words[:10]]
    # for word in p:
    #     text = text.replace(word, 'PYTHON')
    with open('EVA0.txt','w') as f:
        l = 0
        for word in text.split():
            wo = len(word)
            if l + wo + 1 > 100:
                f.write('\n')
                l = 0
            if l == 0:
                f.write(word)
                l += wo
            else:
                f.write(' ' + word)
                l += wo + 1
    print('Топ 10 популярных слов:')
    for i, w in enumerate(sorted_words[:10], 1):
        word, count = w
        print(f'{i} место --- {word} --- {count} раз(а)')
    return text

# Вызов функции
wiki_function("EVA.txt")