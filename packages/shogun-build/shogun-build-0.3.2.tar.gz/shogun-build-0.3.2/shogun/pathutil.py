#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# File: pathutil.py
# Author: Brandon Alba <brandonealba@protonmail.com>
# License: Copyright © 2022 Brandon Alba
# =============================================================================
'''
Helpers for managing directories/paths within a project.
'''

# =============================================================================
# IMPORTS
# =============================================================================

import os
import inspect
import copy

# =============================================================================
# GLOBAL VARIABLES
# =============================================================================

# =============================================================================
# FUNCTION DEFINITIONS
# =============================================================================

def subdir ( initialdir:str ):
    '''
    Shameless copy of meson's subdir() function. Goal is to execute a script located
    in a deeper directory within a project for the purpose of appending to global
    source, include, etc. arrays.
    '''

    # when first calling subdir __caller_abspath__ is not defined.
    try:
        fdir = os.path.dirname(__caller_abspath__)
        fname = os.path.basename(__caller_abspath__)
    except:
        module = inspect.getmodule(inspect.stack()[1][0])
        fdir = os.path.dirname(module.__file__)
        fname = os.path.basename(module.__file__)
        __caller_abspath__ = copy.deepcopy(module.__file__)

    print(f'Set __caller_abspath__ to {__caller_abspath__}')

    print(f'\nCaller dir: {fdir}')
    print(f'Caller file: {fname}')

    fpath = os.path.join(fdir, initialdir, fname)
    print(fpath)
    assert(os.path.isfile(fpath))
    
    exec(open(fpath).read(), globals(), locals())
