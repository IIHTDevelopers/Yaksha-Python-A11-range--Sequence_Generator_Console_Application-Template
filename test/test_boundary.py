import pytest
from test.TestUtils import TestUtils

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_conditions(test_obj):
    """Test empty data and boundary values"""
    try:
        import sequence_generator_console_application as app
        
        # Empty sequences
        empty_basic = app.generate_basic_sequence(0)
        assert empty_basic == [], "Should return empty list for count=0"
        
        empty_props = app.analyze_sequence([])
        assert empty_props["length"] == 0 and empty_props["sum"] == 0 and empty_props["average"] == 0, "Should handle empty sequence analysis"
        
        # Minimal sequences (single element)
        assert app.generate_basic_sequence(1) == [0], "Should return [0] for count=1"
        assert app.generate_custom_sequence(5, 6) == [5], "Should return [5] for range(5,6)"
        assert app.generate_stepped_sequence(0, 10, 10) == [0], "Should return [0] for range(0,10,10)"
        assert app.generate_reverse_sequence(1, 0, -1) == [1], "Should return [1] for range(1,0,-1)"
        
        test_obj.yakshaAssert("TestBoundaryConditions", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryConditions", False, "boundary")
        pytest.fail(f"Boundary conditions test failed: {str(e)}")

def test_large_datasets(test_obj):
    """Test system with large datasets"""
    try:
        import sequence_generator_console_application as app
        
        # Generate large sequence
        large_seq = app.generate_basic_sequence(1000)
        assert len(large_seq) == 1000, "Should handle large sequence generation"
        
        # Analyze properties
        props = app.analyze_sequence(large_seq)
        assert props["length"] == 1000, "Should correctly count large sequence length"
        assert props["sum"] == 499500, "Should correctly sum large sequence"
        assert abs(props["average"] - 499.5) < 0.001, "Should correctly calculate average"
        assert props["even_count"] == 500 and props["odd_count"] == 500, "Should correctly count even/odd numbers"
        
        # Test large stepped sequence
        large_stepped = app.generate_stepped_sequence(0, 10000, 100)
        assert len(large_stepped) == 100, "Should handle large stepped sequence"
        assert large_stepped[-1] == 9900, "Should correctly generate last element"
        
        test_obj.yakshaAssert("TestLargeDatasets", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestLargeDatasets", False, "boundary")
        pytest.fail(f"Large datasets test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])