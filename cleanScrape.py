import re

def remove_invalid_content(file_path, output_path):
    """Parses the input file and removes blocks of content with more than three words containing multiple digits."""
    
    # Open and read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content by '== Content =='
    blocks = content.split('===')[::2]

    # Define a regular expression to find words that contain multiple digits
    word_with_digits_regex = r'\b[a-zA-Z]*[.,!][a-zA-Z]*\d+[a-zA-Z]*\d+[a-zA-Z]*\b'  # Finds words with at least two digits

    # Prepare a list to store valid blocks
    valid_blocks = []

    # Iterate through each block
    for block in blocks:
        # Count words that contain multiple digits
        words_with_digits = re.findall(word_with_digits_regex, block)

        # If there are 3 or fewer words with multiple digits, keep the block
        if len(words_with_digits) <= 3:
            valid_blocks.append(block)

    # Join the valid blocks back together with '=== Content ==='
    filtered_content = '=== Content ==='.join(valid_blocks)

    # Write the filtered content to a new file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(filtered_content)

    print(f"Filtered content saved to {output_path}")

# Usage
remove_invalid_content('scraped_text_3.txt', 'filtered_scraped_text_3.txt')
