class Config:

    # Init_Data
    GENERAL_PATH = \
        "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget." \
        "LinearLayout/android.widget.ExpandableListView/android.widget."
    DESIRED_CAP = {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "Android Emulator",
        "appPackage": "codepath.apps.demointroandroid",
        "appActivity": "codepath.apps.demointroandroid.DemoSelector"
    }
    HOST = "http://localhost:4723/wd/hub"

    # Test_Data
    EXPECTED_XML_TEXT = "firstButton clicked via XML handler"
    EXPECTED_JAVA_TEXT = "secondButton clicked via Java handler in onCreate"
    EXPECTED_TEXT = "Salesforce"
    INPUT_TEXT = "Hello world!"
    INPUT_URL = "salesforce.com"
    ELEMENTS = "android.widget.TextView"
    EXPECTED_SECOND_VIEW_TEXT = "Second TextView for Chapter 1"
    EXPECTED_SIMPLE_VIEW_LIST = ["SimpleListViewActivity", "Bruce", "Wayne", "Bill"]
    EXPECTED_CHAPTER_LIST = ["CodePath Android Demo", "Chapter 1: App Fundamentals",
                             "Chapter 2: User Interface", "Chapter 3: View Controls", "Chapter 4: User Interactions",
                             "Chapter 5: User Flows", "Chapter 6: Networking", "Chapter 7: Advanced Views",
                             "Chapter 8: Preferences", "Chapter 9: Content Providers", "Chapter 10: Publishing"]
