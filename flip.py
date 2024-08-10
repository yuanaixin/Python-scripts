from PIL import Image
import os
 
# 设置输入和输出目录
input_dir = '/path/to/input/directory/'
output_dir = '/path/to/output/directory/'
 
# 循环输入目录中的所有JPEG图像， 这里如果你是别的类型格式图片，直接更改点后图片类型即可
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        
        # 打开图像
        img = Image.open(os.path.join(input_dir, filename))
 
        # 水平镜像并保存
        mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        mirrored_img.save(os.path.join(output_dir, f'horiz_{filename}'))
 
        # 垂直镜像并保存
        mirrored_img = img.transpose(Image.FLIP_TOP_BOTTOM)
        mirrored_img.save(os.path.join(output_dir, f'vert_{filename}'))