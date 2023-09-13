import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy variables and their ranges
sale_condition = ctrl.Antecedent(np.arange(0, 11, 1), 'SaleCondition')
overall_quality = ctrl.Antecedent(np.arange(1, 11, 1), 'OverallQual')
bedrooms = ctrl.Antecedent(np.arange(0, 11, 1), 'BedroomAbvGr')
sale_price = ctrl.Consequent(np.arange(0, 1000000, 1000), 'SalePrice')

# Define the membership functions for each variable
sale_condition['poor'] = fuzz.trimf(sale_condition.universe, [0, 0, 5])
sale_condition['fair'] = fuzz.trimf(sale_condition.universe, [0, 5, 10])
sale_condition['excellent'] = fuzz.trimf(sale_condition.universe, [5, 10, 10])

overall_quality['poor'] = fuzz.trimf(overall_quality.universe, [1, 1, 5])
overall_quality['fair'] = fuzz.trimf(overall_quality.universe, [1, 5, 9])
overall_quality['excellent'] = fuzz.trimf(overall_quality.universe, [5, 9, 9])

bedrooms['few'] = fuzz.trimf(bedrooms.universe, [0, 0, 3])
bedrooms['average'] = fuzz.trimf(bedrooms.universe, [0, 3, 6])
bedrooms['many'] = fuzz.trimf(bedrooms.universe, [3, 6, 6])

sale_price['low'] = fuzz.trimf(sale_price.universe, [0, 0, 500000])
sale_price['medium'] = fuzz.trimf(sale_price.universe, [0, 500000, 1000000])
sale_price['high'] = fuzz.trimf(sale_price.universe, [500000, 1000000, 1000000])

# Define the fuzzy rules
rule1 = ctrl.Rule(sale_condition['poor'] | overall_quality['poor'] | bedrooms['few'], sale_price['low'])
rule2 = ctrl.Rule(sale_condition['fair'] & overall_quality['fair'] & bedrooms['average'], sale_price['medium'])
rule3 = ctrl.Rule(sale_condition['excellent'] | overall_quality['excellent'] | bedrooms['many'], sale_price['high'])

# Create the control system and add the rules
fis = ctrl.ControlSystem([rule1, rule2, rule3])
prediction = ctrl.ControlSystemSimulation(fis)

# Provide input values
prediction.input['SaleCondition'] = 5
prediction.input['OverallQual'] = 7
prediction.input['BedroomAbvGr'] = 4

# Compute the output
prediction.compute()

# Print the predicted sales price
print("Predicted Sales Price: $", prediction.output['SalePrice'])