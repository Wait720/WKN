import re
s=input("Введіть рядок:")
s2="".join(re.split("[^a-z]*",s))
s3="".join(re.split("[^A-Z]*",s))
print(s2)
print(s3)
print("Довжина s2",len(s2))
print("Довжина s3",len(s3))