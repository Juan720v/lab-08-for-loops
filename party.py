partyCountDown = input("How long until the party starts? ")
partyCountDown = int(partyCountDown)

if partyCountDown < 1:
    print("PARTY NOW!")
else:
    for i in range(partyCountDown, 0, -1):
        print(i)
        if i == 1:
            print("PARTY TIME!")
            
