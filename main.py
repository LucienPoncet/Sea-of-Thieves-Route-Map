import math


# chaque bateau aura un nom, une vitesse minimale contre le vent et une vitesse maximale avec le vent


class Ship:
    def __init__(self, name, low_speed: int = 0, high_speed: int = 0):
        self.name = name
        self.low_speed = low_speed
        self.high_speed = high_speed

# les vitesses ont été calculées dans le jeu et sont en noeuds marins, c'est à dire en miles nautiques par heure


sloop = Ship('Sloop', 12, 18)
brigantine = Ship('Brigantine', 11, 21)
galleon = Ship('Galleon', 10, 22)


# chaque île a un nom, un emplacement sur une grille, un type de structure et une région d'appartenance
# la longitude et la latitude n'ont pas besoin d'être remplies ou calculées manuellement puisque l'emplacement sur la
# grille permettront de les trouver plus tard
# grid_longitude correspond donc à une lettre, et grid_latitude à un nombre


class Island:
    islands_list = []

    def __init__(self, name, grid_longitude, grid_latitude, region, structure, longitude: int = 0, latitude: int = 0):
        self.name = name
        self.grid_longitude = grid_longitude
        self.grid_latitude = grid_latitude
        self.region = region
        self.structure = structure
        self.longitude = longitude
        self.latitude = latitude
        self.islands_list.append(self)


cannon_cove = Island("Cannon Cove", 'G', 10, "The Shores of Plenty", 'Large Island')
crescent_isle = Island("Crescent Isle", 'B', 9, "The Shores of Plenty", 'Large Island')
lone_cove = Island("Lone Cove", 'H', 6, "The Shores of Plenty", 'Large Island')
mermaid_s_hideaway = Island("Mermaid's Hideaway", 'B', 13, "The Shores of Plenty", 'Large Island')
sailor_s_bounty = Island("Sailor's Bounty", 'C', 4, "The Shores of Plenty", 'Large Island')
smuggler_s_bay = Island("Smuggler's Bay", 'F', 3, "The Shores of Plenty", 'Large Island')
wanderers_refuge = Island("Wanderers Refuge", 'F', 12, "The Shores of Plenty", 'Large Island')
crook_s_hollow = Island("Crook's Hollow", 'M', 16, "The Ancient Isles", 'Large Island')
devil_s_ridge = Island("Devil's Ridge", 'P', 19, "The Ancient Isles", 'Large Island')
discovery_ridge = Island("Discovery Ridge", 'E', 17, "The Ancient Isles", 'Large Island')
plunder_valley = Island("Plunder Valley", 'G', 16, "The Ancient Isles", 'Large Island')
shark_bait_cove = Island("Shark Bait Cove", 'H', 19, "The Ancient Isles", 'Large Island')
snake_island = Island("Snake Island", 'K', 16, "The Ancient Isles", 'Large Island')
thieves_haven = Island("Thieves' Haven", 'L', 20, "The Ancient Isles", 'Large Island')
kraken_s_fall = Island("Kraken's Fall", 'R', 12, "The Wilds", 'Large Island')
marauder_s_arch = Island("Marauder's Arch", 'Q', 3, "The Wilds", 'Large Island')
old_faithful_isle = Island("Old Faithful Isle", 'M', 4, "The Wilds", 'Large Island')
shipwreck_bay = Island("Shipwreck Bay", 'M', 10, "The Wilds", 'Large Island')
the_crooked_masts = Island("The Crooked Masts", 'O', 11, "The Wilds", 'Large Island')
the_sunken_grove = Island("The Sunken Grove", 'P', 7, "The Wilds", 'Large Island')
ashen_reaches = Island("Ashen Reaches", 'V', 23, "The Devil's Roar", 'Large Island')
fetcher_s_rest = Island("Fetcher's Rest", 'V', 12, "The Devil's Roar", 'Large Island')
flintlock_peninsula = Island("Flintlock Peninsula", 'W', 14, "The Devil's Roar", 'Large Island')
ruby_s_fall = Island("Ruby's Fall", 'Y', 16, "The Devil's Roar", 'Large Island')
the_devil_s_thirst = Island("The Devil's Thirst", 'W', 21, "The Devil's Roar", 'Large Island')
the_glorious_sea_dog = Island("The Glorious Sea Dog", 'K', 11, "the middle of the map", 'Large Island')
the_shores_of_gold = Island("The Shores of Gold", 'Y', 3, "The Devil's Shroud", 'Large Island')
boulder_cay = Island("Boulder Cay", 'G', 5, "The Shores of Plenty", 'Small Island')
lagoon_of_whispers = Island("Lagoon of Whispers", 'D', 12, "The Shores of Plenty", 'Small Island')
lonely_isle = Island("Lonely Isle", 'G', 8, "The Shores of Plenty", 'Small Island')
picaroon_palms = Island("Picaroon Palms", 'I', 4, "The Shores of Plenty", 'Small Island')
rapier_cay = Island("Rapier Cay", 'D', 8, "The Shores of Plenty", 'Small Island')
rum_runner_isle = Island("Rum Runner Isle", 'H', 9, "The Shores of Plenty", 'Small Island')
salty_sands = Island("Salty Sands", 'G', 3, "The Shores of Plenty", 'Small Island')
sandy_shallows = Island("Sandy Shallows", 'D', 5, "The Shores of Plenty", 'Small Island')
sea_dog_s_rest = Island("Sea Dog's Rest", 'C', 11, "The Shores of Plenty", 'Small Island')
twin_groves = Island("Twin Groves", 'H', 11, "The Shores of Plenty", 'Small Island')
barnacle_cay = Island("Barnacle Cay", 'O', 15, "The Ancient Isles", 'Small Island')
booty_isle = Island("Booty Isle", 'K', 20, "The Ancient Isles", 'Small Island')
castaway_isle = Island("Castaway Isle", 'K', 14, "The Ancient Isles", 'Small Island')
chicken_isle = Island("Chicken Isle", 'I', 16, "The Ancient Isles", 'Small Island')
cutlass_cay = Island("Cutlass Cay", 'M', 18, "The Ancient Isles", 'Small Island')
fools_lagoon = Island("Fools Lagoon", 'I', 14, "The Ancient Isles", 'Small Island')
lookout_point = Island("Lookout Point", 'I', 20, "The Ancient Isles", 'Small Island')
mutineer_rock = Island("Mutineer Rock", 'N', 19, "The Ancient Isles", 'Small Island')
old_salts_atoll = Island("Old Salts Atoll", 'F', 18, "The Ancient Isles", 'Small Island')
paradise_spring = Island("Paradise Spring", 'L', 17, "The Ancient Isles", 'Small Island')
black_sand_atoll = Island("Black Sand Atoll", 'O', 3, "The Wilds", 'Small Island')
black_water_enclave = Island("Black Water Enclave", 'R', 5, "The Wilds", 'Small Island')
blind_man_s_lagoon = Island("Blind Man's Lagoon", 'N', 6, "The Wilds", 'Small Island')
isle_of_last_words = Island("Isle of Last Words", 'O', 9, "The Wilds", 'Small Island')
liar_s_backbone = Island("Liar's Backbone", 'S', 11, "The Wilds", 'Small Island')
plunderer_s_plight = Island("Plunderer's Plight", 'Q', 6, "The Wilds", 'Small Island')
scurvy_isley = Island("Scurvy Isley", 'K', 4, "The Wilds", 'Small Island')
shark_tooth_key = Island("Shark Tooth Key", 'P', 13, "The Wilds", 'Small Island')
shiver_retreat = Island("Shiver Retreat", 'Q', 11, "The Wilds", 'Small Island')
tri_rock_isle = Island("Tri-Rock Isle", 'R', 10, "The Wilds", 'Small Island')
brimestone_rock = Island("Brimestone Rock", 'X', 18, "The Devil's Roar", 'Small Island')
cinder_islet = Island("Cinder Islet", 'U', 14, "The Devil's Roar", 'Small Island')
cursewater_shores = Island("Cursewater Shores", 'Y', 13, "The Devil's Roar", 'Small Island')
flame_s_end = Island("Flame's End", 'V', 19, "The Devil's Roar", 'Small Island')
forsaken_brink = Island("Forsaken Brink", 'U', 16, "The Devil's Roar", 'Small Island')
glowstone_cay = Island("Glowstone Cay", 'Z', 18, "The Devil's Roar", 'Small Island')
magma_s_tide = Island("Magma's Tide", 'Y', 20, "The Devil's Roar", 'Small Island')
roaring_sands = Island("Roaring Sands", 'U', 21, "The Devil's Roar", 'Small Island')
scorched_pass = Island("Scorched Pass", 'X', 11, "The Devil's Roar", 'Small Island')
sanctuary_outpost = Island("Sanctuary Outpost", 'F', 7, "The Shores of Plenty", 'Outpost')
port_merrick = Island("Port Merrick", 'D', 10, "The Shores of Plenty", 'Outpost')
plunder_outpost = Island("Plunder Outpost", 'J', 18, "The Ancient Isles", 'Outpost')
ancient_spire_outpost = Island("Ancient Spire Outpost", 'Q', 17, "The Ancient Isles", 'Outpost')
galleon_s_grave_outpost = Island("Galleon's Grave Outpost", 'R', 8, "The Wilds", 'Outpost')
dagger_tooth_outpost = Island("Dagger Tooth Outpost", 'M', 8, "The Wilds", 'Outpost')
morrow_s_peak_outpost = Island("Morrow's Peak Outpost", 'V', 17, "The Devil's Roar", 'Outpost')
the_reaper_s_hideout = Island("The Reaper's Hideout", 'I', 12, "the middle of the map", 'Outpost')
the_spoils_of_plenty_store = Island("The Spoils of Plenty Store", 'B', 7, "The Shores of Plenty", 'Seapost')
the_north_star_seapost = Island("The North Star Seapost", 'H', 10, "The Shores of Plenty", 'Seapost')
the_finest_trading_post = Island("The Finest Trading Post", 'F', 17, "The Ancient Isles", 'Seapost')
stephen_s_spoils = Island("Stephen's Spoils", 'L', 15, "The Ancient Isles", 'Seapost')
three_paces_east_seapost = Island("Three Paces East Seapost", 'S', 10, "The Wilds", 'Seapost')
the_wild_treasures_store = Island("The Wild Treasures Store", 'O', 4, "The Wilds", 'Seapost')
brian_s_bazaar = Island("Brian's Bazaar", 'Y', 12, "The Devil's Roar", 'Seapost')
roaring_traders = Island("Roaring Traders", 'U', 20, "The Devil's Roar", 'Seapost')
keel_haul_fort = Island("Keel Haul Fort", 'C', 6, "The Shores of Plenty", 'Fortress')
hidden_spring_keep = Island("Hidden Spring Keep", 'I', 8, "The Shores of Plenty", 'Fortress')
sailor_s_knot_stronghold = Island("Sailor's Knot Stronghold", 'E', 14, "The Shores of Plenty", 'Fortress')
lost_gold_fort = Island("Lost Gold Fort", 'H', 17, "The Ancient Isles", 'Fortress')
fort_of_the_damned = Island("Fort of the Damned", 'L', 14, "The Ancient Isles", 'Fortress')
the_crow_s_nest_fortress = Island("The Crow's Nest Fortress", 'O', 17, "The Ancient Isles", 'Fortress')
skull_keep = Island("Skull Keep", 'P', 9, "The Wilds", 'Fortress')
kraken_watchtower = Island("Kraken Watchtower", 'L', 6, "The Wilds", 'Fortress')
shark_fin_camp = Island("Shark Fin Camp", 'P', 5, "The Wilds", 'Fortress')
molten_sands_fortress = Island("Molten Sands Fortress", 'Z', 11, "The Devil's Roar", 'Fortress')
royal_crest_fortress = Island("Royal Crest Fortress", 'J', 6, "The Shores of Plenty", 'Sea Fort')
imperial_crown_fortress = Island("Imperial Crown Fortress", 'B', 11, "The Shores of Plenty", 'Sea Fort')
ancient_gold_fortress = Island("Ancient Gold Fortress", 'F', 19, "The Ancient Isles", 'Sea Fort')
old_brinestone_fortress = Island("Old Brinestone Fortress", 'K', 21, "The Ancient Isles", 'Sea Fort')
traitor_s_fate_fortress = Island("Traitor's Fate Fortress", 'S', 6, "The Wilds", 'Sea Fort')
mercy_s_end_fortress = Island("Mercy's End Fortress", 'P', 14, "The Wilds", 'Sea Fort')
treasury_of_sunken_shores = Island("Treasury of Sunken Shores", 'D', 3, "The Shores of Plenty", 'Siren Treasury')
treasury_of_the_lost_ancients = Island("Treasury of the Lost Ancients", 'H', 15, "The Ancient Isles", 'Siren Treasury')
treasury_of_the_secret_wilds = Island("Treasury of the Secret Wilds", 'L', 3, "The Wilds", 'Siren Treasury')
shrine_of_the_coral_tomb = Island("Shrine of the Coral Tomb", 'H', 5, "The Shores of Plenty", 'Siren Shrine')
shrine_of_ocean_s_fortune = Island("Shrine of Ocean's Fortune", 'D', 14, "The Shores of Plenty", 'Siren Shrine')
shrine_of_ancient_tears = Island("Shrine of Ancient Tears", 'N', 20, "The Ancient Isles", 'Siren Shrine')
shrine_of_tribute = Island("Shrine of Tribute", 'G', 18, "The Ancient Isles", 'Siren Shrine')
shrine_of_hungering = Island("Shrine of Hungering", 'Q', 5, "The Wilds", 'Siren Shrine')
shrine_of_flooded_embrace = Island("Shrine of Flooded Embrace", 'N', 12, "The Wilds", 'Siren Shrine')


def path(starting_point, destination, ship):
    for i in range(97, 123):
        g_long = str.upper(chr(i))
        # g_long s'étend de A à Z : si il correspond à la longitude de l'île de départ ou de la destination,
        # on lui attribue son nombre équivalent dans l'alphabet (A = 1, B = 2, etc)
        if starting_point.grid_longitude == g_long:
            # comme la lettre A correspond à 97 en caractère Unicode, on lui soustrait 96 pour donner 1
            starting_point.longitude = i-96
        if destination.grid_longitude == g_long:
            destination.longitude = i-96

    # la carte semblable à un échiquier place le chiffre en 1 en haut à gauche, mais on le préfère en bas à gauche
    # ainsi, nos coordonnées semblent placées sur un repère orthonormé
    # on soustrait donc le point de repère de la latitude de la grille à 27 pour donner la latitude finale
    starting_point.latitude = 27 - starting_point.grid_latitude
    destination.latitude = 27 - destination.grid_latitude

    # la distance entre deux points A(xA;yA) et B(xB;yB) dans un repère orthonormé est la suivante :
    # √((xB-xA)²+(yB-yA)²)
    # 1 mile nautique correspond à 5 carrés sur la carte du jeu, donc ces carrés ont une longueur de 0.2 miles
    # on multiplie donc le nombre trouvé par 0.2, puis on l'arrondit à deux chiffres après la virgule
    path_length = round(math.sqrt(math.pow((destination.longitude - starting_point.longitude), 2) + math.pow(
        (destination.latitude - starting_point.latitude), 2)) * 0.2, 2)

    print('Route length from 'f'{starting_point.name} to 'f'{destination.name} : 'f'{path_length}', end=' ')

    if path_length == 1.00:
        print('mile')

    else:
        print('miles')

    # la durée du trajet est donc calculée en divisant les vitesse du bateau par 60 pour donner du miles par minute
    # puis en divisant la longueur du trajet par ce nombre
    slowest_travel_time = round(path_length / (ship.low_speed / 60), 2)
    fastest_travel_time = round(path_length / (ship.high_speed / 60), 2)

    # pour transformer les décimales des minutes en secondes, on utilise l'opérateur modulo % :
    # on effectuant une division entière par 1 avec le modulo, on ne garde ainsi que ce qu'il y a après la virgule,
    # que l'on peut multiplier par 60 pour donner des secondes
    print(
        'Travel time with a 'f'{ship.name} : between 'f'{int(fastest_travel_time)} min '
        f''f'{round((fastest_travel_time % 1) * 60)} sec and 'f'{int(slowest_travel_time)} min '
        f''f'{round((slowest_travel_time % 1) * 60)} sec')

    print('Go', end=' ')
    # en fonction des latitudes et longitudes des deux points, on peut déterminer quelle direction prendre :
    if destination.longitude > starting_point.longitude:
        # on choisit de pouvoir donner plusieurs angles de directions dans le cas où il faille aller à l'est :
        # aller à l'est tout droit, au sud-est, au sud/sud-est, à l'est/sud-est, au nord-est, au nord/nord-est, et
        # à l'est/nord-est
        if destination.latitude > starting_point.latitude:
            if abs(destination.longitude - starting_point.longitude) <= 1 and \
                    abs(destination.latitude - starting_point.latitude) > 2 or \
                    abs(destination.longitude - starting_point.longitude) <= 2 and \
                    abs(destination.latitude - starting_point.latitude) > 7:
                print('North/', end='')
            elif abs(destination.latitude - starting_point.latitude) <= 1 and \
                    abs(destination.longitude - starting_point.longitude) > 2 or \
                    abs(destination.latitude - starting_point.latitude) <= 2 and \
                    abs(destination.longitude - starting_point.longitude) > 7:
                print('East/', end='')
            print('North-', end='')
        elif destination.latitude < starting_point.latitude:
            if abs(destination.longitude - starting_point.longitude) <= 1 and \
                    abs(destination.latitude - starting_point.latitude) > 2 or \
                    abs(destination.longitude - starting_point.longitude) <= 2 and \
                    abs(destination.latitude - starting_point.latitude) > 7:
                print('South/', end='')
            elif abs(destination.latitude - starting_point.latitude) <= 1 and \
                    abs(destination.longitude - starting_point.longitude) > 2 or \
                    abs(destination.latitude - starting_point.latitude) <= 2 and \
                    abs(destination.longitude - starting_point.longitude) > 7:
                print('East/', end='')
            print('South-', end='')
        print('East')
    elif destination.longitude < starting_point.longitude:
        # c'est la même chose pour l'ouest : 7 directions possibles
        if destination.latitude > starting_point.latitude:
            if abs(destination.longitude - starting_point.longitude) <= 1 and \
                    abs(destination.latitude - starting_point.latitude) > 2 or \
                    abs(destination.longitude - starting_point.longitude) <= 2 and \
                    abs(destination.latitude - starting_point.latitude) > 7:
                print('North/', end='')
            elif abs(destination.latitude - starting_point.latitude) <= 1 and \
                    abs(destination.longitude - starting_point.longitude) > 2 or \
                    abs(destination.latitude - starting_point.latitude) <= 2 and \
                    abs(destination.longitude - starting_point.longitude) > 7:
                print('West/', end='')
            print('North-', end='')
        elif destination.latitude < starting_point.latitude:
            if abs(destination.longitude - starting_point.longitude) <= 1 and \
                    abs(destination.latitude - starting_point.latitude) > 2 or \
                    abs(destination.longitude - starting_point.longitude) <= 2 and \
                    abs(destination.latitude - starting_point.latitude) > 7:
                print('South/', end='')
            elif abs(destination.latitude - starting_point.latitude) <= 1 and \
                    abs(destination.longitude - starting_point.longitude) > 2 or \
                    abs(destination.latitude - starting_point.latitude) <= 2 and \
                    abs(destination.longitude - starting_point.longitude) > 7:
                print('West/', end='')
            print('South-', end='')
        print('West')
    else:
        if destination.latitude > starting_point.latitude:
            print('North')
        elif destination.latitude < starting_point.latitude:
            print('South')
        else:
            print('You have arrived at your destination')

    # informations sur le lieu d'arrivée :
    print('\n')
    print('Destination : 'f'{destination.name} / Type of structure : 'f'{destination.structure} / Region : '
          f'{destination.region}')
    print('\n')

    # on cherche dans toute la liste de la classe Island les mêmes structures que le lieu d'arrivée dans la même région :
    if destination.structure == 'Fortress':
        print('All 'f'{destination.structure}(es) in 'f'{destination.region} :')
    elif destination.structure == 'Siren Treasury':
        print(f'{destination.structure} in 'f'{destination.region} :')
    else:
        print('All 'f'{destination.structure}(s) in 'f'{destination.region} :')

    for i in Island.islands_list:
        if i.structure == destination.structure and i.region == destination.region:
            print(f'{i.name} : 'f'{i.grid_longitude}'f'{i.grid_latitude}')


path(shipwreck_bay, lookout_point, sloop)
