import textwrap # xử lý định dạng văn bản như ngắt dòng hoặc rút gon chuỗi
for i in range(int(input())):
    print(textwrap.shorten(input(), width = 100, placeholder = ''))