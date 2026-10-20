# Python Calculator — CI Pipeline

## Overview

A Python calculator that supports addition, subtraction, and multiplication of positive integers, with input validation, pytest unit tests, Docker, and GitHub Actions CI.

## Features

- Addition, subtraction, and multiplication
- Positive integer input validation
- Automated unit testing with pytest
- Dockerized test execution
- GitHub Actions CI on every push

## Prerequisites

- Python 3.x
- Docker
- Git

## Quick Start

```bash
git clone https://github.com/JACK-dev7/calculator-app.git
cd calculator-app
python -m pip install -r requirements.txt
python -m pytest -v
```

## Docker

```bash
docker build -t calculator-app .
docker run --rm calculator-app
```

## CI Pipeline

GitHub Actions automatically builds the Docker image and runs the unit tests whenever code is pushed.

[View CI Workflow](https://github.com/JACK-dev7/calculator-app/actions)

## Documentation

- [Runbook](docs/RUNBOOK.md) — Setup, execution, troubleshooting, and cleanup.
- [Architecture Diagram](docs/architecture.md) — Application and CI pipeline architecture.