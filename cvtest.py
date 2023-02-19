import cv2


class memegen:
    def __init__(self, image, serial, model):
        image = 'qr.png'
        img = cv2.imread(image)

        height, width, depth = img.shape
        desired_height = 256
        aspect_ratio = desired_height/width
        dimention = (desired_height, int(height*aspect_ratio))
        img_resized = cv2.resize(img, dimention)
        

        BLACK = (85, 54, 124)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_size = 0.5
        font_color = BLACK
        font_thickness = 2
        
        print(len(serial))

        x,y = 10, 250
        img_text = cv2.putText(img_resized, serial, (x,y), font, font_size, font_color, 1, cv2.LINE_AA)
        img_text = cv2.putText(img_resized, model, (x+len(serial)*11,y), font, font_size, font_color, font_thickness, cv2.LINE_AA)

        
        cv2.waitKey(0)

        saveData = "created_labels/"+serial+".png"
        print(saveData)
        cv2.imwrite(saveData, img_text)