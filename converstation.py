def conversation():
    whichabranchustuding="iot\n"
    whereustudy="ongole\n"
    distance="10.5 km\n"
    totalfees="40000 rupees\n"
    print( whichabranchustuding,whereustudy,distance,totalfees)
    branchs=["cse","it","iot","ece","aids","aiml"]
    branchs.append("eee")
    print(branchs)
    passmarks = 75
    if passmarks == 75:
        print("you will get job")
    elif passmarks > 75:
        print("not job")
    else:
        print("try again")
    ramu = 60000
    somu =50000
    if ramu > somu:
        print("richkid")
    else:
        print("poor")
    tab = 22
    for i in range(1 ,11):
        print(tab ,"x", i, "=", tab*i)
    number = 1

    while number <= 50:
        print(number)
        number = number * 5
    s = "humen"
    for i in s:
        print(i)
    games = ["vollyball","batmention","tennis","cricket",]
    index = games.index("tennis")
    print(index)
    w = (1,2,3,4,5,6,7,8)
    p = (7,4,5,6,7,8,9)
    if p == w:
        print("same numbers")
    elif w > p:
        print("one num is less")
    else:
        print("not same")
    ac = 60000
    discount = ac*20/100
    print(discount)
    if ac > 20000:
        print("i will buy")
    elif ac < 50000:
        print("not buy")
    
    a = int(input())
    b = int(input())
    c = a*b
    print(c)
    
conversation()
