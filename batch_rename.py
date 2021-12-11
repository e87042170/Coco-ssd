import os

def batch_rename(path):
    count = 0
    for fname in os.listdir(path):
        new_fname = "image{}{}".format(str(count),".jpg")
        print(os.path.join(path, fname))
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        count = count + 1  

batch_rename("\\\\10.7.103.199\\Web\\169151_web\\coco-ssd\\images-1")   