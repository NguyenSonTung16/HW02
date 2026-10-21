---
name: domain-testing
description: Perform black-box Domain Testing using Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) to design optimal, non-redundant test suites from software specifications. Use when the user asks to perform domain testing, identify equivalence classes, conduct boundary value analysis, generate black-box test cases from input/output conditions or ranges, or create minimum test suites from program specifications.
---

# Domain Testing

Design systematic, high-coverage black-box test suites by partitioning input and output domains into equivalence classes and targeting high-risk boundary values. This skill implements the 4-step Domain Testing methodology (Equivalence Partitioning and Boundary Value Analysis) to select a minimal yet effective set of test cases from large or infinite input populations.

## When to Use

- The user asks to perform Domain Testing, Equivalence Partitioning (EP), or Boundary Value Analysis (BVA) on a software specification, requirement, or function.
- The user wants to identify valid and invalid equivalence classes for input and output variables.
- The user asks for a minimum set of test cases or boundary value test cases covering specified constraints (ranges, discrete sets, data types, or format rules).
- The user wants to reduce a massive or infinite test space into a structured, non-redundant test table.

## Steps

### Step 1: Identify Input and Output Variables

Analyze the program specification to extract every independent input variable and every possible output result before creating partitions.

- List all **Input variables** alongside their expected data types, formats, and constraints.
- List all **Output variables and states**, explicitly including both valid functional outputs (e.g., calculated `SUM`, state transition, record creation) and error outputs (e.g., `Error Message / Invalid Input`).

### Step 2: Identify Equivalence Classes (EC)

Partition the domain of each input and output variable into mutually exclusive sub-domains (equivalence classes) where all values in a class are expected to be handled identically by the program. Because two tests in the same equivalence class yield the same expected behavior, running multiple tests from the same class without boundary targeting is redundant.

For every condition, identify both **Valid Equivalence Classes** (representing valid inputs/outputs) and **Invalid Equivalence Classes** (representing invalid inputs/error outputs) using these four heuristic rules:

1. **Range of values condition** (e.g., `LB <= X <= UB`):
   - Create **1 valid equivalence class**: `LB <= X <= UB`.
   - Create **2 invalid equivalence classes**: `X < LB` (below lower bound) and `X > UB` (above upper bound).

2. **Set of discrete values condition** (where each item is handled differently, e.g., `Vehicle Type in {BUS, TRUCK, TAXI-CAB, PASSENGER, MOTORCYCLE}`):
   - Create **1 valid equivalence class per item** in the allowed set.
   - Create **1 invalid equivalence class** representing any value outside the allowed set (e.g., `TRAILER`).

3. **"Must be" mandatory condition** (e.g., "must be an integer", "must be alphanumeric", "first two characters must be letters"):
   - Create **1 valid equivalence class**: satisfies the mandatory condition.
   - Create **1 invalid equivalence class**: violates the mandatory condition (e.g., not an integer, contains special characters, first two characters are not letters).

4. **Non-identical handling split rule**:
   - Split an equivalence class into two or more smaller equivalence classes whenever there is any reason to believe the program handles elements within that class differently.

Document the resulting partitions in two views:

- **Complete Set of Partitions Table**: Assign sequential IDs (`EC1`, `EC2`, ...) to every valid and invalid partition across all Input and Output variables.
- **Combined Valid and Invalid Summary**: Express the full intersection of valid conditions vs. individual invalid conditions when multiple constraints apply to the same variable (e.g., length between 3 and 15, alphanumeric, and first 2 characters are letters).

### Step 3: Select Representative Test Cases (Minimum Set)

Select concrete test values from each equivalence class to build the **Minimum Set of Test Cases** using asymmetric rules for valid vs. invalid classes:

- **Combine Valid Equivalence Classes (Maximize Valid Coverage per Test)**: Choose test cases that simultaneously cover as many valid equivalence classes as possible across all variables until every valid class is covered.
- **Isolate Invalid Equivalence Classes (One Invalid Class per Test)**: Choose test cases so that each invalid test covers **one and only one** invalid equivalence class while keeping all other input variables within their valid nominal ranges. This prevents one input error from masking bugs in another input's validation logic.

### Step 4: Perform Boundary Value Analysis (BVA)

Refine test selection for ordered domains (numeric ranges, string lengths, array sizes, coordinate bounds) by targeting boundary values. Developers frequently introduce defects at boundaries through mis-specified inequalities (e.g., writing `<=` instead of `<`, which is detectable *only* at the boundary) or mistyped boundary constants (e.g., transposition errors like `52` instead of `25`).

#### The 9-Point Boundary Model (Comprehensive View)

For any ordered partition with Lower Boundary (`LB`) and Upper Boundary (`UB`), consider up to 9 risk points:

1. Nominal value inside the valid partition (`LB < X < UB`)
2. Just above lower boundary: `LB + 1` (Valid)
3. At lower boundary: `LB` (Valid)
4. Just below lower boundary: `LB - 1` (Invalid)
5. Just above upper boundary: `UB + 1` (Invalid)
6. At upper boundary: `UB` (Valid)
7. Just below upper boundary: `UB - 1` (Valid)
8. Smallest possible value allowed via UI (`-alpha`, when UI constraints exist)
9. Largest possible value allowed via UI (`+alpha`, when UI constraints exist)

#### Standard 6-Point Boundary Test Generation (Per Ordered Variable)

For each ordered input variable with valid range `[LB, UB]`, generate **6 boundary test cases** while holding all other input variables at a valid nominal value:

- `LB - 1` -> Expected: Invalid Input (covers `< LB` partition)
- `LB` -> Expected: Valid Output (exact lower boundary)
- `LB + 1` -> Expected: Valid Output (interior lower boundary neighbor)
- `UB - 1` -> Expected: Valid Output (interior upper boundary neighbor)
- `UB` -> Expected: Valid Output (exact upper boundary)
- `UB + 1` -> Expected: Invalid Input (covers `> UB` partition)

Repeat this 6-point sweep independently for each ordered input variable while holding the remaining variables at a valid nominal value.

## Output Format Templates

Present your Domain Testing analysis using these structured Markdown tables.

### 1. Condition Breakdown Table

| Condition | Valid Equivalence Classes | Invalid Equivalence Classes |
| :--- | :--- | :--- |
| Has 1 or 2 digits | `-99 <= Number <= 99` | `< -99` or `> 99` |
| Is an integer | Is an integer | Not an integer |
| Output | `SUM = A + B` | `Invalid Input` |

### 2. Complete Set of Partitions Table

| ID | Input / Output | Equivalence Class Description | Type |
| :--- | :--- | :--- | :--- |
| EC1 | A | `-99 <= A <= 99` | Valid |
| EC2 | A | `A < -99` | Invalid |
| EC3 | A | `A > 99` | Invalid |
| EC4 | A | `A` is not an integer | Invalid |
| EC5 | B | `-99 <= B <= 99` | Valid |
| EC6 | B | `B < -99` | Invalid |
| EC7 | B | `B > 99` | Invalid |
| EC8 | B | `B` is not an integer | Invalid |
| EC9 | SUM | `SUM = A + B` | Valid Output |
| EC10 | SUM | `Error Message (Invalid Input)` | Invalid Output |

### 3. Minimum Set of Test Cases (Equivalence Partitioning)

| #TC | Partitions Tested | Input 1 (A) | Input 2 (B) | Expected Output |
| :--- | :--- | :--- | :--- | :--- |
| TC1 | EC1 (`-99 <= A <= 99`), EC5 (`-99 <= B <= 99`), EC9 (`SUM = A + B`) | 10 | 9 | 19 |
| TC2 | EC2 (`A < -99`), EC10 (`Invalid Input`) | -102 | 9 | Invalid Input |
| TC3 | EC3 (`A > 99`), EC10 (`Invalid Input`) | 102 | 9 | Invalid Input |
| TC4 | EC4 (`A` is not an integer), EC10 (`Invalid Input`) | Abc | 9 | Invalid Input |
| TC5 | EC6 (`B < -99`), EC10 (`Invalid Input`) | 10 | -200 | Invalid Input |
| TC6 | EC7 (`B > 99`), EC10 (`Invalid Input`) | 10 | 200 | Invalid Input |
| TC7 | EC8 (`B` is not an integer), EC10 (`Invalid Input`) | 10 | 1.25 | Invalid Input |

### 4. Boundary Value Analysis Test Cases Table

| #TC | Partition Tested | Input 1 (A) | Input 2 (B) | Expected Output |
| :--- | :--- | :--- | :--- | :--- |
| TC1 | `A < -99` (`LB - 1`) | -100 | 9 | Invalid Input |
| TC2 | `-99 <= A <= 99` (`LB`) | -99 | 9 | -90 |
| TC3 | `-99 <= A <= 99` (`LB + 1`) | -98 | 9 | -89 |
| TC4 | `-99 <= A <= 99` (`UB - 1`) | 98 | 9 | 107 |
| TC5 | `-99 <= A <= 99` (`UB`) | 99 | 9 | 108 |
| TC6 | `A > 99` (`UB + 1`) | 100 | 9 | Invalid Input |
| TC7 | `B < -99` (`LB - 1`) | 10 | -100 | Invalid Input |
| TC8 | `-99 <= B <= 99` (`LB`) | 10 | -99 | -89 |
| TC9 | `-99 <= B <= 99` (`LB + 1`) | 10 | -98 | -88 |
| TC10 | `-99 <= B <= 99` (`UB - 1`) | 10 | 98 | 108 |
| TC11 | `-99 <= B <= 99` (`UB`) | 10 | 99 | 109 |
| TC12 | `B > 99` (`UB + 1`) | 10 | 100 | Invalid Input |

## Gotchas

- **Never combine multiple invalid equivalence classes in a single test case**: If `A = -102` (invalid) and `B = 1.25` (invalid) are tested together and the program returns `Invalid Input`, you cannot verify whether the program actually validates `B` or simply short-circuited on `A`. Always keep all other variables valid when testing an invalid partition.
- **Do not forget non-numeric and type-level "must be" conditions**: Even when a specification states "enter a number from 1 to 99", always include the invalid equivalence class for non-numeric or non-integer inputs (e.g., `"Abc"`, `1.25`) unless the UI strictly prevents non-numeric entry.
- **Pay attention to strict vs. inclusive inequalities**: If a condition states "a positive integer less than 100" (`0 < X < 100`), the valid integer bounds are `LB = 1` and `UB = 99`, making `0` (`X <= 0`) and `100` (`X >= 100`) the invalid boundary values (`LB - 1` and `UB + 1`).
- **Account for Domain Testing blind spots**: Domain testing excels at finding boundary and partition errors with a small test set, but it does not catch errors away from boundaries, complex multi-variable interaction bugs, or hidden internal sub-domains that are invisible in black-box specifications. Note these limitations when advising on overall test strategy.
