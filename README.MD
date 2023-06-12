This is a simple repository to send email via gmail stmp server.

## How to use

1. Clone the repository:

   ```shell
       git clone https://github.com/Cliying94/email-sender.git
   ```

2. Navigate to the project directory and set up a Python virtual environment:
   ```shell
       python3 -m venv .venv
   ```
3. Activate the virtual environment:

   - on windows (powershell)

     ```shell
     .\venv\Scripts\Activate.ps1
     ```

   - on Unix or MacOS

     ```shell
     source .venv/bin/activate
     ```

4. install the required packages:

   - general

     ```shell
     pip install -r requirements.txt
     ```
5. set up the file .env, please see the example file .env.example
6. create the file email-list-test.csv with your own email list, or you can revised the file name in main.py:
    ```python
    with open('email-list-test.csv', 'r') as csvfile:
    ```
7. create the file html-content.html with your own html content, or you can revised the file name in main.py:
    ```python
    with open('html-content.html', 'r') as html_file:
    ```
8. change your email title in main.py:
    ```python
    email_title = "Email title"
    ```
9. run the script:
    ```shell
    python3 main.py
    ```