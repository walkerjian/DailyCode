import threading

class Job:
    def __init__(self, action, delay):
        self.action = action
        self.delay = delay

def execute_job(job):
    job.action()

class JobScheduler:
    def schedule(self, job):
        timer = threading.Timer(job.delay / 1000.0, execute_job, [job])
        timer.start()

def test_scheduler():
    scheduler = JobScheduler()

    test_cases = [
        Job(action=lambda: print("Job 1 executed!"), delay=1000),
        Job(action=lambda: print("Job 2 executed!"), delay=2000),
        # ... Add more test cases as required
    ]

    for job in test_cases:
        scheduler.schedule(job)

    # Wait for a while to allow all jobs to complete.
    import time
    time.sleep(10)

test_scheduler()
