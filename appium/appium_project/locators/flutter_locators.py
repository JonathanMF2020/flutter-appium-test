from appium_flutter_finder.flutter_finder import FlutterFinder

finder = FlutterFinder()

INCREMENT_BUTTON = finder.by_value_key("incrementButton")
COUNTER_TEXT = finder.by_value_key("counterText")