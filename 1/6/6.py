import sched
import datetime
import time


def cuckoo():
    now = datetime.datetime.now()

    for i in range(1, now.hour + 1):
        print("Ку")


scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(0, 0, cuckoo)
scheduler.run()


while True:
    scheduler.run(blocking=False)
    time.sleep(1)
