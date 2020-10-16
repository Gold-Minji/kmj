import PIL.Image as pilimg

data = 'jeju_summer.jpg'


# 이미지 열기
image = pilimg.open(data)

# 이미지 크기 출력: (1440, 810): image.size
print(image.size)

# 이미지 포맷 출력 - JPEG image.format
print(image.format)

# 이미지 모드 출력 - RGB image.mode
print(image.mode)


# 이미지 보이기
image.show()


# PNG 이미지로 저장
image.save('jeju_summer.png')


# 이미지 크기 변경해보기 image.resize
out = image.resize((128,128))
out.show()

# 이미지 회전 하기 image.rotate
out = image.rotate(45)
out.show()

