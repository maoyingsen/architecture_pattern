from shutil import copyfile
import os   
import hashlib

def copy(file_name, file_folder):
    name = file_name.split("/")[-1]
    copyfile(file_name, file_folder + "/" + name)

def rename(file_src, file_des):
    os.rename(file_src, file_des)

def remove(file_name):
    os.remove(file_name)

def hash_fun(file_name):
    with open(file_name, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        #print(hash)
        return hash        

def file_dict(file_folder):
    res = {}
    for root, dirs, files in os.walk(file_folder):
        for f in files:
            fullname = os.path.join(root, f)
            res[hash_fun(fullname)] = fullname
    return res

def compare(src, des):
    src_dic = file_dict(src)
    des_dic = file_dict(des)
    #print(src_dic)
    #print(des_dic)
    for s in src_dic:
        if s not in des_dic:
            copy(src_dic[s], des)
        elif des_dic[s].split('/')[-1] != src_dic[s].split('/')[-1]:
            rename(des_dic[s], src_dic[s])
    
    for d in des_dic:
        if d not in src_dic:
            remove(des_dic[d])
    
"""
compare('/Users/maoyingsen/Documents/architecture_pattern/coding/cha3/source', '/Users/maoyingsen/Documents/architecture_pattern/coding/cha3/dest')
"""