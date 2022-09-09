from time import time
from aim_model import AimModel
from screen_recorder import WindowCapture
import cv2
#
WindowCapture.list_window_names()



net = AimModel("best", confThreshold=0.5, nmsThreshold=0.6)
wincap = WindowCapture("Film e TV")
loop_time = time()

while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    net.detect(screenshot)

    # cv2.imshow("game", screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    cv2.waitKey(1)

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break