# Lab 5 submission

Name: Chirra Yuktha Praneel  
SRN: PES2UG24AM049  
Class: 5th Sem AIML (A)

Assigned repository: https://github.com/SETAPESU26/L5_45_ticket_booking_system

## Contents
- ticket_booking_system.py: cleaned program
- issues.md: 18 documented issues, highest Bandit severity first
- reflection.md: four relevant reflection answers (exact questions absent from handout)
- reports/before and reports/after: the three actual analyzer reports and program output
- reports/after/test_report.txt: six passing tests
- Lab5_PES2UG24AM049_Report.pdf: simple printable summary
- test_ticket_booking_system.py: functional tests
- requirements-dev.txt: tested analyzer versions

The final Flake8 report is intentionally empty: zero output means no findings. Reports analyze the assigned program only, not the supplementary test script. No lint-disable directives or nosec exclusions are used. The source README mentions an input prompt, but the actual assigned script has no input call.

## Run on macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python ticket_booking_system.py
python -m unittest -v
pylint ticket_booking_system.py
bandit -r ticket_booking_system.py
flake8 ticket_booking_system.py
```

Program output includes B1 available=True, promo price=16.0 and sold count=1. The PIN changes between runs. The chart is written in the current directory.

## Submission repository and commits

https://github.com/prxneel007/L5_45_ticket_booking_system

Three commits organize the fixes: Bandit security fixes, Pylint quality fixes, and Flake8 formatting with reports and submission documents. The original course repository is retained as the fork source.
