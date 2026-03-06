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
        r_command: str = None,
        repos: str = "https://cloud.r-project.org"
    ):
        if r_command is None:
            self.RScript = FindR().RScript
        else:
            self.RScript = r_command

        self.repos = repos

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

    def install(
        self,
        package: str,
        repos: str = None
    ) -> subprocess.CompletedProcess:
        """
        Install an R package from CRAN or specified repository.

        Args:
            package (str): Name of the R package to install.
            repos (str, optional): CRAN mirror URL. Defaults to self.repos.

        Returns:
            subprocess.CompletedProcess: Result object with returncode, stdout, stderr.
        """
        result = subprocess.run(
            [
                self.RScript,
                "-e",
                f'install.packages("{package}", repos="{repos or self.repos}")'
            ],
            capture_output=True,
            text=True
        )
        return result

    def is_package_installed(self, package: str) -> bool:
        """
        Check if an R package is installed.

        Args:
            package (str): Name of the R package to check.

        Returns:
            bool: True if the package is installed, False otherwise.

        Examples:
            >>> runner = RunR()
            >>> runner.is_package_installed("ggplot2")
            True
            >>> runner.is_package_installed("nonexistent_package")
            False
        """
        result = subprocess.run(
            [
                self.RScript,
                "-e",
                f'cat(require("{package}", character.only = TRUE, quietly = TRUE))'
            ],
            capture_output=True,
            text=True
        )
        return result.stdout.strip() == "TRUE"

    def help(self, package: str, n: str = "help"):
        pass

    def show_example(self, function: str) -> str:
        """
        Run examples for an R function.

        Args:
            function (str): Name of the R function to show examples for.

        Returns:
            str: The stdout output from running the example.

        Raises:
            RuntimeError: If the example execution fails.

        Examples:
            >>> runner = RunR()
            >>> runner.show_example("mean")
            >>> runner.show_example("ggplot2::ggplot")
        """
        result = subprocess.run(
            [
                self.RScript,
                "-e",
                f'example("{function}")'
            ],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"R example failed:\n{result.stderr}"
            )
        return result.stdout

    def set_rscript(self, r_command: str) -> str:
        self.RScript = r_command
        return self.RScript
