# 📂 Python File Organizer

A simple and lightweight Python automation script that organizes files into categorized folders based on their file extensions. This project helps keep directories clean by automatically moving supported file types into their respective folders.

---

## ✨ Features

- 📄 Moves `.txt` files into a `text_files` folder
- 🖼️ Moves `.jpg` and `.png` files into an `images` folder
- 📁 Automatically creates folders if they don't exist
- ⚡ Fast and lightweight
- 🐍 Built using only Python's standard library (no external dependencies)

---

## 📁 Project Structure

```text
.
├── FileOrganizer.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## 📂 Example

### Before

```text
Downloads/
│
├── notes.txt
├── report.txt
├── vacation.jpg
├── cat.png
├── movie.mp4
├── music.mp3
└── archive.zip
```

### After

```text
Downloads/
│
├── text_files/
│   ├── notes.txt
│   └── report.txt
│
├── images/
│   ├── vacation.jpg
│   └── cat.png
│
├── movie.mp4
├── music.mp3
└── archive.zip
```

Only supported file types are moved. All other files remain unchanged.

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/shoykot31/python-file-organizer.git
```


### Navigate into the project

```bash
cd file-organizer
```

### Run the script

```bash
python FileOrganizer.py
```

Or import the function into another Python script:

```python
from FileOrganizer import organize_files

organize_files("C:/Users/YourName/Downloads")
```

---

## 🛠️ Built With

- Python 3
- os
- shutil

No third-party libraries are required.

---

## 📌 Supported File Types

| Extension | Destination Folder |
|-----------|--------------------|
| `.txt` | `text_files` |
| `.jpg` | `images` |
| `.png` | `images` |

---

## 💡 Future Improvements

- [ ] Support more file types (PDF, DOCX, MP4, MP3, ZIP, etc.)
- [ ] Recursive folder organization
- [ ] Command-line arguments
- [ ] GUI version using Tkinter or CustomTkinter
- [ ] Duplicate filename handling
- [ ] Undo functionality
- [ ] Logging and activity reports
- [ ] Configuration file for custom categories

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the **Beerware License**.

> "If we meet someday and you think this software was useful, you can buy me a beer."

See the `LICENSE` file for details.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates future improvements.

---

## 👨‍💻 Author

**Al Shahariar Mahmud Shoykot**

GitHub: https://github.com/shoykot31

---

Made with ❤️ using Python.
