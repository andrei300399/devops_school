# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода в виде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
#
# 1. После запуска предлагает пользователю ввести текст.
# 2. В качестве ответа печатает наиболее часто встречающееся в тексте слово
# или несколько таких слов, если имеет место "ничья". Также указывая
# сколько именно раз слово встретилось в тексте. (Игнорируйте заглавные буквы
# при отождествлении слов - то есть считайте слова "Подлодка" и "подлодка"
# одинаковыми, а разные формы слов - разными словами)
# После чего ждет следующего ввода.
#
# Пример:
#
# -> собака кот кошка Собака
# 2 - собака
#
# -> собака кот кошка Собака кот
# 2 - собака
# 2 - кот
words = input("Введите строку:").lower().split()
max_count = 0
max_words = {}
for word in words:
    count_tmp = words.count(word)
    if max_count < count_tmp:
        max_count=count_tmp
        max_words.clear()
        max_words[word]=count_tmp
    elif max_count == count_tmp:
        max_words[word]=count_tmp

for word in max_words:
    print(f"{max_count} - {word}")




