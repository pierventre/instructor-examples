# Instructor Examples

## Overview

This repository contains a couple of examples done using [Instructor library](https://github.com/jxnl/instructor/). The project contains
Makefile and targets to run locally the examples on your machine by using [LocalAI](https://localai.io/).

## Get Started

Instructions on how to install and run the examples

### Dependencies

Firstly, please verify that all dependencies have been installed.

```bash
# Return errors if any dependency is missing
make venv_inst
```

This make target will create a venv and install all the deps to run the examples.

### Start, Stop, Logs, Status of LocalAI

You can start a LocalAI process using the following targets

```bash
# Run local-ai process
make local-ai-start
```

```bash
# Stop local-ai process
make local-ai-stop
```

```bash
# Get logs of local-ai process
make local-ai-logs
```

```bash
# Return status of local-ai process
make local-ai-status
```

### Run the examples

Use the following target to run all the examples

```bash
# Run the examples
make run-examples
```
