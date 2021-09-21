import cv2
import os 
source = cv2.VideoCapture('TestVideo.mp4')
if (source.isOpened == False):
    print("opening failed")
frame_array=[]
size=(int(source.get(3)),int(source.get(4)))
result = cv2.VideoWriter('random.mp4',cv2.VideoWriter_fourcc(*'XVID'),60,size,True)
while (True):
    try: 
        ret,image = source.read()
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        gray= cv2.resize(gray,size)
        frame_array.append(gray)
        gray=cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
        cv2.imshow('video',gray)
        result.write(gray)
    
        if cv2.waitKey(10)==ord("q"):
            break
    except:
        break 

c=0

cv2.destroyAllWindows()
source.release()
result.release()
os.system("ffmpeg -i TestVideo.mp4 -f mp3 -ab 192000 -vn sound.mp3")
os.system("ffmpeg -i random.mp4 -i sound.mp3 -c copy -map 0:v:0 -map 1:a:0 newvideo.mp4")
os.remove("random.mp4")
os.remove("sound.mp3")
