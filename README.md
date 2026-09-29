# Geopolitical Threat Predictor

## Overview

**Geopolitical Threat Predictor** is a Python-based terminal application that combines **current geopolitical indicators** with **historical crisis patterns** to calculate a modeled threat index.

The project uses a mathematical weighted-scoring system and historical similarity analysis to provide a structured assessment of the current situation.

> **Note:** This is an educational computational model. It does not provide guaranteed predictions or statistically validated probabilities.

---

## Objective

The main objective of this project is to explore how **Python and mathematical modeling** can be used to analyze geopolitical conditions.

The project focuses on three major indicators:

* **Inflation Level**
* **Border Tension Level**
* **Resource Scarcity Level**

It then compares the current situation with a collection of historical geopolitical and economic crises.

---

## What Problem Does It Solve?

Geopolitical situations involve many different factors, making it difficult to represent them using a single numerical value.

This project attempts to solve this problem by:

1. Converting several qualitative conditions into numerical inputs.
2. Assigning different importance to each indicator.
3. Calculating a current threat score.
4. Comparing the current situation with historical cases.
5. Identifying the most similar historical situations.
6. Combining current conditions and historical patterns into one final modeled threat index.

This provides a simple computational framework for studying how different factors can interact in a geopolitical scenario.

---

## Real-World Use

A system based on this concept could potentially be used as an **analytical support tool** for:

* Historical and geopolitical research
* Educational demonstrations of mathematical modeling
* Comparing current situations with historical events
* Exploring relationships between economic and geopolitical indicators
* Building larger data-driven risk-analysis systems in the future

The current version is intentionally simplified and is primarily designed as an educational Python project.

---

## Origin of the Idea

The idea came from combining two personal interests:

* **History** — especially historical conflicts, crises, and geopolitical events
* **Python programming** — particularly using programming to convert ideas into computational models

The project started as an idea to analyze whether present-day conditions could be compared with historical situations using Python.

It was then developed into a mathematical model that combines **current risk scoring** with **historical pattern similarity**.

---

# Overall Working

The program works through the following major stages:

```text
User Input
    ↓
Current Risk Calculation
    ↓
Historical Similarity Analysis
    ↓
Top 5 Similar Historical Cases
    ↓
Historical Risk Calculation
    ↓
Current + Historical Risk Combination
    ↓
Final Threat Classification
    ↓
Repeat Analysis or Exit
```

The complete analysis is placed inside a **while loop**, allowing the user to perform multiple analyses without restarting the program.

The program continues running until the user enters `bye` or `exit`.

---

## 1. User Input

The user provides three values from **1 to 10**:

| Parameter         | Meaning                                               |
| ----------------- | ----------------------------------------------------- |
| Inflation         | Current level of inflation-related economic pressure  |
| Border Tension    | Current level of geopolitical or border tension       |
| Resource Scarcity | Current level of pressure caused by limited resources |

A value of:

* `1` = Low Risk
* `10` = Extreme Risk

The program also validates the input so that values outside the allowed range or invalid text are rejected.

The user can type **`bye`** or **`exit`** at any input prompt to terminate the program.

---

# 2. Current Risk Engine

The current situation is evaluated using a weighted mathematical equation.

### Weights

```text
Inflation       → 20%
Border Tension  → 30%
Resource Scarcity → 50%
```

The current risk score is calculated using:

```text
Current Risk =
(Inflation × 0.20
+ Border Tension × 0.30
+ Resource Scarcity × 0.50) × 10
```

Resource scarcity receives the highest weight because it is treated as the most influential factor within this particular model.

These weights are **model assumptions** and are not claimed to represent scientifically established geopolitical relationships.

---

# 3. Historical Pattern Engine

The program contains a dataset of historical events such as:

* Cuban Missile Crisis
* Suez Crisis
* Yom Kippur War
* 1973 Oil Crisis
* Iranian Revolution
* Gulf War
* Asian Financial Crisis
* Kosovo Crisis
* 2008 Global Financial Crisis
* Arab Spring
* Crimea Crisis
* COVID-19 Global Crisis
* Russia-Ukraine Escalation

Each historical case has normalized values for:

```text
Inflation
Border Tension
Resource Scarcity
Outcome Category
```

The historical values are **model-assigned normalized values**, not direct official measurements from the historical events.

---

# 4. Historical Similarity Calculation

The program calculates how similar the current situation is to each historical case.

It uses a **weighted Euclidean distance**.

The formula considers the difference between:

```text
Current Inflation ↔ Historical Inflation
Current Tension ↔ Historical Tension
Current Scarcity ↔ Historical Scarcity
```

The model gives the same relative importance to these variables as the current risk system:

```text
Inflation       → 20%
Border Tension  → 30%
Resource Scarcity → 50%
```

A smaller mathematical distance means greater similarity.

The distance is converted into a similarity percentage from approximately:

```text
0% → Very Different
100% → Extremely Similar
```

---

# 5. Selecting Historical Cases

After calculating similarity for every historical case, the program sorts the cases from highest similarity to lowest similarity.

It then selects the:

```text
Top 5 Most Similar Historical Cases
```

These cases are used to calculate the historical risk component.

---

# 6. Historical Outcome Scores

Each historical outcome category has a normalized model score:

| Outcome                  | Model Score |
| ------------------------ | ----------: |
| Stable                   |          25 |
| Economic Instability     |          55 |
| Diplomatic Confrontation |          70 |
| Severe Confrontation     |          80 |
| Military Conflict        |          90 |

These values are used only as numerical representations inside the model.

They are **not probabilities** and do not represent measured historical probabilities.

---

# 7. Historical Risk Calculation

The program calculates a similarity-weighted average of the top five historical cases.

Cases that are more similar to the current situation receive greater influence.

Conceptually:

```text
Historical Risk =
Σ(Outcome Score × Similarity)
÷
Σ(Similarity)
```

This produces a historical-risk score between the model's defined range.

---

# 8. Combined Threat Index

The project combines two components:

```text
Current Risk       → 60%
Historical Risk    → 40%
```

The final equation is:

```text
Final Threat Index =
(Current Risk × 0.60)
+
(Historical Risk × 0.40)
```

This means the current conditions have greater influence, while historical similarity provides additional context.

---

# 9. Final Classification

The final score is classified into three categories:

|      Score | Classification          |
| ---------: | ----------------------- |
|   Below 45 | LOW MODELED THREAT      |
| 45 – 74.99 | MODERATE MODELED THREAT |
|   75 – 100 | HIGH MODELED THREAT     |

The term **"modeled threat"** is deliberately used instead of "probability" because the program does not perform statistical probability estimation.

---

# Key Variables

### `WEIGHT_INFLATION`

```python
WEIGHT_INFLATION = 0.20
```

Controls the contribution of inflation to the current risk calculation.

### `WEIGHT_TENSION`

```python
WEIGHT_TENSION = 0.30
```

Controls the contribution of border tension.

### `WEIGHT_SCARCITY`

```python
WEIGHT_SCARCITY = 0.50
```

Controls the contribution of resource scarcity.

### `CURRENT_RISK_WEIGHT`

```python
CURRENT_RISK_WEIGHT = 0.60
```

Controls how strongly the current situation affects the final score.

### `HISTORICAL_RISK_WEIGHT`

```python
HISTORICAL_RISK_WEIGHT = 0.40
```

Controls how strongly historical similarity affects the final score.

### `TOP_HISTORICAL_CASES`

```python
TOP_HISTORICAL_CASES = 5
```

Determines how many historical cases are used in the historical-risk calculation.

### `HIGH_RISK_THRESHOLD`

```python
HIGH_RISK_THRESHOLD = 75.00
```

Defines the threshold for a high modeled threat.

### `MODERATE_RISK_THRESHOLD`

```python
MODERATE_RISK_THRESHOLD = 45.00
```

Defines the threshold for a moderate modeled threat.

---

# Key Functions

## `get_valid_rating()`

Collects and validates user input.

It ensures that:

* The input is numeric.
* The value is finite.
* The value is between 1 and 10.
* The user can enter `bye` or `exit` to terminate the program.

---

## `calculate_current_risk()`

Calculates the current threat score using the weighted mathematical equation.

---

## `calculate_similarity()`

Compares the current conditions with a historical case using weighted Euclidean distance.

It returns a similarity percentage.

---

## Historical Analysis Function

The historical analysis:

1. Calculates similarity for every historical case.
2. Sorts the cases.
3. Selects the top five.
4. Calculates a similarity-weighted historical risk score.

---

## Classification Logic

The program uses conditional statements to convert the final numerical score into a category:

```text
< 45       → Low Modeled Threat
45–74.99   → Moderate Modeled Threat
≥ 75       → High Modeled Threat
```

---

# How to Run the Program

## Requirements

The project requires:

* Python 3.x
* Terminal / Command Prompt

No external Python packages are required.

The only imported library is Python's built-in:

```python
math
```

---

## Running the Program

### Step 1

Download or clone the GitHub repository.

### Step 2

Open the project folder in a terminal.

### Step 3

Run the Python file:

```bash
python main.py
```

If your system uses `python3`:

```bash
python3 main.py
```

### Step 4

Enter values between `1` and `10` when prompted.

For example:

```text
Current Inflation Level: 6
Current Border Tension Level: 8
Current Resource Scarcity Level: 7
```

### Step 5

The program generates a computational report containing:

* Current risk score
* Historical risk score
* Final threat index
* Top five similar historical cases
* Similarity percentages
* Final modeled threat classification

### Step 6

After completing an analysis, the program automatically starts another analysis.

The user can continue using the program repeatedly without restarting it.

To close the program, type:

```text
bye
```

or:

```text
exit
```

at any input prompt.

---

# Example Workflow

Suppose the user enters:

```text
Inflation = 6
Border Tension = 8
Resource Scarcity = 7
```

The program first calculates the current risk.

It then compares:

```text
6, 8, 7
```

with the corresponding values of every historical case.

The five closest historical situations are selected.

Their outcome scores are combined according to their similarity.

Finally:

```text
60% Current Risk
+
40% Historical Risk
=
Final Threat Index
```

The final score is then converted into a modeled threat category.

After displaying the report, the program returns to the input stage and allows the user to perform another analysis.

---

# Project Structure

```text
Geopolitical-Threat-Predictor/
│
├── main.py
├── README.md
├── project report.pdf
└── other project files (if applicable)
```

The GitHub repository contains the main Python source code, documentation, and the **project report PDF**.

---

# Limitations

This project has several important limitations.

### 1. Simplified Indicators

Real geopolitical situations depend on many more variables, including:

* Political stability
* Military capabilities
* Diplomatic relations
* Trade relationships
* Energy supply
* Population factors
* Government policies
* Alliances
* Public sentiment
* Technological factors
* International intervention

The current model uses only three major indicators.

### 2. Model-Assumed Historical Values

Historical indicator values are normalized values assigned for the purpose of creating a computational model.

They should not be interpreted as official historical measurements.

### 3. Not a Statistical Prediction Model

The project does not use:

* Machine learning
* Regression
* Bayesian probability
* Statistical forecasting
* Large-scale datasets

Therefore, the final score should not be interpreted as an actual probability of conflict.

### 4. Limited Dataset

Only a limited number of historical cases are currently included.

A larger and more carefully documented dataset could improve the analytical usefulness of the system.

---

# Future Improvements

The project could be expanded by adding:

* A much larger historical dataset
* More geopolitical indicators
* Real-world economic datasets
* Real-time data collection
* Machine learning models
* Statistical validation
* Country-specific analysis
* Time-series analysis
* Graphical visualization
* Database integration
* Automated data updates
* Confidence intervals
* Back-testing against historical situations

These improvements could transform the current educational model into a more advanced data-analysis system.

---

# Technologies Used

* **Python**
* **Mathematical modeling**
* **Weighted scoring**
* **Weighted Euclidean distance**
* **Historical pattern analysis**
* **Terminal-based interface**
* **Built-in Python `math` module**
* **While loop for repeated analysis**

---

# Disclaimer

This project is an educational computational model created to demonstrate Python programming, mathematical scoring, and historical pattern analysis.

The results should not be treated as professional geopolitical intelligence, guaranteed predictions, or actual probabilities of future events.

The historical values, weights, thresholds, and outcome scores are assumptions made for the purpose of this project.

---

## Author

**Prateek Kumar Upadhyay**

B.Tech — Computer Science and Engineering

VIT Bhopal University
