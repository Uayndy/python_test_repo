from datetime import datetime as dt
def what_time():
    print(dt.now())

def till_midnight():
    midnight = dt.now()
    midnight.minutes = 59
    midnight.hour = 23
    print(midnight - dt.now())


print("Привет, мир!")

a, b = 0, 0
while b < 15:
    print(b + 1)

what_time()
till_midnight()