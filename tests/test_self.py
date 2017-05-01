import ast
import glob
import os
import unittest

import astunparse

import gast


class SelfTestCase(unittest.TestCase):

    def setUp(self):
        self.srcs = glob.glob(os.path.join(gast.__path__[0], '*.py'))

    def testParse(self):
        for src_py in self.srcs:
            with open(src_py) as f:
                content = f.read()
            gast.parse(content)

    def testCompile(self):
        for src_py in ['/home/travis/build/pbrunet/gast/gast/ast2.py']:#self.srcs:
            with open(src_py) as f:
                content = f.read()
            gnode = gast.parse(content)
            print(content, src_py)
            n = gast.gast_to_ast(gnode)
            for l in n.body:
                print(ast.dump(l))
                compile(ast.Module(body=[l]), src_py, 'exec')
            compile(n, src_py, 'exec')

    def test_unparse(self):
        for src_py in self.srcs:
            with open(src_py) as f:
                content = f.read()
            gnode = gast.parse(content)
            astunparse.unparse(gast.gast_to_ast(gnode))


if __name__ == '__main__':
    unittest.main()
