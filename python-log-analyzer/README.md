# Python SSH Failed Login Analyzer

## Overview
A beginner-friendly Python security project that reads authentication log entries and counts failed login attempts.

## Features
- Reads log entries from `auth.log`
- Detects lines containing `Failed password`
- Counts matching entries
- Handles a missing log file with a custom error message

## Technologies
- Python
- Linux authentication log concepts
- Basic log analysis

## How to Run
1. Ensure Python is installed.
2. Place `log_analyzer.py` and `auth.log` in the same directory.
3. Run:

   `python log_analyzer.py`

## Expected Output
With the supplied sample log:

`Total invalid attempts: 2`

## Limitations
- Uses sample log data, not live system monitoring.
- Detects matching text rather than confirming malicious activity.
- Does not send notifications or automatically block users.

## Future Improvements
- Add unit tests.
- Support configurable log paths.
- Report timestamps and usernames where available.

## Learning Outcome
Practiced Python variables, lists, loops, conditional statements, file handling, counters, f-strings, and exception handling.
