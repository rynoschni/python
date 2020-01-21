staff = ["Sean", "David", "Mary Ella", "Liz", "Nat", "Jake", "Tasha", "Max"]

print(staff)

if "Sean" in staff:
    staff.remove("Sean")
    staff.insert(0, "Ranger")

print(staff)

if "David" in staff:
    indexOfDavid = staff.index("David")
    staff.insert(indexOfDavid, "Not David")
    staff.remove("David")

print(staff)
