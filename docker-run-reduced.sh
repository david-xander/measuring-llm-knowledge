#!/usr/bin/env bash
set -e
mkdir -p results analysis
docker run --rm \
    -v "$(pwd)/results:/artifact/results" \
    -v "$(pwd)/analysis:/artifact/analysis" \
    sle2026-artifact \
    --language ocl