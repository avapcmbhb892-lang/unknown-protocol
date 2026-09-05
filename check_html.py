from pathlib import Path
import re

p = Path("index.html")
text = p.read_text(encoding="utf-8")

errors = []

if text.count("<html") != 1:
    errors.append("❌ Неверное количество <html>")

if text.count("</html>") != 1:
    errors.append("❌ Неверное количество </html>")

if text.count("<body") != 1:
    errors.append("❌ Неверное количество <body>")

if text.count("</body>") != 1:
    errors.append("❌ Неверное количество </body>")

tail = text[text.lower().rfind("</html>") + len("</html>"):]
if tail.strip():
    errors.append("❌ После </html> найден лишний код")

if text.count("<style") != text.count("</style>"):
    errors.append("❌ Не совпадает количество <style> и </style>")

if text.count("<script") != text.count("</script>"):
    errors.append("❌ Не совпадает количество <script> и </script>")

# Проверяем подозрительный CSS вне style
clean = re.sub(r"<style\b[^>]*>.*?</style>", "", text, flags=re.S|re.I)
if re.search(r"\.[a-zA-Z][\w-]*\s*\{[^}]*\}", clean):
    errors.append("❌ Похоже, CSS оказался вне <style>")

if errors:
    print("\n".join(errors))
    print("\n🚫 ПРОВЕРКА НЕ ПРОЙДЕНА")
    raise SystemExit(1)

print("✅ HTML ПРОВЕРЕН")
print("✅ Структура корректная")
print("✅ Лишнего кода после </html> нет")
print("✅ CSS находится внутри <style>")
print("✅ Script-блоки закрыты")
