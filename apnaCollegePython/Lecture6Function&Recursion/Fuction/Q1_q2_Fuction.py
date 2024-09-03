# q1 WAf to print the length of a list .
cities =["delhi","pune","madura","channai"]
states =["madhaya Pradesh", "Uttarpradesh","Chhatishgarh","Rajsthan"]

def calu_len(list):
    len(list)
    print(len(list))
    return len(list)
calu_len(states)
# q2 waf to print the element of a list in a single line .
def one_line_print(list):
    for item in list:
        print(item,end=" ")
one_line_print(states)