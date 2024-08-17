import cv2
import pytesseract

# Set the path to the Tesseract OCR executable (modify this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_text_from_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale for better OCR performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform text recognition using Tesseract
        text = pytesseract.image_to_string(gray, lang='sin')

        # Display the original frame
        cv2.imshow('Webcam', frame)

        # Display the recognized text
        print("Recognized Text:")
        print(text)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_text_from_webcam()
