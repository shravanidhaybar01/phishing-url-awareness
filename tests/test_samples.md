# Test Results

Python version used: Python 3.13.7
Operating system: Windows
Date: 2 november 2026

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | [record actual output] | [PASS/FAIL] |
| 2 | http://192.0.2.10/account | IP address + HTTP | [record actual output] | [PASS/FAIL] |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | [record actual output] | [PASS/FAIL] |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | [record actual output] | [PASS/FAIL] |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | [record actual output] | [PASS/FAIL] |

## Notes

I learned how Python can separate a URL into parts and check for
selected warning signs. I also learned that a URL with no warning
signs is not necessarily safe.