input_a=int(input("请输入三角形第一条边的边长:"))
input_b=int(input("请输入三角形第一条边的边长:"))
input_c=int(input("请输入三角形第一条边的边长:"))
p=(input_a+input_b+input_c)/2
if input_a+input_b<=input_c:
    print("无法构成一个三角形")
elif input_a+input_c<=input_b:
    print("无法构成一个三角形")
elif input_b+input_c<=input_a:
    print("无法构成一个三角形")
else:
    print("三角形的周长是：",input_a+input_b+input_c,"三角形的面积是：",(p*(p-input_a)*(p-input_b)*(p-input_c))**0.5)