import match
import os

print("폴더 주소 입력시 해당 폴더 내 output 폴더가 자동 생성됨")
path = input("img folder:")
match.make_crop(path)
print("해당 폴더 작업 끝")
os.system('pause')