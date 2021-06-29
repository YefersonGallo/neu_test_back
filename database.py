import psycopg2


class Connection:
    '''Verificar el nombre de usuario y contraseña, además del nombre de la base de datos creada'''
    conn = psycopg2.connect(
        host="localhost",
        database="neu_test",
        user="postgres",
        password="root")
    print(
        "Opened database successfully")

    cur = conn.cursor()

    def get_population_by_city(self, name):
        self.cur.execute("SELECT population, trim(name) from location WHERE name=$$" + name + "$$")
        rows = self.cur.fetchall()
        names = {}
        for row in rows:
            names["name"] = row[0]
            names["population"] = row[1]
        return names

    def get_population_by_state(self, name, country=None):
        if country:
            self.cur.execute(
                "SELECT id_state from location WHERE name = $$" + name + "$$ AND country_id = " + country + "")
        else:
            self.cur.execute(
                "SELECT id_state from location WHERE name = $$" + name + "$$")
        rows = self.cur.fetchall()
        state = []
        names = {}
        for row in rows:
            state.append(row[0])
        self.cur.execute("SELECT trim(name), population from location WHERE state_id=" + str(state[0]))
        rows_names = self.cur.fetchall()
        for i, row in enumerate(rows_names):
            names["city_" + str(i)] = {"name": row[0], "population": row[1]}
        return names

    def get_population_by_country(self, name):
        self.cur.execute("SELECT id_country from location WHERE name=$$" + name + "$$")
        rows = self.cur.fetchall()
        country = []
        names = {}
        for row in rows:
            country.append(row[0])
        self.cur.execute("SELECT trim(name), id_state from location WHERE country_id=" + str(country[0]))
        rows_names = self.cur.fetchall()
        for i, row in enumerate(rows_names):
            names["state_" + str(i)] = {"state": str(row[0]),
                                        "cities": self.get_population_by_state(str(row[0]), str(country[0]))}
        return names
