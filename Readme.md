# GitHub Repository Archiver

GitHub Repository Archiver is a Python-based GUI application that allows users to authenticate with their GitHub account, view their repositories, and download selected repositories as ZIP files.

## Features

- **GitHub Authentication**: Authenticate using a GitHub Personal Access Token.
- **Repository Listing**: Fetch and display all repositories associated with the authenticated account.
- **Multi-Selection**: Select multiple repositories to download.
- **Branch Downloads**: Download all branches of the selected repositories as ZIP files.
- **User-Friendly Interface**: Simple and intuitive GUI built with `tkinter`.

## Requirements

- Python 3.10 or higher
- The following Python libraries:
  - `tkinter` (comes pre-installed with Python)
  - `requests`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/git_archiver.git
   cd git_archiver
   ```

2. Install the required Python libraries:
   ```bash
   pip install requests
   ```

3. Run the application:
   ```bash
   python3 git_archiver.py
   ```

## Usage

1. **Start the Application**:
   - Run the script using the command `python3 git_archiver.py`.

2. **Authenticate**:
   - Click the "Login to GitHub" button.
   - Enter your GitHub Personal Access Token in the dialog box. You can create a token [here](https://github.com/settings/tokens).
   - It is Recommended to have the token access to repos (nothing more) and to delete it when done.

3. **Fetch Repositories**:
   - After successful authentication, your repositories will be displayed in a list.

4. **Select Repositories**:
   - Use the list to select one or more repositories.

5. **Download Repositories**:
   - Click the "Download Selected Repos" button.
   - Choose a directory where the repositories will be saved.
   - The application will download all branches of the selected repositories as ZIP files.

## Troubleshooting

- **FileNotFoundError**: Ensure the selected download directory exists and is writable.
- **Authentication Issues**: Verify that your Personal Access Token has the required permissions (e.g., `repo` scope for private repositories).
- **API Rate Limits**: If you encounter rate limits, ensure you are authenticated and not exceeding GitHub's API usage limits.

## Example Output

- Repositories will be saved as ZIP files in the format:
  ```
  <repository_name>_<branch_name>.zip
  ```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Built using the `tkinter` library for the GUI.
- Uses the GitHub REST API for repository and branch management.