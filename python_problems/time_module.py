import time 
# print(time.gmtime())

# print(time.localtime())
# print(time.asctime())
# print(time.strftime("%H:%M:%S"))

def traffic_signal():
    print("Red light -Stop!")
    time.sleep(10)
    print("yellow light - Prepare to stop!")
    time.sleep(5)
    print("Green light - Go!")
    time.sleep(5)

for i in range(3):
    traffic_signal()

