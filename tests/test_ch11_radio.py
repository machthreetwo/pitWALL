from pitwall.radio import box_calls, extract_laptimes, parse_radio, redact_laptimes

LINES = [
    "[L23 14:02:11.532] VER -> PIT: Box box, box this lap",
    "[L24 14:03:40.001] PIT->VER:  Copy. Target 1:22.900",
    "[L30 14:12:00.000] NOR -> PIT: tyres are boxed... I mean done",
    "garbage line",
    "[L31 14:13:31.250] LEC -> PIT: BOX now?",
]


def test_parse_radio():
    msg = parse_radio(LINES[0])
    assert msg == {"lap": 23, "time": "14:02:11.532", "sender": "VER", "receiver": "PIT",
                   "message": "Box box, box this lap"}
    assert parse_radio(LINES[1])["message"] == "Copy. Target 1:22.900"
    assert parse_radio(LINES[3]) is None


def test_extract_laptimes():
    assert extract_laptimes("P1 1:22.900, then 1:23.050; not 12:30.000 or 1:75.000") == [82_900, 83_050]


def test_box_calls_whole_word_case_insensitive():
    assert box_calls(LINES) == [23, 31]   # "boxed" must NOT count


def test_redact():
    assert redact_laptimes("Did 1:22.900 and 1:23.000") == "Did X:XX.XXX and X:XX.XXX"
