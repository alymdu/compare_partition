class Options:
    def __init__(self, username, password, host, port, database):
        self._username = username
        self._password = password
        self._host = host
        self._port = port
        self._database = database
    
    @property
    def username(self):
        if not self._username:
            raise ValueError("Username is not set")
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value
    
    @property
    def password(self):
        if not self._password:
            raise ValueError("Password is not set")
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def host(self):
        if not self._host:
            raise ValueError("Host is not set")
        return self._host
    
    @host.setter
    def host(self, value):
        self._host = value

    @property
    def port(self):
        if not self._port:
            raise ValueError("Port is not set")
        return self._port
    
    @port.setter
    def port(self, value):
        self._port = value

    @property
    def database(self):
        if not self._database:
            raise ValueError("Database is not set")
        return self._database
    
    @database.setter
    def database(self, value):
        self._database = value
