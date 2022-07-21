import sqlite3
path = 'E:/projects/loisde/'

#../mysite/
class DBConnection:
    def __init__(self):
        self.conn = sqlite3.connect(path+'worker.db', check_same_thread=False)
        self.c = self.conn.cursor()

    def GetAllButtons(self):
        return self.c.execute(f"SELECT * FROM buttons").fetchall()

    def GetQiwiToken(self):
        return self.c.execute(f"SELECT * FROM payment WHERE id={1}").fetchone()

    def GetAllTexts(self):
        return self.c.execute(f"SELECT * FROM texts").fetchall()

    def UpdateButton(self, id, text):
        self.c.execute(f"UPDATE buttons SET text = '{text}' WHERE id = '{id}'")
        self.conn.commit()

    def UpdateText(self, id, text):
        self.c.execute(f"UPDATE texts SET text = '{text}' WHERE id = '{id}'")
        self.conn.commit()

    def UpdatePay(self, id, text):
        self.c.execute(f"UPDATE payment SET text = '{text}' WHERE id = '{id}'")
        self.conn.commit()

    def UpdateAdmin(self, id, text):
        self.c.execute(f"UPDATE admins SET id_user = '{text}' WHERE id = '{id}'")
        self.conn.commit()


    def GetAllUsers(self):
        return self.c.execute("SELECT * FROM users").fetchall()

    def GetAllOrders(self):
        return self.c.execute("SELECT * FROM orders").fetchall()

    def GetAllDone(self):
        return self.c.execute("SELECT * FROM forms_buyers").fetchall()

    def GetNotReady(self):
        return self.c.execute("SELECT * FROM forms_buyers").fetchall()[-100:]
    def GEtAdmin(self):
        return self.c.execute("SELECT * FROM admins").fetchall()


    def __del__(self):
        self.c.close()
        self.conn.close()

