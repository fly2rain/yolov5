# 1. generate the train, validation and testing list
python partition_train_val_test.py \
    -src  /media \
    -dst  /media

# 2. Start to train the model
python train.py --img 640 --batch 108 --epochs 100 \
      --data logo_detection_gold_server.yaml \
      --cfg yolov5l.yaml \
      --weights "" \
      --device 0,1,2,3

python -m torch.distributed.launch --nproc_per_node 4 \
		train.py --img 640 --batch 108 --epochs 200 \
	    --data logo_detection_gold_server.yaml \
	    --cfg yolov5x.yaml \
	    --weights '' \
        --device 0,1,2,3

python -m torch.distributed.launch --nproc_per_node 4  train.py --img 640 --batch 128 --epochs 200 \
	    --data logo_detection_gold_server.yaml \
	    --cfg yolov5l.yaml \
	    --weights '' \
        --device 0,1,2,3