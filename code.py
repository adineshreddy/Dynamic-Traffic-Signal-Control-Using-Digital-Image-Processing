import cv2
import time
def videoCapture(video):
    # capture frames from a video 
    cap = cv2.VideoCapture(video) 
  
    # Trained XML classifiers describes some features of some object we want to detect 
    car_cascade = cv2.CascadeClassifier('cars.xml') 
  
    # loop runs if capturing has been initialized.
    nd=0
    while True: 
        # reads frames from a video 
        ret, frames = cap.read() 

        if not ret:
            break
        
        # convert to gray scale of each frames 
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
      
  
        # Detects cars of different sizes in the input image 
        cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
      
        # To draw a rectangle in each cars 
        for (x,y,w,h) in cars: 
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
            nd+=1
  
        #Display frames in a window  
        cv2.imshow('video2', frames) 
        
        #Wait for Esc key to stop    
        if cv2.waitKey(33) == 27: 
            break
  
    # De-allocate any associated memory usage 
    cv2.destroyAllWindows()
    return nd//30

a=videoCapture('video1.mp4')
b=videoCapture('video2.mp4')
c=videoCapture('video3.mp4')
d=videoCapture('video4.mp4')
l=[a,b,c,d]
l1=l.copy()
l1.sort(reverse= True)

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def signal(k,t):
    for i in range(4):
        if i == k:
            prGreen('Signal at Road-{} = GREEN for {}sec'.format(i + 1, t))
        else:
            prRed('Signal at Road-{} = RED for {}sec'.format(i + 1, t))

k=l.index(l1[0])
for i in range(4):
    if i==k:
        prRed('Number of vehicles in Road-{} = {}' .format(i+1,l[i]))
    else:
        prGreen('Number of vehicles in Road-{} = {}' .format(i+1,l[i]))
print('-'*50)
t=(l1[0]/20)*10
signal(k,t)
print('-'*50)
print('After {}sec' .format(t))
print('-'*50)
k=l.index(l1[1])
t=(l1[1]/20)*10
signal(k,t)

print('-'*50)
print('After {}sec' .format(t))
print('-'*50)
k=l.index(l1[2])
t=(l1[2]/20)*10
signal(k,t)

print('-'*50)
print('After {}sec' .format(t))
print('-'*50)
k=l.index(l1[3])
t=(l1[3]/20)*10
signal(k,t)