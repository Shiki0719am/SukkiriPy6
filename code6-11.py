names = []
print(f"変更前のlistのidentity:{id(names)}")
names.append("松田")
print(f"変更後のlistidentity:{id(names)}")

name = "松田"
print(f"変更前のstrのidentity:{id(name)}")
name = "スーパー"+"松田"
print(f"変更後のstrのidentity{id(name)}")