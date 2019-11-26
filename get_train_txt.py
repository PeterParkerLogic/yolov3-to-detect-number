import h5py
import glob
import cv2 


train_img_list = glob.glob("train/*.png")




for idx in range(len(train_img_list)):



	file = open("PyTorch-YOLOv3/data/custom/train1.txt", 'a')
	file.writelines("data/custom/images/"+str(idx+1)+".png"+'\n')
	file.close()
	
	