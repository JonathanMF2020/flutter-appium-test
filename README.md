# Automated Testing Project with Appium

This project contains a set of automated tests for a Flutter application using **Appium**. The main goal is to validate the application's functionality through functional and integration tests.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Running Tests](#running-tests)
- [Next Steps](#next-steps)

---

## Prerequisites

Before running the tests, make sure you have the following prerequisites installed:

1. **Python 3.10+**: [Download Python](https://www.python.org/downloads/)
2. **Appium Server**: [Install Appium](https://appium.io/)
3. **Node.js**: Required to run the Appium Server.
4. **Android SDK**: For testing on Android devices/emulators.
5. **Flutter**: [Install Flutter](https://flutter.dev/docs/get-started/install)
6. **Project Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

The project is organized as follows:

```
appium_test/
├── android/                      # Android project generated by Flutter
│   ├── build.gradle
│   ├── gradlew
│   ├── app/
│   │   ├── build.gradle
│   │   └── src/
│   └── gradle/
│       └── wrapper/
├── lib/                          # Main Flutter source code
│   └── main.dart
├── appium_project/               # Appium-related code
│   ├── config/                   # Appium configuration
│   │   └── flutter_appium_config.json
│   ├── locators/                 # Element locators
│   │   └── flutter_locators.py
│   ├── tests/                    # Automated tests
│   │   └── test_increment.py
│   ├── utils/                    # Utilities and helpers
│   │   ├── driver_manager.py
│   │   └── element_helpers.py
│   └── run.py                    # Script to run tests
├── .env                          # Environment variables
├── .env.example                  # Example environment variable configuration
├── requirements.txt              # Project dependencies
└── README.md
```

## Environment Setup

1. Configure the .env file: Create a .env file in the project root based on the .env.example file. This file should contain the path to the Appium configuration file.

Example:

```bash
    CONFIG_PATH=P:\Proyectos\AppiumTesst\appium_test\appium_project\config\flutter_appium_config.json
```

2. Appium Configuration File: The flutter_appium_config.json file contains the capabilities required to run the tests. Example:

```json
{
  "appium:platformName": "Android",
  "appium:automationName": "Flutter",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.example.appium_test",
  "appium:app": "P:\\Proyectos\\AppiumTesst\\appium_test\\build\\app\\outputs\\apk\\debug\\app-debug.apk"
}
```

3. Install dependencies: Run the following command to install the required dependencies:

```bash
    pip install -r requirements.txt
```

## Running Tests

1. Start the Appium server: Ensure the Appium server is running:

```bash
    appium
```

2. Run all tests: Use the run.py script to execute all tests:

```bash
    python appium_project/run.py
```

3. Run specific tests: You can run a specific test file using pytest:

```bash
    pytest appium_project/tests/test_increment.py
```

4. Generate reports: To generate an HTML report:

```bash
    pytest --html=report.html
```

## Next Steps

Below are the next steps to improve and expand the project's scope:

1. **Add iOS Support**:

   - Configure the necessary capabilities to run tests on iOS devices/emulators.
   - Update the `flutter_appium_config.json` file to include iOS-specific capabilities.
   - Test compatibility with physical devices and iOS simulators.
   - Document the steps required to set up the development environment on macOS.

2. **Add Web Support**:

   - Integrate Selenium WebDriver for browser testing.
   - Create a separate configuration file for browser capabilities (Chrome, Firefox, etc.).
   - Implement specific tests for the web version of the application.
   - Document how to run tests in browsers and set up the environment.

3. **Add Support for Other Platforms**:
   - Explore the possibility of adding support for additional platforms, such as Windows or macOS.
   - Configure platform-specific capabilities.
   - Test compatibility and document the steps required to set up the environment.

These steps will make the project more versatile and cover a wider variety of use cases. If you have additional ideas or want to contribute, feel free to open an issue or submit a pull request.
