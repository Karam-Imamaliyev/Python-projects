def contacts():
    Namen = [ ]
    while len(Namen) < 1:
        x = input('Bitte schreiben Sie den Namen: ')
        y = input('Bitte schreiben Sie den Vornamen: ')
        z = int(input('Bitte schreiben Sie die Telefonnummer: '))
        if x == ' ' or y == ' ' or z == ' ':
            pass
            break
        else :

            print('Kontakt ist hinzugefügt wurden.')
            print(Namen)
contacts()
