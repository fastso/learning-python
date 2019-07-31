import sys

# print(sys.version_info)
# print(sys.version)

# str to bytes
str_sample = 'あいう'
bytes_result = str_sample.encode('utf-8')

# bytes to str
bytes_sample = b'\xe3\x81\x82\xe3\x81\x84\xe3\x81\x86'
str_result = bytes_sample.decode('utf-8')

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i, flavor in enumerate(flavor_list, start=1):
    print('%d: %s' % (i, flavor))

for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i, flavor))
