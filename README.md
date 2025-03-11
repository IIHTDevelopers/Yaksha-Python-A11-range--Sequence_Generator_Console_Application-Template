# System Requirements Specification
# Sequence Generator Console Application Version 1.0
To run all tests 
python -m pytest test/

## TABLE OF CONTENTS
1. Project Abstract
2. Business Requirements
3. Constraints
4. Template Code Structure
5. Execution Steps to Follow

# Sequence Generator Console Requirements Specification

## 1. PROJECT ABSTRACT
Number Sequence Labs, a small educational software company, requires a simple sequence generation application to help students learn about numerical patterns. The company needs a Python console application that demonstrates different ways to use the range() function for generating and working with sequences. The system will generate basic numerical sequences, analyze simple properties, and demonstrate the flexibility of range() iterations in Python.

## 2. BUSINESS REQUIREMENTS
Screen Name: Console input screen

Problem Statement:
1. Application must demonstrate the four ways to use range() function
2. System must generate different types of sequences (basic, custom, stepped, reverse)
3. Program must analyze basic sequence properties (sum, count, etc.)
4. System must handle input validation and error conditions

## 3. CONSTRAINTS

### 3.1 INPUT REQUIREMENTS
1. Sequence Parameters:
   - Must accept parameters for range() function 
   - Parameters include: start, end, step values
   - Example: For range(5, 15, 2) - start=5, end=15, step=2

2. Sequence Types:
   - Basic sequence: range(n)
   - Custom sequence: range(start, end)
   - Stepped sequence: range(start, end, step)
   - Reverse sequence: range(start, end, -step)

### 3.2 CALCULATION CONSTRAINTS

1. Basic Sequence Generation:
   - Must use range() with single parameter
   - Example: range(10) to generate [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   - Must return list of generated sequence values

2. Custom Range Iteration:
   - Must use range() with start, stop parameters
   - Example: range(5, 15) to generate [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
   - Must return list with custom start value

3. Stepped Sequence Generation:
   - Must use range() with start, stop, step parameters
   - Example: range(0, 20, 2) for [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
   - Must use step parameter to control increments

4. Reverse Sequence Generation:
   - Must use range() with negative step parameter
   - Example: range(10, 0, -1) for [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
   - Must handle decreasing sequences correctly

### 3.3 OUTPUT CONSTRAINTS

1. Display Format:
   - Show "Sequence Generator System"
   - Show sequence type and parameters used
   - Show generated sequence and basic properties

2. Sequence Properties:
   - Show length, sum, and average of sequence
   - Show count of even and odd numbers
   - Simple formatted output for readability

## 4. TEMPLATE CODE STRUCTURE
1. Generator Functions:
   - generate_basic_sequence(count)
   - generate_custom_sequence(start, end)
   - generate_stepped_sequence(start, end, step)
   - generate_reverse_sequence(start, end, step)
   - analyze_sequence(sequence)

2. Main Program:
   - Display menu options
   - Get user input for parameters
   - Call appropriate generation function
   - Display results in formatted output

## 5. EXECUTION STEPS TO FOLLOW
1. Run the program
2. Select sequence generation method from menu
3. Enter required parameters
4. View generated sequence and properties
5. Repeat or exit

This application demonstrates proper usage of the range() function in Python for generating and working with numerical sequences.