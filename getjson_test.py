from preprocess_json import get_json

d = get_json('rawstream2.json')

print(d[0]['day'])
print(d[0]['hh'])
print(d[0]['created_at'])
# print(d[0])
