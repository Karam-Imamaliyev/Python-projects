oyun_sahesi = [

    ["___","___","___"],
    ["___","___","___"],
    ["___","___","___"]

]

sira = 0

while True:
    sira +=1
    for i in oyun_sahesi:
        print(*i)
    if sira % 2 == 0 :
        simvol = "X".center(3)
    else:
        simvol = "O".center(3)

    print ("Oyun sırası: ", simvol )

    x = input ("Soldan sağa (1,2,3): ")

    try:
        x = int(x)
    except ValueError:
        print ("Səhv yazdınız, növbənizi itirdiniz")
        continue
    if x > 3 or x < 1 :
        print ("Səhv yazdınız, növbənizi itirdiniz")
        continue

    y = input ("Yuxardan aşağıya (1,2,3): ")

    try:
        y = int(y)
    except ValueError:
        print("Səhv yazdınız, növbənizi itirdiniz")
        continue
    if y > 3 or y < 1 :
        print("Səhv yazdınız, növbənizi itirdiniz")
        continue

    x -= 1
    y -= 1

    oyun_sahesi[x][y] = simvol