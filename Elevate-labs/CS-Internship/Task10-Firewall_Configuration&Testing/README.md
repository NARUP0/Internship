# Task 10: Firewall Configuration & Testing

## 🛠 Tool Used
- Windows Defender Firewall  
- Operating System: Windows  

---

## 🔐 Objective
The objective of this task is to understand firewall concepts and configure firewall rules using Windows Defender Firewall to control inbound and outbound network traffic, test connectivity, block malicious traffic, and analyze the security impact.

---

## 📘 Firewall Concepts
A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predefined rules. It helps protect systems from unauthorized access and network-based attacks.

Key concepts learned:
- Inbound Rules
- Outbound Rules
- Stateful Firewall
- Port-based and application-based filtering

---

## ⚙️ Firewall Configuration Performed

### 1️⃣ Inbound Rule – Block Telnet Port
- Rule Name: Block Telnet Port 23  
- Direction: Inbound  
- Protocol: TCP  
- Port: 23  
- Action: Block  
- Profiles: Domain, Private, Public  

**Purpose:**  
Telnet is an insecure protocol. Blocking port 23 prevents unauthorized and insecure access.

---

### 2️⃣ Outbound Rule – Block Application Internet Access
- Rule Name: Block Notepad Internet Access  
- Direction: Outbound  
- Application: notepad.exe  
- Action: Block  
- Profiles: Domain, Private, Public  

**Purpose:**  
Controls outbound traffic and prevents unauthorized data transmission.

---

### 3️⃣ Block Malicious IP Address
- Rule Name: Block Malicious IP  
- Direction: Inbound  
- Blocked IP: 203.0.113.45  
- Action: Block  

**Purpose:**  
Prevents communication from suspicious or potentially malicious sources.

---

## 🔍 Connectivity Testing
Firewall rules were verified by checking rule enforcement:
- Inbound connections on port 23 are blocked.
- Outbound internet access for Notepad is blocked.

This confirms successful firewall configuration.

---

## 📄 Firewall Rules Summary

| Rule Name | Direction | Action | Purpose |
|--------|---------|--------|--------|
| Block Telnet Port 23 | Inbound | Block | Prevent insecure Telnet access |
| Block Notepad Internet Access | Outbound | Block | Control outbound traffic |
| Block Malicious IP | Inbound | Block | Prevent suspicious IP access |

---

## 📊 Impact of Firewall Configuration
- Reduced attack surface
- Improved control over network traffic
- Prevention of unauthorized access
- Enhanced system security posture

---

## ✅ Conclusion
This task provided hands-on experience with firewall configuration and testing. Windows Defender Firewall was effectively used to secure the system by controlling inbound and outbound traffic and blocking insecure and suspicious connections.

---

## 📌 Final Outcome
Gained practical understanding of firewall management and network security using Windows Defender Firewall.
