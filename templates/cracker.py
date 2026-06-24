import hashlib
import time
from hashing.hasher import hash_all

def dictionary_cracker(target):
    start_time = time.perf_counter()
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as wordlist:
        for line in wordlist:
            guess = line.strip()
            result = hash_all(guess)
            if result[4][1] == target:
                elapsed = (time.perf_counter() - start_time) * 1000
                return guess, elapsed

    return None, None

