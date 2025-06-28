# List of vendor keywords (you can customize this list)
vendor_keywords = ["WordPress", "Wordfence", "Microsoft", "Apache", "Cisco", "Fortinet", "eosphoros-ai"]

# Example text
text = """
The PT Project Notebooks plugin for WordPress is vulnerable to Privilege eosphoros-ai Escalation...
security@wordfence.com https://www.wordfence.com/threat-intel/vulnerabilities/id/552ec9fc...
"""

def ketword_check():

    # Normalize text (optional: lowercase for case-insensitive search)
    text_lower = text.lower()

    # Find all mentioned vendors
    mentioned_vendors = [vendor for vendor in vendor_keywords if vendor.lower() in text_lower]
    return bool(mentioned_vendors)

print(f"There is {ketword_check()}")

