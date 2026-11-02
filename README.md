# EWB Phishing URL Awareness Checker

## Overview

This is a beginner-level cybersecurity mini project made using
Python. It checks URL text for selected warning signs that may
be associated with phishing links.

The program only reads the URL entered by the user. It does
not open websites or send information to any online service.

## Features

- Checks for an @ symbol.
- Checks for URLs longer than 100 characters.
- Checks for IP-address hostnames.
- Checks for five or more hostname segments.
- Checks for a punycode-style hostname.
- Checks for the HTTP scheme.
- Allows repeated URL checks until the user quits.
- Handles certain malformed URLs without crashing.

## Requirements

- Python 3.10 or later
- Visual Studio Code or another code editor
- No extra Python packages required

## How to Run

1. Open the project folder in VS Code.
2. Open Terminal and select New Terminal.
3. Run this command on Windows:

   python phishing_checker.py

4. Enter a sample URL when asked.
5. Type q to exit the program

## Example Output
PS C:\Users\Server\Desktop\projects\Phishing_url_awareness> & C:\Users\Server\AppData\Local\Programs\Python\Python313\python.exe c:/Users/Server/Desktop/projects/Phishing_url_awareness/phishing_checker.py
EWB Phishing URL Awareness Checker
Text checks only - this program does not open URLs.

Enter a sample URL (or type q to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Remember: warning signs are clues, not proof of a phishing attack.

Enter a sample URL (or type q to quit): C:\Users\Server\AppData\Local\Programs\Python\Python313\python.exe c:/Users/Server/Desktop/projects/Phishing_url_awareness/phishing_checker.py

Result:
- Unusually long URL (over 100 characters).
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Remember: warning signs are clues, not proof of a phishing attack.

Enter a sample URL (or type q to quit): C:\Users\Server\AppData\Local\Programs\Python\Python313\python.exe c:/Users/Server/Desktop/projects/Phishing_url_awareness/phishing_checker.py

Result:
- Unusually long URL (over 100 characters).
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Remember: warning signs are clues, not proof of a phishing attack.

Enter a sample URL (or type q to quit): C:\Users\Server\AppData\Local\Programs\Python\Python313\python.exe c:/Users/Server/Desktop/projects/Phishing_url_awareness/phishing_checker.py

Result:
- Unusually long URL (over 100 characters).
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Remember: warning signs are clues, not proof of a phishing attack.

Enter a sample URL (or type q to quit): C:\Users\Server\AppData\Local\Programs\Python\Python313\python.exe c:/Users/Server/Desktop/projects/Phishing_url_awareness/phishing_checker.py

Result:
- Unusually long URL (over 100 characters).
- Uses HTTP. HTTPS alone does not prove trust.

REVIEW CAREFULLY: 2 warning sign(s) found.
Remember: warning signs are clues, not proof of a phishing attack.

## Testing

Five sample URLs from the project workbook were used for testing.
The actual results and pass/fail status are recorded in
tests/test_samples.md.

## Screenshots
Screenshots

1. Sample Run

This screenshot shows the Phishing URL Checker running in the VS Code terminal with a sample suspicious URL and its analysis results.

"Sample Run" (screenshots/sample_run.png)

2. Test Results

This screenshot shows the five test URLs and their expected warning signs.

"Test Results" (screenshots/test_results.png)
### Sample Run

Sample Run

The Phishing URL Checker takes a URL as input and checks for common suspicious characteristics that may indicate a phishing attempt.

Example 1: Suspicious URL

Input:

http://192.0.2.10/account

Output:

Enter URL: http://192.0.2.10/account

URL Analysis Results:
- IP address used instead of domain name
- HTTP connection detected (not HTTPS)

Warning: This URL contains suspicious characteristics.

Example 2: Normal URL

Input:

https://www.example.com/login

Output:

Enter URL: https://www.example.com/login

URL Analysis Results:
No listed warning signs.

Note: No warning signs does not guarantee that a URL is safe.

Screenshots

The following screenshots demonstrate the working of the Phishing URL Checker.

1. Sample Run: Shows the Python program running in VS Code terminal with URL input and analysis output.
2. Test Results: Shows the five test URLs and their expected warning signs.

Screenshots are available in the "screenshots" folder.

### Test Results

![Test results](screenshots/test_results.png)

## Improvements

1. Repeated checking: users can check multiple URL samples
   without restarting the program.
2. Input error handling: certain malformed URLs produce a
   message instead of stopping the program.

## Limitations

This is an educational URL-awareness tool. It checks only
selected text patterns. It does not visit URLs, scan websites,
check online reputation or prove that a URL is safe.

A URL with no listed warning signs may still be dangerous.

## Ethical Use

This project is for defensive cybersecurity learning.
Use the supplied sample URLs and never collect passwords,
OTPs or other credentials.

## Author

Name: shravani dhaybar
Course: ewb AI powered cybersecurity (batch 1)