def output_console(text):
    """
    Функція для виводу тексту у консоль.

    :param text: текст для виводу
    """
    print(text)

def write_file_builtin(file_path, text):
    """
    Функція для запису до файлу за допомогою вбудованих можливостей Python.

    :param file_path: шлях до файлу
    :param text: текст для запису
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
