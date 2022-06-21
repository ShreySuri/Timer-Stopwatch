import time

def time_to_sec(x):
    a = x % 100
    b = int((x - a)/100)
    sec = 60 * b + a
    return(sec)

def base_of_first_num(base, num_orginal):
    parts_list = []
    append_count = 0
    new_num = 0

    while num_original != 0:
        place_val = 0
        while base ** place_val <= num_original:
            place_val = place_val + 1
        place_val = place_val - 1

        part = base ** place_val
        parts_list.append(part)
        append_count = append_count + 1
        num_original = num_original - part

    for i in range (0, append_count):
        log_num = parts_list[i]
        log_val = math.log(log_num, base)
        new_num = new_num + 10 ** log_val
        new_num = int(new_num)
        
    return(new_num)




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

        clock = time_to_sec(clock)

       
        while clock > 0:

            print(base_of_first_num(base, clock))
            clock = clock - 1

            
        print("Time's Up!")

else:

    condition = True
    seconds = 1
    minutes = 0

    while condition == True:
        if seconds < 10:
            print("%s:0%s" % (minutes, seconds))
        else:
            print("%s:%s" % (minutes, seconds))

        seconds = seconds + 1

        if seconds == 60:
            minutes = minutes + 1
            seconds = 0
        else:
            seconds = seconds + 0

        time.sleep(1)
