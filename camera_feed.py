import cv2

if __name__ == "__main__":

    # activate camera

    cam = cv2.VideoCapture(0)

    # create window

    cv2.namedWindow("Camera feed")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("Camera feed", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()