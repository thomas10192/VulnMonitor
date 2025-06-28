import re

test_vendors = ['eosphoros-ai', 'HKUDS']
pattern = r'(' + '|'.join(re.escape(v) for v in test_vendors) + r')'
sample_text = "This CVE affects eosphoros-ai and also mentions HKUDS devices."

match = re.search(pattern, sample_text, re.IGNORECASE)
print("Match found:", bool(match))