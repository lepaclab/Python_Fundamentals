# Python Syntax: Medical Insurance Project
# Suppose you are a medical professional curious 
#about how certain factors contribute to medical 
#insurance costs. Using a formula that estimates 
#a person’s yearly insurance costs, you will investigate 
#how different factors such as age, sex, BMI, etc. affect the prediction.

# Our first step is to create the variables for each factor we will consider when estimating medical insurance costs.

# These are the variables we will need to create:

# age: age of the individual in years
# sex: 0 for female, 1 for male*
# bmi: individual’s body mass index
# num_of_children: number of children the individual has
# smoker: 0 for a non-smoker, 1 for a smoker
# At the top of script.py, create the following variables for a 28-year-old, nonsmoking woman who has three children and a BMI of 26.2





# create the initial variables below
age = 28
sex = 0
bmi = 26.2 
num_of_children = 3
smoker =  0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is", insurance_cost, "dollars.")
# Age Factor
age += 4

# BMI Factor
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

age = 28
bmi  += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Male vs. Female Factor
bmi = 26.2
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars")

# Notice that this time you got a negative value for change_in_insurance_cost. Let’s think about what this means. We changed the sex variable from 0 (female) to 1 (male) and it decreased the estimated insurance costs.
# This means that men tend to have lower medical costs on average than women. Reflect on the other findings you have dug up from this investigation so far.

# Extra Practice
