'''
Question 1
First, take a look at the code in script.py.

The function estimate_insurance_cost() estimates the medical insurance cost for an individual, based on five variables:

    age: age of the individual in years
    sex: 0 for female, 1 for male
    bmi: individual’s body mass index
    num_of_children: number of children the individual has
    smoker: 0 for a non-smoker, 1 for a smoker

These variables are used in the following formula to estimate an individual’s insurance cost (in USD):

insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500insurance\_cost = 250*age - 128*sex + 370*bmi + 425*num\_of\_children + 24000*smoker - 12500insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500

Click “Save” to see the estimated insurance costs for three individuals – Maria, Rohan, and Valentina.

Question 2
We want to compare the estimated insurance costs (as calculated by our function) to the actual amounts that Maria, Rohan, and Valentina paid.

Create a list called names and fill it with the names of the individuals you are estimating insurance costs for:

    "Maria"
    "Rohan"
    "Valentina"

Question 3
Next, create a list called insurance_costs and fill it with the actual amounts that Maria, Rohan, and Valentina paid for insurance:

    4150.0
    5320.0
    35210.0

Question 4
Currently the names and insurance_costs lists are separate, but we want each name to be paired with an insurance cost.

Create a new variable called insurance_data that combines names and insurance_costs using the zip() function.

Print this new variable.

Question 5
The output should look something like:

<zip object at 0x7f1631e86b48>

This output does not mean much to us. To change it to a format we can actually understand, we must convert the zip object to a list by doing the following:

list(zip(____, ____))

Convert the insurance_data object to a list using this method. Click “Save” to see the result – you should now see a list of names and insurance costs.

Question 6
Next, create an empty list called estimated_insurance_data.

This is the list we’ll use to store the estimated insurance costs for our three individuals.

Question 7 
We want to add our estimated insurance data for Maria, Rohan, and Valentina to the estimated_insurance_data list.

Use .append() to add ("Maria", maria_insurance_cost) to estimated_insurance_data. Do the same for Rohan and Valentina.

Question 8
Print estimated_insurance_data.

Make sure the output is what you expected.

Question 9
In the output, you should see two lists. The first one represents the actual insurance cost data and the second one represents the estimated insurance cost data.

However, it’s difficult to know this just by looking at the output. As a data scientist, you want to make sure that your data is clean and easy to understand.

Add to the print statement for insurance_data so that it’s clear what the list contains. The output of the print statement should look like:

Here is the actual insurance cost data: [...list output...]

Question 10
Do the same for the print statement that prints estimated_insurance_data. The output should look like:

Here is the estimated insurance cost data: [...list output...]

Question 11
Click “Save” to see the results.

It should be much more clear from the output what each of the two lists represents, helping you better understand the data you’re working with.

You may notice that there are differences between the actual insurance costs and estimated insurance costs. This means that our estimate_insurance_cost() function does not calculate insurance costs with 100% accuracy.

Compare the estimated insurance data to the actual insurance data. Do the estimated insurance costs seem to be overestimated or underestimated?
 -- Based on Maria's insurance data cost it seems overestimated

Question 12
Congratulations! In this project, you used Python lists to store estimated insurance cost data and then compare that data to actual insurance cost data.

As you’ve seen, lists are data structures in Python that can contain multiple pieces of data in a single object. As a data scientist, you’ll find yourself working with this data structure quite often. You now have a solid foundation to move forward in your data science journey!

If you’d like additional practice on lists, here are some ways you might extend this project:

    Calculate the difference between the actual insurance cost data and the estimated insurance cost data for each individual, and store the results in a list called insurance_cost_difference.
    Estimate the insurance cost for a new individual, Akira, who is a 19 year-old male non-smoker with no children and a BMI of 27.1. Make sure to append his name to names and his actual insurance cost, 2930.0, to insurance_costs.

Happy coding!

'''

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
# Added Akira
akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)

names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]

names.append("Akira")
insurance_costs.append(2930.0)

estimated_insurance_data = []
estimated_insurance_data.append("Maria")
estimated_insurance_data.append(maria_insurance_cost)
estimated_insurance_data.append("Akira")
estimated_insurance_data.append(akira_insurance_cost)

insurance_data = list(zip(names, insurance_costs))

print("Here is the actual insurance cost data: " + str(insurance_data))

print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))
