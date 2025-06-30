def marriagefunction():
    whereareyougoing="wedding\n"
    howmuchdistance="5.5km\n"
    howmanymembersgoing="8 members\n"
    transportcost="200\n"
    print(whereareyougoing,howmuchdistance,howmanymembersgoing
    ,transportcost)
    names=["srikanth","silu","aunty","uncle"]
    names.append("friends")
    print(names[0])
    names=["srikanth","silu","aunty","uncle","friends"]
    print(names[4])
    meals = ["rice","sambar","card","brinjal","rasam"]
    meals1 = ["sweets"]
    if meals <= meals1:
        print("no eat meals")
    else:
        print("i eat meals")
    work=["hcl","tcs","tata","wipro",]
    print(work[1])
    work.append("capgamini")
    print(work)
    friend1_salary = 50000
    friend2_salary = 49999
    if friend1_salary < friend2_salary:
        print("meet another time")
    elif friend1_salary >= friend2_salary:
        print("meet and plan in next week")
    else:
        print("no meet")
marriagefunction()        