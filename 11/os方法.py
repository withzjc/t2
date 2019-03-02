import os
#查看当前所在路径，列举目录下所有文件
print(os.getcwd())
print(os.listdir(os.getcwd()))

print(os.path.abspath('.'))#绝对路径

print(os.path.dirname(os.getcwd()))#返回path中的文件夹部分，结果不包含\‘
#返回path中的文件名
print(os.path.basename(os.getcwd()))

#join将path进行组合，若其中有绝对路径，则之前的path将被删除

print(os.path.join())
