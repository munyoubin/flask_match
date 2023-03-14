import ho_test1
import ho_crop

path = input('img path : ')

ho_test1.make_nukki(path)
ho_crop.make_crop(path+'/output')

