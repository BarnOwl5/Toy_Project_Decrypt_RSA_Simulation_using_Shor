## 🔐 Toy Project: Decrypt RSA Simulation using Shor’s Algorithm

### 📌 Overview

This project is a **toy simulation** that demonstrates the basic concept of RSA encryption and classical emulation of **Shor's algorithm** (used for factoring large integers efficiently using quantum computation).
It's built for educational and experimental purposes to illustrate how factorization can potentially break RSA-based encryption systems.

You can check the details here:
[Toy Project: Decrypt RSA with Shor](https://www.notion.so/Toy-Project-Decrypt-RSA-with-Shor-280224f27a318002b2cfcc7bee1acaa0?source=copy_link)
### ⚙️ Features
  - **RSA Key Generation** (prime selection, φ(n) computation, modular inverse)
  - **Encryption / Decryption** using modular exponentiation 
  - **Shor's Algorithm (mock)** – classical brute-force period-finding simulation
  - **Factor Recovery Demo** – simple flow from ciphertext to recovered plaintext


### 🧮 File Structure  

```bash
Toy_Project_Decrypt_RSA_Simulation_using_Shor/
├── images
├── RSA_Decryption_Via_Shor.py # Main simulation script
└── README.md               # Project overview and notes
```


### 🧰 Code Highlights

Function | Description
|--      |--
`RSA_BASE.__init__()` | Generates primes `p`, `q`, computes `n`, `phi`, and keys
`_pick_e()` | Selects an encryption exponent `e` coprime to `φ(n)`
`encrypt() / decrypt()` | Implements RSA encryption and decryption
`find_period()` | Brute-force search for period `r` where `aʳ ≡ 1` (mod N)
`shor_factor_mock()` | Classical simulation of Shor’s factorization
`demo()` | Demonstrates full process — keygen → encrypt → factor → decrypt

### 🧩 Example Execution

Run:
```bash
python RSA_Decryption_Via_Shor.py
```

Example Output:
```bash
=== Step 1: RSA Key Generation ===
p=13, q=23, n=299, phi=264
e=5, d=53

=== Step 2: Encryption ===
Plaintext: "time is gold"
Ciphertext: [116, 27, 44, 238, 54, 27, 46, 54, 51, 11, 75, 16]

=== Step 3: Factorization Simulation ===
Found factors: (13, 23)

=== Step 4: Factor Recovery & Decryption ===
Recovered private key d: 53
Recovered plaintext: "time is gold"
```
<details>
  <summary>🖥️ View Output Screenshot</summary>

  ![poster](./images/Output_image.png)

</details>



### 🚀 Educational Notes

This project demonstrates:

- The vulnerability of RSA under quantum algorithms like Shor’s.
- How period finding leads to factorization.
- The importance of quantum-resistant cryptography (PQC) for the future.

---
### 📌 **Note**

>This project is designed for **educational and demonstration purposes only.**  
>It does **not represent a practical or production-level implementation**, and does **not endorse** misuse of cryptographic simulations.
>
>
>📄 This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

