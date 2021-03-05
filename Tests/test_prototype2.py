from proprepros.test.prototype2 import process_file, process_string
import unittest
import os

test1_c = """
#include <stdio.h>

/** 
def _range(a):
    return ", ".join([str(i) for i in range(a)])
**/

int main(){
    int a[] = {/*(_range(10))*/};
    return 0;
}
"""
test1_output1 = """
#include <stdio.h>



int main(){
    int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    return 0;
}
"""
test1_output2 = """
#include <stdio.h>

/** 
def _range(a):
    return ", ".join([str(i) for i in range(a)])
**/

int main(){
    int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    return 0;
}
"""
test1_output3 = """
#include <stdio.h>



int main(){
    int a[] = {/*(_range(10))*/0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    return 0;
}
"""

test_path = "proprepros/test/files/test.c"


class TestProtoType2(unittest.TestCase):
    output_path = None

    def setUp(self):
        with open(test_path, "w+") as file:
            file.write(test1_c)

    def tearDown(self):
        if self.output_path is not None:
            os.remove(self.output_path)

    def test_process_file(self):
        self.output_path = test_path + ".c"
        process_file(test_path, self.output_path)

        with open(self.output_path, "r") as file:
            # print(repr(file.read()))
            self.assertEqual(file.read(), test1_output1)

    def test_process_str_replace_eval(self):
        rv = process_string(test1_c, replace_eval=True, replace_exec=False)
        self.assertEqual(rv, test1_output2)

    def test_process_str_replace_exec(self):
        rv = process_string(test1_c, replace_eval=False, replace_exec=True)
        self.assertEqual(rv, test1_output3)
