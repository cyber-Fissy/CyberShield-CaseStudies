# 🎣 Phishing Attack Incident Case Study  

**Author:** Akinola Fisayo  
cybersecurity (Incident Response & Threat Analysis)  
**Date Documented:** 2025  

---

## 📌 Incident Overview  
A mid-sized financial services company reported that several employees received suspicious emails resembling official Office365 login requests.  
The emails contained links to a **spoofed login page** designed to steal employee credentials.  
Some employees entered their usernames and passwords, leading to **multiple compromised accounts** within the organization.  

---

## 🔎 Root Cause  
- Employees were targeted with **spear-phishing emails**.  
- Attackers used **domain spoofing** to make the emails appear legitimate.  
- Victims unknowingly submitted credentials to a **malicious phishing site**.  

---

## ⚠️ Impact  
- Multiple employee accounts compromised.  
- Unauthorized access to internal email systems.  
- Potential risk of **financial fraud** and **data exfiltration**.  

---

## 🛠️ Incident Response Actions  
1. **Detected** unusual login activity from foreign IP addresses.  
2. **Reset passwords** for all affected accounts immediately.  
3. **Blocked the malicious domain** via the email security gateway.  
4. Enabled **Multi-Factor Authentication (MFA)** for all employee logins.  
5. Conducted **organization-wide phishing awareness training**.  

---

## ✅ Lessons Learned  
- **MFA is essential** to protect accounts even if credentials are stolen.  
- Employees must be trained to recognize suspicious links and emails.  
- Regular **phishing simulations** help improve organizational readiness.  
- Domain monitoring tools should be in place to detect spoofed sites quickly.  

---

## 📂 Tags  
`Phishing` `Credential Harvesting` `Incident Response` `Financial Services Security`  
