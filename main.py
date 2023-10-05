import psycopg2
from functions.validation_functions import validate_phonenumber, validate_email
from config.database_config import create_configuration_table, execute_query
import functions.validation_functions

def execute_functions_based_on_status(input_json):
    status = input_json.get("status")

    if status:
        actions = execute_query("""
            SELECT action, action_type FROM configuration_table WHERE status = %s ORDER BY order_number""",
            (status,),
            "fetchall"
        )

        if actions:
            for action in actions:
                if action[1] == "function":
                    validation_func = getattr(functions.validation_functions, action[0], None)
                    if validation_func is not None:
                        validation_func(input_json)
                    else:
                        print('Function not found')
                else:
                    print('Action type should be funciton')

if __name__ == "__main__":
    create_configuration_table()

    sample_input = {
        "status": "Status1",
        "email": "whufwruhfweiruh@fejwfew.com",
        "phone": "9992883923",
    }

    execute_functions_based_on_status(sample_input)
