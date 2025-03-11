# DO NOT MODIFY THE SECTIONS MARKED AS "DO NOT MODIFY"

def generate_basic_sequence(count):
    """
    Generate a basic sequence using range() with a single parameter
    Return: List of integers from 0 to count-1
    Example: generate_basic_sequence(5) returns [0, 1, 2, 3, 4]
    """
    # Validation - DO NOT MODIFY
    if count is None:
        raise TypeError("count cannot be None")
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count cannot be negative")
    
    # TODO: Implement the following
    # 1. Create an empty list for the sequence
    # 2. Use range() with a single parameter (count)
    # 3. Append each number from the range to your list
    # 4. Return the completed sequence list
    pass

def generate_custom_sequence(start, end):
    """
    Generate a custom sequence using range() with start and end parameters
    Return: List of integers from start to end-1
    Example: generate_custom_sequence(5, 10) returns [5, 6, 7, 8, 9]
    """
    # Validation - DO NOT MODIFY
    if start is None or end is None:
        raise TypeError("start and end cannot be None")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    if start >= end:
        raise ValueError("start must be less than end")
    
    # TODO: Implement the following
    # 1. Create an empty list for the sequence
    # 2. Use range() with TWO parameters (start, end)
    # 3. Append each number from the range to your list
    # 4. Return the completed sequence list
    pass

def generate_stepped_sequence(start, end, step):
    """
    Generate a stepped sequence using range() with start, end, and step parameters
    Return: List of integers from start to end-1 with specified step
    Example: generate_stepped_sequence(0, 10, 2) returns [0, 2, 4, 6, 8]
    """
    # Validation - DO NOT MODIFY
    if start is None or end is None or step is None:
        raise TypeError("start, end, and step cannot be None")
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
        raise TypeError("start, end, and step must be integers")
    if step == 0:
        raise ValueError("step cannot be zero")
    if step > 0 and start >= end:
        raise ValueError("start must be less than end for positive step")
    if step < 0 and start <= end:
        raise ValueError("start must be greater than end for negative step")
    
    # TODO: Implement the following
    # 1. Create an empty list for the sequence
    # 2. Use range() with THREE parameters (start, end, step)
    # 3. Append each number from the range to your list
    # 4. Return the completed sequence list
    pass

def generate_reverse_sequence(start, end, step):
    """
    Generate a reverse sequence using range() with negative step parameter
    Return: List of integers from start to end+1 with specified negative step
    Example: generate_reverse_sequence(10, 0, -1) returns [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    # Validation - DO NOT MODIFY
    if start is None or end is None or step is None:
        raise TypeError("start, end, and step cannot be None")
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
        raise TypeError("start, end, and step must be integers")
    if step >= 0:
        raise ValueError("step must be negative for reverse sequence")
    if start <= end:
        raise ValueError("start must be greater than end for reverse sequence")
    
    # TODO: Implement the following
    # 1. Create an empty list for the sequence
    # 2. Use range() with THREE parameters (start, end, step) where step is negative
    # 3. Append each number from the range to your list
    # 4. Return the completed sequence list
    pass

def analyze_sequence(sequence):
    """
    Analyze basic properties of a sequence
    Return: Dictionary with sequence properties
    """
    # Validation - DO NOT MODIFY
    if sequence is None:
        raise TypeError("sequence cannot be None")
    if not isinstance(sequence, list):
        raise TypeError("sequence must be a list")
    
    # TODO: Implement the following
    # 1. Create a dictionary to store sequence properties
    # 2. Calculate and store the following properties:
    #    - length: number of elements in the sequence
    #    - sum: sum of all elements in the sequence
    #    - even_count: number of even elements
    #    - odd_count: number of odd elements
    #    - average: average value of all elements (handle empty sequences)
    # 3. Return the completed properties dictionary
    pass

def display_sequence_report(sequence, properties, sequence_type):
    """Display formatted sequence report"""
    # Validation - DO NOT MODIFY
    if sequence is None or properties is None or sequence_type is None:
        print("Cannot display report: Missing required data")
        return
    
    # TODO: Implement the following
    # 1. Print report header with sequence type
    # 2. Check if sequence is empty and display appropriate message
    # 3. Display the sequence (limit display to 15 items if sequence is long)
    # 4. Print sequence properties (length, sum, average, even/odd counts)
    # 5. Format the output to be readable with clear labels
    pass

def main():
    """Main program execution"""
    # TODO: Implement the following
    # 1. Create a loop that continues until user chooses to exit
    # 2. Display menu options for different sequence types:
    #    - Basic Sequence (range(n))
    #    - Custom Sequence (range(start, end))
    #    - Stepped Sequence (range(start, end, step))
    #    - Reverse Sequence (range(start, end, -step))
    #    - Exit
    # 3. Get user choice with appropriate error handling
    # 4. Based on choice, prompt for necessary parameters
    # 5. Call appropriate function to generate sequence
    # 6. Analyze the sequence properties
    # 7. Display a formatted report
    # 8. Continue until user selects exit option
    pass

if __name__ == "__main__":
    main()