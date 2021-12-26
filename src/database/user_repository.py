from database.database_connection import get_database_connection

class UserRepository:
    def __init__(self):        
        self._connection = get_database_connection()
    
    def get_topfive(self):       
        cursor = self._connection.cursor()

        cursor.execute("select username, score from users order by score desc limit 5")
        
        rows = cursor.fetchall()

        return [{"username":row["username"], "score":row["score"]} for row in rows]

    def check_score(self, username, score):
        topfive = self.get_topfive()
        
        if score == None:
            return False
        for t in topfive:            
            if score > t["score"]:
                cursor = self._connection.cursor()
                cursor.execute("insert into users (username, score) values (?, ?)", (username, score))
                self._connection.commit()
                return True
            
        return False         

