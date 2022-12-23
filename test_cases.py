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
    ],  # 10000 600
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
    ],  # 10100 500
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
    ],  # 10050 550
    [
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
    ],  # 10050 550
    [
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
    ],  # 5300 5300
    [
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
    ],  # 10300 300
    [
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
    ],  # 300 10300
    [
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
    ],  # 5300 5300
    [
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 0,
            "retirement": 10000,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 0,
            "retirement": 100,
        },
    ],  # 0 10600
    [
        {
            "type": DepositPlanTypes.ONE_TIME,
            "high_risk": 0,
            "retirement": 10000,
        },
        {
            "type": DepositPlanTypes.MONTHLY,
            "high_risk": 100,
            "retirement": 0,
        },
    ],  # 600 10000
]
