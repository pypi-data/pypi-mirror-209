"""Utility functions for denemesonuc package."""
def uppercase_tr(s: str) -> str:
    """Convert Turkish string to uppercase.
    
    Args:
        s: The string that will be converted to uppercase.
    
    Returns:
        The converted string.
    """
    return s.replace("i", "İ").replace("ı", "I").upper()
