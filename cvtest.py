import cv2


class memegen:
    def __init__(self, image, text):
        image = 'test.png'
        img = cv2.imread(image)

        height, width, depth = img.shape
        desired_height = 512
        aspect_ratio = desired_height/width
        dimention = (desired_height, int(height*aspect_ratio))
        img_resized = cv2.resize(img, dimention)

        BLACK = (255, 255, 255)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_size = 1.1
        font_color = BLACK
        font_thickness = 2
        
        x,y = 10, 500
        img_text = cv2.putText(img_resized, text, (x,y), font, font_size, font_color, font_thickness, cv2.LINE_AA)

        
        cv2.waitKey(0)

        cv2.imwrite('static/new.png', img_text)