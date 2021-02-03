'''
Question 1
First, take a look at the two lists in script.py.

The list names stores the names of ten individuals, and insurance_costs stores their medical insurance costs.

Let’s add additional data to these lists:

    Append a new individual, "Priscilla", to names.
    Append her insurance cost, 8320.0, to insurance_costs.

Question 2
Currently, the names and insurance_costs lists are separate, but we want each insurance cost to be paired with a name.

Create a new variable called medical_records that combines insurance_costs and names into a list using the zip() function.

The list should have the following structure:

[(cost_0, name_0), (cost_1, name_1), (cost_2, name_2), ...]

Question 3
Print out medical_records in the terminal, and make sure the output is what you expected.

Question 4
Let’s explore our medical data.

We want to see how many medical records we’re dealing with. Create a variable called num_medical_records that stores the length of medical_records.

Question 5
Print num_medical_records with the following message:

There are {number of medical records} medical records.

Question 6
Select the first medical record in medical_records, and save it to a variable called first_medical_record.

Question 7
Print first_medical_record with the following message:

Here is the first medical record: {first medical record

Question 8
Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list.

Print the sorted medical_records with the following message:

Here are the medical records sorted by insurance cost: {sorted list}

Question 9
Let’s look at the three cheapest insurance costs in our medical records.

Slice the medical_records list, and store the three cheapest insurance costs in a list called cheapest_three.

Question 10
Print cheapest_three with the following message:

Here are the three cheapest insurance costs in our medical records: {cheapest three}

Question 11
Let’s look at the three most expensive insurance costs in our medical records.

Slice the medical_records list, and store the three most expensive insurance costs in a list called priciest_three

Question 12
Print priciest_three with the following message:

Here are the three most expensive insurance costs in our medical records: {priciest three}

Question 13
Some individuals in our medical records have the same name. For example, the name “Paul” shows up twice.

Count the number of occurrences of “Paul” in the names list, and store the result in a variable called occurrences_paul.

Print occurrences_paul with the following message:

There are {occurrences Paul} individuals with the name Paul in our medical records. 
'''

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs,names))
print(medical_records)

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))

medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

cheapest_three = medical_records[:2]
print("Here are the three cheapest insurance costs in " + str(cheapest_three))

priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

occurrences_paul = names.count("Paul")
print("There are "+ str(occurrences_paul) + " individuals with the name Paul in our medical records")






