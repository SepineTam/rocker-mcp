# rocker-mcp
Run a R script in docker for AI. 

[![Publish to PyPI](https://github.com/SepineTam/rocker-mcp/actions/workflows/release-pypi.yml/badge.svg)](https://github.com/SepineTam/rocker-mcp/actions/workflows/release-pypi.yml)
[![Build and Push Docker Images](https://github.com/SepineTam/rocker-mcp/actions/workflows/release-docker.yml/badge.svg)](https://github.com/SepineTam/rocker-mcp/actions/workflows/release-docker.yml)
[![PyPI version](https://img.shields.io/pypi/v/rocker-mcp.svg)](https://pypi.org/project/rocker-mcp/)
[![License: AGPL 3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](LICENSE)
[![Issue](https://img.shields.io/badge/Issue-report-green.svg)](https://github.com/SepineTam/rocker-mcp/issues/new)

## Quickly Start
Start R-docker MCP in your Claude Code:
```json
{
  "mcpServers": {
    "rocker-mcp": {
      "command": "docker",
      "args": [
        "run", 
        "-it", 
        "--rm", 
        "--mount", 
        "type=bind,src=$(PWD),dst=$(PWD)",
        "--mount",
        "type=volume,src=r_lib,dst=/usr/local/lib/R/site-library",
        "-w",
        "$(PWD)",
        "ghcr.io/sepinetam/rocker-mcp:latest"
      ]
    }
  }
}
```
