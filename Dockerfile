FROM rocker/r-ver:4.5
LABEL authors="sepinetam"

# Install uv and rocker-mcp
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY . /app
WORKDIR /app
RUN uv sync

# Install common packages
COPY packages.txt install_packages.R /tmp/
RUN Rscript /tmp/install_packages.R && rm /tmp

WORKDIR /workspace

ENTRYPOINT ["/app/.venv/bin/rocker-mcp"]
