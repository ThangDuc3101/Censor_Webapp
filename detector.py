from typing import Any
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import cv2

# The CensorApp class is a Python class that uses OpenCV to detect and blur faces or hands in a video stream or in your webcam

class CensorApp():
    def __init__(self,index_capture,mode="face") -> None:
        self.capture = cv2.VideoCapture(index_capture)
        self.mode = mode
        if self.mode == "face":
            self.detector = FaceDetector()
        elif self.mode == "hand":
            self.detector = HandDetector()
        else:
            return
        
        self.capture.set(3,960)
        self.capture.set(4,480)

    def blur_object(self,img):        
        if self.mode == "face":
            img,bboxes = self.detector.findFaces(img,True)
        else:
            bboxes,img = self.detector.findHands(img,True,True)
        
        for box in bboxes:
            x,y,w,h = box['bbox']
            
            if x<0 : x==0
            if y<0 : y==0
            
            crop = img[y:y+h,x:x+w]
            blur = cv2.blur(crop,(35,35))
            
            img[y:y+h,x:x+w] = blur
        
        return img
    
    def __call__(self, *args: Any, **kwds: Any):
        while self.capture.isOpened():
            ok,frame = self.capture.read()
            
            if not ok:
                continue
            
            frame = self.blur_object(frame)
            
            # cv2.imshow("Censor",frame)
            yield frame
            
            if cv2.waitKey(10) == ord('q'):
                break
            
        self.capture.release()
        cv2.destroyAllWindows()
        return
    
if __name__=="__main__":
    censor = CensorApp(0,"hand")
    for img in censor():
        cv2.imshow("Censor",img)
        if cv2.waitKey(10) == ord('q'):
            break
    cv2.destroyAllWindows()