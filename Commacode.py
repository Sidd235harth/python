def commacode(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

# Example usage
if __name__ == "__main__":
    sample_list = ['apples', 'bananas', 'tofu', 'cats']
    result = commacode(sample_list)
    print("Formatted string:", result)
