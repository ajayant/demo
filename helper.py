import riak

live = riak.RiakClient(protocol='pbc', nodes=[{'host':'192.168.21.235','pb_port':8087}])

key_bucket = live.bucket('UUID_KEYS')

mybucket = live.bucket('device_profile', bucket_type='device_profile_bucket_type')

list1 = mybucket.get_keys()

x = key_bucket.new( key = 'device_profile' , data = list1 )
x.store()

print 'keys stored'


