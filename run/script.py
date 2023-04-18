from options import Options
from toolset import Tool

hostname = "localhost"
user = "test"
password = "12345"
port = 3306
database = "test"

def main():
    
    options = Options(
        username=user,
        password=password,
        host=hostname,
        port=port,
        database=database,
    )

    db = Tool(options)
    db.connect()
    
    my_query = "SELECT 12;"

    cur = db.query(my_query, param=None)
    
    result = cur.fetchall()
    print(result)


if __name__ == "__main__":
    main()
