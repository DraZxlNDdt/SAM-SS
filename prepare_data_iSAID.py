import zipfile
 
f = zipfile.ZipFile("/data/zxl/DataSet/iSAID/val/Images/part1.zip",'r') # 压缩文件位置
for file in f.namelist():
    f.extract(file,"./isaid_segm/val/images/")               # 解压位置
f.close()

f = zipfile.ZipFile("/data/zxl/DataSet/iSAID/val/Semantic_masks/images.zip",'r') # 压缩文件位置
for file in f.namelist():
    print(file)
    f.extract(file,"./isaid_segm/val/masks/")               # 解压位置
f.close()