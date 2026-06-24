import hashlib
import time
import bcrypt

from argon2 import PasswordHasher
ph = PasswordHasher()

def hash_md5(password):
    start_time = time.perf_counter()
    result = hashlib.md5(password.encode()).hexdigest()
    elapsed = (time.perf_counter() - start_time) * 1000
    return "md5", result, elapsed
def hash_sha1(password):
    start_time = time.perf_counter()
    result = hashlib.sha1(password.encode()).hexdigest()
    elapsed = (time.perf_counter() - start_time) * 1000
    return "sha1", result, elapsed
def hash_sha256(password):
    start_time = time.perf_counter()
    result = hashlib.sha256(password.encode()).hexdigest()
    elapsed = (time.perf_counter() - start_time) * 1000
    return "sha256", result, elapsed
def hash_bcrypt(password):
    start_time = time.perf_counter()
    result = bcrypt.hashpw(password.encode(), bcrypt.gensalt(12)).decode()
    elapsed = (time.perf_counter() - start_time) * 1000
    return "bcrypt", result, elapsed
def hash_argon2(password):
    start_time = time.perf_counter()
    result = ph.hash(password)
    elapsed = (time.perf_counter() - start_time) * 1000
    return "argon2", result, elapsed
def hash_all(password):
    step1 = hash_md5(password)
    step2 = hash_sha1(step1[1])
    step3 = hash_sha256(step2[1])
    step4 = hash_bcrypt(step3[1])
    step5 = hash_argon2(step4[1])
    result = [step1, step2, step3, step4, step5]
    return result