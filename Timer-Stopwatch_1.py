import time

task = None
while task != "timer" and task != "stopwatch":
    print("")
    task = input(print("If you would like a timer, enter 'timer'. If you would like a stopwatch, enter 'stopwatch'. "))


    
if task == "timer":

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
    
    while clock != -1:
        seconds = clock % 100
        minutes = int((clock - seconds)/ 100)
        print("%s:%s" % (minutes, seconds))
        clock = clock - 1
        time.sleep(1)
