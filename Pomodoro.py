import time
from plyer import notification

'''
set pmodoro timer count to zero before starting the first one
'''
count = 0
print("The pomodoro timer has started, start working!")

'''
while true, the timer is on for 1800 seconds(30 minutes) and the 
count increases by one. after 30 minutes are over notify the user
and start a 10 minute counter. notify the user when 10 minutes are over.
'''
if __name__ == "__main__":
    while True:
        time.sleep(1800)
        count += 1
        notification.notify(
            title = "Great job!",
            message = "Take a 10 minute break! You have completed " + str(count) + " pomodoros so far",
        )
        time.sleep(600)
        notification.notify(
            title = "Break over, back to work",
            message = "Try doing another pomodoro",
        )
