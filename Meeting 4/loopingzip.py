names = ["Vittorino","Timoteo","Martin"]
ages = [20,22,24]
overall = [87,85,80]

biodata = zip(names,ages,overall)
print(biodata)

for name , ages , overall in zip(names,ages,overall):
    print(f"nama saya {name} dan umur saya {ages} dan overall saya {overall}")