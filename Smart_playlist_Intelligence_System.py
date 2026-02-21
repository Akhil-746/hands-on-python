n=input("Enter the song app: ")
if n=='spotify':
  dur_no = int(input("Enter the number of durations : "))
  x =[]
  z = 0
  for i in range(dur_no):
    y = int(input("Enter duration in seconds : "))
    x.append(y)
    if y<=0:
        z=1
  total_duration = sum(x)
  songs = len(x)
  if z:
    print("Invalid input")
  elif len(x) != len(set(x)):
    print("Category: Repetitive Playlist")
    print("Recommendation:Add variety")
  elif total_duration<300:
    print("Total duration ", total_duration, "seconds")
    print("Songs ", songs)
    print("Too short playlist")
    print("Recommendation: Add playlist")
  elif total_duration>3600:
    print("Total duration ", total_duration, "seconds")
    print("Songs ", songs)
    print("Too long playlist")
    print("Recommendation:Reduce playlist")
  elif 300<=total_duration<=3600 and (len(x) == len(set(x))):
    print("Total duration ", total_duration, "seconds")
    print("Songs ", songs)
    print("Category: Balanced Playlist")
    print("Recommendation: Good listening session")
  else :
    print("Total duration ", total_duration, "seconds")
    print("Songs ", songs)
    print("Category: Irregular playlist")
    print("Recommendation: No valid entries ")
else:
    print("Enter the correct song app")


