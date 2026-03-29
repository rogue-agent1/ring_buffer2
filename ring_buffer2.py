#!/usr/bin/env python3
"""Ring buffer: fixed-size circular queue with overwrite policy."""
import sys

class RingBuffer:
    def __init__(self, capacity):
        self.cap = capacity; self.buf = [None]*capacity
        self.head = 0; self.tail = 0; self.size = 0; self.overflows = 0
    def push(self, item):
        self.buf[self.tail] = item; self.tail = (self.tail + 1) % self.cap
        if self.size == self.cap:
            self.head = (self.head + 1) % self.cap; self.overflows += 1
        else: self.size += 1
    def pop(self):
        if self.size == 0: return None
        item = self.buf[self.head]; self.buf[self.head] = None
        self.head = (self.head + 1) % self.cap; self.size -= 1
        return item
    def peek(self): return self.buf[self.head] if self.size > 0 else None
    def is_full(self): return self.size == self.cap
    def is_empty(self): return self.size == 0
    def to_list(self):
        result = []
        idx = self.head
        for _ in range(self.size):
            result.append(self.buf[idx]); idx = (idx + 1) % self.cap
        return result
    def stats(self):
        return {"size":self.size,"capacity":self.cap,"overflows":self.overflows,
                "utilization":f"{self.size/self.cap*100:.0f}%"}

def main():
    rb = RingBuffer(5)
    for i in range(8): rb.push(i)  # will overflow 3 times
    print(f"  After pushing 0-7 into size-5 buffer: {rb.to_list()}")
    print(f"  Stats: {rb.stats()}")
    print(f"  Pop: {rb.pop()}, {rb.pop()}")
    print(f"  After 2 pops: {rb.to_list()}")
    rb.push(100); rb.push(200)
    print(f"  After 2 more pushes: {rb.to_list()}")

if __name__ == "__main__": main()
