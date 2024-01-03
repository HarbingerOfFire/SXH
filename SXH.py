class New:
    def __init__(self, _algorithm, _buffer):
        try:
            algorithm_module = __import__(_algorithm.upper())
            algorithm_class = getattr(algorithm_module, _algorithm)
            
            algorithm_class(_buffer)
        except ImportError:
            print(f"Error: Algorithm {_algorithm} not found.")
        except AttributeError:
            print(f"Error: Class {_algorithm} not found in the {_algorithm.lower()} module.")

if __name__ == "__main__":
    New("SXH128", b"Hello, World!")
