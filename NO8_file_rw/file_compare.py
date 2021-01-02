import os
import hashlib

def checkmd5(path):
    f=open(path,'rb')
    content=f.read()
    M=hashlib.md5()
    M.update(content)
    return M.hexdigest()

def find_dupliate(folder):
    # folder=input("请输入文件夹名字：")
    # folder = "/Users/zxzx/test"
    md5Lib={}
    md5toName={}
    for root,dirs,files in os.walk(folder):
        # print(root, dirs, files)
        for file in files:
            filename=os.path.join(root,file)
            tempMD5 = checkmd5(filename)
            if not tempMD5 in md5Lib.values():
                md5toName[tempMD5]=filename
                md5Lib[filename]=tempMD5
            else:
                print(filename,'  和\n',md5toName[tempMD5],'\n重复了\n', end=' ')
                os.remove(filename)
                print(filename, "删除\n\n")


if __name__ == '__main__':
    folder = "/Users/zxzx/projects/nowcoder_exp/字节跳动-实习面经"
    find_dupliate(folder)




