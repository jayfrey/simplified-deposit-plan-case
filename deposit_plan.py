from constants import DepositPlanTypes


def deposit_plan(deposit_plans, fund_deposits, customer_portfolios):
    deposit_plans.sort(key=lambda x: x["type"])

    total_fund_deposits = sum(fund_deposits)
    count = 0
    while count < len(deposit_plans):
        deposit_plan = deposit_plans[count].copy()

        # print(f"deposit_plan: {deposit_plan}")

        high_risk_full = 0 == deposit_plan["high_risk"]
        retirement_full = 0 == deposit_plan["retirement"]

        while total_fund_deposits > 0:
            # print(f"high_risk_full: {high_risk_full}")
            # print(f"retirement_full: {retirement_full}")
            # print(f"total_fund_deposits: {total_fund_deposits}")

            total = 0
            check_high_risk_based_on_deposit_plan = True
            check_retirement_based_on_deposit_plan = True

            if high_risk_full or retirement_full:
                step = 1
                if high_risk_full and retirement_full:
                    step = 2
                    high_risk_full = False
                    retirement_full = False

            else:
                step = 2

            if deposit_plan["type"] == DepositPlanTypes.MONTHLY:
                check_high_risk_based_on_deposit_plan = False
                check_retirement_based_on_deposit_plan = False

            # print(f"step: {step}")
            # print(f"deposit_plan[high_risk]: {deposit_plan['high_risk']}")
            # print(f"deposit_plan[retirement]: {deposit_plan['retirement']}")

            for _ in range(1, total_fund_deposits + 1, step):
                if not high_risk_full:
                    customer_portfolios["high_risk"] += 1
                    total += 1
                    if check_high_risk_based_on_deposit_plan:
                        if (
                            customer_portfolios["high_risk"]
                            == deposit_plan["high_risk"]
                        ):
                            high_risk_full = True

                if not retirement_full:
                    customer_portfolios["retirement"] += 1
                    total += 1
                    if check_retirement_based_on_deposit_plan:
                        if (
                            customer_portfolios["retirement"]
                            == deposit_plan["retirement"]
                        ):
                            retirement_full = True

            total_fund_deposits = total_fund_deposits - total
            # print(f"customer_portfolios: {customer_portfolios}")
            # print(f"\n")
            if high_risk_full and retirement_full:
                if not 0 <= 1 < len(deposit_plans):
                    pass
                else:
                    break

        count += 1

    return customer_portfolios
