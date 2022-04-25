Question_3="Write a program that asks the user for a number of seconds and"\
    "prints out how many minutes and seconds that is."\
        "For instance, 200 seconds is 3 minutes and 20 seconds."
        
print(Question_3,"\n")


Time = int(input("Enter the time in seconds: "))
print("")

Sec_minute = 60

print("Minutes =", Time//Sec_minute)

print("Seconds =", Time % Sec_minute)

print("Time in minutes and seconds is ",Time//Sec_minute,"minutes and",Time % Sec_minute,"seconds")


