## 🔒 Daily CVE Alert Script

This script retrieves recently published critical CVEs from the NVD API, filters them based on a vendor list, and sends a daily email report.

## 📌 Features
Fetches CVEs published in the last 24 hours.

Filters for only CRITICAL severity vulnerabilities.

Checks if any predefined vendors are mentioned.

Sends an email with relevant CVE details.

Uses a vendor list stored in an Excel file.

Loads secure email credentials from a .env file.

## 📁 Project Structure 
.<br/>
├── script.py                # Main script <br/>
├── vendors_list.xlsx        # Excel file containing vendor names (1 per cell)<br/>
├── .env                     # Contains email credentials<br/>
├── nvdcve-1.1-recent.json   # Auto-generated file with recent CVEs<br/>
└── README.md                # You're reading this<br/>

## ⚙️ Requirements
Python 3.7+

Dependencies: 
```
# You will need the packages requests, openpyxl and python-dotenv
pip install requests openpyxl python-dotenv
```

## 🛠️ Setup Instructions
Clone the repo or place the script and files in a directory.

Create a .env file in the same directory:
```
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password_or_app_password
EMAIL_TO=recipient1@example.com,recipient2@example.com
``` 
⚠️ If using Gmail, enable "App Passwords" or allow less secure apps.

Create vendors_list.xlsx with vendor names in a single column (one name per row).

## ✉️ Output
Prints matching CVEs in the console.

Sends an email titled: Daily CVE Report.

If no matching CVEs are found: "No new CVEs for today!!!"

### ✅ Example Email Content

There are 2 CVEs to look at!

Relevant CVE: CVE-2025-XXXX
Published Date: 2025-06-27T15:23Z
Severity: CRITICAL
Base Score: 9.8
Vector: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
Description: [Short description]
...
