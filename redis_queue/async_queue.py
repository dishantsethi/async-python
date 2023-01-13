from celery import Celery

REDIS_BASE_URL = 'redis://localhost:6379'
app = Celery(
    'runner',
    broker=f"{REDIS_BASE_URL}/0",
    backend=f"{REDIS_BASE_URL}/1"
)

app.conf.beat_schedule = {
    'print-words': {
        'task': 'runner.print_words',
        'schedule': 5.0, # Runs in every 5 seconds
    },
}

@app.task(name='print-words')
def print_words(word):
    print(word)

def main():
    l = ["Java","Python","PHP","C++"]
    for word in l:
        print_words.delay(word)


# celery -A async_queue.app worker --loglevel=INFO
# celery -A async_queue.app beat --loglevel=INFO