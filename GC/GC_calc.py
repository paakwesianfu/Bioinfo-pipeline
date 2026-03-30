#!/bin/usr/env python3

# Calculate the GC content of a sequence
seq = open("sequence.txt").read().strip().upper()
gc = seq.count("G") + seq.count("C")
total = len(seq)
print("The sequence GC content is :", (gc / total) * 100)

