#!/bin/bash

cd data
python demo.py --pth './anno/ships_keypoints_train2023.json' --save_pth './Ships_Datasets/train' & python demo.py --pth './anno/ships_keypoints_val2023.json' --save_pth './Ships_Datasets/val' & python demo.py --pth './anno/ships_keypoints_test2023.json' --save_pth './Ships_Datasets/test'
cd ..
