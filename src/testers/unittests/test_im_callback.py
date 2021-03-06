#!/usr/bin/env python
# coding: utf-8

import unittest

from triton import *


class TestInstanceMethodCallback(unittest.TestCase):

    """Testing instance method callbacks."""

    def test_get_concrete_memory_value(self):
        self.Triton = TritonContext()
        self.Triton.setArchitecture(ARCH.X86_64)

        self.flag = False
        self.Triton.addCallback(CALLBACK.GET_CONCRETE_MEMORY_VALUE, self.cb_flag)
        self.Triton.processing(Instruction(b"\x48\xa1\x00\x10\x00\x00\x00\x00\x00\x00")) # movabs rax, qword ptr [0x1000]
        self.assertTrue(self.flag)

        self.flag = False
        self.Triton.removeCallback(CALLBACK.GET_CONCRETE_MEMORY_VALUE, self.cb_flag)
        self.Triton.processing(Instruction(b"\x48\xa1\x00\x10\x00\x00\x00\x00\x00\x00")) # movabs rax, qword ptr [0x1000]
        self.assertFalse(self.flag)

    def test_get_concrete_register_value(self):
        self.Triton = TritonContext()
        self.Triton.setArchitecture(ARCH.X86_64)

        self.flag = False
        self.Triton.addCallback(CALLBACK.GET_CONCRETE_REGISTER_VALUE, self.cb_flag)
        self.Triton.processing(Instruction(b"\x48\x89\xd8")) # mov rax, rbx
        self.assertTrue(self.flag)

        self.flag = False
        self.Triton.removeCallback(CALLBACK.GET_CONCRETE_REGISTER_VALUE, self.cb_flag)
        self.Triton.processing(Instruction(b"\x48\x89\xd8")) # mov rax, rbx
        self.assertFalse(self.flag)

    def cb_flag(self, ctx, x):
        self.flag = True

