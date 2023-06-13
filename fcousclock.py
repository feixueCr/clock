import time

def focus_timer():
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("Current Time: {}".format(current_time))
        time.sleep(60)
        
focus_timer()
