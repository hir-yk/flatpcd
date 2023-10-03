import argparse

## コマンドライン引数の定義
parser = argparse.ArgumentParser()
parser.add_argument('--origin_x', type=int, default=0, help='x coordinate of the origin in meters (default: 0)')
parser.add_argument('--origin_y', type=int, default=0, help='y coordinate of the origin in meters (default: 0)')
parser.add_argument('--range_x', type=int, default=100, help='Range x in meters (default: 100)')
parser.add_argument('--range_y', type=int, default=100, help='Range y in meters (default: 100)')
parser.add_argument('--interval', type=float, default=1, help='Interval between points in meters (default: 1)')
args = parser.parse_args()

## settings
OUTFILE = 'testfile.pcd'
origin_x = args.origin_x * 1000 # Convert to millimeters
origin_y = args.origin_y * 1000
range_x = args.range_x * 1000
range_y = args.range_y * 1000
interval = args.interval * 1000

n_points = (range_x/interval)*(range_y/interval)
n_points_str = str(int(n_points)) 

## header strings
head_1="""# .PCD v0.7 - Point Cloud Data file format
VERSION 0.7
FIELDS x y z intensity
SIZE 4 4 4 4
TYPE F F F F
COUNT 1 1 1 1
WIDTH """

head_2="""
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS """

head_3="""
DATA ascii
"""

head=head_1+n_points_str+head_2+n_points_str+head_3


f = open(OUTFILE, 'w')
f.write(head)

# 使用するrange関数を整数用から浮動小数点数用のnumpy.arangeへ変更し、ステップ数をintervalに設定
import numpy as np
for x in np.arange(origin_x, origin_x + range_x, interval):
    for y in np.arange(origin_y, origin_y + range_y, interval):
        print(x / 1000, y / 1000, 0, 20)
        f.write(' '.join(map(str, [x / 1000, y / 1000, 0, 20])) + '\n')

f.close()
