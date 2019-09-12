def bonus(GPA):
    bonus = 500000
    total = GPA * bonus
    return total

listGPA = [3, 2.7, 2.5, 4]
for GPA in listGPA :
    if GPA > 3 :
        print ("Selamat anda mendapatkan bonus", bonus(GPA))
    else :
        print ("Maaf anda tidak mendapatkan bonus") 