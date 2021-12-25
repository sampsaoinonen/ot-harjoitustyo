from database.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            id integer primary key,
            username text,
            score int
        );
    ''')
    cursor.execute('''
        insert into users (username, score) 
        values ("Sampsa", 6);
    ''')
    cursor.execute('''
        insert into users (username, score)
        values ("Jorkki", 2);        
    ''')
    cursor.execute('''
        insert into users (username, score)
        values ("Jukka", 4);        
    ''')
    cursor.execute('''
        insert into users (username, score)
        values ("Pertsa", 2);        
    ''')
    cursor.execute('''
        insert into users (username, score)
        values ("Seppo", 1);        
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()