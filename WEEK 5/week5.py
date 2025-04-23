# Ask the user to enter the file name
filename = input("Enter the name of the file you want to read: ")
try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()
        print("📄 Original content:")
        print(content)

except FileNotFoundError:
    print("❌ The file was not found. Please check the filename and try again.")
    # Modify the content (e.g., make it uppercase)
    modified_content = content.upper()

    # Create a new filename
    new_filename = "modified_" + filename

    # Write the modified content to the new file
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"✅ Success! Modified content saved to '{new_filename}'.")
except PermissionError:
    print("❌ Permission denied. You do not have permission to read this file.")