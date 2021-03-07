import os
from pathlib import Path
import shutil
import hashlib

def hash_fun(file_name):
    with open(file_name, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        #print(hash)
        return hash   


def read_paths_and_hashes(dir):
    hashes = {}
    for folder, _, files in os.walk(dir):
        for fn in files:
            hashes[hash_fun(Path(folder) / fn )] = fn
    return hashes

def sync(src_dic, des_dic, src, des):
    #src_dic = file_dict(src)
    #des_dic = file_dict(des)
    res = []
    for s in src_dic:
        if s not in des_dic:
            res.append(['COPY', src + '/' + src_dic[s], des + '/' + src_dic[s]])
        elif des_dic[s] != src_dic[s]:
            res.append(['RENAME', des + '/' + des_dic[s], des + '/' + src_dic[s]])

    for d in des_dic:
        if d not in src_dic:
            res.append(['REMOVE', des + '/' + des_dic[d]])

    return res

def one(source, dest):
    source_hashes = read_paths_and_hashes(source)
    dest_hashes = read_paths_and_hashes(dest)
    #print(source_hashes)
    #print(dest_hashes)
    actions = sync(source_hashes, dest_hashes, source, dest)
    #print(actions)

    for i in actions:
        print(i)
        if i[0] == 'COPY':
            shutil.copyfile(i[1], i[2])
        if i[0] == 'RENAME':
            os.rename(i[1], i[2])
        if i[0] == 'DELETE':
            os.remove(i[1])

if __name__ == '__main__':
    one('/Users/maoyingsen/Documents/architecture_pattern/coding/cha3/source', '/Users/maoyingsen/Documents/architecture_pattern/coding/cha3/dest')