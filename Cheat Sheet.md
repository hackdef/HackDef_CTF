This is a quick Linux Cheat sheet to troubleshoot problems in Linux servers

1. Safe Environment Check
```
import importlib
import inspect
import sys
from typing import List, Dict, Optional

class SandboxEscapeScanner:
    def __init__(self):
        self.dangerous_patterns = [
            ('constructor', 'call'),  # Pyodide-style FFI
            ('eval', 'exec'),        # Direct code evaluation
            ('_make_', '_call_'),    # Common binding patterns
            ('Function', 'Proxy'),   # JavaScript-like interfaces
            ('untrusted', 'unsafe')  # Common warning terms
        ]
        self.suspicious_packages = []
        self.verified_escapes = []

    def scan_module(self, module_name: str) -> Optional[Dict]:
        """Scan a single module for dangerous patterns"""
        try:
            module = importlib.import_module(module_name)
            results = {
                'module': module_name,
                'patterns_found': [],
                'dangerous_attrs': []
            }

            # Check module-level attributes
            for attr_name, attr in inspect.getmembers(module):
                for pattern in self.dangerous_patterns:
                    if any(p in attr_name.lower() for p in pattern):
                        results['patterns_found'].extend(pattern)
                        try:
                            if callable(attr):
                                results['dangerous_attrs'].append({
                                    'name': attr_name,
                                    'type': 'callable',
                                    'source': inspect.getsource(attr) if inspect.isfunction(attr) else str(attr)
                                })
                            else:
                                results['dangerous_attrs'].append({
                                    'name': attr_name,
                                    'type': type(attr).__name__,
                                    'value': str(attr)
                                })
                        except:
                            continue

            if results['patterns_found']:
                return results
            return None

        except Exception as e:
            return {'module': module_name, 'error': str(e)}

    def test_escape_vector(self, module_name: str, attr_name: str) -> bool:
        """Test if a found attribute can actually execute code"""
        try:
            module = importlib.import_module(module_name)
            attr = getattr(module, attr_name)

            # Test for constructor pattern
            if attr_name.lower() == 'constructor':
                test_fn = attr('return "EXEC_SUCCESS"')
                if callable(test_fn):
                    result = test_fn()
                    if result == "EXEC_SUCCESS":
                        return True

            # Test for direct eval/exec
            if attr_name.lower() in ('eval', 'exec'):
                test_code = 'print("EXEC_TEST")'
                if callable(attr):
                    attr(test_code)
                    return True

            return False
        except:
            return False

    def scan_installed_packages(self) -> List[Dict]:
        """Scan all installed packages for dangerous patterns"""
        for module_name in list(sys.modules.keys()) + self._find_importable_modules():
            if not module_name or module_name.startswith('_'):
                continue

            result = self.scan_module(module_name)
            if result and 'error' not in result:
                self.suspicious_packages.append(result)

                # Test each dangerous attribute
                for attr in result['dangerous_attrs']:
                    if self.test_escape_vector(module_name, attr['name']):
                        self.verified_escapes.append({
                            'module': module_name,
                            'attribute': attr['name'],
                            'type': 'verified_escape'
                        })

        return {
            'suspicious': self.suspicious_packages,
            'verified': self.verified_escapes
        }

    def _find_importable_modules(self) -> List[str]:
        """Find potentially importable modules not yet loaded"""
        import pkgutil
        return [name for _, name, _ in pkgutil.iter_modules()]

def main():
    scanner = SandboxEscapeScanner()
    results = scanner.scan_installed_packages()
    
    print("\n=== Sandbox Escape Scan Results ===")
    print(f"Scanned {len(results['suspicious'])} packages")
    print(f"Found {len(results['verified'])} verified escape vectors")
    
    if results['verified']:
        print("\n[!] CONFIRMED ESCAPE VECTORS:")
        for escape in results['verified']:
            print(f" - {escape['module']}.{escape['attribute']}")
    
    if results['suspicious']:
        print("\n[!] SUSPICIOUS PATTERNS FOUND IN:")
        for pkg in results['suspicious']:
            print(f" - {pkg['module']}: {', '.join(set(pkg['patterns_found']))}")

if __name__ == "__main__":
    main()
```
