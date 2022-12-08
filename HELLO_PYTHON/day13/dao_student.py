import psycopg2

class DaoStudent :
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost", port="5432", dbname="python", user="postgres", password="python")
        self.cur = self.conn.cursor()
        
    def selects(self):
        arr = []
        sql = f"""
            select
                s_id, s_name, mobile, address
            from
                student
            order by
                s_id
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        
        for r in rows :
            arr.append({'s_id':r[0],'s_name':r[1],'mobile':r[2],'address':r[3]})
            
        return arr
    
    def select(self,s_id):
        sql = f"""
            select
                s_id, s_name, mobile, address
            from
                student
            where
                s_id = '{s_id}'
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'s_id':r[0],'s_name':r[1],'mobile':r[2],'address':r[3]}
        return ret
    
    def insert(self,s_id,s_name,mobile,address):
        sql = f"""
            insert into student
                (s_id, s_name, mobile, address)
            values
                ('{s_id}', '{s_name}', '{mobile}','{address}');
        """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
    
    def update(self,s_id,s_name,mobile,address):
        sql = f"""
            update student
            set
                s_name = '{s_name}',
                mobile = '{mobile}',
                address = '{address}'
            where
                s_id = '{s_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        return 1
    
    def delete(self,s_id):
        sql = f""" 
            delete from student
            where
                e_id = '{s_id}'
        """
        self.cur.execute(sql)
        self.conn.commit()
        return 1
    
    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.delete(3)
    print(cnt)