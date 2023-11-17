def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + "さん"
    return names
before_names = ["松田","浅木","工藤"]
copied_names = before_names.copy()
copied_names = before_names[:]
for n in before_names:
    copied_names.append(n)
after_names = add_suffix(copied_names)
print(f"さん付け後:{after_names[0]}")
print(f"さん付け前:{before_names[0]}")