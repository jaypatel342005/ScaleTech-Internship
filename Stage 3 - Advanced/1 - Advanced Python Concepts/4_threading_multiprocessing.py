import threading
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# I/O-bound  → threading or asyncio
# CPU-bound  → multiprocessing (bypasses GIL using separate processes)
# Windows: all worker functions must be at module level so spawned processes can find them


# ---- worker functions ----

def download(name, delay):
    print(f"[thread] {name} started")
    time.sleep(delay)
    print(f"[thread] {name} done")


counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        counter += 1   # not thread-safe - race condition possible


def safe_increment(n):
    global counter
    for _ in range(n):
        with lock:     # only one thread runs this at a time
            counter += 1


def fetch(url):
    time.sleep(0.5)
    return f"response from {url}"


def background_monitor():
    while True:
        print("[monitor] checking...")
        time.sleep(1)


def cpu_task(name, n):
    result = sum(i ** 2 for i in range(n))
    print(f"[process] {name} done, result={result}")


def square(n):
    return n ** 2


def heavy_compute(n):
    return sum(i ** 3 for i in range(n))


def producer(queue, items):
    for item in items:
        print(f"[producer] sending {item}")
        queue.put(item)
    queue.put(None)   # None signals the consumer to stop


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"[consumer] received {item}")


def io_task(n):
    time.sleep(0.5)
    return n * 2


def cpu_heavy(n):
    return sum(i ** 2 for i in range(n))


# ---- main ----

if __name__ == "__main__":

    # sequential vs threaded - I/O bound
    start = time.time()
    download("file1", 2)
    download("file2", 2)
    print(f"sequential: {time.time() - start:.2f}s\n")   # ~4s

    start = time.time()
    t1 = threading.Thread(target=download, args=("file1", 2))
    t2 = threading.Thread(target=download, args=("file2", 2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"threaded: {time.time() - start:.2f}s\n")   # ~2s


    # race condition - threads writing the same variable without a lock
    counter = 0
    threads = [threading.Thread(target=increment, args=(10000,)) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("counter (no lock):", counter)   # may be less than 50000


    # Lock fixes the race condition
    counter = 0
    threads = [threading.Thread(target=safe_increment, args=(10000,)) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("counter (with lock):", counter)   # always 50000


    # daemon thread - killed automatically when main program exits
    monitor = threading.Thread(target=background_monitor, daemon=True)
    monitor.start()
    time.sleep(2.5)
    print("main program done - daemon thread stops automatically")


    # ThreadPoolExecutor - simpler way to manage multiple threads
    urls = [f"https://api.example.com/item/{i}" for i in range(6)]
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fetch, urls))
    for r in results:
        print(r)


    # multiprocessing - each process runs on its own CPU core
    start = time.time()
    cpu_task("task1", 1_000_000)
    cpu_task("task2", 1_000_000)
    print(f"sequential CPU: {time.time() - start:.2f}s\n")

    start = time.time()
    p1 = multiprocessing.Process(target=cpu_task, args=("task1", 1_000_000))
    p2 = multiprocessing.Process(target=cpu_task, args=("task2", 1_000_000))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"multiprocessing CPU: {time.time() - start:.2f}s\n")


    # Pool.map - distribute a list of inputs across multiple processes
    numbers = list(range(10))
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    print("squared:", results)


    # ProcessPoolExecutor - modern equivalent of Pool
    inputs = [500_000, 600_000, 700_000, 400_000]
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(heavy_compute, inputs))
    print("computed:", results)


    # Queue - pass data between processes (they don't share memory)
    q = multiprocessing.Queue()
    prod = multiprocessing.Process(target=producer, args=(q, [1, 2, 3, 4, 5]))
    cons = multiprocessing.Process(target=consumer, args=(q,))
    prod.start()
    cons.start()
    prod.join()
    cons.join()


    # benchmark: threading vs multiprocessing
    numbers = list(range(8))

    start = time.time()
    with ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(io_task, numbers))
    print(f"threading I/O:       {time.time() - start:.2f}s")

    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as ex:
        list(ex.map(io_task, numbers))
    print(f"multiprocessing I/O: {time.time() - start:.2f}s")

    inputs = [500_000] * 8

    start = time.time()
    with ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(cpu_heavy, inputs))
    print(f"threading CPU:       {time.time() - start:.2f}s")

    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as ex:
        list(ex.map(cpu_heavy, inputs))
    print(f"multiprocessing CPU: {time.time() - start:.2f}s")

    print("""
    | Use Case          | Best Choice      |
    |-------------------|------------------|
    | API requests      | asyncio / thread |
    | File I/O          | asyncio / thread |
    | DB queries        | asyncio / thread |
    | Image processing  | multiprocessing  |
    | ML preprocessing  | multiprocessing  |
    | Math calculations | multiprocessing  |
    | Background tasks  | threading        |
    """)
