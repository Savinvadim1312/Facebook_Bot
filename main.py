from Friend_Add import Friend_add
from queue import Queue
import threading

queue = Queue()
accaunts = []

def init():
    with open("data/accaunts.txt", "r") as file:
        for line in file:
            accaunts.append(Friend_add(line.split()[0], line.split()[1], 1))

def init_queue():
    with open("data/people_to_add.txt", "r") as file:
        for line in file:
            queue.put(line.replace('\n', ''))
    queue.join()

def create_workers():
    for accaunt in accaunts:
        t = threading.Thread(target=work, args = [accaunt])
        t.daemon = True
        t.start()

def work(accaunt):
    while True:
        url = queue.get()
        accaunt.invite_friend(url)
        queue.task_done()


init()
create_workers()
init_queue()