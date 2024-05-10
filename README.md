# AutoEnroll

AutoEnroll is a Python script that automates the process of signing up for courses at your university. It uses Selenium with a headless browser to perform the enrollment process silently in the background, allowing you to use your computer for other tasks while it runs.

## Usage

1. **Download:** Clone or download the script from [devthekar.github.io](https://devthekar.github.io/).

2. **Dependencies:** Make sure you have Python installed on your system. Additionally, you'll need to install Selenium and the appropriate WebDriver for your chosen browser (e.g., Chrome WebDriver).

3. **Configuration:** Before running the script, ensure you've correctly configured the `data.txt` file with the following details:

   ```plaintext
   # AutoEnroll Configuration

   This file contains the necessary information for the AutoEnroll script to work properly. Please make sure to fill in the following details:

   1. Your email address: [Your Email]
   2. Your password: [Your Password]
   3. Semester code: 
      - For Fall 2024, use: 202408
      - For Summer 2024, use: 202405
      - For Spring 2024, use: 202401
      - and so on...
   4. Course name (including spaces): [Course Name]
   5. Course CRN (Course Reference Number): [Course CRN]

   Example:
   1. johndoe@example.com
   2. mypassword123
   3. 202408
   4. Communication for Engineers
   5. 54154

   Please ensure each detail is correctly entered on its own line in the 'data.txt' file.

4. **Run the Script:** Open a terminal or command prompt, navigate to the directory containing the script, and run it using Python:

    ```bash
    python AutoEnroll.py
    ```

5. **Sit Back and Relax:** The script will automate the course enrollment process in the background, allowing you to use your computer for other tasks.

## Disclaimer

Please use this script responsibly and in accordance with your university's policies and guidelines regarding course enrollment. Automated enrollment may not be permitted in some cases, so make sure to verify the legality and ethical implications of using this script at your institution.

## Contributions

Contributions and suggestions are welcome! Feel free to submit a pull request or open an issue on GitHub if you have any ideas for improvements or new features.
