# # davaleba 1
# file_path = "sample_file.txt"
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write("Hello, this is a sample text.\nThis is another line.")
# print(f"Text has been written to {file_path}")
# # davaleba 2
# file_path = "sample_file.txt"
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write("Hello, this is a sample text.\nThis is another line.")
#
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
# print("File Content:")
# print(content)
# char_count = len(content)
# print(f"Character count: {char_count}")
#
# # davaleba 3
# file_path = "sample_file.txt"
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write("Hello, this is a sample text.\nThis is another line.")
#
# text_to_append = "\nThis is some appended text!"
# with open(file_path, 'a', encoding='utf-8') as file:
#     file.write(text_to_append)
# print(f"Text has been appended to {file_path}")
#
# # davaleba 4
# source_file = "sample_file.txt"
# destination_file = "copied_file.txt"
#
# with open(source_file, 'w', encoding='utf-8') as f:
#     f.write("Hello, this is a sample text.\nThis is another line.")
#
# with open(source_file, 'r', encoding='utf-8') as source:
#     content = source.read()
#
# with open(destination_file, 'w', encoding='utf-8') as destination:
#     destination.write(content)
# print(f"Content from {source_file} has been copied to {destination_file}")
#
# # davaleba 5
# file1 = "sample_file.txt"
# file2 = "copied_file.txt"
# combined_file = "combined_file.txt"
#
# with open(file1, 'w', encoding='utf-8') as f:
#     f.write("Hello, this is a sample text.\nThis is another line.")
#
# with open(file2, 'w', encoding='utf-8') as f:
#     f.write("This is the content from the copied file.\n")
#
# with open(file1, 'r', encoding='utf-8') as f1:
#     content1 = f1.read()
#
# with open(file2, 'r', encoding='utf-8') as f2:
#     content2 = f2.read()
#
# with open(combined_file, 'w', encoding='utf-8') as combined:
#     combined.write(content1 + "\n" + content2)
# print(f"Contents of {file1} and {file2} have been combined into {combined_file}")
#
# # davaleba 6
# file_path = "sample_file.txt"
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write("Hello, this is a sample text.\nThis is another line.")
#
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
#
# print(content.upper())


