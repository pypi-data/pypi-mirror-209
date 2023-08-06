#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# File: platforms.py
# Author: Brandon Alba <brandonealba@protonmail.com>
# License: Published under MIT license.
# =============================================================================
'''
Provides class definitions for pre-defined platforms, incl. default compiler
flags, compiler command info, etc.
'''

# =============================================================================
# IMPORTS
# =============================================================================

# =============================================================================
# GLOBAL VARIABLES
# =============================================================================

class platform_gcc_base:

    _cmd_prefix = ''
    
    _common_flags = []

    _cc_flags_base = []
    _cpp_flags_base = []
    _ld_flags_base = []

    def __init__ ( self ):
        self._cc_cmd = self._cmd_prefix + 'gcc'
        self._cpp_cmd = self._cmd_prefix + 'g++'
        self._asm_cmd = self._cmd_prefix + 'gcc'
        self._objcopy_cmd = self._cmd_prefix + 'objcopy'
    
    def cc_flags ( self )->list:
        return self._common_flags + self._cc_flags_base

    def cpp_flags ( self )->list:
        return self._common_flags + self._cpp_flags_base
    
    def ld_flags ( self )->list:
        return self._common_flags + self._ld_flags_base

    def add_cc_flags ( self, flags:list ):
        self._cc_flags_base += flags
    
    def add_cpp_flags ( self, flags:list ):
        self._cpp_flags_base += flags

    def add_ld_flags ( self, flags:list ):
        self._ld_flags_base += flags

    def cc ( self ):
        return self._cc_cmd
    
    def cpp ( self ):
        return self._cpp_cmd

    def asm ( self ):
        return self._asm_cmd

    def objcopy ( self ):
        return self._objcopy_cmd

    def common_flags ( self ):
        return self._common_flags

class platform_x86 ( platform_gcc_base ):

    def __init__ ( self ):
        super().__init__()

        self._cc_flags_base = [] 
        self._cpp_flags_base =  [] 
        self._ld_flags_base = []

class cortex_m ( platform_gcc_base ):
    '''
    Class definition for a Cortex-M platform target.
    '''

    _cmd_prefix = 'arm-none-eabi-'

    def __init__ ( self, cpu:str, linkscript:str, fpu:str='', float_abi:str='' ):
        super().__init__()
        self._asm_cmd += ' -x assembler-with-cpp'
        self._linkscript_path = linkscript

        self._CPU = cpu
        self._FPU = fpu
        self._FLOAT_ABI = float_abi

        self._cpp_flags_base = ['-W', '-Wall', '-Wextra', '-Wshadow',
                '-Wdouble-promotion', '-Wformat=2', '-Wundef']
        self._cc_flags_base = self._cpp_flags_base + ['--std=gnu11']

        self._ld_flags_base =  [
            '-lc',
            '-lm',
            '-lnosys',
            f'-Wl,-T{linkscript}',
            '-Wl,--print-memory-usage',
            '-Wl,--gc-sections']

        self._common_flags = [f'-mcpu=cortex-{self._CPU}',
                '-mthumb',
                '--specs=nano.specs',
                '-funsigned-char', # char is always unsigned
                '-ffunction-sections',
                '-fdata-sections',
                '-fdiagnostics-color=always']

        if self._FPU != '':
            self._common_flags += [f'-mfpu={self._FPU}']
        if self._FLOAT_ABI != '':
            self._common_flags += [f'-mfloat-abi={self._FLOAT_ABI}']

    def linkscript ( self ):
        return self._linkscript_path
