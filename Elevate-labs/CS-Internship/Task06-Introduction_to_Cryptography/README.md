# 🔐 Task 6: Introduction to Cryptography

## 📌 Objective
To understand basic cryptography concepts such as encryption, hashing, digital signatures, and their real-world usage using OpenSSL.

---

## 🧠 Concepts Covered
- Symmetric Encryption (AES)
- Asymmetric Encryption (RSA)
- Digital Signatures
- Hashing & Integrity Verification
- Real-world usage (HTTPS, VPN)

---

## 🛠 Tools Used
- OpenSSL  
- Terminal (Linux / Git Bash)

---

## 🔒 Experiments Performed

### 1. AES File Encryption
- Encrypted a text file using **AES-256**
- Decrypted it using the same password
- Demonstrated symmetric encryption

### 2. RSA Key Generation
- Generated a **2048-bit private key**
- Extracted the corresponding **public key**
- Demonstrated asymmetric encryption

### 3. Digital Signatures (Concept)
- Message hash is signed using sender’s private key
- Verified using sender’s public key
- Ensures authenticity and integrity

### 4. Hashing & Integrity Check
- Generated SHA-256 hash of a file
- File modification resulted in a different hash
- Proved data tampering detection

---

## 🌍 Real-World Applications
- HTTPS uses RSA for key exchange and AES for data encryption
- VPNs protect data using encryption
- Hashing ensures file integrity
- Digital signatures verify sender authenticity

---

## 📁 Files Included
- secret.txt
- secret.enc
- decrypted.txt
- private_key.pem
- public_key.pem

---

## ✅ Outcome
Gained strong foundational knowledge of cryptography, encryption techniques, hashing, and their practical security applications.
