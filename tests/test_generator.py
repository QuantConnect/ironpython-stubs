from unittest import TestCase
from stubsGenerator import generator

class Test(TestCase):
    def test_generate(self):
        rootdir = r"E:\Projects\QuantConnect\ironpython2\bin\Debug\net45\Lib\release\stubs\QuantConnect"
        generator(rootdir)
        self.fail()
