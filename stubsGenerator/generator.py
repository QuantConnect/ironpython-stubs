from stubsGenerator import pasta2 as pasta
from stubsGenerator.pasta2 import augment
import os
# for each .py file, loop through each .py_i
# if code part not exisit, append
# dump file out

import re


def generate(rootdir, keep_partial=True, partition=True, size_limit=1048576):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension=='.py':
                file_path = os.path.join(subdir, file)
                tree_original = None
                i = 0
                partial_files=[]
                while (True):
                    dst = file_path + "_" + str(i)
                    if os.path.exists(dst):
                        partial_files.append(dst)
                        if tree_original == None:
                            with open(file_path, "r") as f:
                                file_content = f.read()
                            tree_original = pasta.parse(file_content)
                            lst_tree_original = [pasta.dump(f) for f in tree_original.body]
                        i += 1
                        with open(dst, "r") as f:
                            tree = pasta.parse(f.read())
                        for node in tree.body:
                            if pasta.dump(node) not in lst_tree_original:
                                tree_original.body.append(node)
                    else:
                        break
                # found parts, or partition, rewrite file if file too big
                if i > 0:
                    has_partial = True
                else:
                    has_partial = False
                if partition:
                    partition_file(tree_original, filename, file_extension, file_path, size_limit, has_partial)
                elif has_partial:
                    new_code = pasta.dump(tree_original)
                    with open(file_path, "w") as f:
                        f.write(new_code)
                # delete partial files
                if not keep_partial:
                    for partial in partial_files:
                        os.remove(partial)

def partition_file(tree_original,filename, file_extension,file_path, size_limit, has_partial):
    file_size = 0
    partition = pasta.parse("", "")
    i = 0
    for node in tree_original.body:
        partition.body.append(node)
        file_size += len(pasta.dump(node).encode('utf-8'))
        if file_size > size_limit:
            i += 1
            file_path = os.path.join(os.path.dirname(file_path), filename + "_" + str(i) + file_extension)
            augment.add_import(partition, filename + "_" + str(i))
            with open(file_path, "w") as f:
                f.write(pasta.dump(partition))
    # has partition need to be write to include them
    if (i > 0 and file_size > 0) or has_partial:
        with open(file_path, "w") as f:
            f.write(pasta.dump(partition))


