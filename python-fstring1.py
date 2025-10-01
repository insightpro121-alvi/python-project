import string

def to_title(s: str) -> str:
    """Convert a string to title case."""
    return s.title()

def count_vowels(s: str) -> int:
    """Count vowels (a, e, i, o, u) in a string."""
    return sum(1 for ch in s if ch.lower() in "aeiou")

def remove_punctuation(s: str) -> str:
    """Remove punctuation from a string."""
    return "".join(ch for ch in s if ch not in string.punctuation)

# Demo
print(to_title("hello world"))          # Hello World
print(count_vowels("python"))           # 1
print(remove_punctuation("Hello, world!"))  # Hello world

  