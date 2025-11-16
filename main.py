# main.py
import sys
print("Python version:", sys.version)
print("✅ Testing imports...")

try:
    import setuptools
    print("setuptools version:", setuptools.__version__)
except Exception as e:
    print("setuptools error:", e)

try:
    from telegram.ext import Application
    print("✅ telegram-bot imported successfully")
except Exception as e:
    print("❌ telegram-bot import failed:", e)

print("🚀 Render deployment test completed")
