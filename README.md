# Python Task Manager CLI

A simple command-line task manager built with Python. This project demonstrates object-oriented programming (OOP), command-line argument parsing with `argparse`, and modular Python application design.

## Features

The Task Manager CLI allows users to:

- Add a task to a user
- Mark an existing task as complete
- Receive confirmation messages after successful actions
- Receive helpful error messages when a user or task cannot be found

## Technologies

- Python 3.12
- `argparse`
- Pipenv
- Pytest

## Project Structure

```text
.
├── lib/
│   ├── cli_tool.py
│   └── models.py
├── testing/
│   └── test_cli_tool.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

### `models.py`

Contains the application's object-oriented models:

- `Task` represents an individual task and tracks its completion status.
- `User` represents a user and stores their associated tasks.

### `cli_tool.py`

Contains the command-line interface. It uses Python's `argparse` module to process commands and route them to the appropriate functions.

## Installation

### 1. Clone the Repository

```bash
git clone <repo-url>
cd <repository-name>
```

### 2. Install Dependencies

This project uses Python 3.12 and Pipenv.

Verify that Python 3.12 is installed:

```bash
python3.12 --version
```

Install the project dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

Verify the Python version inside the environment:

```bash
python --version
```

## Usage

Run the CLI from the project root using Python's module syntax.

### Add a Task

```bash
python -m lib.cli_tool add-task Alice "Submit report"
```

Example output:

```text
📌 Task 'Submit report' added to Alice.
```

### Complete a Task

The `complete-task` command accepts a username and task title:

```bash
python -m lib.cli_tool complete-task Alice "Submit report"
```

When the requested user and task exist in the current application state, the task is marked as complete:

```text
✅ Task 'Submit report' completed.
```

If the task cannot be found:

```text
❌ Task not found.
```

If the user cannot be found:

```text
❌ User not found.
```

## Data Persistence

Users and tasks are stored in memory while the Python process is running.

The application does not currently use a database or file-based storage. As a result, data does not persist between separate CLI processes.

## Testing

Run the test suite from the project root with:

```bash
pytest
```

The tests verify CLI behavior including adding tasks and completing tasks.

## Object-Oriented Design

The project separates task-management behavior from command-line handling.

### Task

Each `Task` stores:

- A title
- A completion status

New tasks begin with a completion status of `False`. Calling the task's `complete()` method changes its status to `True`.

### User

Each `User` stores:

- A name
- A list of tasks

Users can add tasks and search their task list by title.

## CLI Design

The CLI uses `argparse` subparsers to provide separate commands for different actions:

- `add-task`
- `complete-task`

Each command accepts a user and task title as positional arguments. The appropriate command function is then selected and executed based on the provided subcommand.

## Screenshot

The screenshot below shows the completed project and successful test results.

![Test Suite Passed](/screenshots/screenshot.png)

## Author

Created by Matthew Swanberg as part of  Course 7 Module 7 (Building a Python Command-Line Interface Tool)