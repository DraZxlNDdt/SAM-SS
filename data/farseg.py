from torch.utils.data.dataset import Dataset
import glob
import os
from PIL import Image
import numpy as np

COLOR_MAP = dict({
    'background': (0, 0, 0),
    'ship': (0, 0, 63),
    'storage_tank': (0, 191, 127),
    'baseball_diamond': (0, 63, 0),
    'tennis_court': (0, 63, 127),
    'basketball_court': (0, 63, 191),
    'ground_Track_Field': (0, 63, 255),
    'bridge': (0, 127, 63),
    'large_Vehicle': (0, 127, 127),
    'small_Vehicle': (0, 0, 127),
    'helicopter': (0, 0, 191),
    'swimming_pool': (0, 0, 255),
    'roundabout': (0, 63, 63),
    'soccer_ball_field': (0, 127, 191),
    'plane': (0, 127, 255),
    'harbor': (0, 100, 155),
})


class RemoveColorMap:
    def __init__(self, color_map=COLOR_MAP):
        super(RemoveColorMap, self).__init__()
        self.colors = np.asarray(list(color_map.values()))

    def __call__(self, mask):
        if isinstance(mask, Image.Image):
            mask = np.array(mask, copy=False)
    
        gt = np.zeros(mask.shape[0:2], dtype=np.int_)
        # loop for each class
        for k, v in enumerate(self.colors):
            gt[(mask==v).all(axis=2)] = k
            
        return gt


class ImageFolderDataset(Dataset):
    def __init__(self, img_dir, mask_dir=None):
        self.fp_list = glob.glob(os.path.join(img_dir, '*.png'))
        self.img_dir = img_dir
        self.mask_dir = mask_dir
        self.rm_color = RemoveColorMap()

    def __getitem__(self, idx):
        image_np = Image.open(self.fp_list[idx])
        image_np = np.array(image_np, copy=False)
        if self.mask_dir is not None:
            mask_fp = os.path.join(self.mask_dir, os.path.basename(self.fp_list[idx]).replace('.png',
                                                                                              '_instance_color_RGB.png'))
            mask_np = Image.open(mask_fp)
            mask_np = np.array(mask_np, copy=False)
            gt_np = self.rm_color(mask_np)
        else:
            gt_np = None
        if len(image_np.shape) == 2:
            image_np = np.stack([image_np] * 3, axis=2)
            
        return image_np, gt_np, os.path.basename(self.fp_list[idx])

    def __len__(self):
        return len(self.fp_list)
