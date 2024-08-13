<h1 align="left">Ship Landmark: An Informative Ship Image Annotation and Its Applications <a href="https://ieeexplore.ieee.org/abstract/document/10550071"><img src="https://upload.wikimedia.org/wikipedia/commons/2/21/IEEE_logo.svg" alt="IEEE Logo" width="50"></a> </h1>

## Introduction
By summarizing the locations of such areas in ships, we define 20 ship landmarks and build the Ship Landmark Dataset (SLAD), the first ship dataset with landmark annotations. We also provide a benchmark for ship landmark detection by evaluating state-of-the-art landmark detection methods on the newly built SLAD. This repository provides the source code for our research on structure-based ship perception, including the vanilla ship recognition, keypoint-aware ship recognition, structure-to-texture ship generation, etc. 

## Code Overview
The structure of the repository is as follows：

* ./data: Dataset annotation and associated scripts and image storage locations.
* ./configs: Parameter configuration module.
* ./model: Our main model with all its building blocks.
* ./utils: Utility functions for training, inference, and postprocessing.
* ./scripts: Scripts related to model training, inference, image and code download, visualization.
* ./visualization: CAM image visualization and experimental performance saving.

## Implementation
**Environment installation**
```shell
conda create -n ships_class python==3.6
conda activate ships_class
pip install -r requirements.txt
```

**Data preparation**

To download and retrieve images from the annotation files in /data/anno/, please use the following command. Before executing the script, kindly sign the AgreementForSLAD.docx file located in /data/ and send it to info@vsislab.com via email. We will proceed with the image download once we receive and confirm your signed agreement. If you encounter difficulties or come across missing data, please inform us of the file names so we can assist you promptly.
```shell
sh ./scripts/data_preparation_class.sh
sh ./scripts/data_preparation.sh
```


**Training recognition Networks**

* Train networks using the vanilla ship images.

```shell
sh ./scripts/train_resnet_vallinia.sh
```

* Train networks using keypoint-aware ship images.

```shell
sh ./scripts/train_resnet_add.sh
```
* CAM image visualization
If further exploration of the CAM image is required, the raw data is stored in *.npy.
```shell
sh ./scripts/cam_download.sh
sh ./scripts/cam_vallina_resnet.sh
sh ./scripts/cam_add_resnet.sh
```

**Structure-to-Texture Generation Network**
For generating network selection, we used [CycleGAN and pix2pix in PyTorch](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix "CycleGAN and pix2pix in PyTorch"), without any additional modifications, and completed the experiments using only paired ship structure-texture images as data.

* Data preparation and training
```shell
sh ./scripts/gan_download.sh
```

* Test with test dataset
```shell
python test.py --dataroot ./datasets/ships --name ships_pix2pix --model pix2pix --direction BtoA --num_test 1000 --epoch 200
```

* Test with multi-view structural images generated from 3D data
```shell
python test.py --dataroot ./datasets/multi_view_ships --name ships_pix2pix --model pix2pix --direction BtoA --num_test 114 --epoch 200
```

## Contact
If you have any questions about the code and data, please contact.
email (info@vsislab.com)
For SLAD, please refer to:
```
@article{zhang2024ship,
  title={Ship Landmark: An Informative Ship Image Annotation and Its Applications},
  author={Zhang, Mingxin and Zhang, Qian and Song, Ran and Rosin, Paul L and Zhang, Wei},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2024},
  publisher={IEEE}
}
```
