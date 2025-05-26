import time

print("Stopwatch started. Press Ctrl+C to stop.")
start = time.time()
try:
    while True:
        print(f"\rElapsed Time: {int(time.time() - start)}s", end='')
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped.")
