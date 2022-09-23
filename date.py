import datetime

# using now() to get current time


def mymain():
    current_time = datetime.datetime.now()

    # Printing attributes of now().
    MonthDict = {1: "January",
                 2: "February",
                 3: "March",
                 4: "April",
                 5: "May",
                 6: "June",
                 7: "July",
                 8: "August",
                 9: "September",
                 10: "October",
                 11: "November",
                 12: "December"
                 }

    # print("Year :", current_time.year)

    # print("Month : ", MonthDict[current_time.month])

    # print("Day : ", current_time.strftime("%A"))

    result = "Today is " + str(current_time.strftime("%A")) + " " + \
        str(MonthDict[current_time.month]) + " "+str(current_time.year)
    return result
# time = datetime.datetime.now().strftime("%I:%M %p")
# list = time.split(':')
# hours = list[0]
# secondPart = list[1]
# print(hours)
# list = secondPart.split(" ")
# minutes = list[0]
# print(minutes)
# timeAmOrPm = list[1]
# print(timeAmOrPm)
