#Hashmap
#This is the code used to make my own dictionary
#Created by Jessica Ice
#Created on June 11, 2016

#This function make the dictionary or hashmap for you
#he is creating an "aMap" and then putting numbered buckets into the mapping
#Those buckets will hold the content that is put in later.
def new(num_buckets=256):
	""" Initializes a Map with the given number of buckets."""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

#Uses hash function to convert a string to a number
#Once he creates a number for the key then he can use the % function \
#along with the len function to get to a bucket where something new can go
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to
	an index for the aMap's bucket"""
	return hash(key) % len(aMap)
	
#This uses the hash_key to find the bucket that a key could be in. 
#This function lets you know if the bucketid will fit into the aMap list
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
#This uses the get_bucket function to find every bucket that an option could be in and
#then rolls through each of the possible options to find the exact match
#Once it finds the exact match it returns the tuple of (i, k, v) which is 
#the index the key was found in, the key itself, and the value set for that key
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)
	
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, default
	
#This is a convenience function to only return the actual value for the map 
def get(aMap, key, default=None):
	"""Gets the value in a bucket for a given key, or the default."""
	i, k, v = get_slot(aMap, key, default = default)
	return v
	
#This will append a new key and value pair on a particular bucket
#It will find the appropriate bucket and either replace the value if it exists
#or append the value if it does not exist
def set(aMap, key, value):
	""" Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	if i >= 0:
		#the key exists, replace it
		bucket[i] = (key, value)
	else:
		#the key does not, append to create it
		bucket.append((key, value))

#This finds the bucket and deletes it using the key to find it
def delete(aMap, key):
	""" Deletes the given key from the Map."""
	bucket = get_backet(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

#This is a debugging function to print out everything that is in a particular bucket
def list(aMap):
	""" Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
				
				
 
