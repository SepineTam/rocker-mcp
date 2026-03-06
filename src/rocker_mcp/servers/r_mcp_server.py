#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : r_mcp_server.py

from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from ..r_manager import RunR

r_mcp = FastMCP(
    name="R-MCP"
)

r_runner = RunR()


@r_mcp.tool()
def set_rscript(
    r_command: str
) -> str:
    """
    Set Rscript command.

    Args:
        r_command (str): Rscript command path

    Returns:
        str: current Rscript path after setting

    Examples:
        >>> set_rscript("/usr/local/bin/Rscript")
        "RScript set to: /usr/local/bin/Rscript"
    """
    new_r_command = r_runner.set_rscript(r_command)
    return "RScript set to: " + new_r_command


@r_mcp.tool()
def run_rscript(
    script_path: str,
    work_dir: str = None
) -> str:
    """
    Execute an R script file and return its output.

    Args:
        script_path (str): Path to the R script file to execute.
        work_dir (str, optional): Working directory for execution.
            Defaults to the script's parent directory if not specified.

    Returns:
        str: The stdout output from the R script execution.

    Raises:
        FileNotFoundError: If the R script file does not exist.
        RuntimeError: If the R script execution fails.
    """
    return r_runner.run(script_path, work_dir)


@r_mcp.tool()
def install_r_package(
    package: str,
    repos: str = None
) -> Dict[str, Any]:
    """
    Install an R package from CRAN or specified repository.

    Args:
        package (str): Name of the R package to install.
        repos (str, optional): CRAN mirror URL.
            Defaults to "https://cloud.r-project.org".

    Returns:
        Dict[str, Any]: Result dictionary with keys:
            - is_error (bool): True if installation failed.
            - msg (str): stdout if success, stderr if failed.

    Examples:
        >>> install_r_package("ggplot2")
        {"is_error": False, "msg": "..."}
        >>> install_r_package("dplyr", repos="https://mirrors.tuna.tsinghua.edu.cn/CRAN/")
        {"is_error": False, "msg": "..."}
    """
    result = r_runner.install(package, repos)
    is_error = result.returncode != 0
    if is_error:
        msg = result.stderr
    else:
        msg = result.stdout
    return {
        "is_error": is_error,
        "msg": msg
    }
