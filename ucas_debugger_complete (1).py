"""
UCAS Debugger - Unified Control Automation System Debugging Tool

Provides method-level instrumentation with execution timing, structured logging,
and performance bottleneck detection for AWS Lambda microservices.

Features:
- Colored console output for local development
- Structured JSON logs for CloudWatch production logging
- Auto-environment detection (no code changes needed)
- Dynamic performance tracking and bottleneck identification
- Visual performance breakdown with color-coded bars

Usage:
    from ucas_debugger import UCASDebugger
    
    # Auto-detect environment
    import os
    is_local = os.getenv('AWS_EXECUTION_ENV') is None
    ucas = UCASDebugger(logger, colored_output=is_local)
    
    # In your methods
    ucas.method_start("my_method", param1="value")
    # ... your code ...
    ucas.method_stop("my_method", result="success")
"""

import time
from aws_lambda_powertools import Logger


class Colors:
    """ANSI color codes for terminal output"""
    # Status colors
    HEADER = '\033[95m'      # Magenta
    CYAN = '\033[96m'        # Cyan
    BLUE = '\033[94m'        # Blue
    GREEN = '\033[92m'       # Green
    WARNING = '\033[93m'     # Yellow
    ERROR = '\033[91m'       # Red
    
    # Special
    PASS = '\033[92m'        # Green (for success)
    STOP = '\033[92m'        # Green (for fast completions)
    
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'          # Reset


class UCASDebugger:
    """
    UCAS Debugger for Lambda microservices.
    
    Provides method-level execution tracking with timing, metrics logging,
    and performance analysis.
    """
    
    def __init__(self, logger_instance: Logger, colored_output: bool = False):
        """
        Initialize UCAS Debugger.
        
        Args:
            logger_instance: AWS Lambda Powertools Logger instance
            colored_output: True for colored console output (local dev),
                          False for structured JSON (production)
        """
        self.logger = logger_instance
        self.colored_output = colored_output
        self.start_time = None
        self.method_name = None
        self.durations = {}  # Store all method durations for analysis
    
    def _color_print(self, color: str, message: str):
        """Print colored message to console."""
        if self.colored_output:
            print(f"{color}{message}{Colors.END}")
    
    def method_start(self, method_name: str, **parameters):
        """
        Log the start of a method execution.
        
        Args:
            method_name: Name of the method being executed
            **parameters: Key-value pairs of method parameters to log
        """
        self.start_time = time.time()
        self.method_name = method_name
        
        if self.colored_output:
            # Colored console output for local development
            params_str = ", ".join(f"{k}={v}" for k, v in parameters.items())
            self._color_print(
                Colors.BLUE + Colors.BOLD,
                f"▶ START: {method_name} ({params_str})"
            )
        else:
            # Structured JSON for CloudWatch
            self.logger.info(
                f"Method started: {method_name}",
                extra={
                    "event": "method_start",
                    "method": method_name,
                    "parameters": parameters
                }
            )
    
    def method_stop(self, method_name: str, **metrics):
        """
        Log the completion of a method execution with timing.
        
        Args:
            method_name: Name of the method that completed
            **metrics: Key-value pairs of metrics to log (e.g., record_count, status)
        """
        duration_ms = None
        if self.start_time:
            duration_ms = round((time.time() - self.start_time) * 1000, 2)
            # Store duration for performance analysis
            self.durations[method_name] = duration_ms
        
        if self.colored_output:
            # Colored console output with visual indicators
            metrics_str = ", ".join(f"{k}={v}" for k, v in metrics.items())
            
            # Color based on duration: green < 1s, yellow >= 1s
            if duration_ms and duration_ms < 1000:
                color = Colors.PASS + Colors.BOLD
            else:
                color = Colors.WARNING + Colors.BOLD
            
            self._color_print(
                color,
                f"■ STOP: {method_name} [{duration_ms}ms] ({metrics_str})"
            )
        else:
            # Structured JSON for CloudWatch with queryable fields
            self.logger.info(
                f"Method completed: {method_name}",
                extra={
                    "event": "method_stop",
                    "method": method_name,
                    "duration_ms": duration_ms,
                    "metrics": metrics
                }
            )
        
        # Reset for next method
        self.start_time = None
    
    def log_metrics(self, **metrics):
        """
        Log intermediate metrics during method execution.
        
        Args:
            **metrics: Key-value pairs of metrics to log
        """
        if self.colored_output:
            # Colored console output
            metrics_str = ", ".join(f"{k}={v}" for k, v in metrics.items())
            self._color_print(
                Colors.WARNING,
                f"  ℹ METRICS: {self.method_name} → {metrics_str}"
            )
        else:
            # Structured JSON for CloudWatch
            self.logger.debug(
                "Method metrics",
                extra={
                    "event": "metrics",
                    "method": self.method_name,
                    "metrics": metrics
                }
            )
    
    def get_performance_breakdown(self):
        """
        Get performance breakdown with percentages.
        
        Returns:
            List of tuples: (method_name, duration_ms, percentage)
            Sorted by duration (slowest first)
        """
        if not self.durations:
            return []
        
        # Calculate total (use handler if available, otherwise sum all)
        total = self.durations.get('handler', sum(self.durations.values()))
        
        # Calculate percentages for each method
        breakdown = []
        for method, duration in sorted(self.durations.items(), key=lambda x: x[1], reverse=True):
            if method != 'handler':  # Exclude handler from breakdown (it's the total)
                percentage = (duration / total) * 100
                breakdown.append((method, duration, percentage))
        
        return breakdown
    
    def get_bottleneck(self):
        """
        Automatically identify the performance bottleneck.
        
        Returns:
            Tuple of (method_name, duration_ms, percentage) or None if no data
        """
        breakdown = self.get_performance_breakdown()
        if not breakdown:
            return None
        
        # Bottleneck is the slowest method (first in sorted list)
        return breakdown[0]
    
    def print_performance_summary(self, total_duration_ms: float = None):
        """
        Print a formatted performance breakdown with visual bars.
        
        Args:
            total_duration_ms: Optional total duration override
        """
        if not self.colored_output:
            return  # Only print for local/colored mode
        
        breakdown = self.get_performance_breakdown()
        if not breakdown:
            return
        
        # Get total duration
        total = total_duration_ms or self.durations.get('handler', sum(d for _, d, _ in breakdown))
        
        # Print header
        print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}📊 Performance Breakdown{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}")
        
        # Print each method with visual bar
        for method, duration, percentage in breakdown:
            # Color based on percentage of total time
            if percentage > 50:
                color = Colors.ERROR  # Red for major bottlenecks
                icon = "🔴"
            elif percentage > 10:
                color = Colors.WARNING  # Yellow for moderate time
                icon = "🟡"
            else:
                color = Colors.PASS  # Green for fast operations
                icon = "🟢"
            
            # Create visual bar (max 50 characters)
            bar_length = int(percentage / 2)
            bar = "█" * bar_length
            
            # Print formatted line with bar
            print(f"{color}{icon} {method:40} {bar} {duration:7.2f}ms ({percentage:5.1f}%){Colors.END}")
        
        # Print footer with totals
        print(f"{Colors.HEADER}{Colors.BOLD}{'─'*70}{Colors.END}")
        print(f"{Colors.BOLD}   Total Duration: {total:.2f}ms{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    def print_bottleneck_alert(self):
        """
        Print an alert highlighting the performance bottleneck.
        """
        if not self.colored_output:
            return
        
        bottleneck = self.get_bottleneck()
        if not bottleneck:
            return
        
        method, duration, percentage = bottleneck
        
        print(f"{Colors.ERROR}{Colors.BOLD}🔴 BOTTLENECK DETECTED:{Colors.END}")
        print(f"   Method: {Colors.BOLD}{method}{Colors.END}")
        print(f"   Duration: {Colors.ERROR}{duration:.2f}ms{Colors.END} ({percentage:.1f}% of total execution)")
        print(f"   💡 Recommendation: Optimize {Colors.UNDERLINE}{method}{Colors.END} for better performance\n")
    
    def print_error(self, error: Exception):
        """
        Print a formatted error message in red.
        
        Args:
            error: The exception that occurred
        """
        if not self.colored_output:
            return
        
        print(f"\n{Colors.ERROR}{Colors.BOLD}{'='*70}{Colors.END}")
        print(f"{Colors.ERROR}{Colors.BOLD}❌ ERROR: {type(error).__name__}{Colors.END}")
        print(f"{Colors.ERROR}{Colors.BOLD}{'='*70}{Colors.END}")
        print(f"{Colors.ERROR}{str(error)}{Colors.END}")
        print(f"{Colors.ERROR}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    def print_summary(self, title: str = "EXECUTION SUMMARY", **summary_items):
        """
        Print a formatted summary box.
        
        Args:
            title: Title for the summary box
            **summary_items: Key-value pairs to display in summary
        """
        if not self.colored_output:
            return
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}{title:^70}{Colors.END}")
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}")
        
        for key, value in summary_items.items():
            formatted_key = key.replace('_', ' ').title()
            print(f"   {formatted_key}: {Colors.BOLD}{value}{Colors.END}")
        
        print(f"{Colors.HEADER}{Colors.BOLD}{'='*70}{Colors.END}\n")
