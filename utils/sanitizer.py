# sanitizer.py

import html

def sanitize_html(content):
    """
    Sanitizes HTML content to prevent potential security risks.

    :param content: The HTML content to sanitize.
    :return: Sanitized content.
    """
    return html.escape(content)

def sanitize_string(text):
    """
    Sanitizes a string by escaping potentially dangerous characters.

    :param text: The string to sanitize.
    :return: Sanitized string.
    """
    # Replace or remove potentially dangerous characters
    # This is a basic example; adjust the logic as per your requirements
    sanitized_text = text.replace('<', '').replace('>', '').replace('"', '').replace("'", '')
    return sanitized_text

# Example usage
if __name__ == '__main__':
    example_html = "<script>alert('malicious code')</script>"
    example_string = "Some potentially unsafe string <script>alert('oops')</script>"

    print("Sanitized HTML:", sanitize_html(example_html))
    print("Sanitized String:", sanitize_string(example_string))
