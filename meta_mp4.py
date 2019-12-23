import cv2

vcap = cv2.VideoCapture('episodio-1.mp4')

if vcap.isOpened():

    fps = vcap.get(cv2.CAP_PROP_FPS)  #taxa de fps
    frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT) #numero de frames
    duration = int(round(frame_count/fps,0)) #arredonda conta 

    h = int(duration / 3600)
    m = int(duration % 3600 / 60)
    s = int(duration % 3600 % 60)

    if h > 0:
        if h <=9:
            h = '0' + str(h)
        print('Duração: '+str(h)+':'+str(m)+':'+str(s)) #HH:MM:SS
    else:
        if m <=9:
            m = str('0'+str(m))
        if s <=9:
            s = '0'+str(s)

        print('Duração: '+str(m)+':'+str(s)) #MM:SS

    print('Qualidade: '+str(vcap.get(4))[:-2]+'p') # vcap.get(4) referente à CAP_PROP_FRAME_HEIGHT
else:
    print(':( arquivo não encontrado!')
    
vcap.release()