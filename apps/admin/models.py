messages_query = """
                 CREATE TABLE IF NOT EXISTS admin
                 (
                     id         SERIAL PRIMARY KEY,
                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )
                 """