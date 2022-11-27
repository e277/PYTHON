import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-VOT1DO6\MSSQLSERVER_NEW;'
    'Database=HelloWorld;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()


def create():
    cursor.execute(
        '''
        CREATE TABLE Movies(
            id INT IDENTITY(1,1) PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            release_year VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            collection_in_mil SMALLMONEY
        )
        CREATE TABLE Reviewers(
            id INT IDENTITY(1,1) PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL
        )
        CREATE TABLE Ratings(
            movie_id INT,
            reviewer_id INT,
            rating INT NOT NULL,
            FOREIGN KEY(movie_id) REFERENCES Movies(id),
            FOREIGN KEY(reviewer_id) REFERENCES Reviewers(id)
        )
        '''
    )
    conn.commit()


def insert1():
    cursor.execute(
        '''
        INSERT INTO Movies
            (title, release_year, genre, collection_in_mil)
        VALUES
            ('movie1', '2000', 'horrr', 1000),
            ('movie2', '2000', 'action', 2500),
            ('movie3', '2000', 'adventure', 1500),
            ('movie4', '2000', 'horror', 7500),
            ('movie5', '2000', 'sci-fi', 9500)
        '''
    )
    conn.commit()

def insert2():
    cursor.execute(
        '''
        INSERT INTO Reviewers
            (first_name, last_name)
        VALUES
            ('john', 'snow'),
            ('name1', 'nile'),
            ('shay', 'brown'),
            ('brian', 'black'),
            ('jay', 'walker')
        '''
    )
    conn.commit()

def insert3():
    cursor.execute(
        '''
        INSERT INTO Ratings
            (movie_id, reviewer_id, rating)
        VALUES
            (1, 1, 9),
            (1, 2, 7),
            (2, 1, 4),
            (1, 3, 3),
            (1, 4, 4)
        '''
    )
    conn.commit()

def highest_collection():
    cursor.execute(
        '''
        SELECT MAX(collection_in_mil) 'Maximum Collection(mil)' FROM Movies
        '''
    )
    for col in cursor.fetchall():
        print(col)
    conn.commit()

def highest_rating():
    cursor.execute(
        '''
        SELECT MAX(rating) 'Highest Rating' FROM Ratings
        '''
    )
    for col in cursor.fetchall():
        print(col)
    conn.commit()

def low_rating():
    cursor.execute(
        '''
        SELECT rating, COUNT(reviewer_id) 'Count of low Rating' FROM Ratings GROUP BY rating HAVING rating < 5
        '''
    )
    for col in cursor.fetchall():
        print(col)
    conn.commit()


if __name__ == "__main__":
    # create()
    # insert1()
    # insert2()
    # insert3()
    # highest_collection()
    # highest_rating()
    low_rating()

    #  Connect DB by using python connectivity
    #  Insert 5 row in all three tables
    #  Find the highest collection
    #  Find the highest rating
    #  Find the count of reviewers who gave low Rating