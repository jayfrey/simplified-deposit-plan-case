from deposit_plan import deposit_plan
from test_cases import deposit_plans_list
from constants import DepositPlanTypes


customer_portfolios = {
    "high_risk": 0,
    "retirement": 0,
}

deposit_plans = [
    {
        "type": DepositPlanTypes.ONE_TIME,
        "high_risk": 10000,
        "retirement": 500,
    },
    {
        "type": DepositPlanTypes.MONTHLY,
        "high_risk": 0,
        "retirement": 100,
    },
]  # 10000 600

fund_deposits = [10500, 100]  # 10600 Total
# fund_deposits = [100, 100, 1000, 1000, 10000, 10000]  # 22200 Total

print(deposit_plan(deposit_plans, fund_deposits, customer_portfolios))


# for deposit_plans in deposit_plans_list:
#     # Reset customer portfolios
#     customer_portfolios = {
#         "high_risk": 0,
#         "retirement": 0,
#     }
#     print(deposit_plan(deposit_plans, fund_deposits, customer_portfolios))
