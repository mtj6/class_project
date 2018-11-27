def make_album(artist_name, album_title, tracks_number=' '):
    """Return information about an album."""
    album = {'name' : artist_name, 'title' : album_title}
    if tracks_number:
        album['tracks_number'] = tracks_number
    return album
    
record = make_album('beyonce', 'lemonade')
print(record)

record = make_album('bob dylan', 'blood on the tracks', tracks_number=10)
print(record)

record = make_album('maclemore', 'gemini')
print(record)