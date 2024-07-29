films={
    "Finding Dory":[3,5],
    "Boure":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]

}
while True:
    choice=input("what films would you like to watch?:").strip().title()
    if choice in films:
        age=int(input("How old are you?:").strip())
        if age>=films[choice][0]:#check user age
                #check the enough  seats
                num_seats=films[choice][1]
                if num_seats>0:
                    print("enjoy film")
                    films[choice][1]=films[choice][1]-1
                else:
                    print("sorry we are sold out")

        else:
            print("your are young to watch film")
    else:
        print("we don't have that film..")