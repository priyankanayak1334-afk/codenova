{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9a34b2ec-d9ef-48f4-bc29-5439f320b927",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import shutil\n",
    "\n",
    "# 1. Define the path of the messy folder you want to clean up\n",
    "# Example: \"C:/Users/YourName/Downloads/TestFolder\"\n",
    "SOURCE_DIR = r\"C:\\Users\\HP\\OneDrive\"\n",
    " \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d0733668-d210-4e25-a9a2-5da53ffc6c7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Map folder names to their respective file extensions\n",
    "EXTENSION_MAP = {\n",
    "    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],\n",
    "    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],\n",
    "    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],\n",
    "    'Music': ['.mp3', '.wav'],\n",
    "    'Archives': ['.zip', '.rar', '.tar']\n",
    "}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3a488a5e-a876-4b38-9680-8d7541f91f3d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Setup successful! Target directory is set to: C:\\Users\\HP\\OneDrive\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "\n",
    "# The 'r' before the quotes fixes the Windows backslash error completely\n",
    "SOURCE_DIR = r\"C:\\Users\\HP\\OneDrive\" \n",
    "\n",
    "# Map folder names to their respective file extensions\n",
    "EXTENSION_MAP = {\n",
    "    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],\n",
    "    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],\n",
    "    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],\n",
    "    'Music': ['.mp3', '.wav'],\n",
    "    'Archives': ['.zip', '.rar', '.tar']\n",
    "}\n",
    "\n",
    "print(\"Setup successful! Target directory is set to:\", SOURCE_DIR)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "373299b8-2eb9-41ea-bb3e-665d20212f04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Scanning folder...\n",
      "[SUCCESS] Moved: calculator.py -> Others/\n",
      "[SUCCESS] Moved: Getting started with OneDrive.pdf -> Documents/\n",
      "[SUCCESS] Moved: Personal Vault.lnk -> Others/\n",
      "[SUCCESS] Moved: v.docx -> Documents/\n",
      "[SUCCESS] Moved: Yashu nayak. R_20240629_222359_00002.docx -> Documents/\n",
      "\n",
      "Organization complete! Total files organized: 5\n"
     ]
    }
   ],
   "source": [
    "# Check if the directory actually exists\n",
    "if os.path.exists(SOURCE_DIR):\n",
    "    print(\"Scanning folder...\")\n",
    "    files_moved = 0\n",
    "    \n",
    "    # Loop through every item inside the folder\n",
    "    for filename in os.listdir(SOURCE_DIR):\n",
    "        file_path = os.path.join(SOURCE_DIR, filename)\n",
    "        \n",
    "        # --- NEW PROTECTION SAFETY CHECKS ---\n",
    "        # Skip hidden files, OneDrive system files, and desktop configuration files\n",
    "        if filename.startswith('.') or filename.startswith('$') or filename.lower() == 'desktop.ini':\n",
    "            continue\n",
    "            \n",
    "        # Make sure it's a file, not an already existing directory/folder\n",
    "        if os.path.isfile(file_path):\n",
    "            _, extension = os.path.splitext(filename)\n",
    "            extension = extension.lower()\n",
    "            \n",
    "            moved = False\n",
    "            \n",
    "            # Match the extension to our map\n",
    "            for folder_name, extensions in EXTENSION_MAP.items():\n",
    "                if extension in extensions:\n",
    "                    target_folder = os.path.join(SOURCE_DIR, folder_name)\n",
    "                    \n",
    "                    if not os.path.exists(target_folder):\n",
    "                        os.makedirs(target_folder)\n",
    "                    \n",
    "                    try:\n",
    "                        shutil.move(file_path, os.path.join(target_folder, filename))\n",
    "                        print(f\"[SUCCESS] Moved: {filename} -> {folder_name}/\")\n",
    "                        files_moved += 1\n",
    "                        moved = True\n",
    "                    except PermissionError:\n",
    "                        print(f\"[SKIPPED] Cannot access locked file: {filename}\")\n",
    "                    break\n",
    "            \n",
    "            # If it doesn't match any category, move it to 'Others'\n",
    "            if not moved:\n",
    "                other_folder = os.path.join(SOURCE_DIR, 'Others')\n",
    "                if not os.path.exists(other_folder):\n",
    "                    os.makedirs(other_folder)\n",
    "                \n",
    "                try:\n",
    "                    shutil.move(file_path, os.path.join(other_folder, filename))\n",
    "                    print(f\"[SUCCESS] Moved: {filename} -> Others/\")\n",
    "                    files_moved += 1\n",
    "                except PermissionError:\n",
    "                    print(f\"[SKIPPED] Cannot access locked file: {filename}\")\n",
    "                \n",
    "    print(f\"\\nOrganization complete! Total files organized: {files_moved}\")\n",
    "else:\n",
    "    print(\"[ERROR] The specified folder path does not exist. Please check your path spelling.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "834b7f7f-32fd-46ad-bd2e-cf8b210b741f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
