import numpy as np
import os
 
img_path='/media/jinhong/数据/datasets/SELFdataset_bag/lab_static_person2'
 
#img_list=sorted(os.listdir(img_path))#文件名按字母排序
rgb_list=sorted(os.listdir(img_path+'/rgb'))
depth_list=sorted(os.listdir(img_path+'/depth'))

rgb_txt_out=[]
for i in range(len(rgb_list)):
    name,extension = os.path.splitext(rgb_list[i])
    rgb_txt_out.append(name+' rgb/'+rgb_list[i]) 
np.savetxt("rgb.txt", rgb_txt_out, delimiter=" ", newline = "\n", fmt="%s")

depth_txt_out=[]
for i in range(len(depth_list)):
    name,extension = os.path.splitext(depth_list[i])
    depth_txt_out.append(name+' depth/'+depth_list[i]) 
np.savetxt("depth.txt", depth_txt_out, delimiter=" ", newline = "\n", fmt="%s")

#rgb_list
#depth_list
