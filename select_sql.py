
import sqlalchemy


engine = sqlalchemy.create_engine('postgresql://.........')
connection = engine.connect()  

year = 2018
albums = connection.execute(f"""
SELECT name, release FROM Albums
WHERE release = {year};
""").fetchall()
print()
print(f'В {year} году вышли альбомы: ')
for i in albums:
    print(i)
print()

max_duration = connection.execute(f"""
SELECT name, duration FROM Tracks
ORDER BY duration DESC
LIMIT 1;
""").fetchall()
print(f'Самый длительный трек с продолжительностью {max_duration[0][1]} минуты называется "{max_duration[0][0]}"')
print()


duration = connection.execute(f"""
SELECT name, duration FROM Tracks
WHERE duration >=3.5;
""").fetchall()
print(f'Треки с продолжительностью более 3,5 минут: ')
for i in duration:
    print(f'"{i[0]}" продолжительностью {i[1]} минут')
print()

compilation = connection.execute(f"""
SELECT name, release FROM Compilation
WHERE release BETWEEN 2018 AND 2020;
""").fetchall()
print(f'Cборники, вышедшие в период с 2018 по 2020 год включительно: ')
for i in compilation:
    print(i)
print()

performers = connection.execute(f"""
SELECT Nickname FROM Performers
WHERE Nickname NOT LIKE '%% %%';
""").fetchall()
print(f'Исполнители, чье имя состоит из 1 слова: ')
for i in performers:
    print(f' "{i[0]}"')
print()

my_track = connection.execute(f"""
SELECT name FROM Tracks
WHERE name LIKE '%%Мой%%' or name LIKE '%%My%%';
""").fetchall()
print(f'названия треков, которые содержат слова "Мой"/"My": ')
for i in my_track:
    print(f'"{i[0]}"')