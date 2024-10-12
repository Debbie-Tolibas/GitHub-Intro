Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello, World!")
Hello, World!
name = input("Enter your name: ")
print(f"Hello, {name}!")
SyntaxError: multiple statements found while compiling a single statement
 name = input("Enter your name: ")
    print("Hello, " + name + "!")
    
SyntaxError: unexpected indent
name = input("Enter your name: ")
    print("Hello, " + name + "!")
    
SyntaxError: multiple statements found while compiling a single statement
name = input("Enter your name: ") print("Hello, " + name + "!")
SyntaxError: invalid syntax
name = input("Enter your name: "); print("Hello, " + name + "!")
Enter your name: Debbie
Hello, Debbie!
