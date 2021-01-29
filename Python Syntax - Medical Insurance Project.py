'''
Question 1
Our first step is to create the variables for each factor we will consider when estimating medical insurance costs.
These are the variables we will need to create:
    age: age of the individual in years
    sex: 0 for female, 1 for male*
    bmi: individual’s body mass index
    num_of_children: number of children the individual has
    smoker: 0 for a non-smoker, 1 for a smoker
At the top of script.py, create the following variables for a 28-year-old, nonsmoking woman who has three children and a BMI of 26.2.
'''
# create the initial variables below
age = 28
# 0 for Female, 1 for Male
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

'''
Question 2
After the declaration of the variables, create a variable called insurance_cost that utilizes the following formula:
insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500\begin{aligned} insurance\_cost = 250*age - 128*sex \\ + 370*bmi + 425*num\_of\_children \\ + 24000*smoker - 12500 \end{aligned}insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500​
'''
# Add insurance estimate formula below
insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500)

'''
Question 3
Let’s display this value in an informative way. Print out the following string in the terminal:
"This person's insurance cost is {insurance_cost} dollars."
You will need to use string concatenation, including the str() function to print out the insurance_cost.
'''
# Add print function below
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

'''
Question 4
We have seen how our formula can estimate costs for one individual. Now let’s play with some individual factors to see what role each one plays in our estimation!
Let’s start with the age factor. Using a plus-equal operator, add 4 years to our age variable.
'''
# Age Factor
age += 4

'''
Question 5
Now that we have changed our age value, we want to recalculate our insurance cost. Declare a new variable called new_insurance_cost underneath the expression that increased age by 4.
Make sure you leave the line with the insurance_cost variable the same. We will use it later in our program!
'''
# New Insurance Cost
new_insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500)

'''
Question 6
Next, we want to find the difference between our new_insurance_cost and insurance_cost. To do this, let’s create a new variable called change_in_insurance_cost and set it equal to the difference between new_insurance_cost and insurance_cost.

Note: depending on the order that we subtract (eg., new_insurance_cost - insurance cost vs. insurance_cost - new_insurance_cost), we’ll get a positive or negative version of the same number. To make this difference interpretable, let’s calculate new_insurance_cost - insurance_cost. Then we can say, “people who are four years older have estimated insurance costs that are change_in_insurance_cost dollars different, where the sign of change_in_insurance_cost tells us whether the cost is higher or lower.
'''

#Change in Insurance Costs
change_in_insurance_cost = new_insurance_cost - insurance_cost

'''
Question 7
We want to display this information in an informative way similar to the output from instruction 3. On the next line, print the following string in the terminal, where XXX is replaced by the value of change_in_insurance_cost:

"The change in cost of insurance after increasing the age by 4 years is XXX dollars."

Doing this will tell us how 4 years in age affects medical insurance cost estimates assuming that all other variables remain the same.
You will need to concatenate strings and use the str() method
'''
#Print the string 
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

'''
Question 8
Now that you have looked at the age factor, let’s move onto another one: BMI. First, we have to redefine our age variable to be its original value.

Set age to 28 following your last piece of code. This will reset its value and allow us to focus on just the change in the BMI factor moving forward.

On the next line, using the plus-equal operator, add 3.1 to our bmi variable.
'''
# BMI Factor
age = 28
bmi += 3.1 

'''
Question 9
Now let’s find out how a change in BMI affects insurance costs. Our next steps are pretty much the same as we have done before when looking at age.

    Below the line where bmi was increased by 3.1, rewrite the insurance cost formula and assign it to the variable 
    name new_insurance_cost.

    Save the difference between new_insurance_cost and insurance_cost in a variable called change_in_insurance_cost

    Display the following string in the output terminal, where XXX is replaced by the value of 
    change_in_insurance_cost:

"The change in estimated insurance cost after increasing BMI by 3.1 is XXX dollars."

You can leave the code above it as is, including the print statements.
'''
# Create the string
new_insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500)
# Change in Insurance Costs
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Print the string
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")


'''
Question 10
Let’s look at the effect sex has on medical insurance costs. Before we make any additional changes, first reassign your bmi variable back to its original value of 26.2.

On a new line of code, reassign the value of sex to 1. A reminder that 1 identifies male individuals and 0 identifies female individuals.
'''
# Male vs. Female Factor
bmi = 26.2
sex = 1

'''
Question 11
Perform the steps below!
    Rewrite the insurance cost formula and assign it to the variable name new_insurance_cost.
    Save the difference between new_insurance_cost and insurance_cost in a variable called change_in_insurance_cost.
    Display the following string in the output terminal, where XXX is replaced by the value of 
    change_in_insurance_cost:
"The change in estimated cost for being male instead of female is XXX dollars."
'''
# Create the string
new_insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500)
# Change in Insurance Costs
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Print the string
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

'''
Question 12
  Notice that this time you got a negative value for change_in_insurance_cost. Let’s think about what this means. We 
  changed the sex variable from 0 (female) to 1 (male) and it decreased the estimated insurance costs.

  This means that men tend to have lower medical costs on average than women. Reflect on the other findings you have 
  dug up from this investigation so far.
'''

'''
Question 13
Great job on the project!!!
So far we have looked at 3 of the 5 factors in the insurance costs formula. The two remaining are smoker and num_of_children. If you want to keep challenging yourself, spend some time investigating these factors!
    Rewrite the insurance cost formula and assign it to the variable name new_insurance_cost.
    Save the difference between new_insurance_cost and insurance_cost in a variable called change_in_insurance_cost
    Display the information in the terminal!
'''
# Extra Practice
smoker = 1
num_of_children = 0
# Create the string
new_insurance_cost = ((250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (2400 * smoker) - 12500)
# Change in Insurance Costs
change_in_insurance_cost = new_insurance_cost - insurance_cost
# Print the string
print("The change in estimated cost for being a smoker and having no children instead of a non-smoker with 3 children is " + str(change_in_insurance_cost) + " dollars.")


