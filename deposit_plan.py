def deposit_plan(deposit_plans, fund_deposits, customer_portfolios):
    total_fund_deposits = sum(fund_deposits)
    count = 0
    while count < len(deposit_plans):
        deposit_plan = deposit_plans[count].copy()

        high_risk_full = 0 == deposit_plan["high_risk"]
        retirement_full = 0 == deposit_plan["retirement"]

        while total_fund_deposits > 0:

            total = 0
            if high_risk_full or retirement_full:
                step = 1
                if high_risk_full and retirement_full:
                    step = 2
                    high_risk_full = False
                    retirement_full = False
            else:
                step = 2

            for _ in range(1, total_fund_deposits + 1, step):
                if not high_risk_full:
                    customer_portfolios["high_risk"] += 1
                    total += 1
                    if customer_portfolios["high_risk"] == deposit_plan["high_risk"]:
                        high_risk_full = True

                if not retirement_full:
                    customer_portfolios["retirement"] += 1
                    total += 1
                    if customer_portfolios["retirement"] == deposit_plan["retirement"]:
                        retirement_full = True

            total_fund_deposits = total_fund_deposits - total

            if high_risk_full and retirement_full:
                if not 0 <= 1 < len(deposit_plans):
                    pass
                else:
                    break
        count += 1

    return customer_portfolios
