import fresh_tomatoes
import media


#Movie class instances
joe_volcano = media.Movie("Joe Versus the Volcano",
                          "A man quits his work life when he's misdiagnosed as dying.",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMyMjU2OTM5OV5BMl5BanBnXkFtZTYwMDMyMzA5._V1_.jpg",
                          "https://www.youtube.com/watch?v=A9lceeNQMwk")

akira = media.Movie("Akira", "A gang leader must save Tokyo from his transformed friend.",
                          "https://upload.wikimedia.org/wikipedia/en/5/5d/AKIRA_%281988_poster%29.jpg",
                          "https://www.youtube.com/watch?v=-UhLderbuGI")

ghost_shell = media.Movie("Ghost in the Shell",
                          "Man and machine meld in this brilliant futurescape.",
                          "https://www.movieposter.com/posters/archive/main/22/A70-11369",
                          "https://www.youtube.com/watch?v=oP2Pt6m3yKU")

powaqqatsi = media.Movie("Powaqqatsi",
                          "Life is shown in elapsed tume.",
                          "https://upload.wikimedia.org/wikipedia/fi/1/14/Powaqqatsi-elokuvajuliste.jpg",
                          "https://www.youtube.com/watch?v=fQxZ2oWvXB4")

koyaanisqatsi = media.Movie("Koyaanisqatsi",
                          "Modern life is potrayed.",
                          "https://image.tmdb.org/t/p/w1280/oPr0osFyj81aGlRVQqhW7nq1D0a.jpg",
                          "https://www.youtube.com/watch?v=1jM2WA2WbDc")

odyssey = media.Movie("2001: A Space Odyssey",
                          "An alien artifact communicates with humans throughout time.",
                          "http://www.reelviews.net/resources/img/posters/thumbs/2001_poster.jpg",
                          "https://www.youtube.com/watch?v=XHjIqQBsPjk")

movies = [joe_volcano, akira, ghost_shell, powaqqatsi, koyaanisqatsi, odyssey]


print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__
