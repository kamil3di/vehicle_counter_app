import cv2

class VideoCapture:

    def __init__(self, videoId):

        self.cap = cv2.VideoCapture(videoId)
        self.frames_count, self.fps, self.width, self.height = int( self.cap.get (cv2.CAP_PROP_FRAME_COUNT)), \
                                                               int( self.cap.get (cv2.CAP_PROP_FPS)), \
                                                               int(self.cap.get (cv2.CAP_PROP_FRAME_WIDTH)), \
                                                               int(self.cap.get (cv2.CAP_PROP_FRAME_HEIGHT))

    def show_result(self):
        print(self.width, self.height, self.fps, self.frames_count)
