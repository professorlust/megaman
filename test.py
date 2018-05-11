import numpy as np
from PIL import ImageGrab
import cv2
import time
from getkeys import key_check
import os
import pyautogui

# data_set = ''     # Willy Fortress 2 stage
data_set = '_mtl'   # Metalman stage

def keys_to_output(keys):
	#[Z,X,left,right,Z+left,Z+right]
    output = [0,0,0,0,0,0]
    if 'Z' in keys:
        if 'J' in keys:
            output[4] = 1
        elif 'L' in keys:
            output[5] = 1
        else:
            output[0] = 1
    elif 'X' in keys:
        output[1] = 1
    # if 'C' in keys:
    #     output[2] = 1
    elif 'J' in keys:
        output[2] = 1
    # if 'I' in keys:
    #     output[4] = 1
    elif 'L' in keys:
        output[3] = 1
    # if 'K' in keys:
    #     output[6] = 1
    if 'P' in keys:
        np.save(file_name,training_data)
        print('saved')
    print(output)
    return output
file_name ='raw_data\\trainingdata{}_.npy'.format(data_set)
if os.path.isfile(file_name):
    print ('loading')
    training_data = list(np.load(file_name))
else:
    print('creating file')
    training_data = []

def process_img(original_image):
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    # processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    keys = key_check()
    output = keys_to_output(keys)
    training_data.append([processed_img,output])
    return processed_img

# Countdown
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

last_time = time.time()
while(True):
    # 800x600
    # 40 px accounts for title bar. 
    screen = np.array(ImageGrab.grab(bbox=(0,40, 390, 350)))
    # screen = cv2.resize(screen, (390,350))
    screen = cv2.resize(screen, (195,175))
    new_screen = process_img(screen)#display processed img

    #print('jump')
    #PressKey(Z)
    #time.sleep(3)
    #print('fire')
    #PressKey(X)

    #print('loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

    cv2.imshow('window', new_screen)
    # if len(training_data) % 500 == 0 :
    #     np.save(file_name,training_data)
    #     print('saved')
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# screen_record()

#VID9 10.21