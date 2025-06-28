## 🔒 Daily CVE Alert Script<br/>

This script retrieves recently published critical CVEs from the NVD API, filters them based on a vendor list, and sends a daily email report.<br/>

## 📌 Features<br/>
Fetches CVEs published in the last 24 hours.<br/>

Filters for only CRITICAL severity vulnerabilities.<br/>

Checks if any predefined vendors are mentioned.<br/>

Sends an email with relevant CVE details.<br/>

Uses a vendor list stored in an Excel file.<br/>

Loads secure email credentials from a .env file.<br/>

## 📁 Project Structure <br/>
.<br/>
├── script.py                # Main script <br/>
├── vendors_list.xlsx        # Excel file containing vendor names (1 per cell)<br/>
├── .env                     # Contains email credentials<br/>
├── nvdcve-1.1-recent.json   # Auto-generated file with recent CVEs<br/>
└── README.md                # You're reading this<br/>

## ⚙️ Requirements<br/>
Python 3.7+<br/>

Dependencies: <br/>
```
# You will need the to install the packages requests, openpyxl and python-dotenv
pip install requests openpyxl python-dotenv
```

## 🛠️ Setup Instructions<br/>
Clone the repo or place the script and files in a directory.<br/>

Create a .env file in the same directory:<br/>

EMAIL_USER=your_email@gmail.com<br/>
EMAIL_PASS=your_email_password_or_app_password<br/>
EMAIL_TO=recipient1@example.com,recipient2@example.com<br/>
SMTP_SERVER=your_smtp_server # Google smtp server: smtp.gmail.com<br/>
 
⚠️ If using Gmail, enable "App Passwords" or allow less secure apps.<br/>

1. Enable 2-Step Verification<br/>
https://myaccount.google.com/security<br/>

2. Create an App Password<br/>
https://myaccount.google.com/apppasswords <br/>
Choose "Mail" > "Windows Computer"<br/>

Create vendors_list.xlsx with vendor names in a single column (one name per row).<br/>

## ✉️ Output<br/>
Prints matching CVEs in the console.<br/>

Sends an email titled: Daily CVE Report.<br/>

If no matching CVEs are found, it sends an email with: "No new CVEs for today!!!"<br/>

### ✅ Example Email Content<br/>

There are 2 CVEs to look at!<br/>

Relevant CVE: CVE-2025-XXXX<br/>
Published Date: 2025-06-27T15:23Z<br/>
Severity: CRITICAL<br/>
Base Score: 9.8<br/>
Vector: AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H<br/>
Description: [Short description]<br/>
...<br/>

![image](https://github.com/user-attachments/assets/0134f320-c13a-40d1-9e17-bc3f8f4d4aa1)<br/>

