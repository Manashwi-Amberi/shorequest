beaches = [
    {"name": "RK Beach", "city": "Visakhapatnam", "lat": 17.7204, "lon": 83.3305},
    {"name": "Rushikonda Beach", "city": "Visakhapatnam", "lat": 17.7828, "lon": 83.3850},
    {"name": "Yarada Beach", "city": "Visakhapatnam", "lat": 17.6588, "lon": 83.2747},
    {"name": "Bheemunipatnam Beach", "city": "Bheemunipatnam", "lat": 17.8900, "lon": 83.4520},
    {"name": "Marina Beach", "city": "Chennai", "lat": 13.0500, "lon": 80.2824},
    {"name": "Elliot's Beach", "city": "Chennai", "lat": 12.9981, "lon": 80.2729},
    {"name": "Mahabalipuram Beach", "city": "Mahabalipuram", "lat": 12.6269, "lon": 80.1920},
    {"name": "Kovalam Beach", "city": "Chennai", "lat": 12.7870, "lon": 80.2526},
    {"name": "Kovalam Beach", "city": "Kovalam", "lat": 8.3988, "lon": 76.9784},
    {"name": "Varkala Beach", "city": "Varkala", "lat": 8.7379, "lon": 76.7163},
    {"name": "Cherai Beach", "city": "Kochi", "lat": 10.1416, "lon": 76.1784},
    {"name": "Bekal Beach", "city": "Kasaragod", "lat": 12.3927, "lon": 75.0344},
    {"name": "Baga Beach", "city": "Goa", "lat": 15.5553, "lon": 73.7517},
    {"name": "Calangute Beach", "city": "Goa", "lat": 15.5439, "lon": 73.7553},
    {"name": "Anjuna Beach", "city": "Goa", "lat": 15.5730, "lon": 73.7407},
    {"name": "Palolem Beach", "city": "Goa", "lat": 15.0100, "lon": 74.0232},
    {"name": "Colva Beach", "city": "Goa", "lat": 15.2797, "lon": 73.9228},
    {"name": "Mandrem Beach", "city": "Goa", "lat": 15.6670, "lon": 73.7150},
    {"name": "Juhu Beach", "city": "Mumbai", "lat": 19.0990, "lon": 72.8265},
    {"name": "Girgaon Chowpatty", "city": "Mumbai", "lat": 18.9543, "lon": 72.8126},
    {"name": "Tarkarli Beach", "city": "Malvan", "lat": 16.0313, "lon": 73.4742},
    {"name": "Alibaug Beach", "city": "Alibaug", "lat": 18.6414, "lon": 72.8722},
    {"name": "Dumas Beach", "city": "Surat", "lat": 21.0873, "lon": 72.7105},
    {"name": "Mandvi Beach", "city": "Kutch", "lat": 22.8326, "lon": 69.3520},
    {"name": "Puri Beach", "city": "Puri", "lat": 19.7983, "lon": 85.8245},
    {"name": "Chandrabhaga Beach", "city": "Konark", "lat": 19.8876, "lon": 86.0945},
    {"name": "Gopalpur Beach", "city": "Gopalpur", "lat": 19.2634, "lon": 84.9145},
    {"name": "Radhanagar Beach", "city": "Havelock Island", "lat": 11.9849, "lon": 92.9486},
    {"name": "Elephant Beach", "city": "Havelock Island", "lat": 12.0128, "lon": 92.9558},
    {"name": "Kanyakumari Beach", "city": "Kanyakumari", "lat": 8.0780, "lon": 77.5410}
]

import os
output_path = os.path.join(os.path.dirname(__file__), "app/data/beaches_data.py")
with open(output_path, "w") as f:
    f.write("beaches = " + repr(beaches) + "\n")
print("beaches_data.py updated successfully")
