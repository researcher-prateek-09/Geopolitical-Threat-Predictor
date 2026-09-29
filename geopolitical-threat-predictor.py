# =====================================================================
# RESEARCH ENGINE: MULTI-PARAMETER WEIGHTED INDEXING (FROM SCRATCH)
# Moving from simple proximity matching to mathematical risk equations
# =====================================================================

import math

print("=== ADVANCED 3-PARAMETER RISK SCORING ENGINE ===")

# 1. DEFINE SYSTEM WEIGHTS (Importance metrics)
# These represent the structural rules of our mathematical model
WEIGHT_INFLATION = 0.20

WEIGHT_TENSION   = 0.30
WEIGHT_SCARCITY  = 0.50

CURRENT_RISK_WEIGHT = 0.60
HISTORICAL_RISK_WEIGHT = 0.40

SIMILARITY_WEIGHT_INFLATION = 0.20
SIMILARITY_WEIGHT_TENSION = 0.30
SIMILARITY_WEIGHT_SCARCITY = 0.50

TOP_HISTORICAL_CASES = 5

HIGH_RISK_THRESHOLD = 75.00
MODERATE_RISK_THRESHOLD = 45.00

MIN_INPUT = 1.00
MAX_INPUT = 10.00


# 2. HISTORICAL OUTCOME SCORES

OUTCOME_SCORES = {
    "stable": 25.00,
    "economic_instability": 55.00,
    "diplomatic_confrontation": 70.00,
    "severe_confrontation": 80.00,
    "military_conflict": 90.00
}


# 3. HISTORICAL CASE DATABASE

historical_cases = [
    {
        "name": "Cuban Missile Crisis",
        "period": "1962",
        "inflation": 3,
        "tension": 10,
        "scarcity": 3,
        "outcome": "severe_confrontation"
    },
    {
        "name": "Suez Crisis",
        "period": "1956",
        "inflation": 4,
        "tension": 9,
        "scarcity": 6,
        "outcome": "military_conflict"
    },
    {
        "name": "Yom Kippur War",
        "period": "1973",
        "inflation": 7,
        "tension": 10,
        "scarcity": 7,
        "outcome": "military_conflict"
    },
    {
        "name": "1973 Oil Crisis",
        "period": "1973-1974",
        "inflation": 9,
        "tension": 7,
        "scarcity": 9,
        "outcome": "economic_instability"
    },
    {
        "name": "Iranian Revolution",
        "period": "1978-1979",
        "inflation": 8,
        "tension": 8,
        "scarcity": 7,
        "outcome": "severe_confrontation"
    },
    {
        "name": "Gulf War",
        "period": "1990-1991",
        "inflation": 5,
        "tension": 10,
        "scarcity": 7,
        "outcome": "military_conflict"
    },
    {
        "name": "Asian Financial Crisis",
        "period": "1997-1998",
        "inflation": 6,
        "tension": 4,
        "scarcity": 6,
        "outcome": "economic_instability"
    },
    {
        "name": "Kosovo Crisis",
        "period": "1998-1999",
        "inflation": 5,
        "tension": 9,
        "scarcity": 6,
        "outcome": "military_conflict"
    },
    {
        "name": "2008 Global Financial Crisis",
        "period": "2008-2009",
        "inflation": 4,
        "tension": 3,
        "scarcity": 7,
        "outcome": "economic_instability"
    },
    {
        "name": "Arab Spring",
        "period": "2010-2012",
        "inflation": 7,
        "tension": 8,
        "scarcity": 8,
        "outcome": "severe_confrontation"
    },
    {
        "name": "Crimea Crisis",
        "period": "2014",
        "inflation": 5,
        "tension": 9,
        "scarcity": 5,
        "outcome": "diplomatic_confrontation"
    },
    {
        "name": "COVID-19 Global Crisis",
        "period": "2020-2021",
        "inflation": 5,
        "tension": 5,
        "scarcity": 9,
        "outcome": "economic_instability"
    },
    {
        "name": "Russia-Ukraine Escalation",
        "period": "2022-2024",
        "inflation": 8,
        "tension": 10,
        "scarcity": 8,
        "outcome": "military_conflict"
    }
]


# 4. INPUT VALIDATION FUNCTION

def get_valid_rating(parameter_name):

    while True:

        user_input = input(
            f"{parameter_name} ({MIN_INPUT:.0f}-{MAX_INPUT:.0f}): "
        ).strip()

        # Allow the user to exit from inside the validation loop
        if user_input.lower() in ["bye", "exit"]:
            return None

        try:
            value = float(user_input)

            if not math.isfinite(value):
                print("Invalid input. Please enter a finite number.")
                continue

            if MIN_INPUT <= value <= MAX_INPUT:
                return value

            print(
                f"Invalid range. Please enter a value between "
                f"{MIN_INPUT:.0f} and {MAX_INPUT:.0f}."
            )

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# 5. CURRENT RISK CALCULATION

def calculate_current_risk(inflation, tension, scarcity):

    weighted_score = (
        inflation * WEIGHT_INFLATION
        + tension * WEIGHT_TENSION
        + scarcity * WEIGHT_SCARCITY
    )

    return weighted_score * 10.00


# 6. HISTORICAL SIMILARITY CALCULATION

def calculate_similarity(current, historical):

    distance = math.sqrt(
        SIMILARITY_WEIGHT_INFLATION *
        (current["inflation"] - historical["inflation"]) ** 2
        +
        SIMILARITY_WEIGHT_TENSION *
        (current["tension"] - historical["tension"]) ** 2
        +
        SIMILARITY_WEIGHT_SCARCITY *
        (current["scarcity"] - historical["scarcity"]) ** 2
    )

    maximum_distance = math.sqrt(
        SIMILARITY_WEIGHT_INFLATION * 81
        +
        SIMILARITY_WEIGHT_TENSION * 81
        +
        SIMILARITY_WEIGHT_SCARCITY * 81
    )

    similarity = (1.00 - (distance / maximum_distance)) * 100.00

    return max(0.00, min(100.00, similarity))


# =====================================================================
# 7. MAIN PROGRAM LOOP
# =====================================================================

while True:

    # 7. COLLECT 3 PARAMETERS FROM THE USER

    print("\nRate the current indicators on a scale of 1.0 (Low Risk) to 10.0 (Extreme Risk):")

    val_inflation = get_valid_rating(
        "1. Current Inflation Level"
    )

    if val_inflation is None:
        print("\nProgram exited. Goodbye!")
        break

    val_tension = get_valid_rating(
        "2. Current Border Tension Level"
    )

    if val_tension is None:
        print("\nProgram exited. Goodbye!")
        break

    val_scarcity = get_valid_rating(
        "3. Current Resource Scarcity Level"
    )

    if val_scarcity is None:
        print("\nProgram exited. Goodbye!")
        break


    # 8. CURRENT RISK ENGINE

    current_risk = calculate_current_risk(
        val_inflation,
        val_tension,
        val_scarcity
    )


    # 9. PREPARE CURRENT CONDITIONS

    current_conditions = {
        "inflation": val_inflation,
        "tension": val_tension,
        "scarcity": val_scarcity
    }


    # 10. HISTORICAL SIMILARITY ANALYSIS

    similarity_results = []

    for case in historical_cases:

        similarity = calculate_similarity(
            current_conditions,
            case
        )

        similarity_results.append({
            "case": case,
            "similarity": similarity
        })


    similarity_results.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )


    # Select top historical cases

    top_cases = similarity_results[
        :TOP_HISTORICAL_CASES
    ]


    # 11. HISTORICAL RISK CALCULATION

    weighted_score = 0.00
    total_similarity = 0.00

    for result in top_cases:

        outcome = result["case"]["outcome"]

        outcome_score = OUTCOME_SCORES[outcome]

        similarity = result["similarity"]

        weighted_score += (
            outcome_score * similarity
        )

        total_similarity += similarity


    if total_similarity > 0:

        historical_risk = (
            weighted_score / total_similarity
        )

    else:

        historical_risk = 0.00


    # 12. COMBINE CURRENT + HISTORICAL RISK

    final_threat_index = (
        current_risk * CURRENT_RISK_WEIGHT
        +
        historical_risk * HISTORICAL_RISK_WEIGHT
    )


    # 13. ALGORITHMIC CLASSIFICATION SYSTEM

    if final_threat_index >= HIGH_RISK_THRESHOLD:

        risk_category = (
            "HIGH MODELED THREAT: Structural Breakdown / "
            "High Modeled Instability"
        )

    elif final_threat_index >= MODERATE_RISK_THRESHOLD:

        risk_category = (
            "MODERATE MODELED THREAT: Elevated instability, "
            "diplomatic intervention may be required"
        )

    else:

        risk_category = (
            "LOW MODELED THREAT: System operating within "
            "manageable parameters"
        )


    # 14. PRINT THE RESEARCH REPORT

    print("\n" + "=" * 50)
    print("             COMPUTATIONAL RISK REPORT")
    print("=" * 50)

    print(
        f"Current Inflation Level : {val_inflation:.2f}"
    )

    print(
        f"Border Tension Level    : {val_tension:.2f}"
    )

    print(
        f"Resource Scarcity Level : {val_scarcity:.2f}"
    )

    print("-" * 50)

    print(
        f"Current Risk Score      : "
        f"{current_risk:.2f} / 100.00"
    )

    print(
        f"Historical Risk Score   : "
        f"{historical_risk:.2f} / 100.00"
    )

    print(
        f"Calculated Threat Index : "
        f"{final_threat_index:.2f} / 100.00"
    )

    print("-" * 50)

    print("TOP 5 SIMILAR HISTORICAL CASES")

    print("-" * 50)

    for index, result in enumerate(top_cases, start=1):

        case = result["case"]

        similarity = result["similarity"]

        print(
            f"{index}. {case['name']} "
            f"({case['period']})"
        )

        print(
            f"   Similarity : {similarity:.2f}%"
        )

        print(
            f"   Outcome    : "
            f"{case['outcome'].replace('_', ' ').title()}"
        )


    print("-" * 50)

    print(
        f"Algorithmic Conclusion  : {risk_category}"
    )

    print("=" * 50)

    print(
        "\nModel Weights:"
    )

    print(
        f"Current Risk     : "
        f"{CURRENT_RISK_WEIGHT * 100:.0f}%"
    )

    print(
        f"Historical Risk  : "
        f"{HISTORICAL_RISK_WEIGHT * 100:.0f}%"
    )

    print("=" * 50)

    print("\nAnalysis complete.")
    print("Starting a new analysis...")
