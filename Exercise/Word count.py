countries = ["India", "United States", "Australia", "Ireland", "Sri lanka",
             "Iceland", "Cuba", "Iran", "Poland"]

# Count all the countries which are starting with "i".
# Also, print all the countries as a list [india ireland iceland iran]
# print("USED A LIST TO PRINT ANOTHER LIST FOR COUNTRIES WITH THE HELP OF LOOPS, FUNCTIONS LIKE APPEND AND STARTSWITH.")

counter = 0
output = []
for country in countries:
    if country.startswith("I"):
        counter = counter + 1
        output.append(country)

print(f"The number of countries start with letter I: {counter} ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"list of countries starts with letter I is: {output}")