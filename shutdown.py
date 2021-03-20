import time, os

timeout = 60*25   # 25 minutes in seconds
timeout_start = time.time()
shutdown = False

while time.time() < timeout_start + timeout:
    if(time.time() + 5 >= timeout_start + timeout):
        shutdown = True
        print("Now going to shut down")

    # Print the remaining time to shut down
    print("I'm still " + str( (timeout_start + timeout) - (time.time() + 5) ) +
    " seconds away from shutting down.")

    # Wait for 10 seconds
    time.sleep(10)

if(shutdown == True):
    os.system('shutdown -s')
