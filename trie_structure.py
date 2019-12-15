count = 0
class TrieNode():
	def __init__(self, val):
		self.value = val
		self.children = {}
		self.is_word = False
		self.lookup = {}
		
	def add(self, word):
		global count
		obj = self
		index = 0
		for char in word:
			if char not in obj.lookup:
				obj.lookup[char] = count
				new_node = TrieNode(char)
				obj.children[count] = new_node
				count += 1
				obj = new_node
			else:
				obj = obj.children[obj.lookup[char]]
			index += 1
			if index == len(word):
				obj.is_word = True
				
	def find(self, word):
		obj = self
		value = 0
		index = 0
		for char in word:
			if char in obj.lookup:
				value = obj.lookup[char]
				obj = obj.children[obj.lookup[char]]
			else:
				return False, index-1, value, obj
			index += 1
		return True, index-1, value, obj
		
#loading

import itertools
import threading
import time
import sys
from os import system

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

#add words here
#set done to True when finished
