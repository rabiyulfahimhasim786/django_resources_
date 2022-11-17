from films.models import Film, Genre
import csv


def run():
    with open('films/text.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Film.objects.all().delete()
        Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre, _ = Genre.objects.get_or_create(name=row[-1])

            film = Film(title=row[0],
                        year=row[2],
                        genre=genre)
            film.save()