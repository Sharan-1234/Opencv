import cv2 as cv
def resizef(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    dimen  =(width, height)
    return cv.resize(frame,dimen, interpolation = cv.INTER_AREA)

while True:
    isTrue, frame = vid.read()
    frame_resize = resizef(frame)
    # frame_res = changeres(frame)
    # cv.imshow('resc',frame_res)
    cv.imshow('vid',frame)
    cv.imshow('res',frame_resize)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
vid.release()
cv.destroyAllWindows()