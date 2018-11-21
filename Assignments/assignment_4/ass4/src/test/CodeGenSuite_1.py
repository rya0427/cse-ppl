import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

procedure main();
begin
    if 1 = 2 then putInt(100);
    else if 2 = 2 then putInt(200);
    else putInt(300);
end

"""
        expect = r"""200"""
        self.assertTrue(TestCodeGen.test(input,expect,1))


"""
procedure foo(
    a, b: Integer;
    x, y: String;
    u, v: Boolean
);
var e, f: Real;
    i, j: integer;
begin

end
"""