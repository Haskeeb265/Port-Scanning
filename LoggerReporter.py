import json
import csv
from datetime import datetime

def log_results(open_ports, ip_input, scan_duration):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    json_filename = f"scan_results_{timestamp}.json"
    csv_filename = f"scan_results_{timestamp}.csv"

    results = {
        "target": ip_input,
        "open_ports": open_ports,
        "scan_duration_sec": scan_duration
    }

    with open(json_filename, 'w') as jf:
        json.dump(results, jf, indent=4)
        print(f"[+] Saved JSON report: {json_filename}")

    with open(csv_filename, 'w', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow(["Target", "Open Ports", "Scan Duration (sec)"])
        writer.writerow([ip_input, ', '.join(str(p) for p in open_ports), scan_duration])
        print(f"[+] Saved CSV report: {csv_filename}")
