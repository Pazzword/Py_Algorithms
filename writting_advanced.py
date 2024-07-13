import csv

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_to_text_file(self, lines):
        try:
            with open(self.filename, 'w') as file:
                for line in lines:
                    file.write(line + '\n')
            print(f"Successfully wrote to {self.filename}")
        except Exception as e:
            print(f"An error occurred while writing to {self.filename}: {e}")

    def read_from_text_file(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
            print(f"Contents of {self.filename}:")
            for line in lines:
                print(line.strip())
        except Exception as e:
            print(f"An error occurred while reading from {self.filename}: {e}")

    def append_to_text_file(self, lines):
        try:
            with open(self.filename, 'a') as file:
                for line in lines:
                    file.write(line + '\n')
            print(f"Successfully appended to {self.filename}")
        except Exception as e:
            print(f"An error occurred while appending to {self.filename}: {e}")

    def write_to_csv_file(self, data):
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"Successfully wrote to {self.filename}")
        except Exception as e:
            print(f"An error occurred while writing to {self.filename}: {e}")

    def read_from_csv_file(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
            print(f"Contents of {self.filename}:")
            for row in data:
                print(row)
        except Exception as e:
            print(f"An error occurred while reading from {self.filename}: {e}")

    def append_to_csv_file(self, new_data):
        try:
            with open(self.filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)
            print(f"Successfully appended to {self.filename}")
        except Exception as e:
            print(f"An error occurred while appending to {self.filename}: {e}")

    def merge_csv_files(self, other_filename, output_filename):
        try:
            combined_data = []

            # Read the first CSV file
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                combined_data.extend(list(reader))

            # Read the second CSV file
            with open(other_filename, 'r') as file:
                reader = csv.reader(file)
                combined_data.extend(list(reader))

            # Write the combined data to a new CSV file
            with open(output_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(combined_data)

            print(f"Successfully merged {self.filename} and {other_filename} into {output_filename}")
        except Exception as e:
            print(f"An error occurred while merging CSV files: {e}")

# Example usage
csv_handler1 = FileHandler('example1.csv')
csv_data1 = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles']
]
csv_handler1.write_to_csv_file(csv_data1)

csv_handler2 = FileHandler('example2.csv')
csv_data2 = [
    ['Name', 'Age', 'City'],
    ['Charlie', 35, 'Chicago'],
    ['David', 40, 'Houston']
]
csv_handler2.write_to_csv_file(csv_data2)

csv_handler1.merge_csv_files('example2.csv', 'merged_example.csv')

# Reading the merged file to verify the merge
merged_handler = FileHandler('merged_example.csv')
merged_handler.read_from_csv_file()
