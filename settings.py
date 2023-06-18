scores = {
    'dcp': {
        'dcp1': {
            "r11": 2,
            "r12": 1,
            "r13": 0,
        },
        'dcp2': {
            "r21": 2,
            "r22": 1,
            "r23": 0,
        },
        'dcp3': {
            "r31": 2,
            "r32": 1,
            "r33": 0,
        },
        'dcp4': {
            "r41": 2,
            "r42": 1,
            "r43": 0,
        },
        'dcp5': {
            "r51": 2,
            "r52": 1,
            "r53": 0,
        },
        'dcp6': {
            "r61": 2,
            "r62": 1,
            "r63": 0,
        },
        'dcp7': {
            "r71": 2,
            "r72": 1,
            "r73": 0,
        },
    }
}


msgs = {
    'dcp': {
        100: "Bonne gestion DCP",
        75: "Bien",
        50: "Correct",
        25: "Insuffisant",
        0: "Mauvais",
    }
}

twins = {
    'Paris': ['Rome', 'Montreal', 'Saint Petersburg', 'Hanoi'],
    'New York City': ['London', 'Tokyo', 'Sydney', 'São Paulo'],
    'Tokyo': ['Seoul', 'Shanghai', 'Mumbai', 'Buenos Aires'],
    'Beijing': ['Moscow', 'Berlin', 'Jakarta', 'Mexico City'],
    'Athens': ['Rome', 'Istanbul', 'Beirut', 'Lisbon'],
    'Madrid': ['Buenos Aires', 'Lima', 'Bogotá', 'Miami'],
    'Cairo': ['Istanbul', 'Mumbai', 'Johannesburg', 'Lagos'],
    'Los Angeles': ['Sydney', 'Mumbai', 'Vancouver', 'São Paulo'],
    'Istanbul': ['Cairo', 'Athens', 'Moscow', 'Tehran'],
    'Rome': ['Paris', 'Athens', 'Alexandria', 'Barcelona'],
    'Montreal': ['Paris', 'Toronto', 'Algiers', 'Chicago'],
    'Saint Petersburg': ['Paris', 'Moscow', 'Havana', 'Shanghai'],
    'Hanoi': ['Paris', 'Bangkok', 'Kuala Lumpur', 'Manila'],
    'London': ['New York City', 'Paris', 'Sydney', 'Toronto'],
    'Sydney': ['New York City', 'Los Angeles', 'London', 'Melbourne'],
    'São Paulo': ['New York City', 'Los Angeles', 'Buenos Aires', 'Rio de Janeiro'],
    'Seoul': ['Tokyo', 'Shanghai', 'Beijing', 'Bangkok'],
    'Shanghai': ['Tokyo', 'Seoul', 'Beijing', 'Hong Kong'],
    'Mumbai': ['Tokyo', 'Cairo', 'Jakarta', 'Delhi'],
    'Buenos Aires': ['Tokyo', 'Madrid', 'São Paulo', 'Rio de Janeiro'],
    'Moscow': ['Beijing', 'Istanbul', 'St. Petersburg', 'Kiev'],
    'Berlin': ['Beijing', 'Moscow', 'Istanbul', 'Vienna'],
    'Jakarta': ['Beijing', 'Mumbai', 'Bangkok', 'Manila'],
    'Mexico City': ['Beijing', 'Buenos Aires', 'São Paulo', 'Los Angeles'],
    'Cairo': ['Athens', 'Istanbul', 'Mumbai', 'Johannesburg'],
    'Alexandria': ['Rome', 'Athens', 'Cairo', 'Jerusalem'],
    'Barcelona': ['Rome', 'Madrid', 'Paris', 'Lisbon'],
    'Toronto': ['Montreal', 'London', 'Chicago', 'Vancouver'],
    'Algiers': ['Montreal', 'Cairo', 'Casablanca', 'Tunis'],
    'Chicago': ['Montreal', 'Toronto', 'New York City', 'Los Angeles'],
    'Havana': ['Saint Petersburg', 'Buenos Aires', 'San Juan', 'Nassau'],
    'Bangkok': ['Seoul', 'Shanghai', 'Hanoi', 'Singapore'],
    'Kuala Lumpur': ['Hanoi', 'Singapore', 'Jakarta', 'Bangkok'],
    'Manila': ['Hanoi', 'Jakarta', 'Hong Kong', 'Taipei'],
    'Delhi': ['Mumbai', 'Kolkata', 'Bangalore', 'Chennai'],
    'Rio de Janeiro': ['São Paulo', 'Buenos Aires', 'Lima', 'Bogotá'],
    'Hong Kong': ['Shanghai', 'Manila', 'Taipei', 'Singapore'],
    'Melbourne': ['Sydney', 'Auckland', 'Brisbane', 'Perth'],
    'Vienna': ['Berlin', 'Prague', 'Budapest', 'Zurich'],
    'Johannesburg': ['Cairo', 'Lagos', 'Cape Town', 'Nairobi'],
    'Lagos': ['Cairo', 'Johannesburg', 'Nairobi', 'Accra'],
    'Alexandria': ['Rome', 'Athens', 'Cairo', 'Jerusalem'],
    'Jerusalem': ['Alexandria', 'Athens', 'Rome', 'Istanbul'],
    'Lisbon': ['Athens', 'Madrid', 'Barcelona', 'Rome'],
    'Vancouver': ['Toronto', 'Los Angeles', 'Seattle', 'Calgary'],
    'Casablanca': ['Algiers', 'Rabat', 'Tangier', 'Marrakech'],
    'San Juan': ['Havana', 'Bogotá', 'Santo Domingo', 'Miami'],
    'Nassau': ['Havana', 'Miami', 'San Juan', 'Kingston'],
    'Singapore': ['Bangkok', 'Kuala Lumpur', 'Hong Kong', 'Manila'],
    'Kolkata': ['Delhi', 'Mumbai', 'Chennai', 'Bangalore'],
    'Chennai': ['Delhi', 'Kolkata', 'Mumbai', 'Bangalore'],
    'Bangalore': ['Delhi', 'Kolkata', 'Chennai', 'Mumbai'],
    'Perth': ['Melbourne', 'Sydney', 'Auckland', 'Brisbane'],
    'Zurich': ['Vienna', 'Munich', 'Milan', 'Paris'],
    'Prague': ['Vienna', 'Berlin', 'Budapest', 'Warsaw'],
    'Budapest': ['Vienna', 'Prague', 'Belgrade', 'Sofia'],
    'Warsaw': ['Prague', 'Berlin', 'Vienna', 'Moscow'],
    'Rabat': ['Casablanca', 'Algiers', 'Tangier', 'Marrakech'],
    'Tangier': ['Casablanca', 'Rabat', 'Algiers', 'Marrakech'],
    'Marrakech': ['Casablanca', 'Rabat', 'Tangier', 'Algiers'],
    'Seattle': ['Vancouver', 'Los Angeles', 'San Francisco', 'Portland'],
    'Calgary': ['Vancouver', 'Edmonton', 'Toronto', 'Montreal'],
    'Riyadh': ['Dubai', 'Doha', 'Jeddah', 'Muscat'],
    'Dubai': ['Riyadh', 'Doha', 'Abu Dhabi', 'Muscat'],
    'Doha': ['Riyadh', 'Dubai', 'Abu Dhabi', 'Muscat'],
    'Abu Dhabi': ['Dubai', 'Doha', 'Riyadh', 'Muscat'],
    'Muscat': ['Riyadh', 'Dubai', 'Doha', 'Abu Dhabi'],
    'Nairobi': ['Johannesburg', 'Cairo', 'Lagos', 'Kampala'],
    'Accra': ['Lagos', 'Cotonou', 'Lomé', 'Abidjan'],
    'Kingston': ['San Juan', 'Miami', 'Santo Domingo', 'Havana'],  
    'Taipei': ['Cebu City', 'Osaka', 'Fukuoka', 'Rotterdam'],
    'Portland': ['Sapporo', 'Guadalajara', 'Kaohsiung', 'Auckland'],
    'Munich': ['Rennes', 'Edinburgh', 'Cincinnati', 'Kyiv'],
    'Cape Town': ['Sydney', 'Rio de Janeiro', 'Perth', 'Dakar'],
    'Brisbane': ['Chongqing', 'Dalian', 'Kaohsiung', 'Tacloban'],
    'San Francisco': ['Oakland', 'Shanghai', 'Cebu City', 'Kaohsiung'],
    'Jeddah': ['Makkah', 'Casablanca', 'Riyadh', 'Kuala Lumpur'],
    'Bogotá': ['Quito', 'La Paz', 'Mexico City', 'Guayaquil'],
    'Cotonou': ['Ouagadougou', 'Porto-Novo', 'Bamako', 'Abidjan'],
    'Auckland': ['Brisbane', 'Kaohsiung', 'Portland', 'Adelaide'],
    'Abidjan': ['Brazzaville', 'Dakar', 'Cotonou', 'Porto-Novo'],
    'Kiev': ['Riga', 'Yekaterinburg', 'Havana', 'Munich'],
    'Belgrade': ['Yerevan', 'Banja Luka', 'Prague', 'Podgorica'],
    'St. Petersburg': ['Murmansk', 'Barcelona', 'Istanbul', 'Riga'],
    'Santo Domingo': ['San Juan', 'Miami', 'Caracas', 'Ponce'],
    'Tehran': ['Istanbul', 'Kuala Lumpur', 'Lima', 'Baghdad'],
    'Kampala': ['Kigali', 'Nairobi', 'Dar es Salaam', 'Lusaka'],
    'Sofia': ['Podgorica', 'Ljubljana', 'Athens', 'Tbilisi'],
    'Lima': ['Arequipa', 'Guayaquil', 'Tehran', 'Istanbul'],
    'Lomé': ['Lagos', 'Cotonou', 'Accra', 'Abuja'],
    'Beirut': ['Nicosia', 'Amman', 'Muscat', 'Tripoli'],
    'Tunis': ['Algiers', 'Casablanca', 'Rabat', 'Tripoli'],
    'Miami': ['Fort Lauderdale', 'Santo Domingo', 'San Juan', 'Port-au-Prince'],
    'Edmonton': ['Calgary', 'Winnipeg', 'Saskatoon', 'Regina'],
    'Milan': ['Turin', 'Bologna', 'Naples', 'Florence']
}

powers = {
    1: 'king',
    2: 'sonic'
}
