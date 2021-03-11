def tp_checker(dictionary):
    people = dictionary["people"]
    number_of_rolls = dictionary["tp"]
    avg_use = 57
    
    total_sheets = number_of_rolls * 500
    daily_use = people * 57
    days = total_sheets // daily_use
    print("Your TP will only last " + str(days) + " days, buy more!" if days < 14 else "Your TP will last " + str(days) + " days, no need to panic!" )

tp_checker({ "people": 4, "tp": 1 })
tp_checker({ "people": 3, "tp": 20 })
tp_checker({ "people": 4, "tp": 12 })