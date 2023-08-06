import cv2
class SensorBar:
    """class to manage sensors"""
    show=1
    last_key=-1
    trail_flag=0
    font = cv2.FONT_HERSHEY_SIMPLE
    selected_sensor=0
    sensor_count=0
    sensor_description=[]
    sensor_key=[]
    
    @staticmethod
    def showpannel(frame,image):
        """
        SensorBar Bar GUI
        
        Parameters:
        frame (Mat): simulator frame
        image (Mat): blank HelpBar frame
        """
        
        cv2.putText(img=image,text="SensorBar",org=(10, 20),fontFace=SensorBar.font,fontScale=1,color=(9,0,0),thickness=2)#pylint: disable= E1101
        if SensorBar.sensor_count>0:
            for i in range(SensorBar.sensor_count+1):
                cv2.rectangle(img=image,pt1=(10,30+i*40),pt2=(40,60+i*40),color=(0,0,0),thickness=3)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_key[i],org=(20,50+i*40),fontFace=SensorBar.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_description[i],org=(50,50+i*40),fontFace=SensorBar.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        elif SensorBar.sensor_count==0:
                cv2.rectangle(img=image,pt1=(10,30),pt2=(40,60),color=(0,0,0),thickness=3)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_key[0],org=(20,50),fontFace=SensorBar.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
                cv2.putText(img=image,text=SensorBar.sensor_description[0],org=(50,50),fontFace=SensorBar.font,fontScale=0.5,color=(0,0,0),thickness=2)#pylint: disable=E1101
        frame=cv2.hconcat([image,frame])#pylint: disable=E1101
        return frame