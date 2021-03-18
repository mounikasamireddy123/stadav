import calendar

for month in range(7,10):
    year = 2018
    cal = calendar.monthcalendar(year, month)
    first_week = cal[0]
    second_week = cal[1]
    third_week = cal[2]
    fourth_week = cal[3]
    fifth_week = cal[4]

    if first_week[calendar.SATURDAY]:
        holi_day = fourth_week[calendar.SATURDAY]
    else:
        holi_day = fifth_week[calendar.SATURDAY]

    day1 = first_week[calendar.SATURDAY]
    day2 = second_week[calendar.SATURDAY]
    day3 = third_week[calendar.SATURDAY]
    day4 = fourth_week[calendar.SATURDAY]
    day5 = fifth_week[calendar.SATURDAY]

    if (day1 != 0 and day1%5 == 0):
        print(year,month,day1)
    elif (day2 != 0 and day2%5 == 0):
        print(year,month,day2)
    elif (day3 != 0 and day3%5 == 0):
        print(year,month,day3)
    elif (day4 != 0 and day4%5 == 0 and day4 != holi_day):
        print(year, month, day4)
    elif (day5 != 0 and day5%5 == 0 and day5 != holi_day):
        print(year,month,day5)

    if(holi_day%5 != 0):
        print(year,month,holi_day)