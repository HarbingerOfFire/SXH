# SXH.py
class New:
    def __init__(self, _algorithm, _buffer):
        try:
            algorithm_module = __import__(_algorithm.upper())
            algorithm_class = getattr(algorithm_module, _algorithm)
            
            self.algorithm_instance = algorithm_class(_buffer)
        except ImportError:
            print(f"Error: Algorithm {_algorithm} not found.")
        except AttributeError:
            print(f"Error: Class {_algorithm} not found in the {_algorithm.lower()} module.")

    def hash(self):
        if hasattr(self, 'algorithm_instance'):
            return self.algorithm_instance.hash()
        else:
            print("Error: Algorithm instance not found.")

    def hexdigest(self):
        if hasattr(self, 'algorithm_instance'):
            hash_result = self.algorithm_instance.hash()
            return self.algorithm_instance.hexidigest(hash_result)
        else:
            print("Error: Algorithm instance not found.")

if __name__ == "__main__":
    print(New("SXH128", b"a").hexdigest())
    print(New("SXH256", b"a").hexdigest())
    print(New("SXH512", b"a").hexdigest())
