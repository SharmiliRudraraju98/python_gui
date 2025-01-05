# metrics/performance_metrics.py
from collections import defaultdict
import statistics
import time

class PerformanceMetrics:
    def __init__(self):
        self.reset()
    
    def reset(self):
        # Dictionary to store operation counts
        self.operations = defaultdict(int)
        # Dictionary to store execution times for each operation
        self.execution_times = defaultdict(list)
        self.comparisons = 0
        self.rotations = 0
    
    def start_operation(self):
        return time.perf_counter()
    
    def end_operation(self, operation_name, start_time):
        end_time = time.perf_counter()
        duration = end_time - start_time
        self.operations[operation_name] += 1
        self.execution_times[operation_name].append(duration)
    
    def get_avg_time(self, operation_name):
        times = self.execution_times.get(operation_name, [])
        if not times:
            return 0.0
        # Filter out any extreme outliers
        filtered_times = [t for t in times if t < 1.0]  # Remove times > 1 second
        return statistics.mean(filtered_times) if filtered_times else 0.0
    def increment_comparisons(self):
        self.comparisons += 1
    
    def increment_rotations(self):
        self.rotations += 1