Only support to predict, training is coming soon!

**step1, install the requirements:
pip install openmim
mim install mmcv-full
mim install mmcls
mim install mmdet

**step2, download the pretrained model weight, place it to ./assets/pretrained/:
wget https://download.openmmlab.com/mmfewshot/detection/attention_rpn/coco/attention-rpn_r50_c4_4xb2_coco_base-training_20211102_003348-da28cdfd.pth \
    -P assets/pretrained

**step3, run the follow command, the "-s" is a image to be detected, and the "support-images-dir" is your template images dir:
tepe predict -t configs/samples/attention_rpn.py \
    -s ./test_data/test.png \
    -w ./assets/pretrained/attention-rpn_r50_c4_4xb2_coco_base-training_20211102_003348-da28cdfd.pth  \
    support-images-dir ./test_data/support
