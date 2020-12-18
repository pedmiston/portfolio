from extensions import celery
import datetime


@celery.task
def celery_delay_method():
    f = open("tmp.txt", "a")
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    f.write("%s" % now)
    f.close()
    print("now", now)
    return 0
