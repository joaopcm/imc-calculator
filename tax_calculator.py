def bonus_calculator(subscription_type: int, annual_revenues: float) -> float:
    subscriptions = {
        1: 'BASIC',
        2: 'SILVER',
        3: 'GOLD',
        4: 'PLATINUM'
    }

    subscriptions_taxes = {
        'BASIC': 0.3,
        'SILVER': 0.2,
        'GOLD': 0.1,
        'PLATINUM': 0.05
    }

    chosen_subscription = subscriptions[subscription_type]
    respective_tax = subscriptions_taxes[chosen_subscription]
    payment_value = annual_revenues * respective_tax

    return payment_value

subscription_type = int(input('Choose your subscription type: (1 - BASIC / 2 - SILVER / 3 - GOLD / 4 - PLATINUM) '))
annual_revenues = float(input('Provide your annual revenues (R$): '))
payment_value = bonus_calculator(subscription_type, annual_revenues)

print('You must pay R${:.2f}'.format(payment_value))
