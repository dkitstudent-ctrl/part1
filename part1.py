'''
Practical Part 1 Functions
'''
import pytest

def calculate_interest(deposit):
    """
    Calculate interest based on tiered deposit rates:
      - First €1,000 at 3%
      - Next €10,000 at 3.5%
      - Up to 100,000 at 4%
      - Amounts above €100,000 at 4.5%
    """

    # --- Input validation ---
    if isinstance(deposit, str):
        raise ValueError("Deposit must not be a string.")

    if isinstance(deposit, bool):
         raise ValueError("Deposit must not be a Boolean.")

    if not isinstance(deposit, (int, float)):
        raise ValueError("Deposit must be a number (int or float).  Received: " + deposit)

    if deposit < 0:
        raise ValueError("Deposit cannot be negative.")

    interest = 0.0

    # Tier definitions
    tier1_limit = 1000
    tier1_rate = 0.03

    tier2_limit = 10000
    tier2_rate = 0.035

    tier3_limit = 100000
    tier3_rate = 0.04

    tier4_rate = 0.045

    # Tier 1
    if deposit > 0:
        amount_in_tier1 = min(deposit, tier1_limit)
        interest += amount_in_tier1 * tier1_rate
        print(f"Tier 1: Deposit: {deposit}, Amount in Tier 1: {amount_in_tier1}, Interest from Tier 1: {amount_in_tier1 * tier1_rate:.2f}") 

    # Tier 2
    if deposit > tier1_limit:
        amount_in_tier2 = min(deposit - tier1_limit, tier2_limit)
        interest += amount_in_tier2 * tier2_rate
        print(f"Tier 2: Deposit: {deposit}, Amount in Tier 2: {amount_in_tier2}, Interest from Tier 2: {amount_in_tier2 * tier2_rate:.2f}")

    # Tier 3
    if deposit > (tier1_limit + tier2_limit):
        amount_in_tier3 = min(deposit, tier3_limit)
        tier3_int = (amount_in_tier3 - (tier1_limit + tier2_limit)) * tier3_rate
        interest += tier3_int
        print(f"Tier 3: Deposit: {deposit}, Amount in Tier 3: {amount_in_tier3}, Interest from Tier 3: {tier3_int:.2f}")


    # Tier 4
    if deposit > tier3_limit:
        amount_in_tier4 = deposit - tier3_limit
        interest += amount_in_tier4 * tier4_rate
        print(f"Tier 4: Deposit: {deposit}, Amount in Tier 4: {amount_in_tier4}, Interest from Tier 4: {amount_in_tier4 * tier4_rate:.2f}")     

    return f"{interest:.2f}"


