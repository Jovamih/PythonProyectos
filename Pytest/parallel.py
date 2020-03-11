# /usr/bin7env python3
import threading

def counter(count):
    
    for l in range(count):
        print(str(l)+' ->Name :{} ID: {}'.format(threading.current_thread().getName(),threading.current_thread().ident))
    print('{} terminado'.format(threading.current_thread().getName()))

if __name__=="__main__":
    thread= threading.Thread(target=counter,name='Thread(1)',args=(12,))
    thread2=threading.Thread(target=counter,name='Thread(2)',args=(13,))
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()
    print('Software principal')
    