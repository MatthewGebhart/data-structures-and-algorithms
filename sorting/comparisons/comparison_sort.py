def sort_by_year(movies):
    sort = sorted(movies, key=lambda x: (x['year'], x['title']), reverse=True)
    return [movie['title'] for movie in sort]


def sort_by_title(movies):
    def remove_leaders(title):
        for leaders in ["The ", "A ", "An "]:
            if title.startswith(leaders):
                return title.replace(leaders, "", 1)
        return title
    sorted_movies = sorted(movies, key=lambda x: remove_leaders(x['title']))
    return [movie['title'] for movie in sorted_movies]
