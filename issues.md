# Lab 5 - Identified Issues

Name: Chirra Yuktha Praneel  
SRN: PES2UG24AM049  
Class: 5th Sem AIML (A)

Line numbers refer to the original assigned script. Bandit severities are copied from the actual report; other types describe the nature of the issue.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| B324: MD5 hash | High / Security | 47 | MD5 is a weak hash for security use. | Replace with SHA-256; do not treat a plain hash as authentication. |
| B605: Shell invocation | High / Security | 58 | A filename is concatenated into a shell command. | Use print directly; never start a shell. |
| B307 / W0123: eval | Medium / Security | 42 | Promo text is executed as Python code. | Accept only base_price * decimal-factor from 0 to 1, validate with a full regex match and calculate directly. |
| B110 / W0702 / E722: Bare except with pass | Low / Security and Bug | 24-27 | All errors are silently ignored during cancellation. | Check seat membership explicitly and return False for unknown seats. |
| B311: Predictable random PIN | Low / Security | 51 | random is not designed for security-sensitive values. | Use secrets.randbelow, retaining four-digit PINs. |
| W0102: Mutable default | Bug | 15 | The same default history list persists between calls. | Default to None and create a fresh list when needed. |
| C0103: Function naming | Maintainability | 15, 71 | reserveSeat does not use Python snake_case. | Rename to reserve_seat and update the call. |
| W1514 / R1732: File resource | Reliability | 55-57 | File uses implicit encoding and manual closing. | Use a with block and UTF-8 encoding. |
| W0611 / F401: Unused import | Quality | 6 | math is never used. | Remove the import. |
| W0612 / F841: Unused variables | Quality | 31, 41, 63 | booking_fee and seat are unused; eval hides the use of base_price from analysis. | Remove booking_fee, loop over values, and use base_price directly in arithmetic. |
| C0121 / E711: None comparison | Style | 32 | None is compared with equality. | Use is None. |
| R1703 / R1705: Redundant branches | Maintainability | 34-37 | A condition is converted to True/False through extra branches. | Return the boolean expression directly. |
| W0621: Shadowed global | Maintainability | 61 | Parameter hides the global seating map. | Rename parameter to seats. |
| C0116: Missing docstrings | Documentation | 15-69 | Functions do not describe their purpose. | Add short function docstrings. |
| E501 / C0209: Long formatting expression | Style | 19 | Old string formatting exceeds Flake8's line limit. | Use an f-string and keep final lines within 79 characters. |
| W292 / C0304: No final newline | Style | 82 | File does not end in a newline. | Add final newline. |
| Hard-coded, printed token | Manual security review | 70, 79 | A secret-like demo string is embedded and displayed. This tool version did not flag it. | Remove the unused token and its print statement. |
| main runs on import | Manual maintainability review | 82 | Importing changes seat state and writes a file. | Add an if __name__ == "__main__" guard. |

## Scope and behavior

Booking, cancellation, availability, discounts, ticket hashing, PIN generation, exports and sold-seat counting are retained. Arbitrary Python promo expressions are deliberately no longer supported. The original example `base_price * 0.80` still returns 16.0 for B1. The function rename and SHA-256 output length are intentional changes. Unknown discount seats raise KeyError; invalid promo expressions raise ValueError. A four-digit PIN remains unsuitable as the sole production authentication mechanism. No analyzer warnings were suppressed.
