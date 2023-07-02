import os
import subprocess
import shutil
from shutil import copytree, ignore_patterns


root_dir = 'data/MSTAR_PUBLIC_TARGETS_CHIPS_T72_BMP2_BTR70_SLICY/TARGETS/'
mstar2jpg_path = 'data/MSTAR_PUBLIC_TARGETS_CHIPS_T72_BMP2_BTR70_SLICY/tools/mstar2jpg.exe'
dest_dir = 'data/converted_data_set'


if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)
    
# 仅复制目录结构，忽略所有文件
copytree(root_dir, dest_dir, ignore=ignore_patterns('*.*'))  

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        input_file = os.path.join(dirpath, filename)
        relative_path = os.path.relpath(dirpath, root_dir) 
        output_file = os.path.join(dest_dir, relative_path, filename + '.jpg')
        cmd = [mstar2jpg_path, '-i', input_file, '-o', output_file, '-q', '95', '-v', '-e']
        
        subprocess.run(cmd, check=True)
