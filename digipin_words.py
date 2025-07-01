import math
import argparse
import hashlib

LAT_MIN = 6.0
LAT_MAX = 38.0
LON_MIN = 68.0
LON_MAX = 97.0

grid_size_m = 3.0

meters_per_deg_lat = 111000.0

def word_to_number(word):
    word_hash = hashlib.md5(word.lower().encode()).hexdigest()
    return int(word_hash[:8], 16)

def number_to_word_hash(number):
    return f"{number:08x}"

def latlon_to_grid_id(lat, lon):
    lat_m = (lat - LAT_MIN) * meters_per_deg_lat
    lat_index = int(lat_m // grid_size_m)
    
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
    w1_num = grid_id % 1000000
    w2_num = (grid_id * 17 + 42) % 1000000
    w3_num = (grid_id * 23 + 137) % 1000000
    
    w1 = f"loc{w1_num:06d}"
    w2 = f"pos{w2_num:06d}"
    w3 = f"pin{w3_num:06d}"
    
    return w1, w2, w3

def words_to_grid_id(w1, w2, w3):
    try:
        if w1.startswith('loc') and w2.startswith('pos') and w3.startswith('pin'):
            w1_num = int(w1[3:])
            w2_num = int(w2[3:])
            w3_num = int(w3[3:])
            
            grid_id = w1_num
            
        else:
            w1_num = word_to_number(w1)
            w2_num = word_to_number(w2)
            w3_num = word_to_number(w3)
            
            grid_id = (w1_num % 10000) * 100000000 + (w2_num % 10000) * 10000 + (w3_num % 10000)
            
        return grid_id
        
    except (ValueError, IndexError):
        print(f"\n❌ Error: Invalid word format. Words should be simple text.")
        return None

def latlon_to_words(lat, lon):
    if not (LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX):
        print(f"\n❌ Error: Coordinates ({lat}, {lon}) are outside India's coverage area.")
        print(f"Valid range: Latitude {LAT_MIN}-{LAT_MAX}, Longitude {LON_MIN}-{LON_MAX}")
        return None
    
    grid_id, lat_idx, lon_idx, total_lon_cells = latlon_to_grid_id(lat, lon)
    return grid_id_to_words(grid_id)

def words_to_latlon(w1, w2, w3):
    grid_id = words_to_grid_id(w1, w2, w3)
    if grid_id is None:
        return None, None
    
    lat_estimate = (LAT_MIN + LAT_MAX) / 2
    meters_per_deg_lon = meters_per_deg_lat * math.cos(math.radians(lat_estimate))
    total_lon_cells = int(((LON_MAX - LON_MIN) * meters_per_deg_lon) // grid_size_m)
    
    lat, lon = grid_id_to_latlon(grid_id, total_lon_cells)
    return lat, lon

def custom_words_to_latlon(w1, w2, w3):
    w1_num = word_to_number(w1)
    w2_num = word_to_number(w2) 
    w3_num = word_to_number(w3)
    
    combined = (w1_num + w2_num * 1000 + w3_num * 1000000) % (2**32)
    
    lat_range = LAT_MAX - LAT_MIN
    lon_range = LON_MAX - LON_MIN
    
    lat = LAT_MIN + (combined % 1000000) / 1000000.0 * lat_range
    lon = LON_MIN + ((combined // 1000000) % 1000000) / 1000000.0 * lon_range
    
    return lat, lon

def latlon_to_custom_words(lat, lon, word1="", word2="", word3=""):
    if not (LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX):
        print(f"\n❌ Error: Coordinates ({lat}, {lon}) are outside India's coverage area.")
        return None
    
    if word1 and word2 and word3:
        test_lat, test_lon = custom_words_to_latlon(word1, word2, word3)
        lat_diff = abs(lat - test_lat)
        lon_diff = abs(lon - test_lon)
        
        if lat_diff < 0.1 and lon_diff < 0.1:
            return word1, word2, word3
        else:
            print(f"\n⚠️  Warning: Words '{word1} {word2} {word3}' map to ({test_lat:.4f}, {test_lon:.4f})")
            print(f"   which is {lat_diff:.4f}° lat, {lon_diff:.4f}° lon away from your coordinates")
            return word1, word2, word3
    
    coord_hash = hashlib.md5(f"{lat:.6f},{lon:.6f}".encode()).hexdigest()
    w1 = f"geo{coord_hash[:4]}"
    w2 = f"loc{coord_hash[4:8]}"  
    w3 = f"pos{coord_hash[8:12]}"
    
    return w1, w2, w3

def main():
    parser = argparse.ArgumentParser(description="DIGIPIN - Flexible geocoder that works with ANY 3 words")
    subparsers = parser.add_subparsers(dest='command')

    parser_encode = subparsers.add_parser('encode', help='Encode lat, lon to 3 words')
    parser_encode.add_argument('--lat', type=float, required=True, help='Latitude')
    parser_encode.add_argument('--lon', type=float, required=True, help='Longitude')
    parser_encode.add_argument('--w1', type=str, help='Custom word 1 (optional)')
    parser_encode.add_argument('--w2', type=str, help='Custom word 2 (optional)')
    parser_encode.add_argument('--w3', type=str, help='Custom word 3 (optional)')

    parser_decode = subparsers.add_parser('decode', help='Decode 3 words to lat, lon')
    parser_decode.add_argument('--w1', type=str, required=True, help='Word 1')
    parser_decode.add_argument('--w2', type=str, required=True, help='Word 2')
    parser_decode.add_argument('--w3', type=str, required=True, help='Word 3')

    parser_custom = subparsers.add_parser('custom', help='Use any 3 words for a location')
    parser_custom.add_argument('--w1', type=str, required=True, help='Any word 1')
    parser_custom.add_argument('--w2', type=str, required=True, help='Any word 2')
    parser_custom.add_argument('--w3', type=str, required=True, help='Any word 3')

    args = parser.parse_args()

    if args.command == 'encode':
        if args.w1 and args.w2 and args.w3:
            words = latlon_to_custom_words(args.lat, args.lon, args.w1, args.w2, args.w3)
        else:
            words = latlon_to_words(args.lat, args.lon)
            
        if words:
            print(f"\n✅ 3 Words for ({args.lat}, {args.lon}): {words[0]} {words[1]} {words[2]}")
        
    elif args.command == 'decode':
        lat, lon = words_to_latlon(args.w1.lower(), args.w2.lower(), args.w3.lower())
        if lat is not None and lon is not None:
            print(f"\n✅ Coordinates for ({args.w1}, {args.w2}, {args.w3}): ({lat:.6f}, {lon:.6f})")
            
    elif args.command == 'custom':
        lat, lon = custom_words_to_latlon(args.w1, args.w2, args.w3)
        print(f"\n✅ Your custom words '{args.w1} {args.w2} {args.w3}' map to:")
        print(f"   Coordinates: ({lat:.6f}, {lon:.6f})")
        print(f"\n💡 To use these words consistently, always use the same spelling and order!")
        
    else:
        parser.print_help()
        print("\n🌟 Examples:")
        print("   python digipin_words.py encode --lat 22.32 --lon 70.76")
        print("   python digipin_words.py decode --w1 geo1a2b --w2 loc3c4d --w3 pos5e6f")
        print("   python digipin_words.py custom --w1 pizza --w2 chair --w3 happy")

if __name__ == "__main__":
    main()