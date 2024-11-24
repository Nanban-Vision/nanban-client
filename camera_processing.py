import cv2

image_filename = os.path.join(current_directory, "captured_image.jpg")

def capture_surroundings():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(image_filename, frame)
        print(f"Image saved to {image_filename}")
    else:
        print("Failed to capture image")
    cap.release()

    return image_filename
