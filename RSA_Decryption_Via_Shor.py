# rsa_shor_demo.py
import random, math

# ---------- RSA (toy) ----------
class RSA_BASE:
    def __init__(self, p=None, q=None):
        # 데모용: 직접 p,q 넣거나, 안 넣으면 작은 소수 랜덤
        small_primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.p = p if p else random.choice(small_primes)
        self.q = q if q else random.choice([x for x in small_primes if x != self.p])
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self._pick_e(self.phi)
        self.d = modinv(self.e, self.phi)

    def _pick_e(self, phi):
        # 65537이랑 gcd가 1이면 쓰고, 아니면 작은 e 탐색
        candidate = 65537
        if math.gcd(candidate, phi) == 1 and candidate < self.n:
            return candidate
        e = 3
        while e < phi:
            if math.gcd(e, phi) == 1:
                return e
            e += 2
        raise ValueError("fail to find e")

    def encrypt(self, plaintext: str):
        # 문자 단위 RSA (데모라서 바이트 분할 안함)
        return [pow(ord(ch), self.e, self.n) for ch in plaintext]

    def decrypt(self, ciphertext):
        return "".join(chr(pow(c, self.d, self.n)) for c in ciphertext)

# ---------- 수학 유틸 ----------
def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("no modular inverse")
    return x % m

# ---------- Shor 흉내(Period 찾기 brute-force) ----------
def find_period(N, a):
    # 가장 작은 r: a^r ≡ 1 (mod N)
    for r in range(1, N):
        if pow(a, r, N) == 1:
            return r
    return None

def shor_factor_mock(N, max_trials=200):
    # 실제 Shor과 다르게 클래식하게 r을 때려맞추는 데모용
    for _ in range(max_trials):
        a = random.randrange(2, N - 1)
        g = math.gcd(a, N)
        if g > 1:
            # 공짜로 하나 얻음
            return g, N // g

        r = find_period(N, a)
        if r is None or r % 2 == 1:
            continue

        x = pow(a, r // 2, N)
        if x in (1, N - 1):
            continue

        g1 = math.gcd(x + 1, N)
        g2 = math.gcd(x - 1, N)
        if 1 < g1 < N and 1 < g2 < N:
            return min(g1, g2), max(g1, g2)

    raise RuntimeError("failed to factor N in demo trials")

# ---------- 통합 데모 ----------
def demo(message="time is gold", p=13, q=23):
    print("=== 1) RSA 키 생성 ===")
    rsa = RSA_BASE(p=p, q=q)
    print(f"p={rsa.p}, q={rsa.q}")
    print(f"n={rsa.n}, phi={rsa.phi}")
    print(f"e={rsa.e}, d={rsa.d}")

    print("\n=== 2) 암호화 ===")
    ct = rsa.encrypt(message)
    print("plaintext :", message)
    print("ciphertext:", ct)

    print("\n=== 3) Shor 흉내로 n 인수분해 ===")
    f1, f2 = shor_factor_mock(rsa.n)
    print(f"factored n={rsa.n} -> ({f1}, {f2})")

    print("\n=== 4) p,q로 d 재복구 & 복호화(공격자 시나리오) ===")
    phi_rec = (f1 - 1) * (f2 - 1)
    d_rec = modinv(rsa.e, phi_rec)
    recovered = "".join(chr(pow(c, d_rec, rsa.n)) for c in ct)
    print(f"recovered d = {d_rec}")
    print("decrypted  :", recovered)

if __name__ == "__main__":
    demo()  # 기본 메시지 & (13,23)
