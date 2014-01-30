import sys
import timeit
import cv2.cv as cv
import cv2
import numpy as np
import urllib
import networktables

#Yonatan Oren

def OpenCV():
    cv2.namedWindow('image')
    #cv2.createTrackbar('OFF','image',0,100,nothing)
    #cv2.createTrackbar('H','image',0,180,nothing)

    #networktables stuff

    networktables.set_client()
    networktables.set_IP('10.1.92.2')
    t = networktables.ITable(networktables.NT.GetTable('vision'))

    while(1):
        

        stream=urllib.urlopen('http://192.168.1.46/axis-cgi/jpg/image.cgi')
        bytes=''
        while True:
            bytes+=stream.read(16384)
            a = bytes.find('\xff\xd8')
            b = bytes.find('\xff\xd9')
            if a!=-1 and b!=-1:
                break
                # jpg = bytes[a:b+2]
                # bytes= bytes[b+2:]
                # i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
                # cv2.imshow('i',i)
                # if cv2.waitKey(1) ==27:
                #     exit(0)   

        #capture = cv2.VideoCapture("rtsp://root:root@http://192.168.1.46/axis-cgi/jpg/image.cgi")#"rtsp://root:root@192.168.1.46/axis-media/media.amp?videocodec=h264")

        #Read the frames
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        frame = img



        
    
        #Smooth it
        frame = cv2.blur(frame,(3,3))
    
        #Convert to hsv and find range of colors
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        H = cv2.getTrackbarPos('H','image')
        OFF = cv2.getTrackbarPos('OFF','image')

        green_lower=np.array([85,40,40],np.uint8)   #BEST: H:95 OFF: ~10
        green_upper=np.array([100,255,255],np.uint8)

        thresh = cv2.inRange(hsv,green_lower, green_upper) #217, 190, 182

            
        #Find contours in the threshold image
        contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

        
        #Finding contour with maximum area and store it as best_cnt
     
        max_area = 0
        if(contours.__len__() > 0):

            #sort contours
            contours_sorted = sorted(contours, key=lambda k: cv2.contourArea(k), reverse=True)[:3]
            contours_sortedXCentroid = sorted(filter(lambda x: validRectangle(x) ,contours_sorted), key=lambda k:int(cv2.moments(k)['m10']/cv2.moments(k)['m00']))
            

            if(contours_sortedXCentroid.__len__() == 3):
                #check which zone is hot
                #LEFT: -_ _ : 0y != 1y && 1y == 2y
                #RIGHT: _ _ - : 0y == 1y && 1y != 2y
                OFFSET = 10
                contours_centroids_y = map(lambda x: int(cv2.moments(x)['m01']/cv2.moments(x)['m00']), contours_sortedXCentroid)
                


                if(contours_centroids_y[0] + OFFSET < contours_centroids_y[1] and contours_centroids_y[1] - OFFSET <= contours_centroids_y[2] <= contours_centroids_y[1] + OFFSET):
                    print "LEFT HOT"
                    updateTableValues(t,True,'left')
                elif(contours_centroids_y[1] + OFFSET < contours_centroids_y[2] and contours_centroids_y[0] - OFFSET <= contours_centroids_y[1] <= contours_centroids_y[0] + OFFSET):
                    print "RIGHT HOT"
                    updateTableValues(t,True,'right')


            else:
                print "move the camera around"
                updateTableValues(t,False,False)
            




            #Finding centroids of top 2 
            for cnt in contours_sortedXCentroid:
                M = cv2.moments(cnt)
                
                    
                #compute centroids
                if(M['m00'] > 0):
                    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
                    #print "x:%s y:%s area:%s" % (cx,cy,cv2.contourArea(cnt))

                    #show rectangles
                    rect = cv2.minAreaRect(cnt)
                    box = cv2.cv.BoxPoints(rect)
                    box = np.int0(box)
                    im = cv2.drawContours(frame,[box],0,(254,100,46),2)

                    # x,y,w,h = cv2.boundingRect(cnt)
                    # rectimg = cv2.rectangle(frame,(x,y),(x+w,y+h),(254,100,46),2)


        else:
            print "nothing found"

 

        cv2.imshow('image',frame)
        cv2.imshow('thresh',thresh)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    
    cv2.destroyAllWindows()


def validRectangle(cnt):
    # if(not(4000 <= cv2.contourArea(cnt) and cv2.contourArea(cnt) <= 7000)):
    #     return False
    # if(cv2.moments(cnt)['m00'] == 0):
    #     return False

    return True
   

def updateTableValues(table, hotValue, direction):
    table['locked'] = hotValue
    table['direction'] = direction

OpenCV()