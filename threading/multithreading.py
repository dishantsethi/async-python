import threading
import time

def cal_square(arr):
    res = []
    for i in arr:
        print(f"square: {i*i}")
        res.append(i*i)
        time.sleep(2)
    print(res)

def cal_cube(arr):
    res = []
    for i in arr:
        print(f"cube: {i*i*i}")
        res.append(i*i*i)
        time.sleep(2)
    print(res)

if __name__ == "__main__":
    arr = [1,2,3,4]
    t = time.time()

    t1 = threading.Thread(target=cal_square, args=(arr,))
    t2 = threading.Thread(target=cal_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print(f"Executed in {time.time() - t} sec")
    print("Done")

# arr = [1,2,3,4]
# t = time.time()
# cal_square(arr)
# cal_cube(arr)
# print(f"{time.time() - t}")