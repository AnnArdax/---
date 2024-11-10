# TODO Найдите количество книг, которое можно разместить на дискете
# Параметры книги
pages = 100  # количество страниц
lines_per_page = 50  # количество строк на странице
chars_per_line = 25  # количество символов в строке
bytes_per_char = 4  # количество байтов для хранения одного символа

# Объем дискеты в мегабайтах
disk_volume_mb = 1.44
# Переводим объем дискеты в байты
disk_volume_bytes = disk_volume_mb * 1024 * 1024  # 1 Мб = 1024 Кб = 1024 * 1024 Б

# Рассчитываем объем одной книги в байтах
book_volume_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

# Рассчитываем, сколько книг можно поместить на дискету
number_of_books = disk_volume_bytes // book_volume_bytes  # целочисленное деление
int(number_of_books)
# Вывод результата
print(f"Количество книг, которые можно поместить на дискету: {number_of_books}")
