filename = "500_nature.txt"  # Replace with the name of your input file
max_lines = 50  # Maximum number of lines per file
dir = "txt_n"
with open(filename, encoding="utf-8") as f:
    file_num = 1
    line_count = 0
    outfile = open("txt_n" + f"/image_{file_num}.txt", "w", encoding="utf-8")
    for line in f:
        if line_count >= max_lines:
            outfile.close()
            file_num += 1
            outfile = open("txt_n" + f"/image_{file_num}.txt", "w", encoding="utf-8")
            line_count = 0
        outfile.write(line)
        line_count += 1
    outfile.close()

# image_160.txt
