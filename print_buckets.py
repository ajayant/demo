import riak

live = riak.RiakClient(protocol='pbc', nodes=[{'host':'192.168.21.235','pb_port':8087}])

bucket1 = live.bucket('UUID_KEYS')

list1 = bucket1.get('device_profile').data

print 'Enter Key: '
z = raw_input()
y = z
data_bucket = live.bucket('device_profile', bucket_type='device_profile_bucket_type')

for x in list1:
	if( x == z):
		print( data_bucket.get(x).data )

print 'delete key[y/n] : '
z = raw_input()
if z == 'y' :
	for x in list1:
		if ( x == y ) :
			data_bucket.get(x).delete()

print 'clear bucket[y/n] : '
z = raw_input()
if z == 'y' :
	for x in list1 :
		data_bucket.get(x).delete()



