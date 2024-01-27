# Coke-Machine Project

This GitHub repository contains a Python program, `coke.py`, that simulates a Coke vending machine, prompting users to insert coins until at least 50 cents is reached, and then providing the calculated change owed. The project is part of CS50's Python curriculum, and testing instructions are included for verification.

## Overview
The `coke.py` program implements a simple Coke Machine simulation in Python. It emulates a vending machine that sells bottles of Coca-Cola for 50 cents and only accepts coins in denominations of 25 cents, 10 cents, and 5 cents. Users are prompted to insert coins one at a time until the amount due reaches at least 50 cents. The program then calculates and displays the change owed to the user.

## Getting Started
1. Log into cs50.dev and open your terminal.
2. Execute the following commands to set up your project:
   ```bash
   mkdir coke
   cd coke
   code coke.py
   ```
3. Write your program in the `coke.py` file.

## Usage
1. Run the program by executing `python coke.py`.
2. Enter valid coin denominations (5, 10, or 25) at the "Insert Coin:" prompt.
3. The program will display the updated "Amount Due" after each input.
4. Once the amount due reaches or exceeds 50 cents, the program will output the "Change Owed" and terminate.

## How to Test
Manually test your code using the following steps:
1. Run your program with `python coke.py`.
2. At the "Insert Coin:" prompt, type the desired coin denomination and press Enter.
3. Verify that the program correctly calculates the amount due and continues prompting for coins.
4. Ensure that the program handles invalid denominations and provides appropriate feedback.
5. Test scenarios where the user inputs enough coins to receive change.
