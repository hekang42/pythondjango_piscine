import sys
def read_file():
    myfile = open("periodic_table.txt", 'r')
    lines = myfile.readlines()
    myfile.close()
    return lines

def html_header():
    header = \
        "<!DOCTYPE html>\r\n<html lang=\"en\">\r\n\t<head>\r\n\t\t<title>\
        \r\n\t\tperiodic_table\r\n\t\t</title>\
        \r\n\t</head>\r\n\t<body>\r\n\t\t<table style=\"width:100%\">\r\n"
    return header

def html_footer():
    footer = \
        "\t\t</table>\r\n\t</body>\r\n</html>"
    return footer

def box(line):
    words = line.split(",")
    name = words[0].split(" ")[0]
    # print(name)
    position = words[0].split(":")[1]
    # print(position)
    number = words[1].split(":")[1]
    # print(number)
    small = words[2].split(" ")[2]
    # print(small)
    molar = words[3].split(":")[1]
    # print(molar)
    box_list = [name, position, number, small, molar]
    # print(box_list)
    return box_list

def empty_box():
    string = ""
    string = string + "\t\t\t\t<td></td>\r\n"
    return string

def filled_box(name, position, number, small, molar):
    string = ""
    if int(position) == 0:
        string = "\t\t\t<tr>\r\n"
    string = string + "\t\t\t\t<td style=\"border: 1px solid black; width:5%; text-align:center;\">\r\n\
        \t\t\t<h4>"+ name +"</h4>\r\n\
        \t\t\t<ul style=\"text-align: left;\">\r\n\
        \t\t\t\t<li>No."+ number +"</li>\r\n\
        \t\t\t\t<li>"+ small +"</li>\r\n\
        \t\t\t\t<li>"+ molar +"</li>\r\n\
        \t\t\t</ul>\r\n\
        \t\t</td>\r\n"
    if int(position) == 17:
        string = string + "\t\t\t</tr>\r\n"
    return string

def make_body(b_list):
    cnt = 0
    box_cnt = 0

    string = ""
    temp = 0

    for cnt in range(0, 18 * 7):
        if (cnt == (int(b_list[box_cnt][1]) + temp)):
            string = string + filled_box(b_list[box_cnt][0], b_list[box_cnt][1], b_list[box_cnt][2], b_list[box_cnt][3], b_list[box_cnt][4])
            box_cnt += 1
            if (cnt - temp == 17):
                temp += 18
        else:
            string = string + empty_box()
            # print(empty_box())
    return string


def make_table():
    lines = read_file()
    body_list = []
    for line in lines:
        body_list.append(box(line))
        # body += "".join(box(line))
    # print(body_list)
    body = make_body(body_list)

    # print(body)
    header = html_header()
    footer = html_footer()
    # ret = header + footer
    # # print(ret)
    ret = header + body + footer
    f = open("./result.html", 'w')
    f.write(ret)
    f.close()

    # print(ret)


if __name__ == '__main__': make_table() 