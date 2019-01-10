songs = {
  ("Bob Marley", "I Shot The Sheriff"),
  ("Lynyrd Skynyrd", "Free Bird"),
  ("Nickelback", "How You Remind Me"),
  ("Metallica", "Nothing Else Matters"),
  ("Grateful Dead", "Casey Jones"),
  ("ZZ Top", "Sharp Dressed Man"),
  ("Nickelback", "Animals"),
  ("Creedence Clearwater Revival", "Bad Moon Rising")
}

print(f'Songs before edit: {songs}')
print("\n\n")

good_songs = set()
[good_songs.add(song) for song in songs if song[0] != "Nickelback"]
print(f'Good songs with Nickelback removed: {good_songs}')