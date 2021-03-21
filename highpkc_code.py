import operator

number_employees = 0
found_goodies = 0
goodies = dict()

# store the contents of the input file
input_file = open("sample_input.txt")

input_split = input_file.readlines()

input_file.close()

#print
#print("input list: ", input_split)
#print

# generate the goodies dictionary
for i in input_split:
    i = i.replace('\n', '')
    input_entries = i.split(":")
    #print("entry: ", input_entries, "len: ", len(input_entries))

    if len(input_entries) < 2:
        continue

    if number_employees == 0:
        if 'Number of employees' == input_entries[0]:
            number_employees = int(input_entries[1])
            print("Number of employees: ", number_employees)

        continue

    if (number_employees > 0) and (found_goodies == 0):
        if 'Goodies and Prices' in input_entries:
            found_goodies = 1
            print("found goodies")

        continue

    goodies[input_entries[0]] = int(input_entries[1])

# check if the number of employees and goodies list are actualy
# present as per the problem statement format. If not present
# the input file is coorupted and we should exit ASAP

if (number_employees == 0):
    print("error: number of employees not provided. exit !!!")
    exit

if (found_goodies == 0):
    print("error: goodies list is provided as per format. exit !!!")
    exit

#print("goodies dict: ", goodies)

# sort the goodies in ascending order based on value
# a tuple is generated
goodies = sorted(goodies.items(), key=lambda x: x[1])
#print
#print("sorted goodies tuple: ", goodies)
#print

# create a dict from ordered tuple
goodies = {k: v for k, v in goodies}
#print
#print("sorted goodies dict: ", goodies)
#print


window = number_employees - 1
num_goodies = len(goodies)

# check if the number of employees is greater than the number of goodies we have.
# If greater we have no way to distribute, exit
if window > num_goodies:
    print("error: number of employees ", number_employees, " greater than the goodies ", num_goodies, "exit !!!")
    exit

goodies_key = list(goodies.keys())
#print
#print("goodies key list: ", goodies_key)
#print
goodies_value = list(goodies.values())
#print
#print("goodies value list: ", goodies_value)
#print

min_index = 0
min_value = goodies_value[window] - goodies_value[0]
print
print("intial: min index ", min_index, "min value ", min_value)
print
# find the goodies window that has the minimum price difference and set
# the min_index and min_value accordingly
for i in range(num_goodies):
    if (i + window) > (num_goodies - 1):
        break

    value = goodies_value[i + window] - goodies_value[i]

    if value < min_value:
        min_value = value
        min_index = i

    print("value ", value, "min value ", min_value, "min index ", min_index)

#print
print("final: min index ", min_index, "min value ", min_value)
#print

# generate the output file as specified in the problem statement
output_file = open("sample_output.txt", "w")

output_file.write("The goodies selected for distribution are:\n")
output_file.write("\n")

for i in range(min_index, min_index + number_employees):
    output_file.write(str(goodies_key[i]) + ": " + str(goodies_value[i]) + "\n")

output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is " + str(min_value))

output_file.close()
