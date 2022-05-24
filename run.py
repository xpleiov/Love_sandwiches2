import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """"
    Get sales figures input from user
    """

    while True:
        print("Please enter sale data from the last market.")
        print("Data Should be six numbers, sparated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter you data here: ")
        
        sales_data = data_str.split(",")
        validate_data(sales_data)

        if validate_data(sales_data):
            print("data is valid")
            break


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren`t excetly 6 values
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provicded {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

get_sales_data()