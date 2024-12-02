import cv2
import os
import time
import hand as htm



cap = cv2.VideoCapture(0)

FolderPath = "hinh"
lst = os.listdir(FolderPath)
#print(lst)
lst_2=[]
for i in lst:
    # print(i)
    image=cv2.imread((f"{FolderPath}/{i}"))
    print(f'{FolderPath}/{i}')
    lst_2.append(image)
# print(len(lst_2))
pTime =0
# print(lst_2[0].shape)
# print(lst_2[1].shape)
# print(lst_2[2].shape)
# print(lst_2[3].shape)
# print(lst_2[4].shape)
# print(lst_2[5].shape)
# print(lst_2[6].shape)
# print(lst_2[7].shape)
# print(lst_2[8].shape)
# print(lst_2[9].shape)
# print(lst_2[10].shape)
# print(lst_2[11].shape)
# print(lst_2[12].shape)
# print(lst_2[13].shape)
# print(lst_2[14].shape)
# print(lst_2[15].shape)
# print(lst_2[16].shape)
# print(lst_2[17].shape)
# print(lst_2[18].shape)
# print(lst_2[19].shape)
# print(lst_2[20].shape)
# print(lst_2[21].shape)
# print(lst_2[22].shape)
# print(lst_2[23].shape)
# print(lst_2[24].shape)
# print(lst_2[25].shape)
# print(lst_2[26].shape)

detector = htm.handDetector(detectionCon=0.5) #Phát hiện bên file hand

fingerid = [4,8,12,16,20]
while True:
    ret, frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False) #phát hiện vị trí
    # print(lmList)


    if len(lmList)!= 0:
        fingers = []
        # viet cho ngon cai
        if lmList[5][1] < lmList[17][1]:  # Điểm mốc số 5 nằm bên trái điểm mốc số 17
            hand = "Left"  # Tay trái
        else:
            hand = "Right"  # Tay phải

            # Xử lý ngón cái
        if hand == "Left":
            if lmList[fingerid[0]][1] < lmList[fingerid[0] - 1][1]:  # So sánh trục X
                fingers.append(1)
            else:
                fingers.append(0)
        else:  # Tay phải
            if lmList[fingerid[0]][1] > lmList[fingerid[0] - 1][1]:  # Ngược lại so sánh trục X
                fingers.append(1)
            else:
                fingers.append(0)

        # Viet cho ngon dai
        for id in range(1,5):
            # print(id)
            if lmList[fingerid[id]][2] < lmList[fingerid[id]-2][2]: #so hai la theo so 2 cua lmlist
                fingers.append(1)
                # print(lmList[fingerid[id]][2])
                # print(lmList[fingerid[id]-2][2])
            else:
                fingers.append(0)


        print(fingers)
        songontay = fingers.count(1)
        # print(songontay)

        h, w, c = lst_2[songontay-1].shape  # cao rộng kênh/ height wide channel
        frame[0:h, 0:w] = lst_2[songontay-1]

        # ve hinh chu nhat hien so ngon tay
        cv2.rectangle(frame,(0,200),(150,400),(0,255,0),-1)
        cv2.putText(frame, str(songontay),(30,390),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),5)







    #show ra FPS
    cTime = time.time() #trả về số giây, tính tù 0:00:00  ngày 1/1/1970 theo giờ utc
    fps = 1/(cTime-pTime)
    pTime = cTime

    #show trên màn hình
    # cv2.putText(frame, f'FPS: {int(fps)}', (150, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)

    cv2.imshow("hoc lap trinh", frame)
    if cv2.waitKey(1) == ord('q'): #Độ trễ 1/1000s
        break

cap.release() #giải phóng cammera
cv2.destroyAllWindows() #giải phóng tất cả cửa sổ