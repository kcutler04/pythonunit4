from pprint import pprint
#Snake species known to be found in the U.S. state of Illinois.
snakes_info = [
    'Agkistrodon contortrix contortrix', 'southern copperhead', 'Viperidae',
    'Yes', 'Agkistrodon contortrix mokasen', 'northern copperhead',
    'Viperidae', 'Yes', 'Agkistrodon piscivorus leucostoma', 'water moccasin',
    'Viperidae', 'Yes', 'Carphophis amoenus helenae', 'midwestern worm snake',
    'Colubridae', 'No', 'Carphophis vermis', 'midwestern worm snake',
    'Colubridae', 'No', 'Clonophis kirtlandii', "Kirtland's snake",
    'Colubridae', 'No', 'Cemophora coccinea copei', 'northern scarlet snake',
    'Colubridae', 'No', 'Coluber constrictor foxii', 'blue racer',
    'Colubridae', 'No', 'Coluber constrictor priapus', 'southern black racer',
    'Colubridae', 'No', 'Crotalus horridus', 'timber rattlesnake', 'Viperidae',
    'Yes', 'Diadophis punctatus arnyi', 'prairie ringneck snake', 'Colubridae',
    'No', 'Diadophis punctatus edwardsii', 'northern ringneck snake',
    'Colubridae', 'No', 'Diadophis punctatus stictogenys',
    'Mississippi ringneck snake', 'Colubridae', 'No',
    'Farancia abacura reinwardtii', 'western mud snake', 'Colubridae', 'No',
    'Heterodon nasicus gloydi', 'dusty hognose snake', 'Colubridae', 'No',
    'Heterodon nasicus nascius', 'plains hognose snake', 'Colubridae', 'No',
    'Heterodon platirhinos', 'eastern hognose snake', 'Colubridae', 'No',
    'Lampropeltis calligaster calligaster', 'prairie kingsnake', 'Colubridae',
    'No', 'Lampropeltis getula holbrooki', 'speckled kingsnake', 'Colubridae',
    'No', 'Lampropeltis getula niger', 'black kingsnake', 'Colubridae', 'No',
    'Lampropeltis triangulum triangulum', 'eastern milk snake', 'Colubridae',
    'No', 'Lampropeltis triangulum syspila', 'red milk snake', 'Colubridae',
    'No', 'Masticophis flagellum flagellum', 'eastern coachwhip', 'Colubridae',
    'No', 'Nerodia cyclopion', 'Mississippi green water snake', 'Colubridae',
    'No', 'Nerodia erythrogaster flavigaster', 'yellowbelly water snake',
    'Colubridae', 'No', 'Nerodia erythrogaster neglecta',
    'copperbelly water snake', 'Colubridae', 'No',
    'Nerodia fasciata confluens', 'broad-banded water snake', 'Colubridae',
    'No', 'Nerodia rhombifer', 'diamondback water snake', 'Colubridae', 'No',
    'Nerodia sipedon pleuralis', 'midland water snake', 'Colubridae', 'No',
    'Nerodia sipedon sipedon', 'northern water snake', 'Colubridae', 'No',
    'Opheodrys aestivus', 'rough green snake', 'Colubridae', 'No',
    'Opheodrys vernalis', 'smooth green snake', 'Colubridae', 'No',
    'Pantherophis emoryi', 'Great Plains ratsnake', 'Colubridae', 'No',
    'Pantherophis spiloides', 'gray ratsnake', 'Colubridae', 'No',
    'Pantherophis vulpina', 'Western fox snake', 'Colubridae', 'No',
    'Pituophis catenifer sayi', 'gophersnake', 'Colubridae', 'No',
    'Pituophis melanoleucus melanoleucus', 'northern pine snake', 'Colubridae',
    'No', 'Regina grahamii', "Graham's crayfish snake", 'Colubridae', 'No',
    'Regina septemvittata', 'queen snake', 'Colubridae', 'No',
    'Sistrurus catenatus catenatus', 'Eastern massasauga', 'Viperidae', 'Yes',
    'Storeria dekayi wrightorum', 'midland brown snake', 'Colubridae', 'No',
    'Storeria occipitomaculata occipitomaculata', 'northern redbelly snake',
    'Colubridae', 'No', 'Tantilla gracilis', 'flat-headed snake', 'Colubridae',
    'No', 'Thamnophis proximus proximus', 'western ribbon snake', 'Colubridae',
    'No', 'Thamnophis radix', 'plains ribbon snake', 'Colubridae', 'No',
    'Thamnophis sauritus sauritus', 'eastern ribbon snake', 'Colubridae', 'No',
    'Thamnophis sauritus septentrionalis', 'northern ribbon snake',
    'Colubridae', 'No', 'Thamnophis sirtalis semifasciatus',
    'Chicago garter snake', 'Colubridae', 'No', 'Thamnophis sirtalis sirtalis',
    'common garter snake', 'Colubridae', 'No',
    'Tropidoclonion lineatum lineatum', 'northern lined snake', 'Colubridae',
    'No', 'Virginia valeriae elegans', 'western earth snake', 'Colubridae',
    'No'
]
snaketype = []
snakerecord = ("Scientific Name", "Common Name",       "Family", "Venomous (Yes/No)")
venomous =[]
nonvenomous =[]
for i in range (0,int(len(snakes_info)/4)):

  snaketype.append(snakerecord)
  snakerecord = list(snakerecord)
  j=4*i
  
  snakerecord[0] = snakes_info[j].title()
  snakerecord[1] = snakes_info[j+1].title()
  snakerecord[2] = snakes_info[j+2].title()
  snakerecord[3] = snakes_info[j+3]
  snakerecord= tuple(snakerecord)

for i in range (0, len(snaketype)):
  
  snakerecord = snaketype[i]
  if snakerecord[3] == "Yes":
    venomous.append(snakerecord)
  else: 
    nonvenomous.append(snakerecord)
print("Venomous")
print ("----------")

for i in range (0, len(venomous)):
  snakerecord= venomous[i]
  print(f"{'Common name:':<30} {snakerecord[1]:<50}")
  print(f"{'Family:':<30} {snakerecord[2]:<50}")
  print(f"{'Scientific Name:':<30} {snakerecord[0]:<50}")
  print("")

print("Venom-Free Snakes")
print ("----------")

for i in range (1, len(nonvenomous)):
  snakerecord= nonvenomous[i]
  print(f"{'Common name:':<30} {snakerecord[1].title():<50}")
  print(f"{'Family:':<30} {snakerecord[2]:<50}")
  print(f"{'Scientific Name:':<30} {snakerecord[0]:<50}")
  print("")

  
