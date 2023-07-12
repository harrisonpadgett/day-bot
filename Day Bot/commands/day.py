from calendar import monthrange
from datetime import date, timedelta, datetime
import requests
import os
from pytz import timezone
import lightbulb
import hikari

 

plugin = lightbulb.Plugin('day')


aEmote = "https://cdn.discordapp.com/attachments/933832464948928532/935335267525623808/aEmote.png"
bEmote = "https://cdn.discordapp.com/attachments/933832464948928532/935335285363982386/bEmote.png"

def checkDay(givenDate):

    
    # {Day : Name of Event, 0 if event does not take up entire day, 1 if event takes up entire day}
    specialDays = {

        "9/05/2022" : ["Labor Day", 1],
        "9/26/2022" : ["a PD Day", 1],
        "10/05/2022" : ["a PD Day", 1],
        "10/21/2022" : ["a PD Day", 1],
        "10/24/2022" : ["a PD Day", 1],
        "11/04/2022" : ["First Quarter Ends - Half Day", 0],
        "11/08/2022" : ["Election Day", 1],
        "11/23/2022" : ["Elementary Schools Closed", 0],
        "11/24/2022" : ["Thanksgiving", 1],
        "11/25/2022" : ["Thanksgiving", 1],
        "12/22/2022" : ["Half Day -- Winter Break", 0],
        "12/23/2022" : ["during Winter Break", 1],
        "12/24/2022" : ["during Winter Break", 1],
        "12/25/2022" : ["during Winter Break", 1],
        "12/26/2022" : ["during Winter Break", 1],
        "12/27/2022" : ["during Winter Break", 1],
        "12/28/2022" : ["during Winter Break", 1],
        "12/29/2022" : ["during Winter Break", 1],
        "12/30/2022" : ["during Winter Break", 1],
        "12/31/2022" : ["during Winter Break", 1],
        "1/1/2023" : ["during Winter Break", 1],
        "1/2/2023" : ["during Winter Break", 1],
        "1/03/2023" : ["Schools Reopen", 0],
        "1/16/2023" : ["MLK Jr.'s Birthday", 1],
        "1/17/2023" : ["First Quarter Ends - Half Day", 0],
        "1/23/2023" : ["a PD Day", 1],
        "2/20/2023" : ["President's Day", 1],
        "3/17/2023" : ["Half Day", 0],
        "3/24/2023" : ["Half Day", 0],
        "4/1/2023" : ["during Spring Break", 1],
        "4/2/2023" : ["during Spring Break", 1],
        "4/3/2023" : ["during Spring Break", 1],
        "4/4/2023" : ["during Spring Break", 1],
        "4/5/2023" : ["during Spring Break", 1],
        "4/6/2023" : ["during Spring Break", 1],
        "4/7/2023" : ["during Spring Break", 1],
        "4/8/2023" : ["during Spring Break", 1],
        "4/9/2023" : ["during Spring Break", 1],
        "4/10/2023" : ["a State Holiday", 1],
        "4/21/2023" : ["a PD Day", 1],
        "5/29/2023" : ["Memorial Day", 1],
        "6/19/2023" : ["Juneteenth", 1],
        "6/20/2023" : ["Assessment Day - Half Day", 0],  
        "6/21/2023" : ["Assessment Day - Half Day", 0]

        }

    # Numbers correlate to the day and month of the appropriate specialDays key
    # Extra zero added if the date is next year (2023)
    specialDaysNumbers = [905, 926, 1005, 1021, 1024, 1104, 1108, 1123, 1124, 1125, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1100, 1200, 10300, 11600, 11700, 12300, 22000, 31700, 32400, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 41000, 42100, 52900, 61900, 62000, 62100]
    

    tz = timezone('EST')
    rn = datetime.now(tz)

    dayAdjust = 0
    
    startDayFull = ['9', '2', '2022'] # Testing date, is an A day. Referenced to check if it's an A or B day

    startMonth = startDayFull[0]
    startDay = startDayFull[1]



    parsedToday = givenDate.split('/')

    month = parsedToday[0]
    day = parsedToday[1]

    # Change date so that it's always two digits if not already
    if len(day) == 1:
        day = "0" + day

    year = parsedToday[2]

    if "23" in year:
        yearNumber = "00"
    else:
        yearNumber = ""

    print(f"Year Number: {yearNumber}")

    currentDayCheckNumber = str(month) + str(day) + str(yearNumber)
    currentDayCheckNumber = int(currentDayCheckNumber)
    print(f"Current Day Check Number: {currentDayCheckNumber}")

    # Check if the requested day is a weekened or known off-day
    print("Checking if the given date is special . . .")
    specialKeysList = list(specialDays.keys())
    specialCheckDate = givenDate.split('/')
    print(specialCheckDate[0][0])
    if specialCheckDate[0][0] == "0":
        specialCheckDate[0] = specialCheckDate[0][1]

    if specialCheckDate[1][0] == "0":
        specialCheckDate[1] = specialCheckDate[1][1]

    if len(specialCheckDate[2]) == 2:
        specialCheckDate[2] = "20" + str(specialCheckDate[2])

    specialCheckDate = f"{specialCheckDate[0]}/{specialCheckDate[1]}/{specialCheckDate[2]}"
    print(specialCheckDate)    

    if str(specialCheckDate) in specialKeysList and specialDays[str(specialCheckDate)][1] == 1:
        print("Given date is a special day.")

        return(f"{specialCheckDate} is {specialDays[str(specialCheckDate)][0]}. There is no school.", "", 5793266, None)

    if len(year) == 2:
        year = "20" + str(year)
    


    if datetime(int(year), int(month), int(day)).weekday() == 6:
        return(f"{givenDate} is a Sunday. There is no school.", "", 5793266, None)
    
    if datetime(int(year), int(month), int(day)).weekday() == 5:
        return(f"{givenDate} is a Saturday. There is no school.", "", 5793266, None)
    #



    daysDifference = int(day) - int(startDay)
    print(f"Days Difference: {daysDifference}")



    if int(month) != int(startMonth):
        
        if "23" in year:
            monthDifference = int(month) - int(startMonth)
            monthDifference = abs(monthDifference) + 3 # Adding 3 because September is 3 months from the next year
        else:
            monthDifference = int(month) - int(startMonth)

        print(f"Month Difference: {monthDifference}")
        for i in range(0, monthDifference):
            print(i)
            
            if i <= 3:
                dayAdjust = dayAdjust + monthrange(2022, int(i + int(startMonth)))[1] # Multiply by the number of days in each month since the start
            else:
                dayAdjust = dayAdjust + monthrange(2022, int(i))[1]

    print(f"Day Adjust: {dayAdjust}")

    for index, key in enumerate(specialDays):

        if currentDayCheckNumber >= specialDaysNumbers[index]:
            
            print(f"Value of dayAdjust before subtracting: {dayAdjust}")
            print(str(key) + " has occured. Subtracting appropriate amount from total days.")
            dayAdjust = dayAdjust - specialDays[key][1]
            print(f"Value of dayAdjust after subtracting: {dayAdjust}")
            print("")
    
    print(f"Day Adjust: {dayAdjust}")



    daysDifference = daysDifference + dayAdjust
    print(f"Days Difference: {daysDifference}")

    aDay = "{} is an A Day".format(givenDate)
    bDay = "{} is a B Day".format(givenDate)

    if (daysDifference % 2) == 0:
        final = aDay
        letter = "an A"
        color = 0xFF0000
        image = aEmote
        return(final, letter, color, image)

    else:
        final = bDay
        letter = "a B"
        color = 0x0000FF
        image = bEmote
        return(final, letter, color, image)





@plugin.command
@lightbulb.option('date', "Example: 4/14/23", type = str)
@lightbulb.command('day', "Find whether a specified date is an A day or B day.")
@lightbulb.implements(lightbulb.SlashCommand)
async def user_data(ctx):

    print(f"User has requested: {ctx.options.date}")

    date = checkDay(str(ctx.options.date))

    print(date)

    embed = (

        hikari.Embed(title = date[0], color = date[2])
        .set_image(date[3])
            
    )


    await ctx.respond(embed = embed)




def load(bot):
    bot.add_plugin(plugin)
