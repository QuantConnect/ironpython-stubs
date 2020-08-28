from stubsGenerator import pasta2 as pasta
from stubsGenerator.pasta2.augment import import_utils
from ast import Module
from typing import List
import ast
import os
# for each .py file, loop through each .py_i
# if code part not exisit, append
# dump file out


def generate(rootdir, keep_partial=True, partition=True, size_limit=1048576):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension != '.py':
                continue

            file_path = os.path.join(subdir, file)
            with open(file_path, "r", encoding='utf-8') as f:
                file_content = f.read()

            tree_original = pasta.parse(file_content, file_path)
            lst_tree_original = [pasta.dump(f) for f in tree_original.body]

            i = 0
            partial_files = []
            while (True):
                dst = file_path + "_" + str(i)
                if os.path.exists(dst):
                    partial_files.append(dst)
                    i += 1
                    with open(dst, "r", encoding='utf-8') as f:
                        tree = pasta.parse(f.read(), dst)

                    for node in tree.body:
                        if pasta.dump(node) not in lst_tree_original:
                            tree_original.body.append(node)
                else:
                    break
            # found parts, or partition, rewrite file if file too big
            has_partial = i > 0

            if partition:
                partition_file(tree_original, filename, file_extension, file_path, size_limit, has_partial)

            elif has_partial:
                new_code = pasta.dump(tree_original)
                with open(file_path, "w", encoding='utf-8') as f:
                    f.write(new_code)

            # delete partial files
            if not keep_partial:
                for partial in partial_files:
                    os.remove(partial)

    moved_files = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            relative_path = os.path.join(subdir, file)
            if len([i for i in files if os.path.join(subdir, i).upper() == relative_path.upper()]) > 1 and not file.startswith('__') and relative_path.upper() not in moved_files:
                # Let's pick the first element and move it into its own folder, as long as it's not a partitioned file
                # or the root of a namespace
                try:
                    # Strips .py extension with [:-3]
                    new_directory = os.path.join(subdir, file[:-3])
                    new_partial_path = os.path.join(new_directory, '__init__.py')

                    os.mkdir(new_directory)
                    os.rename(relative_path, new_partial_path)
                    moved_files.append(relative_path.upper())
                    print(f'Moved {relative_path} to {new_partial_path}')
                except Exception as e:
                    print(str(e))
                    print(f'Failed to move duplicate file to path: {os.path.join(subdir, file)}')

def partition_file(tree_original: Module, filename, file_extension, file_path, size_limit, has_partial):
    file_size = 0
    partition = pasta.parse("")
    i = 0
    imports: List[ast.Import] = []
    for node in tree_original.body:
        if isinstance(node, ast.Import):
            imports.append(node)
            continue

        partition.body.append(node)
        file_size += len(pasta.dump(node).encode('utf-8'))

        if file_size <= size_limit:
            continue

        for import_ in imports:
            partition.body.insert(0, import_)

        i += 1
        # Hides import with __
        new_filename = "__" + filename + "_" + str(i)
        import_utils.add_import(partition, "." + new_filename + ".*", from_import=True)

        with open(file_path, "w", encoding='utf-8') as f:
            f.write(pasta.dump(partition))

        file_size = 0
        file_path = os.path.join(os.path.dirname(file_path), new_filename + file_extension)
        partition = pasta.parse("")

    # has partition need to be write to include them
    if has_partial or (i > 0 and file_size > 0):
        for import_ in imports:
            partition.body.insert(0, import_)

        with open(file_path, "w", encoding='utf-8') as f:
            f.write(pasta.dump(partition))