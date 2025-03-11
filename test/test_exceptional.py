import pytest
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_invalid_inputs(test_obj):
    """Test handling of invalid inputs (None, wrong types, invalid values)"""
    try:
        import sequence_generator_console_application as app
        
        # Test None inputs
        with pytest.raises(TypeError):
            app.generate_basic_sequence(None)
        with pytest.raises(TypeError):
            app.generate_custom_sequence(None, 10)
        with pytest.raises(TypeError):
            app.analyze_sequence(None)
            
        # Test wrong data types
        with pytest.raises(TypeError):
            app.generate_basic_sequence("5")
        with pytest.raises(TypeError):
            app.generate_stepped_sequence(0, 10, "2")
        with pytest.raises(TypeError):
            app.analyze_sequence("not a list")
            
        # Test invalid values
        with pytest.raises(ValueError):
            app.generate_basic_sequence(-5)  # Negative count
        with pytest.raises(ValueError):
            app.generate_custom_sequence(10, 5)  # Start >= end
        with pytest.raises(ValueError):
            app.generate_stepped_sequence(0, 10, 0)  # Zero step
        with pytest.raises(ValueError):
            app.generate_stepped_sequence(10, 5, 1)  # Start >= end with positive step
        with pytest.raises(ValueError):
            app.generate_reverse_sequence(5, 10, -1)  # Start <= end for reverse
        with pytest.raises(ValueError):
            app.generate_reverse_sequence(10, 5, 1)  # Positive step for reverse
            
        test_obj.yakshaAssert("TestInvalidInputs", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInvalidInputs", False, "exception")
        pytest.fail(f"Invalid inputs test failed: {str(e)}")

def test_empty_sequences(test_obj):
    """Test proper handling of valid empty sequences"""
    try:
        import sequence_generator_console_application as app
        
        # Test empty but valid sequences
        empty_basic = app.generate_basic_sequence(0)
        assert empty_basic == [], "Should return empty list for count=0"
        
        # Test analyze_sequence with empty list
        props = app.analyze_sequence([])
        assert props["length"] == 0, "Empty sequence length should be 0"
        assert props["sum"] == 0, "Empty sequence sum should be 0"
        assert props["average"] == 0, "Empty sequence average should be 0"
        assert props["even_count"] == 0, "Empty sequence even count should be 0"
        assert props["odd_count"] == 0, "Empty sequence odd count should be 0"
        
        test_obj.yakshaAssert("TestEmptySequences", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestEmptySequences", False, "exception")
        pytest.fail(f"Empty sequences test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])