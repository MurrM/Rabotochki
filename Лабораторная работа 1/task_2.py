# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
pages = 100
lines = 50
symbols = 25
place = 4

book = pages * lines * symbols # количество символов в одной книге
place_for_book = book * place # размер одной книги в байтах

volume_2 = volume * (1024**2) # объем дискеты в байтах

quantity = volume_2/place_for_book
print("Количество книг, помещающихся на дискету:", round(quantity))
