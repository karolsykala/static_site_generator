# WORK IN PROGRESS
# 🛠️ Static Site Generator 

This repository contains a **Static Site Generator (SSG)** developed to convert plain text files into a structured, static website. The project is implemented using **Python**, with supplementary **HTML**, **CSS**, and **Shell** scripts to facilitate the generation and testing of the static site.

## 📂 Project Structure

- `src/`: Contains the main Python scripts responsible for parsing input files and generating HTML output.
- `public/`: The output directory where the generated static site files are stored.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `main.sh`: A shell script to execute the static site generation process.
- `test.sh`: A shell script containing tests to ensure the generator functions as expected.

## 🛠️ Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/karolsykala/static_site_generator.git
   cd static_site_generator
   ```

2. **Ensure Python is Installed**:
   The generator is built with Python, so ensure you have Python installed on your system.

## 🚀 Usage

1. **Prepare Your Content**:
   Place your plain text or markdown files in a designated input directory.

2. **Generate the Static Site**:
   Execute the `main.sh` script to run the Python generator:
   ```sh
   ./main.sh
   ```
   This will process the input files and output the generated HTML files into the `public/` directory.

3. **View the Site**:
   Open the HTML files located in the `public/` directory in your preferred web browser to view the generated static site.

## 🧪 Testing

To run the test suite and ensure all components are functioning correctly, execute:
```sh
./test.sh
```
This script will run predefined tests and output the results to the console.

