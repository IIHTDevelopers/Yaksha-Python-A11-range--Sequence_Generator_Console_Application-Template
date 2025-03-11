import pytest
import re
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_required_functions(test_obj):
    """Test if all required functions are defined with exact naming"""
    try:
        with open('sequence_generator_console_application.py', 'r') as file:
            content = file.read()
        
        required_functions = {
            'generate_basic_sequence': r'def\s+generate_basic_sequence\s*\(\s*count\s*\)',
            'generate_custom_sequence': r'def\s+generate_custom_sequence\s*\(\s*start\s*,\s*end\s*\)',
            'generate_stepped_sequence': r'def\s+generate_stepped_sequence\s*\(\s*start\s*,\s*end\s*,\s*step\s*\)',
            'generate_reverse_sequence': r'def\s+generate_reverse_sequence\s*\(\s*start\s*,\s*end\s*,\s*step\s*\)',
            'analyze_sequence': r'def\s+analyze_sequence\s*\(\s*sequence\s*\)',
            'main': r'def\s+main\s*\(\s*\)'
        }
        
        missing_funcs = []
        for func_name, pattern in required_functions.items():
            if not re.search(pattern, content):
                missing_funcs.append(func_name)
        
        if missing_funcs:
            test_obj.yakshaAssert("TestRequiredFunctions", False, "functional")
            pytest.fail(f"Missing functions: {', '.join(missing_funcs)}")
        else:
            test_obj.yakshaAssert("TestRequiredFunctions", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestRequiredFunctions", False, "functional")
        pytest.fail(f"Function check failed: {str(e)}")

def test_range_implementation(test_obj):
    """Test if range() is used in all sequence generation functions"""
    try:
        with open('sequence_generator_console_application.py', 'r') as file:
            content = file.read()
        
        required_patterns = {
            'basic_range': r'for\s+\w+\s+in\s+range\s*\(\s*\w+\s*\)',
            'custom_range': r'for\s+\w+\s+in\s+range\s*\(\s*\w+\s*,\s*\w+\s*\)',
            'stepped_range': r'for\s+\w+\s+in\s+range\s*\(\s*\w+\s*,\s*\w+\s*,\s*\w+\s*\)',
            'reverse_range': r'for\s+\w+\s+in\s+range\s*\(\s*\w+\s*,\s*\w+\s*,\s*\w+\s*\)'
        }
        
        missing_patterns = []
        for pattern_name, pattern in required_patterns.items():
            if not re.search(pattern, content):
                missing_patterns.append(pattern_name)
        
        if missing_patterns:
            test_obj.yakshaAssert("TestRangeImplementation", False, "functional")
            pytest.fail(f"Missing required range patterns: {', '.join(missing_patterns)}")
        else:
            test_obj.yakshaAssert("TestRangeImplementation", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestRangeImplementation", False, "functional")
        pytest.fail(f"Range implementation check failed: {str(e)}")

def test_sequence_generation_logic(test_obj):
    """Test if all sequence generation functions produce correct output"""
    try:
        import sequence_generator_console_application as app
        
        # Test basic sequence
        assert app.generate_basic_sequence(5) == [0, 1, 2, 3, 4], "Incorrect basic sequence"
        
        # Test custom sequence
        assert app.generate_custom_sequence(5, 10) == [5, 6, 7, 8, 9], "Incorrect custom sequence"
        
        # Test stepped sequence
        assert app.generate_stepped_sequence(0, 10, 2) == [0, 2, 4, 6, 8], "Incorrect stepped sequence"
        assert app.generate_stepped_sequence(10, 0, -2) == [10, 8, 6, 4, 2], "Incorrect stepped sequence with negative step"
        
        # Test reverse sequence
        assert app.generate_reverse_sequence(10, 0, -1) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "Incorrect reverse sequence"
        assert app.generate_reverse_sequence(5, 0, -2) == [5, 3, 1], "Incorrect reverse sequence with step -2"
        
        test_obj.yakshaAssert("TestSequenceGenerationLogic", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestSequenceGenerationLogic", False, "functional")
        pytest.fail(f"Sequence generation logic failed: {str(e)}")

def test_error_handling(test_obj):
    """Test error handling in all functions"""
    try:
        import sequence_generator_console_application as app
        
        # Test error handling in basic sequence
        with pytest.raises(ValueError):
            app.generate_basic_sequence(-1)
        with pytest.raises(TypeError):
            app.generate_basic_sequence("5")
            
        # Test error handling in custom sequence
        with pytest.raises(ValueError):
            app.generate_custom_sequence(10, 5)
        with pytest.raises(TypeError):
            app.generate_custom_sequence("5", 10)
            
        # Test error handling in stepped sequence
        with pytest.raises(ValueError):
            app.generate_stepped_sequence(0, 10, 0)
        with pytest.raises(ValueError):
            app.generate_stepped_sequence(10, 5, 1)
            
        # Test error handling in reverse sequence
        with pytest.raises(ValueError):
            app.generate_reverse_sequence(10, 0, 1)
        with pytest.raises(ValueError):
            app.generate_reverse_sequence(5, 10, -1)
            
        # Test error handling in analyze sequence
        with pytest.raises(TypeError):
            app.analyze_sequence("not a list")
            
        test_obj.yakshaAssert("TestErrorHandling", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestErrorHandling", False, "functional")
        pytest.fail(f"Error handling test failed: {str(e)}")

def test_analyze_sequence_logic(test_obj):
    """Test if analyze_sequence correctly analyzes sequence properties"""
    try:
        import sequence_generator_console_application as app
        
        # Test with normal sequence
        result = app.analyze_sequence([1, 2, 3, 4, 5])
        assert result["length"] == 5, "Length should be 5"
        assert result["sum"] == 15, "Sum should be 15"
        assert result["average"] == 3.0, "Average should be 3.0"
        assert result["even_count"] == 2, "Even count should be 2"
        assert result["odd_count"] == 3, "Odd count should be 3"
        
        # Test with empty sequence
        result = app.analyze_sequence([])
        assert result["length"] == 0, "Length should be 0"
        assert result["sum"] == 0, "Sum should be 0"
        assert result["average"] == 0, "Average should be 0"
        
        test_obj.yakshaAssert("TestAnalyzeSequenceLogic", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("TestAnalyzeSequenceLogic", False, "functional")
        pytest.fail(f"Analyze sequence logic check failed: {str(e)}")

def test_main_menu_options(test_obj):
    """Test if main function includes all required menu options"""
    try:
        with open('sequence_generator_console_application.py', 'r') as file:
            content = file.read()
        
        required_menu_items = [
            r"Generate Basic Sequence",
            r"Generate Custom Sequence",
            r"Generate Stepped Sequence",
            r"Generate Reverse Sequence",
            r"Exit"
        ]
        
        missing_items = []
        for item in required_menu_items:
            if not re.search(item, content):
                missing_items.append(item)
        
        if missing_items:
            test_obj.yakshaAssert("TestMainMenuOptions", False, "functional")
            pytest.fail(f"Missing menu items: {', '.join(missing_items)}")
        else:
            test_obj.yakshaAssert("TestMainMenuOptions", True, "functional")
            
    except Exception as e:
        test_obj.yakshaAssert("TestMainMenuOptions", False, "functional")
        pytest.fail(f"Main menu options check failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])