# yolov3-to-detect-number
yolov3 to detect number from 0~9
 
 This program is use to detect number 0~9 in the image, and draw the bounding box in the image.
 
 The main program is too big, so you can download from here(https://drive.google.com/open?id=19T-4_GUFK65SVQfxp8n-qR55RSm1JKmQ)
 
 Frist: 
   Using get_label.py to get training data ground truth. Then it will write 'label','left','top','width','height' of the bounding box to txt for each images.
 
 Second:
   Using get_train_txt.py to write all training data names to an txt file. It let main program, train.py, easily to get all training image.
 Third:
   Using train.py to train the model.
 Forth:
   Using order_img.py to rename testing data name from 1.png to 00001.png. It can let dataloader read test image in right way.
 
 
 
 
 
 
 
 
 
 
 
 reference:https://github.com/eriklindernoren/PyTorch-YOLOv3
