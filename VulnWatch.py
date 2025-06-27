import requests
import datetime
import urllib.parse
import json
from itertools import product
from cvss import CVSS3  # pip install cvss
import re
import openpyxl

Vendor_list = []

def Get_vendors():
    # Load NVD data from a local .json file
    dataframe  = openpyxl.load_workbook('vendors_list.xlsx')
    
    # Define variable to read sheet
    dataframe1 = dataframe.active

    for row  in range(0, dataframe1.max_row):
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            Vendor_list.append(col[row].value)
    return Vendor_list


def get_cvss_metrics(metrics):
    cvss_data = None
    vector_version = None

    if "cvssMetricV31" in metrics and metrics["cvssMetricV31"]:
        cvss_data = metrics["cvssMetricV31"][0]["cvssData"]

    elif "cvssMetricV40" in metrics and metrics["cvssMetricV40"]:
        cvss_data = metrics["cvssMetricV40"][0]["cvssData"]
    
    return cvss_data

def check_descriptions_language(description_data):
    description_info = None
    no_desc = "No description"
    
    for desc in description_data:
        
        if desc.get("lang") == "en":
            return desc.get("value", "")
    return no_desc


vendors_list = Get_vendors()

pattern = r'\b(?:' + '|'.join(re.escape(kw) for kw in vendors_list) + r')\b'

def cve_mentions_vendor(cve_entry):
    texts = []

    # 1. Descriptions
    for desc in cve_entry.get("descriptions", []):
        texts.append(desc.get("value", ""))

    # 2. References (URLs or sources might contain vendor names)
    for ref in cve_entry.get("references", []):
        texts.append(ref.get("url", ""))
        texts.append(ref.get("source", ""))

    # 3. (Optional) Metrics source
    metrics = cve_entry.get("metrics", {})
    for key in metrics:
        for metric_item in metrics[key]:
            texts.append(metric_item.get("source", ""))

    # Combine all text and search
    combined_text = " ".join(texts)
    return bool(re.search(pattern, combined_text, re.IGNORECASE))


def fetch_recent_critical_cves_from_history():
   # 1. Calculate UTC timestamps for now and 24 hours ago
    now = datetime.datetime.utcnow()
    start_time = now - datetime.timedelta(days=1)

    # Format to required ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ
    def format_iso8601_z(dt):
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    start_str = format_iso8601_z(start_time)
    end_str = format_iso8601_z(now)

    # 2. Fetch CVE history for that range
    history_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "pubStartDate": start_str,
        "pubEndDate": end_str
    }

    #response = requests.get(history_url, params=params)
    #data = response.json()

    # Serializing json
    #json_object = json.dumps(data, indent=4)
    

    # Writing to sample.json
    #with open("nvdcve-1.1-recent.json", "w") as outfile:
     #  outfile.write(json_object)

    # Load NVD data from a local .json file
    with open("nvdcve-1.1-recent.json", "r") as file:
        data = json.load(file)

    print(f"🔍 Checking CVEs updated between {start_time} and {now}")
    print("  ")

    return data

def main ():

    cve_count = 0
    # Iterate through each CVE item
    data = fetch_recent_critical_cves_from_history()
    
    for item in data.get("vulnerabilities", []):

        cve = item["cve"]["id"]
        cve_data = item["cve"]
        cvss_metric = item["cve"]["metrics"]
        
        
        published= item["cve"]["published"]
        lastModified = item["cve"]["lastModified"]
        descriptions = item["cve"]["descriptions"][0]["value"]
        
        descriptions_lan = item["cve"]["descriptions"][0]["lang"]
            
        GetcvssMetric = get_cvss_metrics(cvss_metric)
        if GetcvssMetric == None:
            continue

        baseSeverity = GetcvssMetric["baseSeverity"]
        version = GetcvssMetric["version"]
        vectorString = GetcvssMetric["vectorString"]
        baseScore = GetcvssMetric["baseScore"]
        
        if baseSeverity == "CRITICAL":

            if cve_mentions_vendor(cve_data):
                cve_count += 1
                print("Relevant CVE:", cve)
                print("NVD Published Date:", published)
                print("NVD Last Modified:", lastModified)
                print("CVSS Version:", version)
                print("Severity:", baseSeverity)
                print("Base Score:", baseScore)
                print("Vector:", vectorString)
                print("Descriptions:", check_descriptions_language(item["cve"]["descriptions"])) 
                print("   ")
    print(f"There is {cve_count} number to look at!!")
    
    if cve_count == 0:
        print("No new CVEs for today!!!")

main()


