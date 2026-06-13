import subprocess
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/devices.txt", "r") as file:
    devices = file.readlines()

report_lines = [
    "========== NETWORK REPORT ==========",
    f"Generated: {timestamp}",
    ""
]

total_devices = 0
online_count = 0
offline_count = 0

for device in devices:
    device = device.strip()

    if not device:
        continue
    total_devices += 1
    
    result = subprocess.run(
        ["ping", "-n", "1", device],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        status = "ONLINE"
        online_count += 1
    else:
        status = "OFFLINE"
        offline_count += 1

    line = f"{device:<15} {status}"

    
    report_lines.append(line)

report_lines.append("")
report_lines.append("========== SUMMARY ==========")
report_lines.append(f"Total Devices : {total_devices}")
report_lines.append(f"Online        : {online_count}")
report_lines.append(f"Offline       : {offline_count}")    

print("\n========== SUMMARY ==========")
print(f"Total Devices : {total_devices}")
print(f"Online        : {online_count}")
print(f"Offline       : {offline_count}")
   
filename = datetime.now().strftime(
    "reports/network_report_%Y%m%d_%H%M%S.txt")

with open(filename, "w") as report:
    report.write("\n".join(report_lines))

print(f"\nReport saved to {filename}")