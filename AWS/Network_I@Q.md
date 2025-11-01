# Networking & Troubleshooting Interview Questions (42–50)

A collection of common networking and troubleshooting questions with simple, clear answers for quick revision.

---

## **1. Explain DNS in simple words**
**Answer:**  
DNS (Domain Name System) works like the internet’s phonebook.  
It converts human-readable names (like `google.com`) into IP addresses (like `142.250.190.14`) so computers can locate each other on the network.

---

## **2. Explain the complete flow of the request from client to server (OSI Model)**
**Answer:**  
When a client (like a browser) requests data from a server, the request passes through the **7 layers** of the OSI model:

1. **Application Layer (L7):** HTTP/HTTPS request sent by the browser.  
2. **Presentation Layer (L6):** Data is encrypted or formatted (e.g., SSL/TLS).  
3. **Session Layer (L5):** Opens, maintains, and closes communication sessions.  
4. **Transport Layer (L4):** Uses TCP/UDP; adds source and destination ports.  
5. **Network Layer (L3):** Adds source and destination IP addresses.  
6. **Data Link Layer (L2):** Adds MAC addresses for physical delivery.  
7. **Physical Layer (L1):** Transmits actual electrical or radio signals.

The response from the server travels back through the same layers in reverse.

---

## **3. Explain the difference between Forward Proxy and Reverse Proxy**
**Answer:**  
| Type | Used By | Purpose | Example |
|------|----------|----------|----------|
| **Forward Proxy** | Client | Hides client’s identity from the internet | Corporate proxy |
| **Reverse Proxy** | Server | Hides backend servers from clients | NGINX, AWS ALB |

> ✅ **Summary:** Forward Proxy protects **clients**, Reverse Proxy protects **servers**.

---

## **4. User reports slowness in the app. How would you approach this?**
**Answer:**  
Step-by-step troubleshooting:

1. **Check Network:** Ping/Traceroute — Is latency high?  
2. **Check DNS:** Is domain resolving properly?  
3. **Backend Performance:** Check slow APIs or DB queries.  
4. **Server Health:** Review CPU, memory, disk I/O.  
5. **Logs & Metrics:** Identify bottlenecks or errors.  
6. **Frontend:** Check large files, JavaScript, or image size.

---

## **5. Curl works with IP but fails with Domain. Why?**
**Answer:**  
This means **DNS resolution is failing.**  

**Possible reasons:**
- DNS server not reachable or not configured.  
- Wrong `/etc/resolv.conf` entry.  
- Domain has incorrect DNS record.

**To verify:**
```bash
nslookup example.com
```
If this fails → DNS issue confirmed.

---

## **6. Website returns 502 HTTP Status Code. What can be the issue?**
**Answer:**  
**502 = Bad Gateway** → Proxy or Load Balancer can’t reach the backend server.

**Possible causes:**
- Backend is down or not responding.  
- Wrong backend IP or port configured.  
- Timeout between proxy and backend.  
- SSL/TLS handshake failure.

---

## **7. What is the difference between 0.0.0.0 and 127.0.0.1?**
**Answer:**  
| Address | Meaning | Use Case |
|----------|----------|----------|
| **0.0.0.0** | All IP addresses on the local machine | Listen on all interfaces |
| **127.0.0.1** | Loopback address (localhost) | Access same machine only |

**Example:**
- `0.0.0.0:80` → Server accessible from anywhere.  
- `127.0.0.1:80` → Accessible only locally.

---

## **8. What is the difference between Public and Private Subnets?**
**Answer:**  
| Type | Internet Access | Route Table | Use Case |
|------|------------------|-------------|-----------|
| **Public Subnet** | Yes | Has route to Internet Gateway | Web servers |
| **Private Subnet** | No | No direct Internet Gateway route | Databases, backend servers |

---

## **9. You accidentally created a private subnet instead of public. How will you fix it?**
**Answer:**  
To convert a private subnet to public:

1. **Edit Route Table:** Add route to Internet Gateway (`0.0.0.0/0 → igw-xxxx`).  
2. **Enable Auto-assign Public IP:** In subnet settings.  
3. **Associate Correct Route Table:** Ensure subnet uses the public route table.

✅ The subnet now has internet access — it’s public.

---

**Prepared by:** _Invryom Technologies (By Pradeep)_  
**Purpose:** Networking fundamentals and troubleshooting quick reference.
