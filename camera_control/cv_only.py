import cv2
import cProfile
import keyboard

cap = cv2.VideoCapture(0)
armed = False


def cycle(frame):
    armed = False
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Convert into grayscale
    # Detect faces
    cv2.imwrite("frame.jpg", frame)  # save frame as JPEG file
    img = cv2.imread('frame.jpg')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # center_x = (left + right) // 2
    # center_y = (top + bottom) // 2
    # converted_frame = cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
    # Display the resulting frame
    height = frame.shape[0]
    width = frame.shape[1]
    screen_center_x = int(width / 2)
    screen_center_y = int(height / 2)
    # box_center_x = int((left + right) / 2)
    # box_center_y = int((top + bottom) / 2)
    # vector_x = screen_center_x - box_center_x
    # vector_y = screen_center_y - box_center_y
    # x_adjust = screen_center_x - box_center_x
    # y_adjust = screen_center_y - box_center_y
    # print(x_adjust, y_adjust)
    # distance = ((screen_center_x - box_center_x) ** 2 + (screen_center_y - box_center_y) ** 2) ** 0.5
    # print(distance)
    # if distance <= 15:
    #     armed = True

    if armed:
        pass
        # cv2.line(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # cv2.line(frame, (left, bottom), (right, top), (0, 0, 255), 2)
        # cv2.line(frame, (box_center_x, top), (box_center_x, bottom), (0, 0, 255), 3)
        # cv2.line(frame, (left, box_center_y), (right, box_center_y), (0, 0, 255), 3)
        # cv2.line(frame, (box_center_x, box_center_y), (screen_center_x, screen_center_y), (0, 0, 255), 2)
        # cv2.imshow('frame', converted_frame)
    else:
        cv2.imshow('frame', img)


def main():

    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    for i in range(60):
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cycle(frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


cProfile.run('main()')
