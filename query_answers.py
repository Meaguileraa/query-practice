# 1 Find the user with the email cats@gmail.com.

user = User.query.filter_by(email='cats@gmail.com').one()
#or
#user = db.session.query(User).filter(User.email == 'cats@gmail.com').one() 




# 2 Find any movies with the exact title “Cape Fear”.

movies = Movie.query.filter_by(title='Cape Fear').all()
#or
#movies = db.session.query(Movie).filter(Movie.title == 'Cape Fear').all()



# 3 Find all users with the zipcode 90703.



# 4 Find all ratings of with the score of 5.



# 5 Find the rating for the movie whose id is 7, from the user whose id is 6.



# 6 Find all ratings that are larger than 3.