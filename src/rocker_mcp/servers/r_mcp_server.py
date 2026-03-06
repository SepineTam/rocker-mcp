#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2026 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam (谭淞)
# @Email  : sepinetam@gmail.com
# @File   : r_mcp_server.py

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

