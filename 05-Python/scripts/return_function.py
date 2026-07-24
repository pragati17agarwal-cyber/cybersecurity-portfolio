#  A q a 1 z
#return = statement used to end function and 
# send a result back to caller
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Bro", "code")
print(full_name)
full_name = create_name("Captain", "Underpants")
print(full_name)
