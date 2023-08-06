from mat import *
import vertica_python
import datetime
import decimal

class VerticaConnector:
    """ 
        Wrapper del driver vertica_python para funcionar con MAT Credentials.
        Contiene algunos metodos basicos para probar conexiones basicas.
    """
    connection = None
    cursor = None
    
    def __init__(self, hostname, database=None, stored_credentials=None):
        inv = Inventory()
        port = 5433
        autocommit = True
        
        mathost = inv.get(module = "mathost", query = f"data.hostname={hostname}")
        if not mathost:
            raise Exception("El equipo ingresado no se encuentra en Network Elements")
        mathost = mathost[0]["data"]
        
        if stored_credentials:
            matcredentials = inv.get("matcredentials", query=f"data.credentialName={stored_credentials}")
            if not stored_credentials:
                raise Exception("Debe ingresar una credencial correcta")
            matcredentials = matcredentials[0]
        else:
            matcredentials = mathost.get('storedCredentials')
        
        host = mathost["managementIp"]
        user = matcredentials["data"]["username"]
        password = matcredentials["data"]["password"]
        var_list = mathost["env_vars"]
        for var in var_list:
            if var["name"] == "port": port = int(var["value"])
            if var["name"] == "database" and not database: database = var["value"]
            if var["name"] == "autocommit": autocommit = bool(var["value"])
        
        database  = 'cnamx' if not database else database
        password = crypto.aes256.MATCipher().decrypt(password)
        
        if database:
            self.connection = vertica_python.connect(host=host, port=port, user=user, password=password, database=database, autocommit=autocommit, connection_timeout= 420)
        else:
            self.connection = vertica_python.connect(host=host, port=port, user=user, password=password, autocommit=autocommit, connection_timeout= 420)
        self.cursor = self.connection.cursor()
    
    def get_headers(self):
        """ Devuelve el nombre y orden de las columnas del cursor acutal """
        return [row[0] for row in self.cursor.description]
    
    def get(self, query, schema=None, values=None):
        """ Ejecuta una query generica y devuelve la respuesta en forma de diccionario """
        try:
            if values:
                if isinstance(values, list):
                    self.cursor.execute(query, values)
                elif isinstance(values, dict):
                    self.cursor.execute(query, **values)
                else:
                    raise Exception('Values format not supported for query')
            else:
                self.cursor.execute(query)
            
            rows = self.cursor.fetchall()
            columns = self.get_headers()
            self.connection.commit()
            
            data = [dict(zip(columns, row)) for row in rows]
            for item in data:
                for key, value in item.items():
                    if isinstance(value, datetime.datetime):
                        item[key] = str(value)
                    if isinstance(value, decimal.Decimal):
                        item[key] = str(value)
            
            msg = "Successful"
            return True, msg, data
        except Exception as err:
            msg = f"Error al ejecutar la query. {err}"
            return False, msg, None
        

        
    def close(self):
        self.connection.close()
