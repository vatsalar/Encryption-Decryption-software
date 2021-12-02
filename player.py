from Crypto.Cipher import AES
import hashlib
import os

import cv2
import numpy as np



def decryption():
    password = b'mypassword'
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = 'This is an IV456'

    cipher = AES.new(key,mode,IV)

    with open('encrypted_file2','rb' ) as e:
        encrypted_file = e.read()
			
    decrypted_file = cipher.decrypt(encrypted_file)

    with open('decrypted_video_test1', 'wb') as df:
        df.write(decrypted_file.rstrip(b'0'))
    
    src='decrypted_video_test1'
    dst='decrypted_video_test1.mp4'
    
    os.rename(src,dst)
    
    return dst



def Video():
    

    path=decryption()
    cap = cv2.VideoCapture(path)

    if (cap.isOpened()== False): 
      print("Error opening video  file")

    while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
            cv2.imshow('Frame', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

      else:
        break

    cap.release()  

    cv2.destroyAllWindows()

    os.remove(path)
  
	