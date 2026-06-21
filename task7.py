# 1. Create a Python program that initializes an empty dictionary to store user profiles
# Keys: User IDs, Values: User Names
user_profiles = {}
print("Initial empty dictionary:", user_profiles)
print("-" * 50)


# 2. Implement a function to add a new user profile to the dictionary
def add_user(user_id, name):
    user_profiles[user_id] = name
    print(f"Added User ID {user_id}: {name}")
    print("Current Dictionary:", user_profiles)


# 3. Implement a function to retrieve a user's name by their ID
def get_user_name(user_id):
    # Checking if ID exists using .get() or 'in' operator to handle missing keys
    if user_id in user_profiles:
        name = user_profiles[user_id]
        print(f"Retrieved - User ID {user_id} belongs to: {name}")
        return name
    else:
        print(f"Error: User ID {user_id} not found in the dictionary.")
        return None


# 4. Implement a function to update an existing user's name, given their ID and new name
def update_user_name(user_id, new_name):
    if user_id in user_profiles:
        old_name = user_profiles[user_id]
        user_profiles[user_id] = new_name
        print(f"Updated User ID {user_id}: Changed from '{old_name}' to '{new_name}'")
        print("Current Dictionary:", user_profiles)
    else:
        print(f"Error: Cannot update. User ID {user_id} does not exist.")


# 5. Implement a function to remove a user profile by their ID
def remove_user(user_id):
    if user_id in user_profiles:
        removed_name = user_profiles.pop(user_id)
        print(f"Removed User ID {user_id}: {removed_name}")
        print("Current Dictionary:", user_profiles)
    else:
        print(f"Error: Cannot remove. User ID {user_id} not found.")


# =====================================================================
# 6. Test each function with sample data to demonstrate their correctness
# =====================================================================
print("\n--- Testing Add Function ---")
add_user(101, "Laxmi")
add_user(102, "Tejaswi")
add_user(103, "Naveen")

print("\n--- Testing Retrieve Function ---")
get_user_name(102)     # Existing ID
get_user_name(999)     # Non-existing ID (handles missing case)

print("\n--- Testing Update Function ---")
update_user_name(101, "S. Laxmi") # Existing ID
update_user_name(555, "Stranger") # Non-existing ID

print("\n--- Testing Remove Function ---")
remove_user(103)       # Existing ID
remove_user(999)       # Non-existing ID (handles missing case)

print("\nFinal resulting dictionary:", user_profiles)