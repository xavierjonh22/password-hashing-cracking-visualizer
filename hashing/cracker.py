import hashlib
import time
from hashing.hasher import hash_all
from hashing.hasher import hash_md5

def dictionary_cracker(target):
    start_time = time.perf_counter()
    attempts = 0
    max_attempts = 500
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as wordlist:
        for line in wordlist:
            if attempts <= max_attempts:
                elapsed = (time.perf_counter() - start_time) * 1000
                return None, elapsed, attempts
            guess = line.strip()
            result = hash_all(guess)
            if result[4][1] == target:
                elapsed = (time.perf_counter() - start_time) * 1000
                return guess, elapsed, attempts
            attempts += 1

    return None, None, attempts
def crack_md5(target):
    start_time = time.perf_counter()
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as wordlist:
        for line in wordlist:
            guess = line.strip()
            result = hash_md5(guess)
            if result[1] == target:
                elapsed = (time.perf_counter() - start_time) * 1000
                return guess, elapsed
    return None, None