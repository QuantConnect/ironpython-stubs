from unittest import TestCase
from stubsGenerator import generator
from stubsGenerator import pasta2 as pasta
import os
path = r"C:\Projects\QuantConnect\JoeYuZhou\ironpython-stubs\release\stubs\QuantConnect"


class Test(TestCase):
    def test_generate(self):
        generator.generate(path, keep_partial=False, partition=True, size_limit=1048576)
        self.assertTrue(True)


class Test(TestCase):
    def test_partition_file(self):
        file_path = r"C:\Projects\QuantConnect\JoeYuZhou\ironpython-stubs\release\stubs\QuantConnect\Data\Consolidators.py"
        filename, file_extension = os.path.splitext(file_path)
        with open(file_path, "r") as f:
            file_content = f.read()

        tree_original = pasta.parse(file_content)
        generator.partition_file(tree_original, "Consolidators", file_extension,file_path, 10000, True)
        self.assertTrue(True)
