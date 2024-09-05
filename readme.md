# Job Positions to XLSX

This script automates the process of performing Google searches and saving the results in an Excel (.XLSX) file to help you manage your job applications more efficiently.

### Features

- **Automated Search:** Conducts Google searches based on pre-configured sites.
- **Excel Output:** Saves the search results into separate tabs within a single Excel file.
- **Organized Data:** Easily track and manage job applications by accessing categorized search results.

## How to Use

To execute this project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:marcuswd/scrap_positions.git
   ```

2. **Setup:**
   - Navigate to the folder where you cloned the project and create a file called **roles.txt** in the root folder. Add one role per line (e.g.):
     ```
     react.js
     react native
     ```
   - Inside the **br** and **ext** folders, you will find a file called **sources.txt**. This file contains a list of sites where the search will be conducted. Add one URL per line if you need to include additional sites.

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Perform the Search:**
   Run the script with:
   ```bash
   python scrap.py
   ```
   Follow the instructions in the terminal to perform your search. The script will search Google for each role and save any results into the corresponding tab in the Excel file.

**Attention:** Frequent use of Selenium may result in Google redirecting you to a CAPTCHA challenge. If this happens, a message will be printed in the terminal. You will need to complete the CAPTCHA manually and then press _**Enter**_ in the terminal to continue the search.
