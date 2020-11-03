# 1. generate the train, validation and testing list
python partition_train_val_test.py \
    -src  /media/fyzhu/data2T_0/yolov3_training/forklift_model/data_20191210 \
    -dst /media/fyzhu/data2T_0/yolov3_training/forklift_model?data_20191210

# 2. Start to train the model
python train.py --img 640 --batch 16 --epochs 5 --data forklift_my_server.yaml --weights yolov5s.pt