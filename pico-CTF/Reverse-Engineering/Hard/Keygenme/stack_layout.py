import sys

def draw_layout(layout_file:str , sub_rsp: int) -> None:
	with open(layout_file, 'w') as file:
		no_of_qword = sub_rsp // 8
		digit_len_of_qword = len(str(no_of_qword))
		offset_digit_len = len(str(no_of_qword * 8))
		file.write(f"rbp\t\t\t<+{0:<{offset_digit_len}}>\n")

		for qword in range(no_of_qword):
			offset = (qword + 1) * 8
			file.write(f"{no_of_qword - qword:0{digit_len_of_qword}} - QWORD \t\t<-{offset:<{offset_digit_len}}>\n")

def main():
	assert len(sys.argv) > 1 , "script expects <filename> to write stack_layout"
	sub_rsp = int(input("Enter the value subtracted from RSP: "))
	draw_layout(sys.argv[1],sub_rsp)

main()
