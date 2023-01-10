## settings
OUTFILE='testfile.pcd'
range_x=100000  #[mm]
range_y=100000
interval=500

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


## create newpcd ##
f=open(OUTFILE, 'w')
f.write(head)

for x in range(0, range_x, interval):
  for y in range(0, range_y, interval):
    print(x/1000, y/1000, 0, 20)
    f.write(' '.join(map(str,[x/1000, y/1000, 0, 20]))+'\n' )

f.close()
