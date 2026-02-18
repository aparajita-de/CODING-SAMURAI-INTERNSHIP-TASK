# test_venv_complete.py - Fixed Version
import sys
import platform

print("=" * 50)
print("PYTHON ENVIRONMENT TEST")
print("=" * 50)

print(f"\n📌 Python version: {platform.python_version()}")
print(f"📌 Python executable: {sys.executable}")
print(f"📌 Platform: {platform.system()} {platform.release()}")

# Test imports
print("\n📦 Testing package imports:")
print("-" * 40)

# Test requests
try:
    import requests
    print(f"✅ requests: {requests.__version__}")
except ImportError as e:
    print(f"❌ requests: NOT INSTALLED - {e}")

# Test BeautifulSoup (fixed version - no __version__ attribute)
try:
    from bs4 import BeautifulSoup
    # BeautifulSoup doesn't have __version__, so we check differently
    print("✅ BeautifulSoup: Installed successfully")
    # Try to get version from the module
    import bs4
    print(f"   bs4 version: {bs4.__version__}")
except ImportError as e:
    print(f"❌ BeautifulSoup: NOT INSTALLED - {e}")

# Test pandas
try:
    import pandas as pd
    print(f"✅ pandas: {pd.__version__}")
except ImportError as e:
    print(f"❌ pandas: NOT INSTALLED - {e}")

# Test csv (built-in)
try:
    import csv
    print("✅ csv: Built-in module")
except ImportError as e:
    print(f"❌ csv: Should be built-in, something's wrong - {e}")

print("\n" + "=" * 50)
print("\n🎉 Test complete!")
print("=" * 50)

input("\nPress Enter to exit...")