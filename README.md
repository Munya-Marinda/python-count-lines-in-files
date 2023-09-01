# Line Counter

This Python script allows you to count the number of lines in each file within a specified folder and provides a total line count. This can be useful for analyzing codebases, text files, or any collection of files where you want to track the total number of lines.

<img src="https://github.com/Munya-Marinda/python-count-lines-in-files/assets/84540577/492f3c52-d752-4998-a0ff-91fc78533fe7" alt="App Icon" width="500px" > 

## Prerequisites

Before running the script, ensure you have the following:

- Python: You must have Python installed on your system. This script is compatible with both Python 2 and Python 3.

## How to Use

1. Clone or download this repository to your local machine.

2. Navigate to the directory where you have saved the script.

3. Open the script file (`line_counter.py`) in a text editor of your choice.

4. Modify the `folder_path` variable to specify the directory where you want to count lines. For example, if your files are located in a folder named 'count-these', set `folder_path = 'count-these'`.

5. Save the changes to the script.

6. Open your terminal or command prompt.

7. Navigate to the directory where the script is located.

8. Run the script using the following command:

   ```
   python line_counter.py
   ```

9. The script will count the lines in each file within the specified folder and display the results, including individual file line counts and a total line count.

## Example

Here's an example of what the script output might look like:

```
File: test_file_1.txt, Lines: 84
File: test_file_2.txt, Lines: 63
File: test_file_3.txt, Lines: 44

Total: 191
```

## Error Handling

The script is designed to handle exceptions gracefully. If there are any issues while attempting to read a file, it will catch the exception and display an error message, but it won't terminate the entire process.

## License

This project is licensed under the MIT License. 

## Author

- Munyaradzi Marinda

## Acknowledgments

- Inspiration for this script came from the need to analyze codebases and text files efficiently.

Feel free to customize this README.md to add more details or instructions specific to your use case.
