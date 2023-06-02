#functions with output
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You're missing an argument"
    return (f_name + " " + l_name).title()

print(format_name("luKas", "hAusEr"))

#function with multiple outputs
def format_name2(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You're missing an argument"
    return f_name.title(), l_name.title()

formated_f_name, formated_l_name = format_name2("LuKa", "miKUlic")
print(f'{formated_f_name} {formated_l_name}')