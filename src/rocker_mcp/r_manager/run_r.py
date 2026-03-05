#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : run_r.py

from .find_r import FindR


class RunR:
    def __init__(
        self,
        r_command: str = None
    ):
        if r_command is None:
            self.RScript = FindR.RScript
        else:
            self.RScript = r_command

    def run(
        self,
        script_path: str,
        work_dir: str
    ) -> str:
        pass

    def set_rscript(self, r_command: str) -> str:
        self.RScript = r_command
        return self.RScript
