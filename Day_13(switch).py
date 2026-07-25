# Match-case statement (switch) :  An alternative to using many 'elif' statemnt
#                                 executed if value match the case

def day_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3 :
            return  "Tuesday"
        case 4 :
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Not a valid day"

choose=(input("Choose a day number (1-7): "))
print(day_week(choose))        