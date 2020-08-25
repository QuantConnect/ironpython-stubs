from unittest import TestCase
from stubsGenerator import pasta2 as pasta


class Test(TestCase):
    def test_custom_sanitizer(self):
        src = """
        pass

    def Get(self, *__args):
# Error generating skeleton for function Get: Method must be called on a Type for which Type.IsGenericParameter is false.

    def GetEnumerator(self):
        """
        src = pasta.custom_sanitizer(src)
        print(src)

        self.fail()
