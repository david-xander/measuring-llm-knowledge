FROM python:3.11-slim

# No Java needed — ANTLR parsers are pre-compiled to Python .py files.
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /artifact

# Install dependencies before copying the full project (layer cache).
COPY requirements-docker.txt .
RUN pip install --no-cache-dir -r requirements-docker.txt

# Copy the full project (includes pre-populated datasets/hf_cache).
COPY . .

# HuggingFace offline mode — datasets/hf_cache is bundled; no network calls.
ENV HF_DATASETS_OFFLINE=1
ENV TRANSFORMERS_OFFLINE=1

# analysis/ and results/ are written at runtime — mount them as volumes
# so the host can access notebooks and CSVs after the run.
VOLUME ["/artifact/results", "/artifact/analysis"]

ENTRYPOINT ["python", "experiment/main.py"]
# Default: full run over all languages.
CMD ["--language", "ALL"]