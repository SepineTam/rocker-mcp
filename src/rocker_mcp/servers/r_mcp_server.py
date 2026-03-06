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
    new_r_command = r_runner.set_rscript(r_command)
    return "RScript set to: " + new_r_command


@r_mcp.tool()
def run_rscript(
    script_path: str,
    work_dir: str
) -> str:
    return r_runner.run(script_path, work_dir)

