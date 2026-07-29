def read_file(file_name):
    with open(file_name,"r") as file:
        contents = file.read()
    print(contents)
    return contents

def read_file_into_list(file_name):
    lines = []
    with open(file_name,"r") as file:
        for line in file:
            lines.append(line)
    return lines
    


def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split("\n")[0]
    with open(output_filename,"w") as file:
        file.write(first_line)
    


def read_even_numbered_lines(file_name):
    lines = []
    with open(file_name,"r") as file:
        for i,line in enumerate(file,start=1):
            if 1%2 == 0:
                lines.append(line)
    return lines
    


def read_file_in_reverse(file_name):
    with open(file_name,"r") as file:
        lines = file.readlines()
    lines.reverse()
    print(lines)
    return lines
    

def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)
    
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()
