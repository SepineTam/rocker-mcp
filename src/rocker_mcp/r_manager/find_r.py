#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : find_r.py

import os
from dataclasses import dataclass
from typing import Literal


@dataclass
class RLib:
    r: str = os.getenv("R", "/usr/bin/R")
    rscript: str = os.getenv("RSCRIPT", "/usr/bin/Rscript")


class FindR:
    def __init__(
        self,
        start_by: Literal["docker"] = "docker"
    ):
        self.start_by = start_by

        self.r_lib = self.find_r()

    def find_r(self):
        if self.start_by == "docker":
            return RLib()
        else:
            print("[Warning] R-MCP is not supported on your platform.")
            return RLib()

    @property
    def RScript(self) -> str:
        return self.r_lib.rscript
