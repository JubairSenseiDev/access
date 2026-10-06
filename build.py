import marshal

with open("offline.py", "r", encoding="utf-8") as f:
    code = compile(f.read(), "offline.py", "exec")

with open("payload.bin", "wb") as f:
    marshal.dump(code, f)

print("✓ payload.bin created")
