from pprint import pprint

device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

# SIMPLE PRINT
print("\n______SIMPLE PRINT________________")
print("device:", device)
print("device name:", device["name"])

# PRETTY PRINT
print("\n_______PRETTY PRINT____________")
pprint(device)


# FOR LOOP, NICELY FORMATTED PRINT
print("\n_____FOR LOOP, USING F-STRING______")
for key, value in device.items():
    print(f"{key:>16s} : {value}")



