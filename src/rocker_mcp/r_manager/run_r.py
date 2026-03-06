#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : run_r.py

import subprocess
from pathlib import Path

from .find_r import FindR


class RunR:
    def __init__(
        self,
        r_command: str = None
    ):
        if r_command is None:
            self.RScript = FindR().RScript
        else:
            self.RScript = r_command

    def run(
        self,
        script_path: str | Path,
        work_dir: str | Path = None
    ) -> str:
        """
        Run R-script file in given directory.

        Args:
            script_path (str | Path): R-script file path
            work_dir (str | Path): working directory

        Returns:
            str: subprocess running result (if success)

        Raises:
            FileNotFoundError: If the R script file does not exist.
            RuntimeError: If the R script execution fails (non-zero exit code).
        """
        script_path = Path(script_path)
        if not script_path.exists():
            raise FileNotFoundError(
                f"R script file not found: {script_path}"
            )

        if work_dir is None:
            work_dir = script_path.parent
        else:
            work_dir = Path(work_dir)

        result = subprocess.run(
            [self.RScript, script_path],
            cwd=work_dir,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"R script failed:\n{result.stderr}"
            )

        return result.stdout

    def set_rscript(self, r_command: str) -> str:
        self.RScript = r_command
        return self.RScript
