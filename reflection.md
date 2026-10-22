# Lab 5 - Reflection

Name: Chirra Yuktha Praneel  
SRN: PES2UG24AM049

Note: The supplied README requests four reflection questions, but the supplied four-page handout does not contain their wording. These are four relevant reflection prompts and answers, not quotations from the handout.

## 1. What did each tool help identify?
Pylint found code quality problems such as the mutable default list, missing docstrings and unused variables. Bandit found security problems such as eval, MD5 and the shell command. Flake8 found formatting and style problems, including long lines and the missing final newline. Some findings overlapped.

## 2. Which issues were fixed first and why?
The high-severity MD5 and shell-command findings were addressed first, followed by the medium-severity eval finding. SHA-256 replaced MD5, print replaced the shell command, and validated arithmetic replaced eval. The remaining Bandit findings were also fixed. This removed all five reported security findings.

## 3. How were the fixes verified?
All three tools were run again on the cleaned ticket_booking_system.py. Pylint improved from 5.37 to 10.00, Bandit went from five findings to zero, and Flake8 went from seven findings to zero. Six unit tests checked booking history, cancellation, discounts, hashes and PIN ranges, exports and sold counts, and importing without running the demo. The program was also run successfully.

## 4. What are the benefits and limitations of static analysis?
Static analysis quickly finds suspicious patterns and helps keep code readable. It does not prove that the program works correctly or is completely secure. For example, the hard-coded token was removed during manual review even though this Bandit run did not report it. Functional tests are still needed. The safe promo format is now intentionally limited, so that change must be documented for callers.
