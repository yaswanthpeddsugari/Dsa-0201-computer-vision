import cv2

video_path = r'C:/Users/karan/OneDrive/Desktop/OPEN CV/cv video.mp4'
speeds = {
    "Normal": 30,
    "Slow Motion": 100,
    "Fast Motion": 10
}

for title, delay in speeds.items():

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow(title, frame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
import cv2

video_path = r'C:/Users/karan/OneDrive/Desktop/OPEN CV/cv video.mp4'

modes = [
    ("Normal Speed", 30),
    ("Slow Motion", 100),
    ("Fast Motion", 1)
]

for title, delay in modes:

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break
        if title == "Fast Motion":
            cap.read()

        cv2.imshow(title, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cap.release()
    cv2.destroyAllWindows()

print("Video playback completed.")
