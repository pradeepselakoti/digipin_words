# DIGIPIN - 3 Words Geocoding System

A geocoding system inspired by What3Words that converts latitude/longitude coordinates to memorable 3-word combinations for locations within India.

## 🌟 What is DIGIPIN?

DIGIPIN divides India into a 3-meter grid system where each location is represented by exactly 3 words from a curated dictionary. This makes it easy to share precise locations using simple, memorable words instead of complex coordinates.

**Example:**
- Coordinates: `22.3215616, 70.7657728`
- 3 Words: `crow place whale`

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher installed on your computer
- Basic familiarity with command line/terminal

### Installation

1. **Download the files**
   - Save `digipin_words.py` to a folder on your computer
   - Create a project folder (e.g., `digipin-3words`)

2. **Open Terminal/Command Prompt**
   - **Windows:** Press `Win + R`, type `cmd`, press Enter
   - **Mac:** Press `Cmd + Space`, type `Terminal`, press Enter
   - **Linux:** Press `Ctrl + Alt + T`

3. **Navigate to your project folder**
   ```bash
   cd path/to/your/digipin-3words
   ```
   *Replace `path/to/your/digipin-3words` with the actual path to your folder*

## 📍 How to Use

### Convert Coordinates to 3 Words

```bash
python digipin_words.py encode --lat 22.3215616 --lon 70.7657728
```

**Output:**
```
3 Words for (22.3215616, 70.7657728): ('crow', 'place', 'whale')
```

### Convert 3 Words to Coordinates

```bash
python digipin_words.py decode --w1 crow --w2 place --w3 whale
```

**Output:**
```
Coordinates for (crow, place, whale): (22.321562, 70.765773)
```

## 🔧 Command Reference

### Encoding (Coordinates → Words)
```bash
python digipin_words.py encode --lat [LATITUDE] --lon [LONGITUDE]
```

**Parameters:**
- `--lat`: Latitude (decimal degrees, e.g., 22.3215616)
- `--lon`: Longitude (decimal degrees, e.g., 70.7657728)

### Decoding (Words → Coordinates)
```bash
python digipin_words.py decode --w1 [WORD1] --w2 [WORD2] --w3 [WORD3]
```

**Parameters:**
- `--w1`: First word
- `--w2`: Second word  
- `--w3`: Third word

## 📋 Examples

### Example 1: Mumbai Location
```bash
# Encode coordinates
python digipin_words.py encode --lat 19.0760 --lon 72.8777

# Decode words (example output)
python digipin_words.py decode --w1 apple --w2 bench --w3 chair
```

### Example 2: Delhi Location
```bash
# Encode coordinates
python digipin_words.py encode --lat 28.6139 --lon 77.2090

# Decode words (example output)
python digipin_words.py decode --w1 eagle --w2 flame --w3 globe
```

## 🗺️ Coverage Area

- **Country:** India
- **Latitude Range:** 6.0° to 38.0°
- **Longitude Range:** 68.0° to 97.0°
- **Precision:** 3-meter grid squares

## 📚 Available Words

The system uses a curated dictionary of 20 common English nouns (expandable to thousands):

`apple`, `bench`, `chair`, `crow`, `dance`, `eagle`, `flame`, `globe`, `horse`, `kites`, `lions`, `mango`, `nails`, `ocean`, `place`, `queen`, `river`, `snake`, `tiger`, `whale`

## ❓ Troubleshooting

### "Python is not recognized"
- Make sure Python is installed: Download from [python.org](https://python.org)
- Add Python to your system PATH during installation

### "Word not found in wordlist"
- Use only words from the available dictionary listed above
- Check spelling carefully
- Words are case-sensitive (use lowercase)

### "No such file or directory"
- Make sure you're in the correct folder using `cd` command
- Check that `digipin_words.py` is in your current directory
- Use `ls` (Mac/Linux) or `dir` (Windows) to list files

### Getting Help
```bash
python digipin_words.py --help
```

## 🔮 Future Enhancements

- Expand wordlist to 5,000-10,000 words for better coverage
- Add support for other countries
- Web interface for easy access
- Mobile app integration
- Offline functionality

## 🤝 Contributing

This is a demonstration project. For production use:
1. Expand the wordlist significantly
2. Add input validation
3. Optimize grid calculations
4. Add error handling

## 📄 License

This project is for educational and demonstration purposes.

---

**Need help?** Make sure Python is installed and you're running the commands from the correct directory containing the `digipin_words.py` file.