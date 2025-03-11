from datetime import datetime

def generate_basic_sequence(count):
    """
    Generate a basic sequence using range() with a single parameter
    Return: List of integers from 0 to count-1
    Example: generate_basic_sequence(5) returns [0, 1, 2, 3, 4]
    """
    if count is None:
        raise TypeError("count cannot be None")
    
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    
    if count < 0:
        raise ValueError("count cannot be negative")
        
    sequence = []
    
    for num in range(count):
        sequence.append(num)
        
    return sequence

def generate_custom_sequence(start, end):
    """
    Generate a custom sequence using range() with start and end parameters
    Return: List of integers from start to end-1
    Example: generate_custom_sequence(5, 10) returns [5, 6, 7, 8, 9]
    """
    if start is None or end is None:
        raise TypeError("start and end cannot be None")
    
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    
    if start >= end:
        raise ValueError("start must be less than end")
        
    sequence = []
    
    for num in range(start, end):
        sequence.append(num)
        
    return sequence

def generate_stepped_sequence(start, end, step):
    """
    Generate a stepped sequence using range() with start, end, and step parameters
    Return: List of integers from start to end-1 with specified step
    Example: generate_stepped_sequence(0, 10, 2) returns [0, 2, 4, 6, 8]
    """
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
        
    sequence = []
    
    for num in range(start, end, step):
        sequence.append(num)
        
    return sequence

def generate_reverse_sequence(start, end, step):
    """
    Generate a reverse sequence using range() with negative step parameter
    Return: List of integers from start to end+1 with specified negative step
    Example: generate_reverse_sequence(10, 0, -1) returns [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    if start is None or end is None or step is None:
        raise TypeError("start, end, and step cannot be None")
    
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
        raise TypeError("start, end, and step must be integers")
    
    if step >= 0:
        raise ValueError("step must be negative for reverse sequence")
    
    if start <= end:
        raise ValueError("start must be greater than end for reverse sequence")
        
    sequence = []
    
    for num in range(start, end, step):
        sequence.append(num)
        
    return sequence

def analyze_sequence(sequence):
    """
    Analyze basic properties of a sequence
    Return: Dictionary with sequence properties
    """
    if sequence is None:
        raise TypeError("sequence cannot be None")
    
    if not isinstance(sequence, list):
        raise TypeError("sequence must be a list")
        
    properties = {
        "length": len(sequence),
        "sum": sum(sequence),
        "even_count": 0,
        "odd_count": 0
    }
    
    # Skip further analysis if empty
    if not sequence:
        properties["average"] = 0
        return properties
    
    # Count even and odd numbers
    for num in sequence:
        if num % 2 == 0:
            properties["even_count"] += 1
        else:
            properties["odd_count"] += 1
    
    # Calculate average
    properties["average"] = properties["sum"] / len(sequence)
    
    return properties

def display_sequence_report(sequence, properties, sequence_type):
    """Display formatted sequence report"""
    print("\nSequence Generator System")
    print(f"Sequence Type: {sequence_type}")
    print("-" * 50)
    
    if not sequence:
        print("Empty sequence - no data to display")
        return
    
    # Format sequence for display (limit to 15 items if longer)
    if len(sequence) > 15:
        display_seq = str(sequence[:15])[:-1] + ", ...]"
    else:
        display_seq = str(sequence)
    
    print(f"Generated Sequence: {display_seq}")
    print("-" * 50)
    print(f"Sequence Length: {properties['length']}")
    print(f"Sum: {properties['sum']}")
    print(f"Average: {properties['average']:.2f}")
    print(f"Even Numbers: {properties['even_count']}")
    print(f"Odd Numbers: {properties['odd_count']}")

def main():
    """Main program execution"""
    while True:
        print("\nSequence Generator System")
        print("1. Generate Basic Sequence (range(n))")
        print("2. Generate Custom Sequence (range(start, end))")
        print("3. Generate Stepped Sequence (range(start, end, step))")
        print("4. Generate Reverse Sequence (range(start, end, -step))")
        print("5. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            
            if choice == 1:
                count = int(input("Enter count (n): "))
                sequence = generate_basic_sequence(count)
                properties = analyze_sequence(sequence)
                display_sequence_report(sequence, properties, "Basic Sequence")
                
            elif choice == 2:
                start = int(input("Enter start value: "))
                end = int(input("Enter end value: "))
                sequence = generate_custom_sequence(start, end)
                properties = analyze_sequence(sequence)
                display_sequence_report(sequence, properties, "Custom Sequence")
                
            elif choice == 3:
                start = int(input("Enter start value: "))
                end = int(input("Enter end value: "))
                step = int(input("Enter step value: "))
                sequence = generate_stepped_sequence(start, end, step)
                properties = analyze_sequence(sequence)
                display_sequence_report(sequence, properties, "Stepped Sequence")
                
            elif choice == 4:
                start = int(input("Enter start value: "))
                end = int(input("Enter end value: "))
                step = int(input("Enter step value (must be negative): "))
                sequence = generate_reverse_sequence(start, end, step)
                properties = analyze_sequence(sequence)
                display_sequence_report(sequence, properties, "Reverse Sequence")
                
            elif choice == 5:
                print("Thank you for using the Sequence Generator System!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                
        except ValueError as e:
            if str(e).startswith("invalid literal for int"):
                print("Invalid input. Please enter a number.")
            else:
                print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()