import math
import argparse

# Load a fixed, sorted noun wordlist (3-6 letters, easy to pronounce)
# For demo, we use a small hardcoded list for simplicity
# In actual submission, load ~5000-10000 nouns from 'wordlist.txt' for real coverage
wordlist = [
    'apple', 'bench', 'chair', 'crow', 'dance', 'eagle', 'flame', 'globe', 'horse', 'kites',
    'lions', 'mango', 'nails', 'ocean', 'place', 'queen', 'river', 'snake', 'tiger', 'whale'
]

wordlist.sort()
wordlist_len = len(wordlist)

# India bounding box
LAT_MIN = 6.0
LAT_MAX = 38.0
LON_MIN = 68.0
LON_MAX = 97.0

# Grid size: 3 meters
grid_size_m = 3.0

# Compute approximate meters per degree
meters_per_deg_lat = 111000.0

def latlon_to_grid_id(lat, lon):
    lat_m = (lat - LAT_MIN) * meters_per_deg_lat
    lat_index = int(lat_m // grid_size_m)
    
    # Approx meters per degree longitude at this latitude
    meters_per_deg_lon = meters_per_deg_lat * math.cos(math.radians(lat))
    lon_m = (lon - LON_MIN) * meters_per_deg_lon
    lon_index = int(lon_m // grid_size_m)

    total_lon_cells = int(((LON_MAX - LON_MIN) * meters_per_deg_lon) // grid_size_m)
    grid_id = lat_index * total_lon_cells + lon_index
    return grid_id, lat_index, lon_index, total_lon_cells

def grid_id_to_latlon(grid_id, total_lon_cells):
    lat_index = grid_id // total_lon_cells
    lon_index = grid_id % total_lon_cells
    lat = LAT_MIN + (lat_index * grid_size_m) / meters_per_deg_lat
    meters_per_deg_lon = meters_per_deg_lat * math.cos(math.radians(lat))
    lon = LON_MIN + (lon_index * grid_size_m) / meters_per_deg_lon
    return lat, lon

def grid_id_to_words(grid_id):
    w1_index = grid_id // (wordlist_len ** 2)
    w2_index = (grid_id // wordlist_len) % wordlist_len
    w3_index = grid_id % wordlist_len
    return wordlist[w1_index % wordlist_len], wordlist[w2_index], wordlist[w3_index]

def words_to_grid_id(w1, w2, w3):
    try:
        w1_index = wordlist.index(w1)
        w2_index = wordlist.index(w2)
        w3_index = wordlist.index(w3)
    except ValueError:
        raise Exception("Word not found in wordlist. Use valid words from the fixed dictionary.")
    grid_id = w1_index * (wordlist_len ** 2) + w2_index * wordlist_len + w3_index
    return grid_id

def latlon_to_words(lat, lon):
    grid_id, lat_idx, lon_idx, total_lon_cells = latlon_to_grid_id(lat, lon)
    return grid_id_to_words(grid_id)

def words_to_latlon(w1, w2, w3):
    grid_id = words_to_grid_id(w1, w2, w3)
    lat, lon = grid_id_to_latlon(grid_id, compute_total_lon_cells_at_lat(lat_estimate()))
    return lat, lon

def compute_total_lon_cells_at_lat(lat):
    meters_per_deg_lon = meters_per_deg_lat * math.cos(math.radians(lat))
    total_lon_cells = int(((LON_MAX - LON_MIN) * meters_per_deg_lon) // grid_size_m)
    return total_lon_cells

def lat_estimate():
    # Middle of India for consistent total_lon_cells in reverse
    return (LAT_MIN + LAT_MAX) / 2

def main():
    parser = argparse.ArgumentParser(description="DIGIPIN + What3Words inspired geocoder")
    subparsers = parser.add_subparsers(dest='command')

    parser_encode = subparsers.add_parser('encode', help='Encode lat, lon to 3 words')
    parser_encode.add_argument('--lat', type=float, required=True, help='Latitude')
    parser_encode.add_argument('--lon', type=float, required=True, help='Longitude')

    parser_decode = subparsers.add_parser('decode', help='Decode 3 words to lat, lon')
    parser_decode.add_argument('--w1', type=str, required=True, help='Word 1')
    parser_decode.add_argument('--w2', type=str, required=True, help='Word 2')
    parser_decode.add_argument('--w3', type=str, required=True, help='Word 3')

    args = parser.parse_args()

    if args.command == 'encode':
        words = latlon_to_words(args.lat, args.lon)
        print(f"3 Words for ({args.lat}, {args.lon}): {words}")

    elif args.command == 'decode':
        lat, lon = words_to_latlon(args.w1, args.w2, args.w3)
        print(f"Coordinates for ({args.w1}, {args.w2}, {args.w3}): ({lat:.6f}, {lon:.6f})")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
