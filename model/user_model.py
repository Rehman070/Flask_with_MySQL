import mysql.connector
import json
class user_model():
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host ="localhost",user="root",password="khan123",database="flask_tut")
            self.conn.autocommit = True
            print ("Connection established")
            self.cur = self.conn.cursor(dictionary=True)
        except:
            print("Error")
            
    def get_all_user(self):           
        self.cur.execute("SELECT * FROM user")
        result = self.cur.fetchall()
        if len(result) > 0:
            return result
        else:
            return "No Data Available"
        
    def add_user(self, data):           
       
        self.cur.execute(f"INSERT INTO user(name, email, phone, role) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}')")
        return "Added User Successfully"
    
    def update_user(self, data):           
        self.cur.execute(f"UPDATE user SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}' WHERE id = {data['id']}")
        if self.cur.rowcount > 0:
            return "Updated User Successfully"
        else:
            return "No Users Updated"
        
    def delete_user(self, id):           
        self.cur.execute(f"DELETE FROM user WHERE id = {id}")
        if self.cur.rowcount > 0:
            return "Delete User Successfully"
        else:
            return "No Users Deleted"
        