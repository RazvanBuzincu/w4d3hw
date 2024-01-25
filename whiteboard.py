# Create a function that given a list which represents street lights 
# given as a parameter(lights), determine if an outage has occurred. 
# A street with a total number of "F" greater than or equal to 2 returns 
# "Outage", anything below returns "Power"

# Example Input: lights = [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

# Example Input: lights = ['T', 'F', 'T']
# Example Output: "Power"

def lights1(t):
    outage = 0
    for i in t:
        if i == 'F':
            outage += 1
    if outage >= 2:
        return "Outage"
    if outage <= 2:
        return "power"
print(lights1(['T', 'F','F','F']))
print(lights1(['T','F','T']))