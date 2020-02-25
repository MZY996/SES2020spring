
import os

path = "C:\\Users\\Aurora\\Desktop\\readme.txt"  ## set the path here

if os.path.isfile(path):
    file = open(path, 'r')
    words_num = len(file.read().split())
    print("the number of words is {}.".format(words_num))
    file.close()

else:
    print("There is no such file!")