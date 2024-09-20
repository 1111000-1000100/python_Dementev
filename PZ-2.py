def full_kilobytes(file_size_bytes):
    kilobytes = file_size_bytes // 1024
    return kilobytes

file_size = int(input("Введите размер файла в байтах: "))

full_kilobytes = full_kilobytes(file_size)
print(f"Количество полных килобайтов, занимаемых файлом: {full_kilobytes} кБ")