import itertools
import threading
import time
import sys

# done = False
#  here is the animation

#From Stackoverflow
# def animate():
#     for c in itertools.cycle(['|', '/', '-', '\\']):
#         if done:
#             break
#         sys.stdout.write('\rloading ' + c)
#         sys.stdout.flush()
#         time.sleep(0.1)
#     sys.stdout.write('\rDone!     ')


# t = threading.Thread(target=animate)
# t.start()

# # long process here
# time.sleep(10)
# done = True

print("Loading:")

# animation = ["1%", "2%", "3%", "40%",
#              "50%", "64%", "70%", "80%", "99%", "100%"]
animation = [".", "..", "...", "....", ".....",
             "......", ".......", "........", ".........", ".........."]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n") #Can be skipped
