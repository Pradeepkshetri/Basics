file= open('demo.txt','w')
file.write("Hello guys, what have you been doing?")
file.close()

file= open('demo.txt','a')
file.write("I am trying to write this on the next line.")
file.close()

file=open('demo.txt','r')
content= file.read()
print(content)
file.close()

