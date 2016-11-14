#!/usr/bin/env python
import os.path
import numpy as np
import matplotlib.pyplot as plt

def parser():
	rewards = []
	basePath = os.path.dirname(__file__)
	filePath = os.path.abspath(os.path.join(basePath,"rewards.txt"))
	f = open(filePath,"r")
	lines = f.read().splitlines()
	f.close()

	for i,line in enumerate(lines):
		rewards.append(lines[i])

	plt.plot(rewards, '.')
	plt.show()

def main():
	parser()

main()
