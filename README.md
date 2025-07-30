# 📚 Open Source Islamic Projects (from Awesome-Muslims)

# Table of Contents

- [Prayer Times](#prayer-times)
- [Quran](#quran)
- [Other](#other)
- [Islamic Calendar](#islamic-calendar)
- [Hadith](#hadith)
- [Azkar & Dua](#azkar--dua)
    
## **Prayer Times**

### **JavaScript**

* [**Openadhan**](https://github.com/adelpro/Openadhan) – ⭐ 8  
  *Deployment:* Web application (React PWA)  
  *Description:* Web app for calculating Muslim prayer times using local (auto-detected) position or manual city search.  
  *Features:*  
  * Automatic location detection for prayer times, with option to search and set location manually.  
  * PWA with offline support and a multilingual interface (English/Arabic), including configurable settings and Adhan notifications.  
* [**next-salat**](https://github.com/ayoubsousali/next-salat) – ⭐ 4  
  *Deployment:* Web application  
  *Description:* Prayer times web app focused on Morocco (by city, according to official ministry timings).  
  *Features:*  
  * Provides daily prayer schedules for cities across Morocco based on the Ministry of Islamic Affairs’ official timetable.  
  * Simple interface to select cities and view precise prayer timings, with responsive design for accessibility.  
* [**salati**](https://github.com/slimaneakalie/salati) – ⭐ 3  
  *Deployment:* Browser extension (Google Chrome)  
  *Description:* Muslim prayer time extension for Google Chrome.  
  *Features:*  
  * Displays upcoming prayer times in the browser and sends notifications at prayer times, including playing Adhan audio.  
  * Offers user configuration (location, calculation method, notification preferences) and even optional actions like muting audio or closing tabs during prayers for focus.  
* [**prayer-times-mosque-finder**](https://github.com/jadmadi/prayer-times-mosque-finder) – ⭐ 1  
  *Deployment:* Web application  
  *Description:* A web app that provides prayer times and locates nearby mosques using OpenStreetMap data.  
  *Features:*  
  * Determines local prayer times based on the user’s GPS location and displays the full daily schedule.  
  * Interactive map integration to find the nearest mosques, with markers and directions using OpenStreetMap.

### **C\#**

* [**Adhan-csharp**](https://github.com/davidpet86/Adhan-csharp) – ⭐ 17  
  *Deployment:* .NET Library (NuGet package)  
  *Description:* High precision Islamic prayer time calculation library for C\#.  
  *Features:*  
  * Calculates five daily prayer times with high accuracy, supporting multiple calculation methods (MWL, ISNA, etc.), juristic adjustments (Hanafi/Shafi’i for Asr), and custom offsets.  
  * Easy to integrate into .NET applications with a simple API, allowing developers to get prayer times and related data (like sunrise) without external dependencies.

### **Swift**

* [**adhan-swift**](https://github.com/batoulapps/adhan-swift) – ⭐ 198  
  *Deployment:* iOS Library (Swift Package)  
  *Description:* High precision Islamic prayer time library for Swift.  
  *Features:*  
  * Provides precise prayer times for any location with support for numerous calculation conventions and parameters (angles, high-latitude adjustments, etc.).  
  * Includes Qibla direction calculation and is well-tested and documented, compatible with Swift and Objective-C for use in iOS apps and watchOS complications.  
* [**PrayerTimes-Swift**](https://github.com/ashikahmad/PrayerTimes-Swift) – ⭐ 61  
  *Deployment:* iOS Library (Swift)  
  *Description:* Islamic prayer time calculation code in Swift (converted from the PrayTimes.org algorithms).  
  *Features:*  
  * Calculates prayer times for any given date and location, supporting various official calculation methods and Asr juristic rules (Hanafi/Shafi’i) as well as high latitude adjustments.  
  * Simple integration into Swift projects – just import the class and get daily prayer times formatted as needed, with ability to set output time format (12/24h).

### **Dart**

* [**flutter\_qiblah**](https://github.com/medyas/flutter_qiblah) – ⭐ 144  
  *Deployment:* Flutter plugin (Android/iOS)  
  *Description:* Flutter plugin to display Qiblah (prayer direction) in apps, supporting both Android and iOS.  
  *Features:*  
  * Provides a Qibla compass widget that uses device sensors to calculate the direction of Makkah relative to current location in real time.  
  * Handles sensor availability and permissions: checks for device support, requests location access, ensures GPS is enabled, and then delivers accurate Qibla bearing with a smooth compass UI.  
* [**adhan-dart**](https://github.com/iamriajul/adhan-dart) – ⭐ 100  
  *Deployment:* Dart/Flutter Library  
  *Description:* Adhan for Dart – Muslim prayer times library, making retrieval of prayer times in Dart easier than ever.  
  *Features:*  
  * High precision prayer time calculations with well-tested astronomical algorithms (ported from Batoul Apps’ Adhan libraries), working across all Dart platforms (Flutter mobile/web, server, etc.) without external dependencies.  
  * Supports all major calculation methods, madhab adjustments, and even includes convenience functions (like time until next prayer). It’s well-documented for easy use in Flutter apps (even includes an example with dynamic GPS location input).  
* [**prayer-times**](https://github.com/flutterturkey/prayer-times) – ⭐ 45  
  *Deployment:* Mobile app (Flutter)  
  *Description:* A simple Flutter application for displaying prayer times (Turkish example project).  
  *Features:*  
  * Shows daily prayer times for a chosen location, using data from a reliable source (e.g., Turkey’s Diyanet API) with an easy-to-read UI.  
  * Includes features such as prayer countdowns and location selection, demonstrating a practical Flutter implementation of a prayer timetable with potential for notifications.  
* [**simply\_qibla**](https://github.com/TowardsIkhlaas/simply_qibla) – ⭐ 21  
  *Deployment:* Mobile app (Android, Flutter)  
  *Description:* Minimalist, accurate, and privacy-focused Qibla direction app. (Download available via provided link)  
  *Features:*  
  * Highly accurate Qibla compass that works offline, using device sensors and location to point exactly towards the Kaaba without requiring any tracking or internet access.  
  * Privacy and simplicity are central: no ads or unnecessary permissions, just a clean interface showing the compass and distance to Makkah, making it fast and lightweight.

### **Kotlin**

* [**Prayer-Times-Android-Azan**](https://github.com/ahmedeltaher/Prayer-Times-Android-Azan) – ⭐ 373  
  *Deployment:* Android Library (Kotlin)  
  *Description:* A library aimed to calculate Muslim prayer times in Android apps with one line of code (no more headache implementing from scratch).  
  *Features:*  
  * Easy integration: developers can get prayer times by simply initializing the library with location and calling a function – the library handles all complex astronomical calculations internally (sun angles, timezone, DST, etc.).  
  * Supports multiple calculation methods and includes Azan time computation along with convenience functions (like retrieving times for all prayers, Imsak, etc.), all written in Kotlin for modern Android development.  
* [**prayer-times-android**](https://github.com/metinkale38/prayer-times-android) – ⭐ 256  
  *Deployment:* Android app  
  *Description:* A comprehensive prayer times application (Namaz Vakti) with a set of tools needed by every Muslim.  
  *Features:*  
  * **Worldwide Prayer Times:** Offers prayer schedules globally with multiple source options (calculations or official calendars like Diyanet, IGMG, etc.), automatic location detection, Adhan audio at prayer times, and notifications (including early warnings and silent mode toggling during prayers).  
  * **All-in-One Toolkit:** Beyond prayer times, the app includes Qibla compass (with 2D, 3D, and map views), a widget and notification display, Islamic calendar with religious holidays, 99 Names of Allah, morning/evening Azkar, prayer habit trackers (missed prayer counter), a dhikr (tasbeeh) counter, hadith collections (Sahih Bukhari), and more – all in one lightweight app.  
* [**adhan-kotlin**](https://github.com/batoulapps/adhan-kotlin) – ⭐ 177  
  *Deployment:* Multiplatform Library (Kotlin)  
  *Description:* High precision Islamic prayer time library (Adhan) for Java/Kotlin.  
  *Features:*  
  * Written in Kotlin Multiplatform, allowing it to run on JVM (Android/Java) and possibly other platforms, it computes accurate prayer times with the same reliability as Batoul Apps’ Adhan libraries in other languages.  
  * Well-documented and tested, it supports various prayer time calculation methods and parameters, making it easy to get correct prayer times and even Qibla direction with minimal code in Android or Kotlin-based applications.  
* [**PrayerWatchFace**](https://github.com/3llomi/PrayerWatchFace) – ⭐ 13  
  *Deployment:* Wear OS Watch Face (Android Wear)  
  *Description:* A smartwatch watchface that displays prayer times.  
  *Features:*  
  * Custom watch face that elegantly shows the upcoming prayer name and time (and possibly the time remaining) directly on the smartwatch, keeping users informed at a glance.  
  * Synchronizes with phone or internal calculations for location-based prayer times, updating automatically throughout the day, and includes support for ambient mode so the prayer info is visible even in low-power display mode.

### **Python**

* [**adhanpy**](https://github.com/alphahm/adhanpy) – ⭐ 29  
  *Deployment:* Python library  
  *Description:* An offline prayer times library in Python.  
  *Features:*  
  * Calculates daily prayer times locally without any internet connection, using proven algorithms (likely based on PrayTimes or Adhan) for accuracy.  
  * Simple API that allows specifying location and method, returning all prayer times; useful for building Python applications or scripts that need prayer timings (e.g., integrating into Raspberry Pi projects or backend services).

### **PHP**

* [**api.aladhan.com**](https://github.com/islamic-network/api.aladhan.com) – ⭐ 141  
  *Deployment:* Web API (self-hosted service)  
  *Description:* The backend powering the AlAdhan API – a global prayer times API service.  
  *Features:*  
  * Provides a RESTful API that returns prayer times for any location (by city or coordinates) for a given date, with support for different calculation methods and Madhab settings.  
  * Additional functionality includes endpoints for Qibla direction calculation and Hijri-Gregorian date conversion, making it a comprehensive public API for Islamic date/times data (widely used in many apps and websites).

### **C**

* [**next-prayer**](https://github.com/AbdeltwabMF/next-prayer) – ⭐ 54  
  *Deployment:* CLI tool (Linux)  
  *Description:* Islamic prayer time reminder for Unix-like status bars (terminal utility).  
  *Features:*  
  * Lightweight command-line program that outputs prayer time information (e.g., next prayer name/time, time left, or all prayer times for the day), which can be easily integrated into status bars for window managers (i3blocks, dwm, polybar, etc.).  
  * Works offline by fetching or calculating prayer times and includes flexible output options (previous prayer, next prayer, countdown, Hijri date). It can be installed via package managers (like AUR for Arch) or run in a Docker container for convenience.

### **Java**

* [**PrayerTimes**](https://github.com/HouariZegai/PrayerTimes) – ⭐ 180  
  *Deployment:* Desktop application (Java FX)  
  *Description:* Desktop app for calculating Muslim prayer times 🕌 and setting an alarm (Adhan) ⏰ for those times.  
  *Features:*  
  * Built-in database of prayer times for all cities in Algeria (users can simply select their city to get accurate local prayer timings without internet). It remembers user settings like chosen city and preferred Adhan sound.  
  * Runs in the system tray for convenience: it can hide/minimize to tray and then play Adhan alarms at prayer times. The interface is simple to use and offers a settings page to customize Adhan alerts and other options.

### **TypeScript**

* [**adhan-js**](https://github.com/batoulapps/adhan-js) – ⭐ 442  
  *Deployment:* JavaScript/TypeScript Library (NPM)  
  *Description:* High precision Islamic prayer time library for JavaScript.  
  *Features:*  
  * Computes prayer times in the browser or Node.js with excellent accuracy, mirroring the well-tested algorithms from Batoul Apps (also available in Swift/Kotlin). Developers can easily get today’s prayer times for a location with a few lines of code, with support for all major calculation methods and adjustments.  
  * Also provides additional utility like Qibla direction calculation given coordinates. It’s lightweight and dependency-free, making it ideal for web apps, extensions, or server-side use where prayer timing functionality is needed.  
* [**prayer-times-extension**](https://github.com/mohamedmansour/prayer-times-extension) – ⭐ 65  
  *Deployment:* Browser Extension (Chrome/Firefox)  
  *Description:* **Under Development:** Prayer time calculation based on geolocation for Chromium and Firefox browsers.  
  *Features:*  
  * Automatically detects your location and displays the daily prayer timetable directly in the browser (e.g., in a popup or new tab), so users can quickly check prayer times without a separate app.  
  * Intended to work cross-browser (Chrome and Firefox) and likely includes configurable calculation methods and notifications for upcoming prayers once fully developed.  
* [**adhan-time**](https://github.com/mzaien/adhan-time) – ⭐ 3  
  *Deployment:* Raycast extension (macOS)  
  *Description:* Adhan Time extension for Raycast (a macOS productivity tool).  
  *Features:*  
  * Allows Mac users to quickly view upcoming prayer times or the next prayer directly through Raycast’s command interface, integrating prayer reminders into their desktop workflow.  
  * Likely includes the ability to see time remaining for the next prayer and possibly notification support or invocation via a simple keyboard shortcut, all without opening a separate app.

### **CSS**

* [**TimeForSalahWebsite**](https://github.com/buildwithmalik/TimeForSalahWebsite) – ⭐ 13  
  *Deployment:* Website (static JavaScript app)  
  *Description:* A Muslim Prayer Timing website built with pure JavaScript (no frameworks). *(As of June 2020, it had 300+ estimated visits.)*  
  *Features:*  
  * Standalone web page that provides daily prayer times, likely using browser geolocation or a user-selected location to display the five prayer times.  
  * Implemented in vanilla JS and CSS, it demonstrates a lightweight approach to showing prayer schedules, possibly including a simple UI/clock and requiring no backend – all calculations are done on the client side for a fast experience.

### **Vue**

* [**salat-vue**](https://github.com/elattariyassine/salat-vue) – ⭐ 15  
  *Deployment:* Web application (Vue.js)  
  *Description:* Prayer time web app built with Vue.js.  
  *Features:*  
  * Modern Vue.js frontend that shows prayer times for the user’s location (or selected city) with a clean, reactive UI and possibly dynamic features like countdown to next prayer.  
  * Likely supports worldwide locations and different calculation presets, and being a Vue PWA, it may also work offline or send notifications. It comes with a live preview link, indicating a deployed version for users to try out.

## **Quran**

### **Kotlin**

* [**quran\_android**](https://github.com/quran/quran_android) – ⭐ 2187  
  *Deployment:* Android app  
  *Description:* The official Quran reading application for Android (open source Quran.com app).  
  *Features:*  
  * **High-Quality Quran Text:** Displays the Quran in the original Uthmani script with crystal-clear Madani compliant images, plus support for zooming and smooth page transitions for an intuitive reading experience.  
  * **Audio and Bookmarking:** Offers gapless audio playback from a wide selection of reciters, with features like ayah-by-ayah audio, bookmarks and tags for verses, note-taking, and sharing of ayat. It also includes translations, search functionality, night mode, and more, making it one of the most feature-rich Quran apps.  
* [**AlQuran-Android**](https://github.com/AzharRivaldi/AlQuran-Android) – ⭐ 48  
  *Deployment:* Android app  
  *Description:* Source code for a tutorial Quran application on Android.  
  *Features:*  
  * Allows reading the entire Quran text in Arabic with a user-friendly interface, including basic navigation by surah or juz.  
  * Includes features like translation (in Indonesian, given the author/audience) and simple audio playback or bookmarks, intended as a learning example for building Quran apps.  
* [**AyatuRabbi\_Quran**](https://github.com/3llomi/AyatuRabbi_Quran) – ⭐ 17  
  *Deployment:* Android app  
  *Description:* *Ayatu Rabbi – The easiest app to read the Holy Quran.*  
  *Features:*  
  * Provides a very straightforward Quran reading experience, focusing on clarity and ease for the user (perhaps larger text, simple controls to jump to surahs/ajza).  
  * Likely includes bookmarking or last-read position memory, and possibly a night mode or adjustable text for comfortable reading, aiming to be lightweight and accessible.  
* [**Al-Quran**](https://github.com/thefaisalurrehman/Al-Quran) – ⭐ 3  
  *Deployment:* Android app  
  *Description:* Al Quran is a 100% Free and Open Source app without any ads or tracking – a simple text-based Quran app for Android.  
  *Features:*  
  * Fully offline Quran text for reading, with no frills – the focus is on simplicity and low size, making it very fast and accessible even on older devices.  
  * Features basic navigation (surah list, jump to verse) and possibly bookmarks. No advertisements or permissions required, providing a distraction-free experience.

### **Perl**

* [**quran.com-images**](https://github.com/quran/quran.com-images) – ⭐ 448  
  *Deployment:* Asset repository / Generation scripts  
  *Description:* A repository of Quran text images generated using fonts from the King Fahd Quran Complex (qurancomplex.org).  
  *Features:*  
  * Contains high-quality images for each page (or verse) of the Quran using the authentic calligraphy and layout from the Madinah Mushaf, which can be used in apps or websites for crystal-clear Quranic text display.  
  * May include scripts or tools to regenerate these images using the provided fonts, enabling developers to produce new images (for different resolutions or styles) while maintaining the original calligraphic style.

### **Swift**

* [**quran-ios**](https://github.com/quran/quran-ios) – ⭐ 505  
  *Deployment:* iOS app (core engine)  
  *Description:* QuranEngine – the engine powering the Quran.com iOS app.  
  *Features:*  
  * Provides the core functionality for the Quran iOS app, including efficient retrieval of verses, navigation by surah/ayah, and management of Quran text and audio resources on device.  
  * Supports advanced features such as search, bookmarking, highlighting verses, and synchronization of user data. It likely also interfaces with audio playback and translation databases, serving as the backbone so the iOS app UI can be built on top of it.

### **Java**

* [**QuranyApp**](https://github.com/MahmoudMabrok/QuranyApp) – ⭐ 213  
  *Deployment:* Android app  
  *Description:* An open source Holy Quran app providing features to Read, Listen, view Tafseer, and even Test knowledge – all in a very small app size.  
  *Features:*  
  * **Read & Listen:** Users can read the Quran text and listen to recitations. The app likely offers multiple reciters and the ability to stream or download audio for offline use, all while keeping the app lightweight.  
  * **Tafseer & Quizzes:** Includes Quran tafsir (explanation/translation) for deeper understanding, and a quiz or test feature to help users memorize verses or test their knowledge of Quranic content, making it an interactive learning tool.  
* [**QuranOnAndroid**](https://github.com/hussien89aa/QuranOnAndroid) – ⭐ 122  
  *Deployment:* Android app  
  *Description:* Listen to Quran online – a free open source project for Quran audio.  
  *Features:*  
  * Focuses on audio streaming of Quran recitations: users can select surahs and choose from available reciters to stream Quran audio on their device.  
  * Likely includes basic playback controls (play/pause, next ayah/surah) and may show the text of the current verse being recited. It’s designed to be a simple way to listen to the Quran anywhere with an internet connection.  
* [**quranVerses**](https://github.com/bullheadandplato/quranVerses) – ⭐ 19  
  *Deployment:* Android library / sample  
  *Description:* Displays random Quran verses in an Android app.  
  *Features:*  
  * Provides functionality to fetch or select a random ayah (verse) from the Quran, which can be used for “Verse of the Day” features. It likely includes an internal Quran text database to draw from.  
  * Easy to integrate into apps: with minimal code, developers can show a random Quranic verse (perhaps along with its translation) on demand or at app launch, to inspire users.

### **Dart**

* [**the-holy-quran-app**](https://github.com/mhmzdev/the-holy-quran-app) – ⭐ 851  
  *Deployment:* Cross-platform app (Flutter)  
  *Description:* Holy Qur’an application developed with Flutter.  
  *Features:*  
  * **Multiplatform Experience:** A beautifully designed Quran app for Android and iOS (and possibly web) with Flutter, offering the full Quran text with smooth page scrolling or flipping and multi-language support for translations.  
  * **Rich Functionality:** Likely includes features such as search, bookmarks, favorite verses, and audio playback of recitations. The UI takes advantage of Flutter’s widgets to provide a modern, interactive experience (e.g., highlighting verses during recitation, dark mode, etc.), all within a single codebase.  
* [**Quran-Flutter**](https://github.com/SadaqaWorks/Quran-Flutter) – ⭐ 230  
  *Deployment:* Cross-platform app (Flutter)  
  *Description:* Quran app made with Flutter for all platforms (initial development phase).  
  *Features:*  
  * Designed to run on Android, iOS, and possibly web/desktop using Flutter, providing flexibility in where users can read the Quran.  
  * Even in early development, it aims to include the essential features: Quran text rendering, basic navigation by surah/juz, and future plans likely include translations and audio. The goal is an accessible, open-source Quran app that anyone can improve or adapt.  
* [**quran\_app**](https://github.com/yunusefendi52/quran_app) – ⭐ 184  
  *Deployment:* Mobile app (Flutter)  
  *Description:* Quran app built with Flutter.  
  *Features:*  
  * A complete Quran reading app with a simple Flutter-based interface, likely including Arabic text and at least one translation. Users can navigate to any Surah or Juz easily.  
  * May support bookmarking verses and possibly playing audio for verses. Its Flutter implementation ensures smooth performance and the potential to expand to multiple platforms or add features like theming and font size adjustments.  
* [**Al-quran-Al-karim**](https://github.com/HoussemTN/Al-quran-Al-karim) – ⭐ 115  
  *Deployment:* Mobile app (Flutter)  
  *Description:* “The Noble Qur’an \- Hafs from Asim \[Arabic Edition\]” – a Quran app focusing on the Arabic text.  
  *Features:*  
  * Presents the Quran in Arabic (Hafs narration) with an intuitive Flutter interface, optimized for Arabic reading (right-to-left support, clear Uthmani font).  
  * Likely offers offline access to the entire Quran text and simple navigation (surah list, page by page), making it a straightforward digital Mushaf without additional translations or commentary, ideal for native Arabic readers.

### **C++**

* [**quran-companion**](https://github.com/0xzer0x/quran-companion) – ⭐ 163  
  *Deployment:* Desktop application (Qt/C++)  
  *Description:* A free and open-source desktop Quran reader and player 💻.  
  *Features:*  
  * Cross-platform desktop Quran app built with Qt, providing a rich interface to read the Quran and listen to recitations. It likely supports multiple translations which can be shown alongside the Arabic text, given Qt’s capabilities.  
  * Includes an audio player for Quran recitations, enabling users to play verses or surahs with ease. The design probably focuses on productivity (with features like search and bookmarks) and a pleasant reading experience on larger screens.  
* [**QuranApp-Linux**](https://github.com/Muslim-Programmers/QuranApp-Linux) – ⭐ 21  
  *Deployment:* Desktop application (Linux, C++/Qt)  
  *Description:* Simple Quran reading app with multiple translations support and optional streaming of beautiful Quran recitation.  
  *Features:*  
  * Allows reading the Quran text on a Linux desktop, with the ability to switch between different language translations for each verse, catering to a wide audience.  
  * Users can stream audio recitations within the app if they want to listen while reading. The interface is likely minimal and focused on the text, ensuring low resource usage and smooth performance on Linux systems.

### **HTML**

* [**quran**](https://github.com/fawazahmed0/quran) – ⭐ 17  
  *Deployment:* Web application / static site  
  *Description:* “Read Quran in 90+ Languages” – a project providing Quran content in numerous languages.  
  *Features:*  
  * A multilingual Quran reader that aggregates translations in over 90 languages, allowing users to read the Quran’s meaning in their preferred language. It might offer side-by-side Arabic and translation, or selection of language which then displays the entire Quran in that language.  
  * Likely a static site or client-side app with all translation data included (possibly via JSON files), so it can work offline once loaded. It serves as a single resource for a vast array of translations without needing separate apps for each language.  
* [**Quranipfs**](https://github.com/adelpro/Quranipfs) – ⭐ 15  
  *Deployment:* Web application (IPFS)  
  *Description:* Quran over IPFS – a browser-based Quran that streams and downloads content via the InterPlanetary File System (IPFS).  
  *Features:*  
  * Utilizes decentralized IPFS technology to store and deliver Quran content (text, audio, or PDFs), meaning users can read or listen to the Quran through a peer-to-peer network, which increases availability and resilience (no single server dependency).  
  * Provides both streaming (for instant access to recitations or large files) and downloading options (to save content locally from IPFS). This approach ensures that even if traditional servers are down, the Quran content remains accessible through the distributed network.

### **JavaScript**

* [**quran-api**](https://github.com/gadingnst/quran-api) – ⭐ 786  
  *Deployment:* Web API \+ Database  
  *Description:* Simple Quran API & database including Indonesian Tafsir and audio (murattal by Sheikh Mishary Rashid Alafasy).  
  *Features:*  
  * Offers a RESTful API to retrieve Quran text, translations (with a focus on the Indonesian language), and even tafsir (exegesis) entries. This makes it easy for developers to get verses or surahs in JSON format, along with interpretations.  
  * Includes media integration: provides links or streaming for Quran audio recitations (specifically Sheikh Mishary’s recitations) so that applications can play verse or surah audio. Essentially, it’s a full package for Quran data and media, ready to be plugged into applications.  
* [**audio.quran.com**](https://github.com/quran/audio.quran.com) – ⭐ 140  
  *Deployment:* Website (Audio streaming service)  
  *Description:* The official repository for Quranicaudio.com (audio Quran site).  
  *Features:*  
  * Powers a dedicated Quran audio platform where users can browse and stream Quran recitations by various reciters. It likely organizes audio by Surah and by reciter, and allows continuous playback.  
  * The site probably offers features like playlists or favorites and provides an API for the audio content. The open-source code covers the web frontend and possibly backend that serve thousands of Quran audio files to users with a clean UI.  
* [**quran-extension**](https://github.com/shahednasser/quran-extension) – ⭐ 92  
  *Deployment:* Browser Extension (Chrome/Firefox)  
  *Description:* New Tab replacer extension that shows Quran verses and beautiful nature pictures.  
  *Features:*  
  * Replaces the new tab page in your browser with a randomly selected Quran verse (often with translation) displayed over or alongside a stunning nature background image, offering inspiration with every new tab.  
  * Allows some customization: users might cycle through verses, choose languages for translation, or click a reference to read more context. It’s an unobtrusive way to remind oneself of the Quran during daily browsing.  
* [**quran**](https://github.com/mohdovais/quran) – ⭐ 6  
  *Deployment:* Web application  
  *Description:* Quran reader in Arabic.  
  *Features:*  
  * A simple online Quran reading interface focusing purely on the Arabic text of the Quran, likely presenting the text by Surah without additional commentary or translation.  
  * May include basic navigation (select Surah/juz or scroll continuously) and perhaps a search function for finding specific verses. The project’s simplicity suggests it’s meant to allow quick access to the Arabic Quran text in a web browser.

### **Python**

* [**PyQuran**](https://github.com/hci-lab/PyQuran) – ⭐ 144  
  *Deployment:* Python library  
  *Description:* PyQuran – a Python package for Quranic analysis.  
  *Features:*  
  * Offers tools to analyze the text of the Quran, possibly including features like counting letters/words, finding verses by keywords, or extracting statistical information (e.g., frequency of certain words or letters).  
  * Likely contains datasets and functions for handling Quranic text (in Arabic and maybe transliteration/translation) within Python, enabling researchers or developers to perform tasks like searching the Quran, analyzing verses, or working with Arabic script processing (e.g., finding roots of words).  
* [**quran-svg**](https://github.com/batoulapps/quran-svg) – ⭐ 114  
  *Deployment:* Asset collection  
  *Description:* SVG files for the pages of the Quran.  
  *Features:*  
  * A complete set of Scalable Vector Graphics files representing each page of the Quran. SVG format ensures the text and artwork scale without losing clarity, which is ideal for high-DPI displays or printing.  
  * These files likely mirror the layout of a standard Quran Mushaf, enabling developers to render page images in their apps or websites with minimal load (SVG can be very efficient) and with the possibility to manipulate or highlight portions of text via SVG markup if needed.  
* [**django-quran**](https://github.com/idris/django-quran) – ⭐ 27  
  *Deployment:* Django app (pluggable module)  
  *Description:* Quranic models and helpers for use in Django projects.  
  *Features:*  
  * Provides Django ORM models for Quran data (such as Surah, Ayah, Juz, etc.), making it easy to integrate the entire Quran text into a Django application’s database.  
  * Includes utility functions or template tags for common needs (like retrieving a verse or range of verses, formatting Arabic text properly, or searching within the Quran). This allows Django developers to quickly add Quran features to websites (for example, displaying daily verses or creating a Quran exploration tool).  
* [**python-quran-odoa**](https://github.com/Keda87/python-quran-odoa) – ⭐ 12  
  *Deployment:* Python library  
  *Description:* Python library to get a random ayah from the Quran for the “One Day One Ayah (ODOA)” campaign.  
  *Features:*  
  * A convenient function to fetch a random Quran verse (ayah) from the 6236 verses, intended to encourage daily reflection by providing one ayah per day.  
  * Likely includes the Quran text (and possibly translations) in its data. It may ensure that each day a different verse is returned, and might even maintain state (to avoid repeats too soon). This is useful for apps or bots that share a daily verse automatically.

### **Ruby**

* [**quran.com-api**](https://github.com/quran/quran.com-api) – ⭐ 1027  
  *Deployment:* Web API (Ruby on Rails)  
  *Description:* Quran.com content APIs.  
  *Features:*  
  * Serves as the backend for Quran.com, providing JSON APIs for verses, chapters, translations, audio files, and more. It consolidates all Quranic content (Arabic text, multiple translations, tafsir, audio timings) and exposes them via endpoints.  
  * Highly optimized for production use, it supports complex queries (like full-text search in Quran or filtering by chapter) and is scalable to handle a large number of requests from the Quran.com website and any external apps utilizing the API.  
* [**quran.com-frontend-v2**](https://github.com/quran/quran.com-frontend-v2) – ⭐ 470  
  *Deployment:* Web application (Frontend)  
  *Description:* The second version of Quran.com’s front-end (web interface).  
  *Features:*  
  * A complete user-facing website that lets users read the Quran in Arabic, with options to view translations side-by-side, listen to recitations, and use features like verse highlighting, bookmarking, and sharing.  
  * Likely built with modern web technologies (could be older React/Redux or even earlier Rails views, given it’s v2) and focuses on performance and responsiveness. It includes an interactive UI (for example, allowing users to pick a reciter or adjust font size) to enhance the experience of exploring Quranic text online.

### **Unknown**

* [**quran-api**](https://github.com/fawazahmed0/quran-api) – ⭐ 823  
  *Deployment:* Static API service / JSON data  
  *Description:* Free Quran API service with 90+ different languages and 400+ translations.  
  *Features:*  
  * Provides an extensive collection of Quran translations in JSON format for over 90 languages, encompassing more than 400 translation sources. This allows retrieval of verses in many languages via simple HTTP requests (no API key needed).  
  * The project likely includes all data in a structured way (perhaps each translation as a JSON file per surah), which can be used offline as well. It’s an invaluable resource for developers who need multilingual Quranic text, eliminating the need to gather and format translations manually.  
* [**quranjson**](https://github.com/semarketir/quranjson) – ⭐ 675  
  *Deployment:* Data (JSON files)  
  *Description:* Quran JSON – contains all 6236 verses, 114 surahs, 30 juz in JSON format.  
  *Features:*  
  * A comprehensive JSON representation of the Quran’s structure and text. Likely includes an array of surahs, each containing its verses (with verse number, text, etc.), as well as mappings for juz’. This single dataset can be used to power Quran apps or for computational analysis without dealing with custom parsing.  
  * The data is in a developer-friendly format (JSON) which can be easily imported into databases or used directly in web/mobile apps. It focuses purely on the Quran’s Arabic text and organizational units, enabling quick access to any ayah by index.  
* [**Quran-App-Data**](https://github.com/Mohamed-Nagdy/Quran-App-Data) – ⭐ 209  
  *Deployment:* Data repository  
  *Description:* *“كل كتب وصور تطبيقات القرآن”* (Arabic for “All books and images of Quran applications”) – a repository of resources for Quran apps.  
  *Features:*  
  * Contains a large collection of Quran-related assets: possibly images of Quran pages, text files of Quran content, translations, and books (like tafsir or hadith books) used in various Quran apps.  
  * By centralizing these files (fonts, PDFs, JSON data, audio, etc.), it provides a one-stop for developers to grab necessary resources for building a Quran application without individually sourcing each component. For example, it might include high-quality page scans, translation files, and audio in a ready-to-use form.  
* [**quran-csv**](https://github.com/azvox/quran-csv) – ⭐ 26  
  *Deployment:* Dataset (CSV format)  
  *Description:* CSV files containing Quran data.  
  *Features:*  
  * Offers the Quran text (and possibly translations or transliterations) in a CSV (comma-separated values) format. This could be one file per surah or one big file with all verses, where each row has fields like Surah, Ayah number, Arabic text, etc.  
  * Useful for quick import into spreadsheet software or databases. By providing Quranic content in CSV, it lowers the barrier for data analysis or integration with systems that handle CSV easily (e.g., importing into SQL or Excel for study or verification).

### **TypeScript**

* [**open-mushaf-native**](https://github.com/adelpro/open-mushaf-native) – ⭐ 9  
  *Deployment:* Mobile app (Expo/React Native)  
  *Description:* **Open Mushaf Native** – a modern Quran Mushaf app built with Expo & React Native for immersive reading on mobile (and web via Expo). Emphasizes performance, offline functionality, and accessibility with gesture-based navigation.  
  *Features:*  
  * **Seamless Reading Experience:** Implements fluid, gesture-driven navigation (like swipes to turn pages or move between surahs) to mimic the feel of a physical Mushaf. The UI is optimized for full-screen reading and supports landscape/portrait modes.  
  * **Offline & Cross-Platform:** Content is accessible offline once downloaded (Quran text, maybe audio), and the app is designed to work on both mobile devices and as a Progressive Web App. It focuses on accessibility features (perhaps text scaling, contrast modes) to accommodate all users.  
* [**open-mushaf**](https://github.com/adelpro/open-mushaf) – ⭐ 3  
  *Deployment:* Web application (Next.js PWA)  
  *Description:* An open-source Quran Mushaf implementation built with TypeScript using Next.js, plus PWA support and TailwindCSS for responsive design and offline access.  
  *Features:*  
  * **Fast Web Quran Reader:** A server-rendered (Next.js) web app that loads Quran pages quickly and can be used like a native app thanks to PWA capabilities (offline reading, add-to-home-screen functionality).  
  * **Responsive and Configurable:** TailwindCSS is used for a flexible design that works on desktop, tablet, and mobile browsers. The application likely offers features such as different themes, easy navigation by page or surah, and possibly search, all while keeping performance and bundle size in mind for a smooth user experience.

## **Other**

### **TypeScript**

* [**al-azan**](https://github.com/meypod/al-azan) – ⭐ 215  
  *Deployment:* Mobile app (React Native)  
  *Description:* Privacy-focused, ad-free open-source Muslim Adhan (prayer times) and Qibla app.  
  *Features:*  
  * **Prayer Times & Adhans:** Provides accurate prayer timings for your location and plays Adhan notifications at those times, all without any ads or trackers. Users can customize calculation methods and prayer reminders in a totally privacy-respecting environment.  
  * **Additional Tools:** Includes an integrated Qibla compass to find the direction of Mecca and likely other features such as Hijri calendar date and daily scripture or duas. The interface is clean and modern, focusing on essentials without clutter.  
* [**qafiyah**](https://github.com/alwalxed/qafiyah) – ⭐ 186  
  *Deployment:* Web app & API  
  *Description:* Open-source Arabic poetry database and website, with 944k+ verses by 932 poets from 10 eras (built with Next.js, Hono, and Supabase).  
  *Features:*  
  * **Vast Poetry Database:** A comprehensive collection of Arabic poems across centuries, searchable and browsable by poet, era, or keywords. It provides verses in Arabic (and possibly their rhythmic meter info, given the name “Qafiyah” implies rhyme/meter).  
  * **Web Interface & API:** The Next.js frontend offers a user-friendly way to explore the poetry (with features like random poem, favorites, etc.), while the Supabase backend and Hono (a web framework) likely provide an API for developers to query the poetry data. This allows integration of classical Arabic poetry into other apps or analyses.  
* [**muslim**](https://github.com/abdenassar01/muslim) – ⭐ 9  
  *Deployment:* Android app  
  *Description:* An Android app to help you read Al-Quran and Azkar.  
  *Features:*  
  * Combines two main functions: a Quran reader (providing the text of the Quran for reading, presumably with bookmarking and possibly translation support) and a collection of Azkar (supplications/remembrances) for daily use.  
  * Likely includes categorized Azkar (morning, evening, prayer after Salah, etc.) so users can easily follow daily remembrance routines. The interface probably allows quick switching between Quran reading mode and Azkar lists, making it a handy all-in-one spiritual companion.

### **Unknown**

* [**Pray-Times**](https://github.com/abodehq/Pray-Times) – ⭐ 225  
  *Deployment:* Multi-language library (JavaScript with ports in other languages)  
  *Description:* “PrayTimes” – an Islamic project providing an open-source library for calculating Muslim prayer times (originally by PrayTimes.org).  
  *Features:*  
  * **Cross-Platform Code:** The project includes implementations of the prayer time calculation algorithm in several programming languages (JavaScript, Python, PHP, Java, C++, C\#, Objective-C, etc.), making it accessible to developers on almost any platform.  
  * **Flexible Calculations:** Supports a variety of calculation methods (MWL, ISNA, Umm al-Qura, Egyptian, and custom angles) and adjustments, as well as functions for getting prayer times easily by inputting date, coordinates, and timezone. It also typically includes documentation and a manual explaining the formulas and how to adjust parameters for different conventions.

### **Python**

* [**api**](https://github.com/sunnah-com/api) – ⭐ 379  
  *Deployment:* Web API  
  *Description:* Official API for **sunnah.com** (Hadith collections).  
  *Features:*  
  * Provides developers access to a large repository of Hadith from various books (Bukhari, Muslim, Abu Dawood, etc.) through REST endpoints. You can retrieve hadith texts by collection/book number, search for words in hadith, and get metadata like book names and chapter titles.  
  * The API returns structured data (likely JSON) including the hadith in Arabic and translations (e.g., English), along with grading info if available. This allows integration of hadith content into apps or websites without web scraping sunnah.com manually.  
* [**alfanous**](https://github.com/Alfanous-team/alfanous) – ⭐ 267  
  *Deployment:* Quran search engine API  
  *Description:* Alfanous is an Arabic search engine API providing simple and advanced search in the Quran, with many features and multiple interfaces.  
  *Features:*  
  * **Advanced Search Capabilities:** Allows users to perform complex searches in the Quran text (for example, all verses containing certain words or phrases, maybe even by root letters or phonetics) and returns relevant verses. It supports both simple queries and advanced options (like exact phrase, wildcard, etc.).  
  * **Multiple Interfaces:** While the core is an API, Alfanous likely had different frontends or integrations (maybe a web interface, a desktop GUI, or plugins) demonstrating its use. It provides features like contextual results (showing the verse with some surrounding text or translation) and could support both Arabic input and transliterated search, helping researchers or developers build powerful Quranic search tools.  
* [**pyIslam**](https://github.com/abougouffa/pyIslam) – ⭐ 108  
  *Deployment:* Python library  
  *Description:* pyIslam – a Python library that calculates prayer times, Hijri date, Qiblah direction, and more.  
  *Features:*  
  * **Prayer & Qibla Calculations:** Functions to compute daily prayer times for any location, plus determine the Qibla direction (bearing from North) given coordinates, all using offline algorithms.  
  * **Hijri Calendar and Beyond:** Includes conversion between Gregorian and Hijri dates (likely using the Umm al-Qura calendar for accuracy). It may also offer other utilities (the “and more” could include things like determining Islamic months or maybe Zakat calculations). Essentially, it’s a toolkit of common Islamic computations in one Python package.  
* [**ayah-detection**](https://github.com/quran/ayah-detection) – ⭐ 104  
  *Deployment:* Scripts/Tools (Python)  
  *Description:* Scripts to detect Ayah markers from Quran images.  
  *Features:*  
  * Processes images of Quran pages to find and pinpoint the locations of verse boundaries (ayah markers). This can involve image processing techniques to recognize the ornate verse-ending symbols or the verse numbers in the margin.  
  * Useful for developers digitizing Quran texts: by knowing where each verse is on an image, one can create clickable verse regions, or align text with images. The scripts likely output coordinates or cut the images into per-ayah segments. It’s a specialized tool for bridging printed Quran layout with digital referencing.  
* [**qpc-fonts**](https://github.com/nuqayah/qpc-fonts) – ⭐ 99  
  *Deployment:* Assets (Fonts)  
  *Description:* King Fahd Glorious Quran Printing Complex fonts.  
  *Features:*  
  * A collection of high-quality Arabic fonts released by the Quran Printing Complex, tailored for typesetting the Quran. These likely include fonts that precisely match the Madinah Mushaf calligraphy, including all diacritics and ornate decorations, as well as Indo-Pak script fonts.  
  * By using these fonts, developers and designers can render Quranic text in applications or print with the exact style used in official prints. They support the necessary ligatures and markings that general Arabic fonts might not, ensuring the Quran text is displayed correctly and beautifully.  
* [**athany**](https://github.com/0xzer0x/athany) – ⭐ 23  
  *Deployment:* Desktop application (Python)  
  *Description:* A lightweight Python-based prayer times/athan application for Windows and Linux that operates offline.  
  *Features:*  
  * Sits in the system tray and calculates prayer times locally for the user’s location, then gives a gentle reminder or plays an Adhan at each prayer time. Being offline means it doesn’t rely on internet and thus preserves privacy and reliability.  
  * Minimalistic interface to show upcoming prayer times and allow configuration (location, calculation method, which Adhan sound to play). It’s designed to use very little system resources, making it suitable to run in the background on PCs throughout the day.

### **JavaScript**

* [**Muezzin**](https://github.com/DBChoco/Muezzin) – ⭐ 156  
  *Deployment:* Desktop application (Windows, macOS, Linux – Electron)  
  *Description:* A prayer times (Adhan) and Quran app for desktop (Windows, macOS, GNU/Linux).  
  *Features:*  
  * **Prayer Times with Notifications:** Calculates local prayer times and gives Adhan alerts on a desktop computer, with options to customize the notification and sound. The interface likely displays today’s prayer schedule and countdown to the next prayer.  
  * **Built-in Quran Reader:** Also includes a Quran component, so users can read the Quran within the same app. This might feature the full Quran text with navigation by surah and possibly audio playback or a search function. It essentially brings mobile “Islamic app” features to the desktop in one package.  
* [**muslim-companion**](https://github.com/CosmicCoder13/muslim-companion) – ⭐ 3  
  *Deployment:* Browser extension (Chrome)  
  *Description:* A comprehensive browser extension for Muslims featuring prayer times, Qibla direction, Islamic quotes, and more.  
  *Features:*  
  * **Prayer Times & Qibla:** The extension likely adds a toolbar popup or new tab that shows daily prayer times and a compass indicating Qibla direction, all within the browser so information is one click away.  
  * **Inspirational and Informative:** Includes daily Islamic quotes or verses/hadith, Hijri date, and possibly other quick-access info like a Tasbeeh counter or Islamic calendar events. Presented in a sleek, modern interface, it aims to be a one-stop mini-dashboard for Islamic needs without leaving your web browser.

### **Kotlin**

* [**LaamMuslimAndroid**](https://github.com/luthfiarifin/LaamMuslimAndroid) – ⭐ 36  
  *Deployment:* Android app  
  *Description:* An Islamic project for prayer schedules, Quran reading, etc.  
  *Features:*  
  * Provides local prayer times and alarms for each prayer, helping users never miss a prayer. It likely uses device location or manual city selection for calculations.  
  * Also features a built-in Quran reader (possibly with translations) and other components (the description suggests etc., which could include things like daily Duas, Hijri calendar or a Qibla compass). The app strives to cover multiple daily Muslim practices in one place.  
* [**Wazaker**](https://github.com/hamza94max/Wazaker) – ⭐ 30  
  *Deployment:* Android app  
  *Description:* An Islamic application to read morning and evening Azkar, find Qibla direction, count Dhikr, and read a collection of 42 hadith.  
  *Features:*  
  * **Azkar Collection:** Provides the full set of morning and evening supplications from the Prophetic Sunnah (Hisn al-Muslim), as well as other categories like prayers before sleep or after Salah, all in an easy-to-read format.  
  * **Utilities:** Includes a Qibla compass to accurately find the direction of prayer, a Tasbeeh counter for counting adhkar or tasbih repetitions, and a curated list of 42 important hadiths for the user to learn and reference. It’s a handy toolkit for daily spiritual routines.  
* [**muslim-data-android**](https://github.com/my-prayers/muslim-data-android) – ⭐ 26  
  *Deployment:* Android library  
  *Description:* “Muslim Data” – an Android library providing Prayer Times, Offline Geocoder, Names of Allah, and Azkars.  
  *Features:*  
  * **Prayer Times & Geocoding:** Offers easy-to-use methods to calculate prayer times for given coordinates, and even an offline geocoder that can convert coordinates to a readable location (city/country) without an internet connection, which is useful for tagging location in prayer times or finding nearest city.  
  * **Islamic Content Data:** Provides data sets and APIs for 99 Names of Allah (perhaps with meanings) and collections of Azkar (supplications) from the Quran and Hadith. This library lets app developers fetch this content readily, so they don’t need to hard-code or source it themselves – speeding up development of comprehensive Islamic apps.

### **Java**

* [**Muslim-App**](https://github.com/choubari/Muslim-App) – ⭐ 173  
  *Deployment:* Android app  
  *Description:* Daily Muslim Android App containing Prayer times, Remembrance (Azkar), Qibla Finder, Zakat Calculator and other features. *(Project note: planned to be migrated to another language)*  
  *Features:*  
  * **Prayer and Qibla:** Core functionality to display accurate prayer times with Adhan notifications and a built-in Qibla compass to guide users towards Mecca for prayer.  
  * **Holistic Toolkit:** Includes a Zakat calculator to help users compute their charity obligations, a collection of daily Azkar (morning/evening remembrances, du’as) for spiritual practice, and potentially other features like Islamic date conversion or a mosque locator. It aims to be an all-in-one resource for a Muslim’s daily needs.  
* [**NoorUlHuda**](https://github.com/mirfatif/NoorUlHuda) – ⭐ 96  
  *Deployment:* Android app  
  *Description:* “Noor Ul Huda” – a simple, open source Quran reader app with extra features, completely free forever.  
  *Features:*  
  * **Quran Reader:** Allows offline reading of the entire Quran with a clean interface. It may include features like bookmarks, night mode, and possibly translations or transliterations to assist understanding and reading.  
  * **Extras:** Likely includes prayer times and Duas – since description says “with extras,” it might show daily prayer times or have a prayer reminder, and include a library of common supplications (duas) or a Hijri calendar. The focus is on being free and open, so no ads or locked content.  
* [**itl-java**](https://github.com/fikr4n/itl-java) – ⭐ 68  
  *Deployment:* Java library  
  *Description:* A Java library for calculating prayer (salat) times, Hijri date, and Qibla direction, based on ITL (Islamic Tools and Libraries).  
  *Features:*  
  * **Prayer Time Calculation:** Implements reliable formulas to get all daily prayer times for given location and date, supporting multiple conventions and adjustments, as part of the ITL suite (which suggests standardized tools).  
  * **Extended Utilities:** Can convert between Gregorian dates and Hijri calendar dates (useful for finding Islamic events or displaying Islamic date), and calculate the Qibla direction from any location. This all-in-one library spares developers from using separate libraries for each function and ensures consistency across Islamic calculations.  
* [**Ayah-intellij**](https://github.com/0x61nas/Ayah-intellij) – ⭐ 47  
  *Deployment:* IntelliJ IDE plugin  
  *Description:* Get a verse (ayah) from the Quran during your coding session in JetBrains IDEs. Stay connected with the words of God.  
  *Features:*  
  * Displays a random Quranic verse (and possibly its translation) in the IDE, either in a tool window or as a popup, at a set interval or on demand. This serves as a gentle reminder or inspiration while programming.  
  * Likely allows some customization, such as choosing the language of translation or how frequently a new verse appears (for example, a new ayah each time you open the IDE or every few hours). It keeps developers spiritually mindful without leaving their development environment.  
* [**MuslimMateAndroid**](https://github.com/fekracomputers/MuslimMateAndroid) – ⭐ 32  
  *Deployment:* Android app  
  *Description:* “Muslim Mate” – an android application to organize a Muslim’s life.  
  *Features:*  
  * **Organizer & Reminders:** Provides prayer times and Adhan alerts, Qibla direction, and likely a Hijri calendar to track Islamic dates and events. Possibly includes reminders for important actions like fasting on Mondays/Thursdays or prayer of Duha, etc.  
  * **Content & Tools:** Could encompass a Quran reader or daily verse, an Azkar section for daily remembrances, a Zakat calculator, and a Ramadan timetable. The goal is to integrate religious schedule and content in one app to help users manage worship and daily life efficiently.  
* [**Salawat**](https://github.com/DBChoco/Salawat) – ⭐ 29  
  *Deployment:* Desktop application (Java, JavaFX)  
  *Description:* A prayer times (Adhan) app for Windows and GNU/Linux written in JavaFX.  
  *Features:*  
  * **Prayer Timetable & Adhan:** Calculates local prayer times and notifies the user at each prayer with a chosen Adhan sound. The interface likely displays today’s schedule and a countdown to the next prayer.  
  * **Minimal & Native:** Being JavaFX, it offers a native-like UI on desktop, possibly with the ability to run in the background/tray. “Salawat” (plural of Salat) might also imply it can show the salawat (perhaps sending peace upon the Prophet) or it simply refers to prayers. In essence, it’s a straightforward, no-frills desktop prayer reminder.  
* [**kiblat-Campass-android**](https://github.com/najamiqbal/kiblat-Campass-android) – ⭐ 3  
  *Deployment:* Android app  
  *Description:* “Kiblat Compass” – an Islamic app (likely for Qibla direction).  
  *Features:*  
  * Uses the device’s sensors to show an arrow pointing towards the Kaaba (Qibla) from the user’s current location. The compass UI probably also displays the distance to Mecca and degree offset from North.  
  * May include basic additional info such as current prayer time or a simple prayer timetable, but given the name and size, it’s primarily a compass utility for ensuring one faces the correct direction during prayer.

### **Dart**

* [**Mi-raj**](https://github.com/Isko21/Mi-raj) – ⭐ 36  
  *Deployment:* Mobile app (Flutter)  
  *Description:* “Mi’raj” – an app that helps Muslims around the world perform daily worship. It includes the complete Qur’an, Qiblah direction, and Prayer Times.  
  *Features:*  
  * **Holy Quran:** Full Quran text available to read, likely with translations and maybe audio playback, all within the app.  
  * **Prayer Toolkit:** Provides daily prayer times with reminders and a Qibla compass to find the prayer direction. It might also feature other tools implied by “daily worship” – possibly a Tasbeeh counter or a section for Duas. The Flutter design ensures it’s cross-platform (Android/iOS) with a cohesive experience integrating all these features.

### **Swift**

* [**muslim-data-ios**](https://github.com/my-prayers/muslim-data-ios) – ⭐ 28  
  *Deployment:* iOS library (Swift)  
  *Description:* “Muslim Data” library for iOS, providing Prayer Times, Offline Geocoder, Names of Allah, and Azkars.  
  *Features:*  
  * **Prayer Times & Qibla for iOS:** Functions to calculate daily prayer times and possibly Qibla direction on iOS, similar to its Android counterpart, allowing app developers to embed prayer calculations without writing it from scratch.  
  * **Built-in Data:** Contains resources like the 99 Names of Allah (with descriptions) and collections of Azkar (e.g., morning/evening supplications) which can be fetched and displayed in an iOS app easily. Additionally, the offline geocoder can translate coordinates to city names within an iOS app, enabling automatic location naming for prayer time settings.

### **HTML**

* [**altaqwaa-desktop**](https://github.com/rn0x/altaqwaa-desktop) – ⭐ 235  
  *Deployment:* Desktop application (Windows/Linux, Electron)  
  *Description:* **التقوى (Al-Taqwaa)** – An Islamic desktop application for Windows and Linux, easy to use and packed with many features needed daily by Muslims.  
  *Features:*  
  * **Quran with 158 Reciters:** Offers the Holy Quran text and the ability to listen to recitations from over 158 different Qaris. Users can stream or download audio for offline listening and choose between reciters easily.  
  * **Comprehensive Azkar & Tools:** Contains a large collection of Azkar (morning, evening, before/after eating, sleep, prayer, etc.), diverse supplications and du’as, and prayer times based on your location (with Adhan notifications). It likely also includes other utilities like a Hijri calendar, maybe religious stories or a prayer tracker. All features are accessible in a unified desktop interface with Arabic support and possibly English as well.  
* [**MuslimMateWebsite**](https://github.com/fekracomputers/MuslimMateWebsite) – ⭐ 16  
  *Deployment:* Web application (Dashboard)  
  *Description:* A website that displays a daily dashboard of information needed for Muslims (Prayer times, Hijri Calendar, Weather).  
  *Features:*  
  * **Daily Prayer Schedule:** Shows the five daily prayer times for the user’s location (likely auto-detected or set) prominently on the dashboard, along with countdowns or highlights for the next prayer.  
  * **Integrated Info:** Also displays today’s date in both Gregorian and Hijri, which helps in tracking Islamic dates. Additionally, it pulls local weather information so users have worldly context (weather forecast) along with spiritual timings. The site’s goal is to be the browser start page for a Muslim user, concentrating useful daily info (possibly also including things like a Quran verse of the day or a hadith).

## **Islamic Calendar**

### **Java**

* [**HijriDatePicker**](https://github.com/alhazmy13/HijriDatePicker) – ⭐ 147  
  *Deployment:* Android library  
  *Description:* Material Date & Time Picker (Dual Gregorian-Hijri picker for Android).  
  *Features:*  
  * A custom DatePicker component that allows users to select dates in both Gregorian and Hijri calendars seamlessly, styled according to Google’s Material Design for consistency in Android apps.  
  * Developers can easily plug it into forms where Islamic date selection is needed (e.g., picking a date for Ramadan events or birthdays in Hijri). It handles the conversion internally and can return both corresponding dates. Supports Android 5.0+ and is localized for Arabic right-to-left layout when showing Hijri dates.

### **JavaScript**

* [**Hijri.js**](https://github.com/xsoh/Hijri.js) – ⭐ 81  
  *Deployment:* JavaScript library  
  *Description:* A tool for the Islamic calendar (Hijri) in JavaScript.  
  *Features:*  
  * Provides functions to convert between Gregorian and Hijri dates accurately, likely based on known algorithms or tables (could include support for different moon-sighting criteria or use Umm al-Qura calculations).  
  * May also include utility to get current Hijri date, add or subtract days in the Hijri calendar, and format Hijri dates. This library enables web developers to easily include Hijri calendar functionality in web apps (like displaying today’s Hijri date or scheduling events on the Islamic calendar).  
* [**hijri-date-picker**](https://github.com/abublihi/hijri-date-picker) – ⭐ 27  
  *Deployment:* Web component (React)  
  *Description:* A simple and reusable React component for a Hijri date picker.  
  *Features:*  
  * Allows users to pick dates in Hijri format through a visual calendar widget. Likely also shows the equivalent Gregorian date or allows toggling between calendars for convenience.  
  * The component is designed to be easily dropped into any React application, with props to configure initial date, localization (perhaps Arabic labels), and styling. It simplifies the process of selecting Islamic dates (e.g., selecting Ramadan 1st or Eid day) in web forms.

### **Python**

* [**hijridate**](https://github.com/dralshehri/hijridate) – ⭐ 72  
  *Deployment:* Python library  
  *Description:* Accurate Hijri-Gregorian date converter based on the Umm al-Qura calendar.  
  *Features:*  
  * Uses the official Umm al-Qura calendar data (the system used by Saudi Arabia, known for accuracy for civil purposes) to convert dates, ensuring that the conversions match the widely recognized calendar in the Muslim world.  
  * Provides simple Python API: given a Gregorian date it returns the corresponding Hijri date and vice versa. It likely covers a range of years as defined by available Umm al-Qura data. Also, it might adjust for day boundaries and timezone differences properly. Ideal for applications that need to display Islamic dates or calculate age in Hijri, etc., with precision.

## **Hadith**

### **JavaScript**

* [**hadiths**](https://github.com/fawazahmed0/hadiths) – ⭐ 14  
  *Deployment:* Data (JSON) / Static API  
  *Description:* Hadith collections in multiple languages and with multiple authenticity grades.  
  *Features:*  
  * Aggregates hadith texts from various sources (possibly the major six books and others) and provides them in a structured format, including translations in different languages.  
  * Each hadith entry likely includes its grading (e.g., Sahih, Hasan, Da’if) and reference info. The project probably provides an easy way to fetch or search these hadith via JSON files or a simple static API, enabling developers to incorporate hadith content into apps without dealing with scraping or databases.  
* [**check-hadith-native**](https://github.com/adelpro/check-hadith-native) – ⭐ 3  
  *Deployment:* Mobile app (React Native)  
  *Description:* Check Hadith (Nabawi) authenticity using the Dorar API (React Native version).  
  *Features:*  
  * Allows a user to input or search for a phrase from a hadith and then uses the Al-Dorar al-Sunniah API to retrieve information about that hadith – including its source, text, and authenticity grading.  
  * Mobile-friendly interface for quick fact-checking of hadiths on the go. It likely displays multiple results if a phrase matches several hadiths and shows details so the user can verify if a circulating hadith is authentic (Sahih) or not.

### **Unknown**

* [**hadith-api**](https://github.com/fawazahmed0/hadith-api) – ⭐ 337  
  *Deployment:* Web API / Data service  
  *Description:* Free Hadith API service with multiple languages and multiple grades.  
  *Features:*  
  * Exposes hadith data via a RESTful API, allowing queries for hadith by collection (Bukhari, Muslim, etc.), by number, or by keywords, returning the hadith text in various languages.  
  * Includes authenticity grades from scholars for each hadith when available, so developers can filter or display the status of hadith. It covers multiple collections and provides a unified interface to access a wealth of hadith literature without setting up one’s own database.  
* [**Open-Hadith-Data**](https://github.com/mhashim6/Open-Hadith-Data) – ⭐ 172  
  *Deployment:* Dataset  
  *Description:* Open Hadith Library of the databases of 9 different books (including the Six Major Books of Hadith).  
  *Features:*  
  * Provides the content of nine important hadith collections (such as the Sihah Sitta: Bukhari, Muslim, Tirmidhi, Abu Dawood, Nasa’i, Ibn Majah, and perhaps others like Muwatta, Musnad Ahmad, etc.) in a structured and open format.  
  * This data can be in SQL, JSON, or CSV form, and includes the hadith text (Arabic, and possibly translations), references (book, hadith number), and potentially gradings or commentary. It’s a treasure trove for developers and researchers, enabling offline access and analysis of hadith corpora without legal or technical barriers.

### **Kotlin**

* [**SunnahAssistant**](https://github.com/saidmsaid81/SunnahAssistant) – ⭐ 12  
  *Deployment:* Android app  
  *Description:* An Android app for setting reminders that help you become a better person (by following Sunnah practices).  
  *Features:*  
  * Allows users to set personalized reminders for various Sunnah acts – for example, fasting on Mondays and Thursdays, praying Duha, reading Qur’an daily, or giving charity regularly. The app might come pre-loaded with common good deeds and sunnah tasks to choose from.  
  * Tracks and encourages consistency: it could have features like streaks or gentle nudges if a user misses a practice. Essentially, it’s like a habit tracker specifically tailored to Islamic Sunnah habits, helping users gradually incorporate more good practices in daily life.

### **TypeScript**

* [**hadith-json**](https://github.com/AhmedBaset/hadith-json) – ⭐ 154  
  *Deployment:* Dataset (JSON)  
  *Description:* Database of Prophet’s hadiths: includes 50,884 hadiths from 17 books, among them the nine books.  
  *Features:*  
  * A massive compilation of hadith in JSON format, covering far more than the six canonical collections – it spans 17 books which likely include not just Bukhari, Muslim, etc., but also collections like Musnad Ahmad, Sunan Darimi, or others.  
  * Each hadith entry in the JSON presumably contains the book name, hadith number, Arabic text, and perhaps English translation and authenticity. Having all this in JSON makes it easy to index, search, or integrate into apps and analysis tools directly, saving countless hours of data entry.

### **HTML**

* [**check-hadith**](https://github.com/adelpro/check-hadith) – ⭐ 6  
  *Deployment:* Web application (PWA)  
  *Description:* Check Hadith Nabawi with Dorar API (web version).  
  *Features:*  
  * A lightweight web interface where users can input a hadith or a part of it (in Arabic, likely) and the app will query the Dorar API to find matches. It then displays the hadith text, its source (which book and reference), and the authenticity grading as given by Dorar’s scholars.  
  * Likely works as a Progressive Web App, meaning it can be installed on mobile home screens, works offline to some extent (maybe caching recent queries), and has a simple, mobile-friendly UI (since this complements the React Native version, the functionality is similar, just accessible via browser).

## **Azkar & Dua**

### **JavaScript**

* [**hisnmuslim\_app**](https://github.com/rn0x/hisnmuslim_app) – ⭐ 16  
  *Deployment:* Web app (Cordova/HTML/JS)  
  *Description:* **حصن المسلم (Hisn al-Muslim)** – an app based on the famous book “Fortress of the Muslim” which compiles authentic duas (supplications) from the Quran and Sunnah.  
  *Features:*  
  * Contains a comprehensive collection of Azkar and Duas categorized for various occasions: morning, evening, after prayers, before eating, travel, illness, etc., all in Arabic (often with translation and transliteration).  
  * Provides a user-friendly interface (likely Arabic text with optional translations) and possibly features like search or favorites. As a web app, it might be cross-platform and could be packaged via Cordova for mobile. It ensures you have the proper supplication for any situation readily available.

### **Java**

* [**Azkar-App**](https://github.com/AbdelrahmanBayoumi/Azkar-App) – ⭐ 115  
  *Deployment:* Desktop application (Java)  
  *Description:* Desktop Application 💻 for calculating Muslim prayer times 🕌, with Morning and Night Azkar 🤲 and notifications for random Azkar pop-ups at specific times.  
  *Features:*  
  * **Prayer Times on PC:** Computes and displays daily prayer times for a chosen location on the desktop, with the ability to set alarms or notifications at those times (so your computer can remind you or play Adhan).  
  * **Azkar with Notifications:** Includes the collection of Morning (after Fajr) and Evening (after Asr/Maghrib) Azkar. It not only lets you read them, but also can send a notification with a random dhikr (remembrance) or dua at certain intervals or times of day, prompting you to remember Allah during work. It likely sits in the system tray, running in the background to gently remind users of Azkar.
