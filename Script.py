import os

# Create a test file
filename = "test_file.txt"
with open(filename, "w") as f:
    f.write("Hello, this is a test upload via Rclone!")

print(f"{filename} created successfully!")
