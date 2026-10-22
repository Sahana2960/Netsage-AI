def check_missing_vlan(show_output):
    if "VLAN 30" not in show_output:
        return "Missing VLAN"
    return None


def check_interface_down(show_output):
    if "administratively down" in show_output.lower():
        return "Interface Down"
    return None


def check_missing_route(show_output):
    if "0.0.0.0" not in show_output:
        return "Missing Route"
    return None


# Sample Test
sample = """
Switch# show vlan brief

VLAN 10 active
VLAN 20 active
"""

print("Sample Test:", check_missing_vlan(sample))

# Case 1 - Missing VLAN
try:
    with open("../sample_outputs/case_1.txt", "r") as f:
        case1 = f.read()

    result = check_missing_vlan(case1)

    if result:
        print("Case 1 Diagnosis:", result)
    else:
        print("Case 1 Diagnosis: No issue found")

except FileNotFoundError:
    print("case_1.txt not found")


# Case 2 - Missing Route
try:
    with open("../sample_outputs/case_2.txt", "r") as f:
        case2 = f.read()

    result = check_missing_route(case2)

    if result:
        print("Case 2 Diagnosis:", result)
    else:
        print("Case 2 Diagnosis: No issue found")

except FileNotFoundError:
    print("case_2.txt not found")


# Case 3 - Interface Down
try:
    with open("../sample_outputs/case_3.txt", "r") as f:
        case3 = f.read()

    result = check_interface_down(case3)

    if result:
        print("Case 3 Diagnosis:", result)
    else:
        print("Case 3 Diagnosis: No issue found")

except FileNotFoundError:
    print("case_3.txt not found")