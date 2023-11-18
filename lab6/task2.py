from string import ascii_letters as asl


def strfunc(string: str) -> str:
    return ''.join([asl[(asl.index(i)+1) %len(asl)] if i in asl else i for i in string])

assert(strfunc("VolodymyrOleksandrovichZelenskyi"))
print(strfunc("VolodymyrOleksandrovichZelenskyi"))
             
