import os
print("Test a path exists or not:")
#C:\Users\ASUS\Desktop\PP2
path = 'C:\Users\Замир\Desktop\Zama\lab6\dir\text'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))