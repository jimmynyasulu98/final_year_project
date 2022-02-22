import cv2
import time
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi',fourcc,20.0,(640,480)) 
# define a video capture object
vid = cv2.VideoCapture(0)
wait = 0 
while(True):
      
    # Capture the video frame
    # by frame
    
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('video', frame)
    out.write(frame) 
   
    
    if cv2.waitKey(1) & wait > 400:
        break
    wait += 1

# After the loop release the cap object
vid.release()
out.release()
# Destroy all the windows
cv2.destroyAllWindows()