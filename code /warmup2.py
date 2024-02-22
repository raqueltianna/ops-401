

log_entries = """[2024-02-01 08:30:15] WARNING: Unauthorized access attempt detected from IP address 192.168.1.100.
[2024-02-01 09:45:22] ERROR: Database connection failure. Unable to establish a connection to the database server.
[2024-02-01 10:15:50] WARNING: Suspicious network activity detected. Potential port scanning from IP address 10.0.0.5.
[2024-02-01 11:20:05] ERROR: Critical system file not found. System integrity compromised.
[2024-02-01 12:40:18] THREAT: Malware detected in file 'system32.dll'. Immediate action required.
[2024-02-01 14:05:30] ERROR: Server overload. High CPU and memory usage detected.
[2024-02-01 15:10:45] WARNING: Outdated software version. Update required for security patches.
[2024-02-01 16:30:02] THREAT: Brute-force attack on user accounts detected. Lockout initiated.
[2024-02-01 17:45:12] ERROR: File deletion error. Critical files deleted due to unauthorized access.
[2024-02-02 08:30:15] WARNING: Multiple failed login attempts from IP address 192.168.1.102. Potential account compromise.
[2024-02-02 09:45:22] ERROR: Network intrusion detected. Unusual traffic patterns observed.
[2024-02-02 10:15:50] WARNING: Anomalous behavior in user account 'admin'. Possible unauthorized access.
[2024-02-02 11:20:05] ERROR: Security certificate expired. Communication encryption compromised.
[2024-02-02 12:40:18] THREAT: Distributed Denial of Service (DDoS) attack in progress. Services degraded.
[2024-02-02 14:05:30] ERROR: File integrity check failed. Files modified without authorization.
[2024-02-02 15:10:45] WARNING: Unusual outbound traffic from internal network. Possible data exfiltration.
[2024-02-02 16:30:02] THREAT: Advanced Persistent Threat (APT) detected. Covert activities observed.
[2024-02-02 17:45:12] ERROR: Critical system process terminated unexpectedly. System instability detected."""

warning_file = open("warning_log.txt", "w")
error_file = open("error_log.txt", "w")
threat_file = open("threat_log.txt", "w")


for line in log_entries:
    if log_level == 'WARNING':
        warning_file.write(f"[{timestamp}] {message}\n")
    elif log_level == 'ERROR':
        error_file.write(f"[{timestamp}] {message}\n")
    elif log_level == 'THREAT':
        threat_file.write(f"[{timestamp}] {message}\n")


# Close all files 
warning_file.close()
log_file.close()
threat_file.close()