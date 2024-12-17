import mysql.connector as conn
con = conn.connect(host = 'localhost', user = 'root', passwd = 'XXX')
cur = con.cursor()
#cur.execute('drop database if exists MovieCentre')
cur.execute('create database MovieCentre')
cur.execute('use MovieCentre')
cur.execute('create table nows(sno int primary key,M_name varchar(20),releases date not null,price int not null)')
cur.execute('insert into nows values(1,"Salaar","2023-12-22",400),(2,"Jailer","2023-08-10",500),(3,"Ghost","2023-10-19",700),(4,"VTK","2022-09-15",600),(5,"Leo","2023-10-19",500),(6,"Doctor","2021-10-09",200),(7,"KGF","2022-04-14",1000),(8,"Master","2021-01-13",500),(9,"RRR","2022-03-25",300)')
 
def add_movie():
    num = int(input('Enter how many movies you would like to add to your favourites'))
    for i in range(num):
        M_name = input('Enter movie name : ')
        cur.execute('insert into Fav values({},"{}")'.format(i,M_name))
    con.commit()
    cur.execute('select * from Fav')
    list = cur.fetchall()
    print('+-----------+---------------+')
    print('| Serial no |   Movie name  |')
    print('+-----------+---------------+')
    for i in list:
        a,b = i
        print('|    ',a+1,'    |',b,' '*(12-len(b)),'|')
    print('+-----------+---------------+')
cur.execute('create table Fav(sno int primary key,Movie_Name varchar(20) not null)')
def price():
    num = int(input('Enter how many movies you would like to change the price'))
    for i in range(num):
        M_name = input('Enter movie name : ')
        price = int(input('Enter the price of the movie'))
        cur.execute('update nows set price = {} where M_name = "{}"'.format(price,M_name))
    con.commit()
    cur.execute('select sno,M_name,price from nows')
    list = cur.fetchall()
    print('+-----------+---------------+---------------+')
    print('| Serial no |   Movie name  |     Price     |')
    print('+-----------+---------------+---------------+')
    for i in list:
        a,b,c = i
        print('|    ',a,'    |',b,' '*(12-len(b)),'|',c,' '*(12-len(str(c))),'|')
    print('+-----------+---------------+---------------+')
cur.execute('create table bookings(sno int primary key,Movie_Name varchar(20) not null, price int, bookings date not null, Theatre_name varchar(20), Tickets int)')
def book_mov():
    print('It is good to book your movies in advance as the tickets get sold out really quickly')
    num = int(input('Enter how many movies you would like to book'))
    for i in range(num):
        M_name = input('Enter movie name : ')
        price = int(input('Enter the price of the movie : '))
        date = input('Enter when you would like to watch the movie [in the form year-month-day]: ')
        theatre = input('Enter the theatre name : ')
        tickets = int(input('Enter the number of tickets you would like to book for the movie'))
        cur.execute('insert into bookings values({},"{}",{},"{}","{}",{})'.format(i,M_name,price,date,theatre,tickets))
    con.commit()
    cur.execute('select * from bookings')
    list = cur.fetchall()
    print('+-----------+---------------+---------------+---------------+---------------+---------------+')
    print('| Serial no |   Movie name  |     Price     |      Date     |    Theatre    |    Tickets    |')
    print('+-----------+---------------+---------------+---------------+---------------+---------------+')
    for i in list:
        a,b,c,d,e,f = i
        print('|    ',a+1,'    |',b,' '*(12-len(b)),'|',c,' '*(12-len(str(c))),'|',d,' '*(12-len(str(d))),'|',e,' '*(12-len(e)),'|',f,' '*(12-len(str(f))),'|')
    print('+-----------+---------------+---------------+---------------+---------------+---------------+')
cur.execute('create table rev(sno int primary key,Movie_Name varchar(20) not null,name varchar(20), review varchar(50) not null, Rating int not null)')
def rev():
    print('Please give your Feedback on the movie')
    num = int(input('Enter how many movies you would like to comment on :'))
    cur.execute('Delete from rev')
    for i in range(num):
        M_name = input('Enter movie name : ')
        name = input('Enter your name : ')
        review = input('Please enter your review : ')
        rating = int(input('Rate this movie out of 5*\'s'))
        if name != '':
            cur.execute('insert into rev values({},"{}","{}","{}",{})'.format(i,M_name,name,review,rating))
        else:
            cur.execute('insert into rev values({},"{}","Anonymous","{}",{})'.format(i,M_name,review,rating))
    con.commit()
    cur.execute('select * from rev')
    list = cur.fetchall()
    print('+-----------+---------------+-----------------------+------------------+----------------+')
    print('| Serial no |   Movie name  |          Name         |      Review      |     Rating     |')
    print('+-----------+---------------+-----------------------+------------------+----------------+')
    for i in list:
        a,b,c,d,e = i
        print('|    ',a+1,'    |',b,' '*(12-len(b)),'|',c,' '*(20-len(c)),'|',d,' '*(15-len(d)),'|',e,' '*(13-len(str(e))),'|')
    print('+-----------+---------------+-----------------------+------------------+----------------+')
def M_rating():
    M_name = input('Enter the movie name:')
    rate = int(input('Enter the rating for which you want the number of people who rated that for all movies : '))
    cur.execute('select movie_name,count(rating) from rev where movie_name = "{}" and rating = {}'.format(M_name,rate))
    list = cur.fetchall()
    print('+---------------+-----------------------------+')
    print('|   Movie name  | No.of people who rated',rate,'*s','|')
    print('+---------------+-----------------------------+')
    for i in list:
        a,b, = i
        print('|',a,' '*(12-len(a)),'|',b,' '*(26-len(str(b))),'|')
    print('+---------------+-----------------------------+')
def nows():
    cur.execute('select * from nows')
    list = cur.fetchall()
    print('+-----------+---------------+---------------+---------------+')
    print('| Serial no |   Movie name  |     Date      |     Price     |')
    print('+-----------+---------------+---------------+---------------+')
    for i in list:
        a,b,c,d = i
        print('|    ',a,'    |',b,' '*(12-len(b)),'|',c,' '*(12-len(str(c))),'|',d,' '*(12-len(str(d))),'|')
    print('+-----------+---------------+---------------+---------------+')
while True:
    print('Welcome to MφvieCentre!!')
    print('What would you like to do ?')
    print('Enter (1) if you would like to add a movie to your Favourites and see your Favourites list')
    print('Enter (2) if you would like to change the price of a movie')
    print('Enter (3) if you would like to book a movie')
    print('Enter (4) if you would like to give your review on a movie')
    print('Enter (5) if you would like to see how well a movie is rated')
    print('Enter (6) if you would like to see which movies are currently running in our Theatres')
    ch = int(input('Enter your choice : '))
    if ch == 1:
        add_movie()
    if ch == 2:
        price()
    if ch == 3:
        book_mov()
    if ch == 4:
        rev()
    if ch == 5:
        M_rating()
    if ch == 6:
        nows()
    else:
        break
