import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for common phishing warning signs."""

    url = raw_url.strip()
    findings = []

    # Check empty input
    if not url:
        return ["No URL entered."]

    # Add a default scheme if missing
    candidate = url if "://" in url else "http://" + url

    # Safely analyse URL format
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    # Check whether hostname exists
    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: Long URL
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IP address hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Many hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode hostname
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP instead of HTTPS
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    # No warning signs found
    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )

    return findings


# Improvement 1: Identify whether warnings were found
INFO_MESSAGES = (
    "No URL entered.",
    "Could not identify",
    "This text is not a valid URL format.",
    "No listed warning signs"
)


def has_warnings(findings):
    return not findings[0].startswith(INFO_MESSAGES)


# Main program with repeat option
def main():

    print("=" * 50)
    print("       EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 50)

    print("Text checks only - this program does not open URLs.")
    print("This tool is for educational purposes only.")

    # Improvement 2: Loop to check multiple URLs
    while True:

        raw_url = input(
            "\nEnter a sample URL (or type q to quit): "
        )

        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("\nGoodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)

        print("\nURL Analysis Results:")
        print("-" * 35)

        for item in findings:
            print("- " + item)

        # Display warning summary
        if has_warnings(findings):
            print(
                "\nREVIEW CAREFULLY: "
                + str(len(findings))
                + " warning sign(s) found."
            )
        else:
            print("\nNo warning signs were identified.")

        print("\nReminder: Never enter passwords")
        print("on unexpected or suspicious links.")


if __name__ == "__main__":
    main()