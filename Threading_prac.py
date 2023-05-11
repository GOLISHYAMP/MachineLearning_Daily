import threading
import time
# @classmethod/
def add(a,b):
    print(a+b)
    time.sleep(5)
    print("lagged")

class A:
    @classmethod
    def divide(cl,a,b):
        print(a/b)
    

if __name__ == "__main__":
    print("in main")
    A.divide(40,50)
    print("HELLO")
    thread = threading.Thread(name="Addfunc",target=add(40,50))
    thread.run()
    