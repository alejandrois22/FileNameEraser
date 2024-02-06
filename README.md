# FileNameEraser
# Overview
FileNameEraser is a powerful and intuitive file renaming tool that allows users to remove specific strings from filenames within a directory and all of its subdirectories. It is designed to support a wide range of file management tasks from organizing digital libraries to preparing data for analysis.

# Features
Recursive renaming: Process files in selected directory and all subdirectories.
Pattern matching: Remove exact text or use wildcards for broader matches.
User-friendly: Simple interface and straightforward functionality.
Versatile: Suitable for photographers, developers, and general file organization.
Installation
Download the latest version from the releases page and run the installer. Requires Python to be installed on your system.

# Usage
To use FileNameEraser, simply specify the directory path and the text pattern you wish to remove from the filenames. The tool will then recursively rename all affected files.

# FAQ
Q: I received a "FileNotFoundError" when trying to run the script. How can I resolve this?
A: Ensure that the path provided is correct and accessible. This error often occurs when the path is misspelled, the drive is disconnected, or the permissions are not set correctly.

Q: The script did not rename any files, and there was no output. What might be the issue?
A: This can happen if the specified text to remove is not found in any filenames. Check the exact text string you're trying to remove and ensure it matches the filenames' text.

Q: I noticed that the script added an extra space at the end of filenames. How can I prevent this?
A: The latest version of FileNameEraser includes a fix for this issue. Make sure you're using the most recent release. The script now trims any whitespace at the end of filenames before saving changes.
