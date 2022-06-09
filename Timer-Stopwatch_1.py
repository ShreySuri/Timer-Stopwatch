import time

def time_to_sec(x):
    a = sec % 100
    b = int((x - a)/100)
    sec = 60 * b + a
    return(sec)



task = None
while task != "timer" and task != "stopwatch":
    print("")
    task = input(print("If you would like a timer, enter 'timer'. If you would like a stopwatch, enter 'stopwatch'. "))


    
if task == "timer":


    base = 0.5
    while base < 1 or base > 9 or base % 1 != 0:
        print("")
        base = input(print("Enter which base you would like your timer in (2 - 9). If you would like a regular timer, type '1'. "))
        base = float(base)
    base = int(base)

    if base == 1:
        clock = 0.5
        while clock % 1 != 0:
            print("")
            clock = input(print("Type the time as an integer, disregarding the colon. If you are confused about the format, type 'example'. "))
            if clock == "example":
                print("0:32 --> 32")
                print("1:28 --> 128")
                print("2:56 --> 256")
                print("5:12 --> 512")
                print("10:24 --> 1024")
                print("")
                print("Reload the program and enter a time. ")
            else:
                clock = int(clock)


        interval = input(print("Enter an interval. If you are confused as to what this means, type 'example' ."))
        if interval == "example":
            print("1/100 second --> 0.01")
            print("1/10 second --> 0.1")
            print("1 second --> 1")
            print("Please reload the application and try again.")
        else:
            interval = float(interval)
            interval = 100 * interval
            interval = int(interval)
            interval = interval / 100

        end = False
    
        while clock > 0 and end == False:
            seconds = clock % 100
            seconds = 100 * seconds
            seconds = int(seconds)
            seconds = seconds / 100
            minutes = int((clock - seconds)/ 100)
            if seconds > 9:
                print("%s:%s" % (minutes, seconds))
            else:
                print("%s:0%s" % (minutes, seconds))
            if seconds == 0:
                clock = clock - 40 - interval
            else:
                clock = clock - interval
            time.sleep(interval)
        print("Time's Up!")

    else:
        clock = 0.5
        while clock % 1 != 0:
            print("")
            clock = input(print("Type the time as an integer, disregarding the colon. If you are confused about the format, type 'example'. "))
            if clock == "example":
                print("0:32 --> 32")
                print("1:28 --> 128")
                print("2:56 --> 256")
                print("5:12 --> 512")
                print("10:24 --> 1024")
                print("")
                print("Reload the program and enter a time. ")
            else:
                clock = int(clock)
    

