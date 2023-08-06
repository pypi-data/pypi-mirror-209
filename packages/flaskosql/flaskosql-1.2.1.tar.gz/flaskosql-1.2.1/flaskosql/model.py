import cx_Oracle
from flaskosql.field import Field

class Model:
    _connection = None
    
    # Constructor : it takes two arguments (self ("this" in other languages and *kwargs wich can be translated to string of values))
    def __init__(self, **kwargs):
        # Initialize the object with provided attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    @classmethod
    def set_connection(cls, connection):
        cls._connection = connection
    
    # Method to return that create a table with the same name as the class :
    @classmethod
    def create_table(cls):
        # Create the table with the same name as the class
        # This method is a static method (it could be called from the class without instance (read OOP concepts and the documentation))
        table_name = cls.__name__
        # The connect method takes no parameters, it loads the data from the .env file, but it can takes parametrs two (read the documentation)
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                columns = []
                for attr_name, attr_value in cls.__dict__.items():
                    if isinstance(attr_value, Field):
                        columns.append(attr_value.get_column_definition())

                create_query = "CREATE TABLE {} ({})".format(table_name, ", ".join(columns))
                cursor.execute(create_query)
                connection.commit()
                print("Table '{}' created successfully!".format(table_name))
            except cx_Oracle.Error as e:
                print(f"Error creating table: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")

    def save(self):
        # Save the object to the database
        connection = self.__class__._connection
        if connection:
            try:
                cursor = connection.cursor()
                columns = []
                values = []
                placeholders = []
                for key, value in self.__dict__.items():
                    columns.append(key)
                    values.append(value)
                    placeholders.append(':{}'.format(key))

                table_name = self.__class__.__name__  # Get the table name from the class
                insert_query = "INSERT INTO {} ({}) VALUES ({})".format(
                    table_name, ", ".join(columns), ", ".join(placeholders))
                cursor.execute(insert_query, values)
                connection.commit()
                print("Object saved successfully!")
            except cx_Oracle.Error as e:
                print(f"Error saving object to database: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")

    def update(self):
        # Update the object in the database
        connection = self.__class__._connection
        if connection:
            try:
                cursor = connection.cursor()
                set_values = []
                for key, value in self.__dict__.items():
                    set_values.append("{} = :{}".format(key, key))

                table_name = self.__class__.__name__  # Get the table name from the class
                update_query = "UPDATE {} SET {} WHERE id = :id".format(
                    table_name, ", ".join(set_values))
                cursor.execute(update_query, self.__dict__)
                connection.commit()
                print("Object updated successfully!")
            except cx_Oracle.Error as e:
                print(f"Error updating object in the database: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")
    
    def delete(self):
        # Delete the object from the database
        connection = self.__class__._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = self.__class__.__name__  # Get the table name from the class
                delete_query = "DELETE FROM {} WHERE id = :id".format(table_name)
                cursor.execute(delete_query, self.__dict__)
                connection.commit()
                print("Object deleted successfully!")
            except cx_Oracle.Error as e:
                print(f"Error deleting object from the database: {e}")
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")

    @classmethod
    def get(cls, **conditions):
        # Retrieve an object from the database based on the specified conditions
        connection = cls._connection
        if connection:
            try:
                cursor = connection.cursor()
                table_name = cls.__name__  # Get the class name
                conditions_str = " AND ".join(f"{key} = :{key}" for key in conditions)
                select_query = f"SELECT * FROM {table_name} WHERE {conditions_str}"
                cursor.execute(select_query, conditions)
                result = cursor.fetchone()
                if result:
                    columns = [column[0] for column in cursor.description]
                    obj_data = dict(zip(columns, result))

                    # Create an instance of the class with dynamic attribute assignment
                    model_instance = cls(**obj_data)
                    return model_instance
                else:
                    print("Object not found in the database.")
                    return None
            except cx_Oracle.Error as e:
                print(f"Error retrieving object from the database: {e}")
                return None
            finally:
                if cursor:
                    cursor.close()
                    # connection.close()
        else:
            print("Failed to connect to the database.")
            return None
