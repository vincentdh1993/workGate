import numpy as np
import cv2
import torch
from facenet_pytorch import MTCNN, InceptionResnetV1
from tkinter import *
import threading
import PIL.Image, PIL.ImageTk
import pygame  # For playing sounds
import time  # To keep track of time

# Initialize MTCNN and InceptionResnetV1
mtcnn = MTCNN()
resnet = InceptionResnetV1(pretrained='vggface2').eval()

# Load known face embeddings and labels
known_face_embeddings = np.load('known_face_embeddings.npy')
known_face_labels = np.load('known_face_labels.npy')


def get_face_embedding(image):
    """Detect face in an image and return its embedding and bounding box"""
    boxes, probs = mtcnn.detect(image)
    if not np.any(boxes):
        return None, None

    box = boxes[0].astype(int)
    face = mtcnn.extract(image, torch.Tensor([box]), None)
    if face is not None:
        embedding = resnet(face.unsqueeze(0))
        return embedding, box
    else:
        return None, None

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.ok = True  # Flag to control the loop in video streaming thread
        self.cap = cv2.VideoCapture(video_source)
        self.last_sound_play_time = 0  # Keep track of when the sound was last played
        self.han_detection_counter = 0  # Counter for consecutive detections of Han

        # Canvas for video streaming
        self.canvas = Canvas(window, width=800, height=600)
        self.canvas.pack()

        # Console Box
        self.console = Text(window, width=80, height=20)
        self.console.pack()

        # Run the video streaming thread
        self.thread = threading.Thread(target=self.stream_video)
        self.thread.start()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.window.mainloop()

    def reset_bg(self):
        self.window.configure(background='green')

    def play_sound(self):
        pygame.mixer.music.stop()  # stop any current playing sound
        pygame.mixer.music.load('trimmed_file.mp3')  # load the sound
        pygame.mixer.music.play()  # play the sound
        timer = threading.Timer(18.0, pygame.mixer.music.stop)  # stop playing after 5 seconds
        timer.start()

    def stream_video(self):
        while self.ok:
            ret, frame = self.cap.read()
            if ret:
                embedding, box = get_face_embedding(frame)
                self.window.configure(background='green')
                if embedding is not None:
                    distances = np.linalg.norm(known_face_embeddings - embedding.detach().numpy(), axis=1)
                    threshold = 0.7
                    min_distance_index = np.argmin(distances)
                    if distances[min_distance_index] < threshold:
                        label = known_face_labels[min_distance_index]
                        if label == 'Dongho':
                            pass
                        elif label == 'Han':
                            self.console.insert(END, "Yewon is here\n")
                            self.window.configure(background='red')
                            frame = cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 2)
                            self.han_detection_counter += 1  # Increment counter for Han detection

                            if self.han_detection_counter == 3:  # Check if Han has been detected twice in a row
                                current_time = time.time()
                                if current_time - self.last_sound_play_time > 10:  # Play sound every 10 seconds
                                    self.play_sound()
                                    self.last_sound_play_time = current_time
                        else:
                            self.console.insert(END, "Face Detected\n")
                            self.han_detection_counter = 0  # Reset counter for Han detection
                    else:
                        self.console.insert(END, "Face not recognized\n")
                        self.han_detection_counter = 0  # Reset counter for Han detection

                    self.console.see(END)

                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(image))
                self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

                # Reset the background after 5 seconds
                self.window.after(5000, self.reset_bg)

        self.cap.release()

    def __del__(self):
        self.ok = False  # Stop the video streaming thread
        self.window.after(10, self.window.destroy)  # Destroy the window after 10ms


# Initialize pygame mixer
pygame.mixer.init()

# Create a window and pass it to the Application object
App(Tk(), "Face Detection")
