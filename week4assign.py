# File Read & Write Challenge
# Junior Developer Version

def main():
    # Ask user for the input filename
    filename = input("Enter the filename you want to read: ")

    try:
        # Try opening the file in read mode
        with open(filename, "r") as f:
            content = f.read()

        # Modify the content (for example, make everything uppercase)
        modified_content = content.upper()

        # Write the modified content into a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified_content)

        print(f"Modified file has been saved as: {new_filename}")

    except FileNotFoundError:
        # Handle case where file doesn’t exist
        print("Error: File not found. Please check the filename and try again.")

    except PermissionError:
        # Handle case where file can’t be read due to permissions
        print("Error: You don’t have permission to read this file.")

    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
