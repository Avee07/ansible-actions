import os

greeting = os.environ.get("GREETING")
dynamic_var = os.environ.get("MY_DYNAMIC_VAR")

print(f"GREETING from GitHub Actions: {greeting}")
print(f"Today's date (from MY_DYNAMIC_VAR): {dynamic_var}")
