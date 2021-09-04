#!/bin/bash -eu

set -o pipefail

python3 -m venv venv
. venv/bin/activate

# Lint
black apps config --check
flake8
