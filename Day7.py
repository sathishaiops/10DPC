# Examples of Set and frozenset iteration

skill = { "Java", "C++", "Python", "JavaScript"}
print("Initial set:", skill)

required_skills = {"Machine Learning", "Data Analysis"}
skill.update(required_skills)
print("After update():", skill)

common_skills = skill & required_skills
print("Common skills:", common_skills)

# Create an immutable frozenset from the current set
frozenset_skills = frozenset(skill)
print("Frozenset skills (immutable snapshot):", frozenset_skills)

# Iterate over the frozenset
print("\nIterating over frozenset_skills:")
for s in frozenset_skills:
    print("-", s)

# Demonstrate that frozenset is immutable (attempting .add will raise AttributeError)
try:
    frozenset_skills.add("SQL")  # will raise AttributeError
except AttributeError:
    print("\nCannot modify frozenset: it is immutable (AttributeError raised).")

# The original set can still be modified; the frozenset snapshot does not change
skill.add("SQL")
print("\nOriginal set after adding 'SQL':", skill)
print("Frozenset remains unchanged:", frozenset_skills)


