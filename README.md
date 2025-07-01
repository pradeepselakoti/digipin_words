# DIGIPIN - 3 Words Geocoding System

A geocoding system inspired by What3Words that converts latitude/longitude coordinates to memorable 3-word combinations for locations within India.

## 🌟 What is DIGIPIN?

DIGIPIN divides India into a 3-meter grid system where each location can be represented by exactly 3 words - **ANY words you choose!** This makes it easy to share precise locations using simple, memorable words instead of complex coordinates.

**Examples:**
- Coordinates: `22.3215616, 70.7657728`
- Auto-generated: `geo1a2b loc3c4d pos5e6f`
- Custom words: `pizza chair happy`
- Your choice: `monday coffee laptop`

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

### 1. Convert Coordinates to Auto-Generated Words

```bash
python digipin_words.py encode --lat 22.3215616 --lon 70.7657728
```

**Output:**
```
✅ 3 Words for (22.3215616, 70.7657728): geo1a2b loc3c4d pos5e6f
```

### 2. Convert Words Back to Coordinates

```bash
python digipin_words.py decode --w1 geo1a2b --w2 loc3c4d --w3 pos5e6f
```

**Output:**
```
✅ Coordinates for (geo1a2b, loc3c4d, pos5e6f): (22.321562, 70.765773)
```

### 3. Use ANY Custom Words (NEW!)

```bash
python digipin_words.py custom --w1 pizza --w2 chair --w3 happy
```

**Output:**
```
✅ Your custom words 'pizza chair happy' map to:
   Coordinates: (19.234567, 73.456789)

💡 To use these words consistently, always use the same spelling and order!
```

### 4. Assign Your Own Words to a Location

```bash
python digipin_words.py encode --lat 22.32156 --lon 70.76577 --w1 birthday --w2 party --w3 home
```

This will check if your custom words map close to your coordinates!

## 🔧 Command Reference

### Auto-Generated Words (Coordinates → Words)
```bash
python digipin_words.py encode --lat [LATITUDE] --lon [LONGITUDE]
```

### Custom Words (Coordinates → Your Words)
```bash
python digipin_words.py encode --lat [LATITUDE] --lon [LONGITUDE] --w1 [WORD1] --w2 [WORD2] --w3 [WORD3]
```

### Decoding (Words → Coordinates)
```bash
python digipin_words.py decode --w1 [WORD1] --w2 [WORD2] --w3 [WORD3]
```

### Any Words to Location
```bash
python digipin_words.py custom --w1 [ANY_WORD1] --w2 [ANY_WORD2] --w3 [ANY_WORD3]
```

**Parameters:**
- `--lat`: Latitude (decimal degrees, e.g., 22.3215616)
- `--lon`: Longitude (decimal degrees, e.g., 70.7657728)
- `--w1`, `--w2`, `--w3`: Any words you want to use

## 📋 Examples

### Example 1: Auto-Generated Words
```bash
# Generate words automatically
python digipin_words.py encode --lat 19.0760 --lon 72.8777
# Output: geo4f3a loc8b2c pos9d1e

# Decode back to coordinates
python digipin_words.py decode --w1 geo4f3a --w2 loc8b2c --w3 pos9d1e
```

### Example 2: Use Your Own Memorable Words
```bash
# Use any words you like
python digipin_words.py custom --w1 coffee --w2 laptop --w3 monday
# Output: Maps to some coordinates in India

# Always gets the same location
python digipin_words.py custom --w1 coffee --w2 laptop --w3 monday
```

### Example 3: Assign Custom Words to Specific Location
```bash
# Assign your words to your home coordinates
python digipin_words.py encode --lat 28.6139 --lon 77.2090 --w1 home --w2 sweet --w3 family

# Use different words for your office
python digipin_words.py custom --w1 office --w2 work --w3 delhi
```

### Example 4: Fun with Any Words
```bash
# Use absolutely any words
python digipin_words.py custom --w1 pizza --w2 unicorn --w3 rainbow
python digipin_words.py custom --w1 birthday --w2 party --w3 celebration
python digipin_words.py custom --w1 mountain --w2 river --w3 forest
```

## 🗺️ Coverage Area

- **Country:** India
- **Latitude Range:** 6.0° to 38.0°
- **Longitude Range:** 68.0° to 97.0°
- **Precision:** 3-meter grid squares

## 📚 How It Works

The system now supports **unlimited flexibility**:

### Auto-Generated Words
- System creates deterministic words like `geo1a2b loc3c4d pos5e6f`
- Same location always gets same auto-generated words
- Perfect for technical use

### Custom Words (ANY words!)
- **Use ANY words**: `pizza chair happy`, `coffee laptop monday`, `birthday party home`
- Words are converted to numbers using cryptographic hashing
- Same 3 words always map to the same location
- **Remember**: Spelling and order matter!

### Word Rules
- ✅ Any English words work: `apple`, `celebration`, `mountain`
- ✅ Numbers work too: `123`, `456`, `789`
- ✅ Mixed: `home2024`, `office`, `monday`
- ⚠️ **Important**: Same words = same location, different spelling = different location

## ❓ Troubleshooting

### "Python is not recognized"
- Make sure Python is installed: Download from [python.org](https://python.org)
- Add Python to your system PATH during installation

### Words don't map to expected location
- **Remember**: Same words always map to same place
- Check spelling carefully (`home` ≠ `Home` ≠ `home123`)
- Word order matters (`pizza chair happy` ≠ `happy chair pizza`)

### Invalid coordinates
- Make sure coordinates are within India (Lat: 6-38°, Lon: 68-97°)
- Use decimal format (22.3215616, not 22°19'17.6"N)

### Getting Help
```bash
python digipin_words.py --help
python digipin_words.py encode --help
python digipin_words.py custom --help
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
