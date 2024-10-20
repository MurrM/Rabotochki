volume=1.44
pages=100
lines=50
symbols=25
place=4

book = pages * lines * symbols
place_for_book = book * place
volume_2 = volume * (1024**2)

quantity = volume_2/place_for_book
print("Количество книг, помещающихся на дискету:", round(quantity))
