import cv2
from segment_anything import build_sam, SamAutomaticMaskGenerator
from PIL import Image, ImageDraw
import clip
import torch
import numpy as np


def add_RGB_segment(result, segmentation_mask, annotation):
    result[segmentation_mask] = annotation[segmentation_mask]

import os
import glob


def update_patch(mask_generator, image, annotation, result, device):
    masks = mask_generator.generate(image)

    for mask in masks:
        mask["segmentation"] = torch.tensor(mask["segmentation"]).to(device)
        add_RGB_segment(result, mask["segmentation"], annotation)

def run(process_id, image_path, segpath, mask_generator, device):
    print(device)
    image = Image.open(image_path)
    image = np.array(image)
    if len(image.shape) == 2:
        image = np.stack([image] * 3, axis=2)

    file_name = os.path.basename(image_path)
    print(process_id, file_name)

    annotation = Image.open(os.path.join(segpath, file_name))
    annotation = np.array(annotation)
    annotation = torch.tensor(annotation).to(device)
    # display(annotation)

    result = torch.zeros_like(annotation).to(device)
    
    step = 800
    for h_start in range(0, image.shape[0], step):
        for w_start in range(0, image.shape[1], step):
            h_end = np.min([h_start+step, image.shape[0]])
            w_end = np.min([w_start+step, image.shape[1]])
            # print(h_start, h_end, w_start, w_end)
            update_patch(mask_generator, image[h_start:h_end, w_start:w_end], 
                         annotation[h_start:h_end, w_start:w_end], result[h_start:h_end, w_start:w_end], device)
    if not os.path.exists(segpath+'_fixed'):
        os.mkdir(segpath+'_fixed')
    Image.fromarray(result.cpu().numpy()).save(os.path.join(segpath+'_fixed', file_name))

def run_list(process_id, image_path_list, segpath, device):
    # x = torch.zeros((50000,)).to(device)
    # print(process_id + x)
    
    sam = build_sam(checkpoint="sam_vit_h_4b8939.pth")
    mask_generator = SamAutomaticMaskGenerator(sam.to(device))

    for image_path in image_path_list:
        run(process_id, image_path, segpath, mask_generator, device)

from torch import multiprocessing

if __name__ == "__main__":
    
    img_dir = 'isaid_segm/val/images/images'
    image_path_list = glob.glob(os.path.join(img_dir, '*.png'))
    segpath = "farsegResultWithThreshold=0.5"

    gpu_num = 8

    new_image_path_list = np.array_split(np.array(image_path_list), gpu_num)

    multiprocessing.set_start_method('spawn')
    e = multiprocessing.Event()
    workers = [multiprocessing.Process(
                        target=run_list,
                        args=(i, new_image_path_list[i], segpath, torch.device("cuda:"+str(i))))
                    for i in range(gpu_num)]

    for worker in workers:
        worker.start()
