# Tuple (tuple) → Immutable (cannot change values once created)
# a = (11, 22, "dev")
# a[2] = "ops"   #  Error: tuples are immutable

# =======================================================

# List (list) → Mutable (values can be changed)
a2 = [11, 22, "dev"]
a2[2] = "ops"   # works
print(a2)

# ============================================================================

# Set (set) → Mutable but unordered & unindexed

# a3 = {11,22,"dev"}
# a3[2] = "ops"   # sets have no index

# ================================================================================
#  String (str) → Immutable

a4 = "dev"
print(a4.replace("dev","ops"))
print(a4)   # still dev

### You must reassign it if you want the change:

a4 = a4.replace("dev", "ops")
print(a4)  # ops

# ============================================================================

# Dict (dict) -> Mutable (values can be changed using keys)

d = {"name":"dev"}
d["name"] = "ops"
print(d)     # {'name' : 'ops'}

# =========================================================================

# set -> Mutable, but does not allow duplicates and you can only add/remove items (no indexing)

s = {1,2,3}
s.add(4)   #
s.remove(2)  # 

# =====================================================================
# Frozen set (frozenset) → Immutable version of set.

fs = frozenset([1,2,3])
# fs.add(4)     # Error can not change
#===========================================================================================

# Final Rule of Thumb (for interviews)

# Immutable: tuple, string, frozenset, int, float, bool

# Mutable: list, dict, set