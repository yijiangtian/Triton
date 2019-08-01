#!/usr/bin/env python2
# coding: utf-8
"""Issue from Github."""

import unittest

from triton import *



class TestIssue656(unittest.TestCase):

    """Testing #656."""

    @staticmethod
    def sym_exec_gadget(gadget):
        ctx = TritonContext()
        ctx.setArchitecture(ARCH.X86_64)
        ctx.enableMode(MODE.ALIGNED_MEMORY, True)

        r = ctx.registers
        gprs = (
            r.rax, r.rbx, r.rcx, r.rdx,
            r.rsi, r.rdi, r.esp, r.ebp,
            r.r8, r.r9, r.r10, r.r11,
            r.r12, r.r13, r.r14
        )

        for gpr in gprs:
            ctx.convertRegisterToSymbolicVariable(gpr)

        for assembly in gadget:
            i = Instruction()
            i.setOpcode(assembly)
            ctx.processing(i)

        srax = ctx.getSymbolicRegister(ctx.registers.rax)

        return srax


    def test_issue(self):
        e = self.sym_exec_gadget((b'\x89\xd8', b'\xc2\x04\x00'))
        self.assertEqual(str(e), '(define-fun ref!15 () (_ BitVec 64) ((_ zero_extend 32) ((_ extract 31 0) ref!1))) ; MOV operation')
        a = e.getAst()
        self.assertEqual(str(a + 1), '(bvadd ((_ zero_extend 32) ((_ extract 31 0) ref!1)) (_ bv1 64))')
        self.assertEqual(str(1 + a), '(bvadd (_ bv1 64) ((_ zero_extend 32) ((_ extract 31 0) ref!1)))')
        self.assertEqual(str(e.getComment()), 'MOV operation')
        self.assertEqual(e.getId(), 15)
        self.assertEqual(str(e.getAst()), str(e.getNewAst()))
        self.assertEqual(str(e.getOrigin()), 'rax:64 bv[63..0]')
        self.assertEqual(e.getType(), SYMBOLIC.REGISTER_EXPRESSION)
        self.assertEqual(e.isMemory(), False)
        self.assertEqual(e.isRegister(), True)
        self.assertEqual(e.isSymbolized(), True)
        e.setComment('test')
        self.assertEqual(str(e.getComment()), 'test')
        n = e.getNewAst() + 1
        e.setAst(n)
        self.assertEqual(str(e.getAst()), str(n))



class TestIssue673(unittest.TestCase):

    """Testing #673."""

    def setUp(self):
        """Define the arch."""
        self.ctx = TritonContext()
        self.ctx.setArchitecture(ARCH.X86_64)


    def test_issue1(self):
        inst = Instruction(b"\xc0\xc0\x00") # rol al, 0
        self.ctx.processing(inst)
        self.assertEqual(len(inst.getUndefinedRegisters()), 0)
        self.assertEqual(len(inst.getReadRegisters()), 1)
        self.assertEqual(len(inst.getWrittenRegisters()), 2)


    def test_issue2(self):
        inst = Instruction(b"\xc0\xc0\x01") # rol al, 1
        self.ctx.processing(inst)
        self.assertEqual(len(inst.getUndefinedRegisters()), 0)
        self.assertEqual(len(inst.getReadRegisters()), 2)
        self.assertEqual(len(inst.getWrittenRegisters()), 4)


    def test_issue3(self):
        inst = Instruction(b"\xc0\xc0\x07") # rol al, 7
        self.ctx.processing(inst)
        self.assertEqual(len(inst.getUndefinedRegisters()), 1)
        self.assertEqual(len(inst.getReadRegisters()), 2)
        self.assertEqual(len(inst.getWrittenRegisters()), 4)



class TestIssue792(unittest.TestCase):

    """Testing #792."""

    def setUp(self):
        """Define the arch."""
        self.ctx = TritonContext()
        self.ctx.setArchitecture(ARCH.X86_64)


    def test_issue(self):
        ac = self.ctx.getAstContext()

        var1 = self.ctx.newSymbolicVariable(64, 'var1')
        var2 = self.ctx.newSymbolicVariable(64, 'var2')

        ast_original  = ac.bvadd(ac.variable(var1), ac.variable(var2))
        ast_duplicate = ac.duplicate(ast_original)
        ast_unrolled  = ac.unrollAst(ast_original)

        self.ctx.setConcreteVariableValue(var1, 4)
        self.ctx.setConcreteVariableValue(var2, 2)

        self.assertEqual(ast_original.evaluate(), 6)
        self.assertEqual(ast_duplicate.evaluate(), 6)
        self.assertEqual(ast_unrolled.evaluate(), 6)

        ast_original.setChild(0, ac.bv(1, 64))

        self.assertEqual(ast_original.evaluate(), 3)
        self.assertEqual(ast_duplicate.evaluate(), 6)
        self.assertEqual(ast_unrolled.evaluate(), 6)

        ast_duplicate.setChild(0, ac.bv(10, 64))

        self.assertEqual(ast_original.evaluate(), 3)
        self.assertEqual(ast_duplicate.evaluate(), 12)
        self.assertEqual(ast_unrolled.evaluate(), 6)



class TestIssue795(unittest.TestCase):

    """Testing #795."""

    def setUp(self):
        """Define the arch."""
        self.ctx = TritonContext()
        self.ctx.setArchitecture(ARCH.X86_64)


    def test_issue(self):
        ast = self.ctx.getAstContext()

        var1    = self.ctx.newSymbolicVariable(64, 'var1')
        var2    = self.ctx.newSymbolicVariable(64, 'var2')
        var1ast = ast.variable(var1)
        var2ast = ast.variable(var2)

        a1 = ast.bvadd(var1ast, var2ast)
        b1 = ast.bvnot(a1)
        b2 = ast.duplicate(b1)

        self.assertEqual(len(a1.getParents()), 1)
        self.assertEqual(len(b2.getParents()), 0)
        self.assertEqual(len(b2.getChildren()[0].getParents()), 1)
        self.assertEqual(len(var1ast.getParents()), 2)
        self.assertEqual(len(var2ast.getParents()), 2)

        self.assertEqual(b1.evaluate(), b2.evaluate())
        self.ctx.setConcreteVariableValue(var1, 4)
        self.ctx.setConcreteVariableValue(var2, 2)
        self.assertEqual(b1.evaluate(), b2.evaluate())
