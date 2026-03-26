names = []

# Take input for multiple names separated by commas
input_names = input("Enter names (each consisting of first and last name separated by a space):\n").split(",")


# Add the names to the list
for name in input_names:
    names.append(name.strip().split())  # Split each name into parts (first and last name)

# Print the full names
print("\nFull Names:")
for full_name in names:
    print(" ".join(full_name))

# Print the initials
print("\nInitials:")
for full_name in names:
    first_initial = full_name[0][0]  # First letter of the first name
    last_initial = full_name[1][0]    # First letter of the last name
    print(f"{first_initial}.{last_initial}.")
