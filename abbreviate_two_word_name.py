def abbrev_name(name):
  name = name.split(' ')
  firstName = name[0][0]
  lastName = name[1][0]
  return f"{firstName}.{lastName}"
