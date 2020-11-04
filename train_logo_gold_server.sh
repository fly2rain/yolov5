# 1. generate the train, validation and testing list
python partition_train_val_test.py \
    -src  /media \
    -dst  /media

# 2. Start to train the model
python train.py --img 640 --batch 512 --epochs 100 \
      --data logo_detection_gold_server.yaml \
      --cfg yolov5l.yaml \
      --device 0,1,2,3