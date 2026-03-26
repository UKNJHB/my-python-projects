class Movies:
    def __init__(self,movie,title,director,year,genre):
        self.movie = movie
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    def display_movie(self):
        print(f"Movie {self.movie} Details:")
        print(f"Titel: {self.title}")
        print(f"Director: {self.director}")
        print(f"Release Year: {self.year}")
        print(f"Gener: {self.genre}")

    def up_date_director(self,new_director):
        self.director=new_director
          

movie1=Movies("1","Inception","Christopher Nolan","2010","Sci-Fi")
movie2=Movies("2","The Godfather","Francis Ford Coppola","1972","Crime")
movie3=Movies("3","Parasite","Bong Joon-Ho","2019","Thriller")

print("_____MOVIES LIST_____\n\n")
movie1.display_movie()
print("______________________\n")
movie2.display_movie()
print("______________________\n")
movie3.display_movie()
print("______________________\n\n")
        
print("Changing Movie directors...\n\n")

movie1.up_date_director(input("Enter new director name: "))
movie2.up_date_director(input("Enter new director name: "))
movie3.up_date_director(input("Enter new director name: "))
        
 
movie1.display_movie()
print("______________________\n")
 
movie2.display_movie()
print("______________________\n")

movie3.display_movie()
print("______________________")
