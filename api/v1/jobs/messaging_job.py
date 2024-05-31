from models.message import Message
from rq import Queue
from redis import Redis


def send_message_job(message: Message):
    """
    Send message job
    """
    try:
        redis_conn = Redis()
        q = Queue("nkhunda_message_queue", connection=redis_conn)
        job_id = f"{message.app_id}-{message.recipient_id}"
        q.enqueue("send_message", dict(message), job_id=job_id)
        return True
    except Exception as e:
        return False