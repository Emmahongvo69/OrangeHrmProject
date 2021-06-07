from datetime import datetime
import time

now = datetime.now()
for x in range(0,10):
    print(int(round(time.time() * 1000)))
