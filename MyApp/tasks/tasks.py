from celery import shared_task

@shared_task
def long_running_task(data):
    # Simulate a long-running task (e.g., sending emails, processing images)
    import time
    time.sleep(5)
    return f"Task completed for data: {data}"
