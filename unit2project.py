#Mr. Helbig owns a pizza shop and needs a way to find the change for when people pay himself.
#You can only buy a slice and a drink at a time, multiple of types of pies, and garlicknots individually.

def equalityfunction(cashgiven):
    slice = 3
    smallpie = 10
    bigpie = 16
    drink = 1.50
    garlicknots = 3
    if cashgiven == slice:
        print("the change is 0")
    elif cashgiven == smallpie:
        print("the change is 0")
    elif cashgiven == bigpie:
        print("the change is 0")
    elif cashgiven == drink:
        print("the change is 0")
    elif cashgiven == garlicknots:
        print("the change is 0")
    equalityfunction(slice)


def changefunction(change):
    food = input("what items were purchased? only write the names of the items on the menu. Please follow restaurant ordering rules!")
    moneys = int(input("how much cash was given (in numeric dollar amount as a number only)"))
    slice = 3
    smallpie = 10
    bigpie = 16
    drink = 1.50
    garlicknots = 3
    for change in changefunction:
        if food == slice:
            print(moneys - slice)
            moneys - slice == change

        elif food == smallpie:
            print(moneys-smallpie)
            moneys - smallpie == change
        elif food == bigpie:
            print(moneys-bigpie)
            moneys - bigpie == change
        elif food == drink:
            print(moneys-drink)
            moneys - drink == change
        elif food == garlicknots:
            print(moneys - garlicknots)
            moneys - garlicknots == change
        elif food == slice and drink:
            print(moneys - slice and moneys - drink):
            moneys - slice and moneys - drink == change
        elif food == int(smallpie):
            print(moneys - int(smallpie)
            moneys - smallpie * int == change
        elif food == bigpie * int:
            print(moneys - int(bigpie))
            moneys - bigpie * int == change
