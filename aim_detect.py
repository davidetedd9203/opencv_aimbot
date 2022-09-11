from time import time
from aim_model import AimModel
from screen_recorder import WindowCapture
import cv2
#
# WindowCapture.list_window_names()
net = AimModel("cfg/custom_training/model/best", confThreshold=0.1, nmsThreshold=0.1, classes=["enemy"])
wincap = WindowCapture("Film e TV")
loop_time = time()

while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    net.detect(screenshot)

    # cv2.imshow("game", screenshot)
    # cv2.waitKey(1)
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
