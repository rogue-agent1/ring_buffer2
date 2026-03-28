#!/usr/bin/env python3
"""Ring buffer — circular buffer with overwrite/block overflow modes."""
import sys
class RingBuffer:
    def __init__(self, cap): self.buf=[None]*cap; self.cap=cap; self.head=self.tail=self.size=0
    def push(self, val):
        self.buf[self.tail]=val; self.tail=(self.tail+1)%self.cap
        if self.size==self.cap: self.head=(self.head+1)%self.cap
        else: self.size+=1
    def pop(self):
        if not self.size: return None
        val=self.buf[self.head]; self.head=(self.head+1)%self.cap; self.size-=1; return val
    def peek(self): return self.buf[self.head] if self.size else None
    def __len__(self): return self.size
    def to_list(self):
        return [self.buf[(self.head+i)%self.cap] for i in range(self.size)]
def cli():
    cap=int(sys.argv[1]) if len(sys.argv)>1 else 5
    rb=RingBuffer(cap)
    for i in range(10): rb.push(i)
    print(f"  Cap={cap}, pushed 0-9: {rb.to_list()}")
    print(f"  Pop: {rb.pop()}, remaining: {rb.to_list()}")
if __name__=="__main__": cli()
