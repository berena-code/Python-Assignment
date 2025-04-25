#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Read from a file
#with open("practice.txt", "r") as file:
   # data = file.read()
   # print("Original Data:")
   # print(data)
# Modify the data
#modified_data = data.replace("old", "new")
# Write to a new file
#with open("modified_practice.txt", "w") as new_file:
   # new_file.write(modified_data)
    #print("Modified Data written to modified_practice.txt")




#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.


def read_and_modify_file():
    try:
        # The file name is hardcoded as "practice.txt"
        filename = "practice.txt"

        # Read and modify the content
        with open(filename, "r") as file:
            content = file.read().upper()  # Convert content to uppercase

        # Write modified content to a new file
        with open("modified_" + filename, "w") as new_file:
            new_file.write(content)

        print("Modified content written to 'modified_" + filename + "'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Run the function
read_and_modify_file()
