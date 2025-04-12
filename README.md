# Proyecto de Pruebas Automatizadas con Appium

Este proyecto contiene un conjunto de pruebas automatizadas para una aplicación Flutter utilizando **Appium**. El objetivo principal es validar la funcionalidad de la aplicación mediante pruebas funcionales y de integración.

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración del Entorno](#configuración-del-entorno)
- [Ejecución de las Pruebas](#ejecución-de-las-pruebas)
- [Detalles de las Pruebas](#detalles-de-las-pruebas)
- [Buenas Prácticas](#buenas-prácticas)
- [Contribuciones](#contribuciones)

---

## Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener los siguientes requisitos instalados:

1. **Python 3.10+**: [Descargar Python](https://www.python.org/downloads/)
2. **Appium Server**: [Instalar Appium](https://appium.io/)
3. **Node.js**: Necesario para ejecutar Appium Server.
4. **Android SDK**: Para pruebas en dispositivos/emuladores Android.
5. **Flutter**: [Instalar Flutter](https://flutter.dev/docs/get-started/install)
6. **Dependencias del Proyecto**:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
appium_test/
├── android/                      # Proyecto Android generado por Flutter
│   ├── build.gradle
│   ├── gradlew
│   ├── app/
│   │   ├── build.gradle
│   │   └── src/
│   └── gradle/
│       └── wrapper/
├── lib/                          # Código fuente principal de Flutter
│   └── main.dart
├── appium_project/               # Código relacionado con Appium
│   ├── config/                   # Configuración de Appium
│   │   └── flutter_appium_config.json
│   ├── locators/                 # Localizadores de elementos
│   │   └── flutter_locators.py
│   ├── tests/                    # Pruebas automatizadas
│   │   └── test_increment.py
│   ├── utils/                    # Utilidades y helpers
│   │   ├── driver_manager.py
│   │   └── element_helpers.py
│   └── run.py                    # Script para ejecutar las pruebas
├── .env                          # Variables de entorno
├── .env.example                  # Ejemplo de configuración de variables de entorno
├── requirements.txt              # Dependencias del proyecto
└── [README.md](http://_vscodecontentref_/0)
```

## Configuración del Entorno

1. Configurar el archivo .env: Crea un archivo .env en la raíz del proyecto basado en el archivo .env.example. Este archivo debe contener la ruta al archivo de configuración de Appium.

Ejemplo:

```bash
   CONFIG_PATH=P:\Proyectos\AppiumTesst\appium_test\appium_project\config\flutter_appium_config.json
```

2. Archivo de Configuración de Appium: El archivo flutter_appium_config.json contiene las capacidades necesarias para ejecutar las pruebas. Ejemplo:

```json
{
  "appium:platformName": "Android",
  "appium:automationName": "Flutter",
  "appium:deviceName": "emulator-5554",
  "appium:appPackage": "com.example.appium_test",
  "appium:app": "P:\\Proyectos\\AppiumTesst\\appium_test\\build\\app\\outputs\\apk\\debug\\app-debug.apk"
}
```

3. Instalar las dependencias: Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
   pip install -r requirements.txt
```

## Ejecución de pruebas

1. Iniciar el servidor de Appium: Asegúrate de que el servidor de Appium esté corriendo:

```bash
   appium
```

2. Ejecutar todas las pruebas: Usa el script run.py para ejecutar todas las pruebas:

```bash
   python appium_project/run.py
```

3. Ejecutar pruebas específicas: Puedes ejecutar un archivo de prueba específico con pytest:

```bash
   pytest appium_project/tests/test_increment.py
```

4. Generar reportes: Para generar un reporte en HTML:

```bash
   pytest --html=report.html
```

## Siguientes Pasos

A continuación, se describen los próximos pasos para mejorar y ampliar el alcance del proyecto:

1. **Dar soporte para iOS**:

   - Configurar las capacidades necesarias para ejecutar pruebas en dispositivos/emuladores iOS.
   - Actualizar el archivo de configuración `flutter_appium_config.json` para incluir capacidades específicas de iOS.
   - Probar la compatibilidad con dispositivos físicos y simuladores iOS.
   - Documentar los pasos necesarios para configurar el entorno de desarrollo en macOS.

2. **Dar soporte para Web**:

   - Integrar Selenium WebDriver para pruebas en navegadores web.
   - Crear un archivo de configuración separado para capacidades de navegador (Chrome, Firefox, etc.).
   - Implementar pruebas específicas para la versión web de la aplicación.
   - Documentar cómo ejecutar pruebas en navegadores y cómo configurar el entorno.

3. **Dar soporte para otras plataformas**:
   - Explorar la posibilidad de agregar soporte para plataformas adicionales, como Windows o macOS.
   - Configurar capacidades específicas para estas plataformas.
   - Probar la compatibilidad y documentar los pasos necesarios para configurar el entorno.

Estos pasos permitirán que el proyecto sea más versátil y pueda cubrir una mayor variedad de casos de uso. Si tienes ideas adicionales o deseas contribuir, no dudes en abrir un issue o enviar un pull request.
