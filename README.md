# 🔍 Half-Scan SYN Port Scanner

> ⚠️ **For educational purposes only. Use responsibly.**

A **low-level SYN port scanner** built to deeply understand **TCP/IP internals** by implementing everything from scratch without high-level libraries.

---

## 🧩 What Happens Under the Hood

### 🚦 Flow of Logic

1. **Input**  
   Accept target IP from the user.

2. **SYN Packet Crafting**  
   For each target port:
   - Craft a TCP SYN packet with:
     - Source IP & ephemeral source port
     - Destination IP & target port
     - TCP flags = SYN

3. **Send Packets**  
   Send crafted SYN packets using raw sockets.

4. **Sniff Responses**  
   Listen for incoming packets:
   - `SYN + ACK` received ➔ **Port is open**
   - `RST` received ➔ **Port is closed**
   - No response ➔ **Host is down**

5. **Send RST**  
   If `SYN + ACK` is received, immediately send an `RST` to avoid completing the TCP handshake.

6. **Log Results**  
   Store port status for later reference.

7. **Exit**  
   Clean up sockets/sniffers and present a final report of open/closed/filtered ports.

---

## 🛠️ Modules

### 1️⃣ Input
- Parse user input.
- Validate IP addresses/domains.

### 2️⃣ Packet Crafter
- Craft SYN packets using **`socket` + `struct`** instead of Scapy to **understand packet crafting at the lowest level**.

### 3️⃣ Packet Sender
- Send crafted SYN packets to each port.
- Optional multithreading for faster scans.

### 4️⃣ Packet Sniffer
- Capture incoming packets using raw sockets.
- Filter relevant packets for analysis.

### 5️⃣ Response Analyzer
- Analyze received packets.
- Handle timeouts for each port scan gracefully.

### 6️⃣ RST Sender
- Send `RST` if `SYN + ACK` is detected to terminate the handshake immediately.

### 7️⃣ Logger & Reporter
- Print live scanning results.
- Generate a summary:
  - Scan duration
  - Open ports
  - Closed ports

---

## 🚀 Why This Project?

✅ Learn TCP internals practically  
✅ Understand raw sockets, SYN scanning, and packet crafting  
✅ Build offensive security tooling responsibly for labs & CTF learning

---

## ⚡ Notes

- Built using **Python** with **raw sockets**.
- Intended for **personal labs, CTF practice, and self-learning**, not unauthorized scanning.

---

> ⭐ If you find this project helpful in your learning journey, consider giving it a star!
