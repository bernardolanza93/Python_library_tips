#hi guys!

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

image = cv2.resize(image,(int(image.shape[1] / 4), int(image.shape[0] / 4)))

