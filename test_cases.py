from constants import DepositPlanTypes

deposit_plans_list = [
    [
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
    ],  # 10000 900
    [
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 10000,
            "retirement": 500,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 100,
            "retirement": 0,
        },
    ],  # 10400 500
    [
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 10000,
            "retirement": 500,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 100,
            "retirement": 100,
        },
    ],
    [  # 10200 700
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 10000,
            "retirement": 500,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 0,
            "retirement": 0,
        },
    ],
    [  # 10200 700
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 0,
            "retirement": 0,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 100,
            "retirement": 100,
        },
    ],
    [  # 5450 5450
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 10000,
            "retirement": 0,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 100,
            "retirement": 100,
        },
    ],
    [  # 10800 100
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 0,
            "retirement": 10000,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 100,
            "retirement": 100,
        },
    ],
    [  # 100 10800
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 0,
            "retirement": 0,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 100,
            "retirement": 200,
        },
    ],  # 5450 5450
]
