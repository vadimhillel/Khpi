def strfunc(str: str) -> str:
    initials = str.split()
    return f"{initials[0][0]}. {initials[1][0]}. {initials[2]}"
    
print(strfunc("Volodymyr Oleksandrovich Zelenskyi"))

