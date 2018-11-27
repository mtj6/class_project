def make_album(artist_name, album_title, tracks_number=' '):
    """Return information about an album."""
    album = {'name' : artist_name, 'title' : album_title}
    if tracks_number:
        album['tracks_number'] = tracks_number
    return album
    
while True:
    print("\nEnter an album's information:")
    print("Enter 'q' at any time to quit.")
    
    a_name = input("Artist Name: ")
    if a_name == 'q':
        break
    
    a_title = input("Album Title: ")
    if a_title == 'q':
        break
        
    t_number = input("Number of Tracks: ")
    if t_number == 'q':
        break
        
    record = make_album(a_name, a_title, t_number)
    print(record)