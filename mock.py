import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE)
print(response.json())

# input("Press Enter for the next")
#
# payload = {'value': 'value1', 'mode': 'value2', "replace_with": "null"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {'value': 'value1', 'mode': 'value2', "wrong_key": "null"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {'value': 'value1', 'mode': 'value2', "replace_with": "--original--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {'value': 'value1', 'mode': 'value2', "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {'value': 'value1', 'mode': 'name', "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {'value': 'value1', 'mode': 'phone', "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {'value': 'value1', 'mode': 'amount', "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {"value": "(512) 234-9293", "mode": "phone", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {"value": "unknown", "mode": "phone", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {"value": "unknown", "mode": "phone", "replace_with": "--original--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {"value": "Robert Lance Smith", "mode": "name", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "12234", "mode": "name", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "-12234", "mode": "name", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "unknown", "mode": "name", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": " ", "mode": "name", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
# input("Press Enter for the next")
#
# payload = {"value": "Robert Lance Smith", "mode": "name", "replace_with": "--original--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "12234", "mode": "name", "replace_with": "--original--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "unknown", "mode": "name", "replace_with": "--original--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": " ", "mode": "name", "replace_with": "--original--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "2 * 2", "mode": "amount", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "3.14159 + 2", "mode": "amount", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "dir()", "mode": "amount", "replace_with": "--blank--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())
#
#
# input("Press Enter for the next")
#
# payload = {"value": "dir()", "mode": "amount", "replace_with": "--original--"}
# print("The payload", payload)
# r = requests.post(BASE, data=payload)
# print(r.json())

#
input("Press Enter for the next")

payload = {"value": "$12,345.6", "mode": "amount", "replace_with": "--blank--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())

input("Press Enter for the next")

payload = {"value": "Hello World", "mode": "amount", "replace_with": "--blank--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())

input("Press Enter for the next")

payload = {"value": "35", "mode": "amount", "replace_with": "--blank--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())


input("Press Enter for the next")

payload = {"value": "", "mode": "amount", "replace_with": "--blank--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())


input("Press Enter for the next")

payload = {"value": "$12,345.6", "mode": "amount", "replace_with": "--original--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())


input("Press Enter for the next")

payload = {"value": "Hello World", "mode": "amount", "replace_with": "--original--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())


input("Press Enter for the next")

payload = {"value": "35", "mode": "amount", "replace_with": "--original--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())


input("Press Enter for the next")

payload = {"value": "", "mode": "amount", "replace_with": "--original--"}
print("The payload", payload)
r = requests.post(BASE, data=payload)
print(r.json())

print("Fin")

