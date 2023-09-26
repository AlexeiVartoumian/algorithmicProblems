"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.
"""
#check for three things 1 its well formed
#numbers are in range
# no trailing zeroes at the front . if val is zero only one allowed.
def solution(inputString):
    
    
    thing = inputString.split(".")

    
    
    if len(thing) != 4:
        return False
    
   
    for i in thing:
        if not i.isnumeric():
            return False
        
        if int(i) <0 or int(i) >255:
            return False
        
        elif len(i) > 1 and i[0] == "0":
            return False
    
    return True