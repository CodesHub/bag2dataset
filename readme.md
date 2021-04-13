# ros制作TUM数据集
1. `record2bag.sh` 录制bag
2. `python2 ./bag2dataset.py` 提取bag为图片序列（需要修改源码里文件位置，话题名）
3. `python3 ./TUM提取文件名.py` 提取图片为rgb.txt depth.txt （需要修改源码里文件位置）
4. `python associate.py ./rgb.txt ./depth.txt > associate.txt`
