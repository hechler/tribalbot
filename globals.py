import threading

lock = threading.RLock()
lock_main = threading.Lock()
my_threads = []