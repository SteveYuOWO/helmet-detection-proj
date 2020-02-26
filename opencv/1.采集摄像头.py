import cv2 as cv
import datetime

def video_capture():
    num = 0
    capture = cv.VideoCapture(0)
    c = -1
    # sec按下，退出循环
    while c != 27:
        now = datetime.datetime.now().strftime("%Y-%m-%d %T")
        num += 1
        pic_path = "../camera/" + now + " " + str(num) + ".png"
        if num == 10:
            num = 0
        # 进行捕获画面，成功ret为True
        ret, frame = capture.read()
        # 镜像变化
        frame = cv.flip(frame, 1)
        # 写入camera目录
        cv.imwrite(pic_path, frame)
        # 显示窗口
        cv.imshow("video", frame)
        # 等待50ms
        c = cv.waitKey(50)


if __name__ == '__main__':
    video_capture()