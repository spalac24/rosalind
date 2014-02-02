from sys import stdin,setrecursionlimit

class node (object):
	def __init__ (self):
		self.children = {}
		self.has = set([])
	def add(self, s,app,first):
		if len(s) == 0:
			self.children.get(app,None)
			self.children[app]=node()
		else:
			if (s[0] in self.children):
				self.children[s[0]].add(s[1:],app,first)
				self.has.add(app)
			elif first:
				self.children.get(s[0],None)
				self.children[s[0]] = node()
				self.children[s[0]].add(s[1:],app,first)
		self.has.add(app);
			
	def traverse(self, deep = 0):
		for a,b in self.children.items():
			print " "*deep, a
			b.traverse(deep+4)
	def add_suffixes(self,s,app, first=False):
		if len(s) == 0:
			return
		self.add(s,app,first)
		self.add_suffixes(s[1:],app,first)
	def has_string(self,s):
		if len(s) == 0:
			return '$' in self.children
		if s[0] in self.children:
			return self.children[s[0]].has_string(s[1:])
		return False
	def find(self,s):
		if len(s) == 0:
			return self
		if s[0] in self.children:
			return self.children[s[0]].find(s[1:])
		return None
	def find_deepest(self,lset):
		best_s = ""
		for key,val in self.children.items():
			s = key+val.find_deepest(lset)
			if len(s) > len(best_s):
				best_s = s
		return best_s
	def check(self,n):
		for key,val in self.children.items():
			if len(val.has)!=n:
				self.children.pop(key)
			val.check(n)


setrecursionlimit(2000)
lines = ''.join([i.strip() if i[0]!='>' else '>'for i in stdin.readlines()]).split('>')[1:]
root = node()
for idx,x in enumerate(lines):
	root.add_suffixes(x,"$"+str(idx), first=(idx==0))
	root.check(idx+1)
	#print x
	#root.traverse()
	#print "------"
print root.find_deepest(len(lines))