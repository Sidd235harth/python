def print_table(table_data):
    # Find the maximum number of rows in any column
    max_rows = max(len(col) for col in table_data)

    # Normalize all columns to the same length by padding with empty strings
    for col in table_data:
        while len(col) < max_rows:
            col.append("")

    # Calculate column widths
    col_widths = [max(len(str(item)) for item in col) for col in table_data]

    # Print each row
    for row_index in range(max_rows):
        row_items = [
            str(table_data[col_index][row_index]).rjust(col_widths[col_index])
            for col_index in range(len(table_data))
        ]
        print(" | ".join(row_items))


# Example usage
if __name__ == "__main__":
    table_data = [
        ['Name', 'Alice', 'Bob', 'Charlie'],
        ['Class', 'Wizard', 'Rogue', 'Fighter'],
        ['Level', '5', '4', '3']
    ]

    print_table(table_data)
