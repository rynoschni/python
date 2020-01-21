# configuration
PROMPT_TOTAL = 'Total bill amount? '
PROMPT_SERVICE = 'Level of service?'
SERVICE_GOOD = 'good'
SERVICE_FAIR = 'fair'
SERVICE_BAD = 'bad'
MESSAGE_INVALID_INPUT = 'Invalid input. They can\'t be that bad.'
MESSAGE_TIP_AMOUNT = 'Tip amount: %.2f'
MESSAGE_TOTAL_AMOUNT = 'Total amount: %.2f'

GOOD_TIP_PERCENTAGE = 0.2
FAIR_TIP_PERCENTAGE = 0.15
BAD_TIP_PERCENTAGE = 0.1

total_bill_input = input(PROMPT_TOTAL)
level_of_service_input = input(PROMPT_SERVICE)
total_bill = float(total_bill_input)
level_of_service = level_of_service_input.lower()


tip = FAIR_TIP_PERCENTAGE

# processing
if level_of_service == SERVICE_GOOD:
  tip = GOOD_TIP_PERCENTAGE
elif level_of_service == SERVICE_FAIR:
  tip = FAIR_TIP_PERCENTAGE
elif level_of_service == SERVICE_BAD:
  tip = BAD_TIP_PERCENTAGE
else:
  print(MESSAGE_INVALID_INPUT)

total_tip = total_bill * tip
total_amount_owed = total_tip + total_bill

# result
print(MESSAGE_TIP_AMOUNT % (total_tip))
print(MESSAGE_TOTAL_AMOUNT % (total_amount_owed))
