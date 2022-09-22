#hi guys!

import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

#cut in proportion an image
image = cv2.resize(image,(int(image.shape[1] / 4), int(image.shape[0] / 4)))

def check_folder(relative_path):
    """
    check_folder : check and if not create the path for the results

    :param relative_path:path to be checked


    :return nothing:
    """

    workingDir = os.getcwd()
    path = workingDir + relative_path

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        logging1.info("The new directory is created! %s", str(path))
    else:
        logging1.info("directory ok:%s", str(path))

