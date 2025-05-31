# try:
#     file = open('hello.txt', 'w', encoding='utf-8')
#     file.write('Hello world!')
# finally:
#     file.close()

# with open('hello.txt', 'w', encoding='utf-8') as file:
#     file.write('hello world!')
# print('end')

# with open('input.txt', 'r') as in_file, open('output.txt', 'w') as out_file:
#     pass


# class WritableFile:
#     def __init__(self, file_path):
#         self.file_path =file_path
    
#     def __enter__(self):
#         self.file_obj = open(self.file_path, 'w')
#         return self.file_obj
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file_obj:
#             self.file_obj.close()

from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, 'w')
    try:
        yield file
    finally:
        file.close()