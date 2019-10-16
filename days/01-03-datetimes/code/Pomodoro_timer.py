
from datetime import datetime
from datetime import timedelta


def start_task(task_name):
    print("The " + task_name + " started")


def pomodoro_timer():
    startTime = datetime.now()
    timer = timedelta(seconds=30)
    print("The pomodoro timer is started")
    while True:
        if datetime.now() > startTime + timer:
            print("the pomodoro is up")
            print(datetime.now())
            break
        else:
            continue
    return 1

def take_break(minutes):
    break_timer = timedelta(seconds=minutes*60)
    startTime = datetime.now()
    print("Break is started for " + str(minutes) + " minutes")
    while True:
        if datetime.now() > startTime + break_timer:
            print("the break is up")
            print(datetime.now())
            break
        else:
            continue
    return

def pomodoro_set():
    count = 0
    while count < 4:
        count += pomodoro_timer()
        print("The count is " + str(count))
        take_break(1)



if __name__ == "__main__":
    start_task("Study")
    pomodoro_set()
    take_break(2)
    pomodoro_set()
    take_break(2)