from fake_useragent import UserAgent
import datetime
import datetime
import random
import string


def encpw(pw):
    time = int(datetime.datetime.now().timestamp())
    return f'#PWD_INSTAGRAM:0:{time}:{[pw]}'


xiaomi = [
    {
        "model": "Redmi 4 Prime",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "markw",
        "hardware": "qcom"
    },
    {
        "model": "MI 6",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "sagit",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4 Z",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "411",
        "brand": "Xiaomi",
        "os": "markw",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3 Pro",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "430",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5A",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "riva",
        "hardware": "qcom"
    },
    {
        "model": "MIBOX3",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "240",
        "brand": "Ugoos",
        "os": "AM3",
        "hardware": "amlogic"
    },
    {
        "model": "Redmi Note 3 PRO",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "POCOPHONE F1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2246",
        "dpi": "461",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "MI NOTE Pro",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "leo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4X",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "288",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "MI Note 2",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "scorpio",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "352",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "MI 8",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2248",
        "dpi": "392",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "redmi note 8",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "cereus",
        "hardware": "mt6765"
    },
    {
        "model": "Redmi Note 7 Pro",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "violet",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1980",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Go",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "272",
        "brand": "Xiaomi",
        "os": "tiare",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5A Prime",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "ugg",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "493",
        "brand": "xiaomi",
        "os": "ginkgo",
        "hardware": "qcom"
    },
    {
        "model": "M2006C3MG",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "Redmi",
        "os": "angelica",
        "hardware": "mt6765"
    },
    {
        "model": "2014811",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "HM2014811",
        "hardware": "qcom"
    },
    {
        "model": "M2007J20CG",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "POCO",
        "os": "surya",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4X",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Mi A1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "tissot_sprout",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4x",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "violet",
        "hardware": "qcom"
    },
    {
        "model": "MI 5s",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "capricorn",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4 x",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "MIX 2",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "chiron",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 8",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "olive",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "374",
        "brand": "xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "Redmi S2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "260",
        "brand": "xiaomi",
        "os": "ysl",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3 32GB",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 2",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "hermes",
        "hardware": "mt6795"
    },
    {
        "model": "POCO F1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2246",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6A",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "cactus",
        "hardware": "mt6762m"
    },
    {
        "model": "MIX 2S",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "polaris",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "Xiaomi",
        "os": "violet",
        "hardware": "qcom"
    },
    {
        "model": "2014818",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "HM2014818",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "MI 8",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2248",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "MIBOX3",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "240",
        "brand": "Xiaomi",
        "os": "KM8_PRO",
        "hardware": "amlogic"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "MI 9",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cepheus",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 3",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "ido",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "378",
        "brand": "Xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3 Pro",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "428",
        "brand": "Xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "MIBOX3",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "240",
        "brand": "Xiaomi",
        "os": "once",
        "hardware": "amlogic"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "MI 3W",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cancro",
        "hardware": "qcom"
    },
    {
        "model": "21061119AG",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "selene",
        "hardware": "mt6768"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "PoisonATV_V4.5",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "200",
        "brand": "PoisonATV_V4.5",
        "os": "PoisonATV_V4.5",
        "hardware": "amlogic"
    },
    {
        "model": "MI 5",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "gemini",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 6 Pro",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "tulip",
        "hardware": "qcom"
    },
    {
        "model": "MIBOX3",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "240",
        "brand": "Xiaomi",
        "os": "once",
        "hardware": "amlogic"
    },
    {
        "model": "BASIC",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "willow",
        "hardware": "qcom"
    },
    {
        "model": "Mi 9T",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "378",
        "brand": "Xiaomi",
        "os": "davinci",
        "hardware": "qcom"
    },
    {
        "model": "POCOPHONE F1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2246",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "HM NOTE 1LTE TD",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "dior",
        "hardware": "dior"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "MI 5",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "gemini",
        "hardware": "qcom"
    },
    {
        "model": "Mi Note 10 Lite",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "toco",
        "hardware": "qcom"
    },
    {
        "model": "MIBOX3",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "once",
        "hardware": "amlogic"
    },
    {
        "model": "Redmi S2",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "ysl",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "384",
        "brand": "xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "M2002J9G",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "monet",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "460",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3 pro SE",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kate",
        "hardware": "qcom"
    },
    {
        "model": "MI 5s",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "capricorn",
        "hardware": "qcom"
    },
    {
        "model": "Pocophone F1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2246",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 Pro",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "MI 6",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "sagit",
        "hardware": "qcom"
    },
    {
        "model": "M2004J19C",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "lancelot",
        "hardware": "mt6768"
    },
    {
        "model": "Redmi Note 5 Pro",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4A",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1280",
        "dpi": "306",
        "brand": "Xiaomi",
        "os": "rolex",
        "hardware": "qcom"
    },
    {
        "model": "Mi Note 3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "jason",
        "hardware": "qcom"
    },
    {
        "model": "MI 5",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "gemini",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "ginkgo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "403",
        "brand": "Xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 2",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "HM2014811",
        "hardware": "qcom"
    },
    {
        "model": "2014818",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "HM2014818",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1440",
        "dpi": "256",
        "brand": "Xiaomi",
        "os": "rosy",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3 pro ",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 7",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "336",
        "brand": "xiaomi",
        "os": "onc",
        "hardware": "qcom"
    },
    {
        "model": "M2012K11C",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "352",
        "brand": "Redmi",
        "os": "haydn",
        "hardware": "qcom"
    },
    {
        "model": "Mi Note 3",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "490",
        "brand": "Xiaomi",
        "os": "jason",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4X",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "nikel",
        "hardware": "mt6797"
    },
    {
        "model": "HM 1SW",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "unknown",
        "hardware": "armani"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "MI 8 Lite",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "platina",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "M2007J3SY",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "490",
        "brand": "Xiaomi",
        "os": "apollo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "503",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX 2",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "384",
        "brand": "Xiaomi",
        "os": "oxygen",
        "hardware": "qcom"
    },
    {
        "model": "M2006C3LVG",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "Redmi",
        "os": "dandelion",
        "hardware": "mt6762"
    },
    {
        "model": "Redmi Y3",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1520",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "onc",
        "hardware": "qcom"
    },
    {
        "model": "Mi A3",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1560",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "laurel_sprout",
        "hardware": "qcom"
    },
    {
        "model": "M2012K11AG",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "POCO",
        "os": "alioth",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "461",
        "brand": "xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "MI 5s",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "capricorn",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 3S",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "Xiaomi",
        "os": "land",
        "hardware": "qcom"
    },
    {
        "model": "MI 5X",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "tiffany",
        "hardware": "qcom"
    },
    {
        "model": "Mi A2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2009",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "jasmine_sprout",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Y1 Lite",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "ugglite",
        "hardware": "qcom"
    },
    {
        "model": "M2003J15SC",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "merlin",
        "hardware": "mt6769z"
    },
    {
        "model": "Redmi S2",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1440",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "ysl",
        "hardware": "qcom"
    },
    {
        "model": "M2102J20SG POCO X3 PRO VAYU",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "POCO",
        "os": "vayu",
        "hardware": "qcom"
    },
    {
        "model": "HM NOTE 1LTE",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "dior",
        "hardware": "dior"
    },
    {
        "model": "M2006C3LG",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1544",
        "dpi": "320",
        "brand": "Redmi",
        "os": "dandelion",
        "hardware": "mt6762"
    },
    {
        "model": "Redmi 4",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "markw",
        "hardware": "qcom"
    },
    {
        "model": "MI 8",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2248",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "M2004J19C",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "421",
        "brand": "Redmi",
        "os": "lancelot",
        "hardware": "mt6768"
    },
    {
        "model": "Redmi Note 2",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "hermes",
        "hardware": "mt6795"
    },
    {
        "model": "poco m2 pro",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "POCO",
        "os": "gram",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "352",
        "brand": "xiaomi",
        "os": "violet",
        "hardware": "qcom"
    },
    {
        "model": "MI 2SC",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "aries",
        "hardware": "qcom"
    },
    {
        "model": "MI 8",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2158",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4X",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Mi A1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "tissot_sprout",
        "hardware": "qcom"
    },
    {
        "model": "2201117TG",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "spes",
        "hardware": "qcom"
    },
    {
        "model": "Mi MIX 2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "432",
        "brand": "Xiaomi",
        "os": "chiron",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX 3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "nitrogen",
        "hardware": "qcom"
    },
    {
        "model": "MI 3W",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cancro",
        "hardware": "qcom"
    },
    {
        "model": "2014817",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "HM2014817",
        "hardware": "qcom"
    },
    {
        "model": "MI 9",
        "sdk": "29",
        "android_version": "10.0",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "cepheus",
        "hardware": "qcom"
    },
    {
        "model": "POCO F1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2156",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "Mi A1",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "tissot_sprout",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "markw",
        "hardware": "qcom"
    },
    {
        "model": "M2102J20SG",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "POCO",
        "os": "vayu",
        "hardware": "qcom"
    },
    {
        "model": "MI 8",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2248",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2264",
        "dpi": "440",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Mi MIX 2",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "chiron",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "hennessy",
        "hardware": "mt6795"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "MI 8 SE",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2158",
        "dpi": "352",
        "brand": "Xiaomi",
        "os": "sirius",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4A",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "rolex",
        "hardware": "qcom"
    },
    {
        "model": "MI 4W",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cancro",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4X",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Mi 9T Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "raphael",
        "hardware": "qcom"
    },
    {
        "model": "MIBOX3",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "280",
        "brand": "Xiaomi",
        "os": "once",
        "hardware": "amlogic"
    },
    {
        "model": "M2007J17G",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "437",
        "brand": "Xiaomi",
        "os": "gauguin",
        "hardware": "qcom"
    },
    {
        "model": "Mi Mix 2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "378",
        "brand": "Xiaomi",
        "os": "chiron",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 2",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "hermes",
        "hardware": "mt6795"
    },
    {
        "model": "2201122C",
        "sdk": "31",
        "android_version": "12",
        "display": "1440x3200",
        "dpi": "560",
        "brand": "Xiaomi",
        "os": "zeus",
        "hardware": "qcom"
    },
    {
        "model": "MI 3W",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cancro",
        "hardware": "qcom"
    },
    {
        "model": "MI PLAY",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "lotus",
        "hardware": "mt6765"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "hennessy",
        "hardware": "mt6795"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "461",
        "brand": "xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "Mi A2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "jasmine_sprout",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "nikel",
        "hardware": "mt6797"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "MI 8 Lite",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "platina",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "432",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "461",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "461",
        "brand": "xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 7 pro",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "onc",
        "hardware": "qcom"
    },
    {
        "model": "Mi-4a",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "libra",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 3S",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "land",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 8",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1520",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "olive",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5A",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "ugg",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K3 Note",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "hermes",
        "hardware": "mt6752"
    },
    {
        "model": "M2003J15SC",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "merlinnfc",
        "hardware": "mt6768"
    },
    {
        "model": "MI PAD 4",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "clover",
        "hardware": "qcom"
    },
    {
        "model": "MIBOX3",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "240",
        "brand": "Xiaomi",
        "os": "once",
        "hardware": "amlogic"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "384",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "21081111RG",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "amber",
        "hardware": "mt6893"
    },
    {
        "model": "POCOPHONE F1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2156",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 3S",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "land",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 6 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "tulip",
        "hardware": "qcom"
    },
    {
        "model": "MI 5C",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "meri",
        "hardware": "meri"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Pro",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "omega",
        "hardware": "mt6797"
    },
    {
        "model": "M2006C3LG",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "235",
        "brand": "Redmi",
        "os": "dandelion",
        "hardware": "mt6762"
    },
    {
        "model": "Redmi 5A",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "riva",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "378",
        "brand": "Xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6A",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "cactus",
        "hardware": "mt6765"
    },
    {
        "model": "MI MAX",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "hydrogen",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5A",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "ugglite",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4X",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "432",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "Redmi Note 8T",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "461",
        "brand": "xiaomi",
        "os": "willow",
        "hardware": "qcom"
    },
    {
        "model": "MI 6X",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "wayne",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "403",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Y1",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "ugg",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 9S",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "curtana",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4x",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "300",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "MI 4S",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "aqua",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 7",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "onc",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4X",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "MI 4W",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "460",
        "brand": "Xiaomi",
        "os": "cancro",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX 2",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "oxygen",
        "hardware": "qcom"
    },
    {
        "model": "Mi A2 Lite",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "daisy_sprout",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 3 pro",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "ido_rifle007",
        "hardware": "qcom"
    },
    {
        "model": "Mi A2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "jasmine_sprout",
        "hardware": "qcom"
    },
    {
        "model": "2201117TG",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "spes",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 9S",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "curtana",
        "hardware": "qcom"
    },
    {
        "model": "MI 9",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "cepheus",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX 2",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "503",
        "brand": "Xiaomi",
        "os": "oxygen",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Mi A2 Lite",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "daisy_sprout",
        "hardware": "qcom"
    },
    {
        "model": "POCOPHONE F1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2246",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "Mi A3",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "laurel_sprout",
        "hardware": "qcom"
    },
    {
        "model": "MI 5s Plus",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "natrium",
        "hardware": "qcom"
    },
    {
        "model": "MI 6",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "sagit",
        "hardware": "qcom"
    },
    {
        "model": "MI NOTE LTE",
        "sdk": "23",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "Xiaomi",
        "os": "virgo",
        "hardware": "qcom"
    },
    {
        "model": "HMNOTE1S",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "HMNOTE1S",
        "hardware": "qcom"
    },
    {
        "model": "21061119DG",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "352",
        "brand": "Redmi",
        "os": "eos",
        "hardware": "mt6768"
    },
    {
        "model": "MI 8",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2038",
        "dpi": "400",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "hydrogen",
        "hardware": "qcom"
    },
    {
        "model": "Mi A1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "tissot_sprout",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3 pro prime",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4X",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "300",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "MI 5C",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "meri",
        "hardware": "song"
    },
    {
        "model": "Mi Note 3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "352",
        "brand": "Xiaomi",
        "os": "jason",
        "hardware": "qcom"
    },
    {
        "model": "2014811",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "HM2014818",
        "hardware": "qcom"
    },
    {
        "model": "MI 2",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "aries",
        "hardware": "qcom"
    },
    {
        "model": "MI 5s Plus",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "natrium",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8T",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "willow",
        "hardware": "qcom"
    },
    {
        "model": "MI 4W",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cancro",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 9 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "joyeuse",
        "hardware": "qcom"
    },
    {
        "model": "MI 5s",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "capricorn",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4X",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "330",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 9 Pro",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "400",
        "brand": "Redmi",
        "os": "joyeuse",
        "hardware": "qcom"
    },
    {
        "model": "Remo Note 8 pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "MI PAD 2",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "latte",
        "hardware": "latte"
    },
    {
        "model": "MI 9",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "cepheus",
        "hardware": "qcom"
    },
    {
        "model": "Mi A2 Lite",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "daisy_sprout",
        "hardware": "qcom"
    },
    {
        "model": "MI 9",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "cepheus",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6A",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "223",
        "brand": "xiaomi",
        "os": "cactus",
        "hardware": "mt6765"
    },
    {
        "model": "M2004J19C",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "461",
        "brand": "Redmi",
        "os": "lancelot",
        "hardware": "mt6768"
    },
    {
        "model": "2201117PG",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "POCO",
        "os": "fleur",
        "hardware": "mt6781"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "384",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Mi-4c",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "libra",
        "hardware": "qcom"
    },
    {
        "model": "Symphony P6 Pro",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Symphony",
        "os": "Symphony P6 Pro",
        "hardware": "mt6735"
    },
    {
        "model": "Mi Note 3",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "jason",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "rosy",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4x",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Mi MIX 2S",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "polaris",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1980",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6 Pro",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "432",
        "brand": "Android",
        "os": "phhgsi_arm64_a",
        "hardware": "qcom"
    },
    {
        "model": "POCO F2 Pro",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "POCO",
        "os": "lmi",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6A",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "256",
        "brand": "xiaomi",
        "os": "cactus",
        "hardware": "mt6765"
    },
    {
        "model": "Redmi 7A",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "pine",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6A",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "360",
        "brand": "xiaomi",
        "os": "cactus",
        "hardware": "mt6765"
    },
    {
        "model": "M2006C3MNG",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "Redmi",
        "os": "angelican",
        "hardware": "mt6765"
    },
    {
        "model": "Redmi S2",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1440",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "ysl",
        "hardware": "qcom"
    },
    {
        "model": "MI 9",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "cepheus",
        "hardware": "qcom"
    },
    {
        "model": "Mi 9T Pro",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "raphael",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 6 Pro",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "tulip",
        "hardware": "qcom"
    },
    {
        "model": "M2004J19C",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "galahad",
        "hardware": "mt6768"
    },
    {
        "model": "Mi A1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "tissot",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "454",
        "brand": "xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "HM 1SW",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "armani",
        "hardware": "armani"
    },
    {
        "model": "M2006C3LC",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "Redmi",
        "os": "dandelion",
        "hardware": "mt6762"
    },
    {
        "model": "Mi-4c",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "Xiaomi",
        "os": "libra",
        "hardware": "libra"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "ginkgo",
        "hardware": "qcom"
    },
    {
        "model": "M2004J19C",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "416",
        "brand": "Redmi",
        "os": "galahad",
        "hardware": "mt6768"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "M2003J15SC",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "merlin",
        "hardware": "mt6768"
    },
    {
        "model": "Redmi Go",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "tiare",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 9 Pro",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "396",
        "brand": "Redmi",
        "os": "joyeuse",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kate",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "272",
        "brand": "xiaomi",
        "os": "cereus",
        "hardware": "mt6762"
    },
    {
        "model": "Mi-4c",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "libra",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8 Pro",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "begonia",
        "hardware": "mt6785"
    },
    {
        "model": "M2102J2SC",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "thyme",
        "hardware": "qcom"
    },
    {
        "model": "Mi A2",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "jasmine_sprout",
        "hardware": "qcom"
    },
    {
        "model": "MI 5",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "gemini",
        "hardware": "qcom"
    },
    {
        "model": "Mi 9T",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "davinci",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 9S",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "352",
        "brand": "Redmi",
        "os": "curtana",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8T",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "willow",
        "hardware": "qcom"
    },
    {
        "model": "2201123G",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "cupid",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3 Pro",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Y2",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "ysl",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8T",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "Xiaomi",
        "os": "willow",
        "hardware": "qcom"
    },
    {
        "model": "Mi Note 2",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "scorpio",
        "hardware": "qcom"
    },
    {
        "model": "Mi A1",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "tissot_sprout",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6 Pro",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "sakura_india",
        "hardware": "qcom"
    },
    {
        "model": "Mi 9 SE",
        "sdk": "29",
        "android_version": "10.0",
        "display": "1080x2340",
        "dpi": "467",
        "brand": "Xiaomi",
        "os": "grus",
        "hardware": "qcom"
    },
    {
        "model": "Mi A1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "tissot_sprout",
        "hardware": "qcom"
    },
    {
        "model": "MI 2S",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "aries",
        "hardware": "qcom"
    },
    {
        "model": "M2003J15SC",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "merlinnfc",
        "hardware": "mt6769z"
    },
    {
        "model": "MI NOTE LTE",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "virgo",
        "hardware": "qcom"
    },
    {
        "model": "HM 1SW",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "armani",
        "hardware": "armani"
    },
    {
        "model": "Redmi 4X",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "220",
        "brand": "Xiaomi",
        "os": "santoni",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "420",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "29",
        "android_version": "10.0",
        "display": "1080x2340",
        "dpi": "421",
        "brand": "xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "xiaomi",
        "os": "cereus",
        "hardware": "mt6762"
    },
    {
        "model": "Mi Note 10 Lite",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2340",
        "dpi": "396",
        "brand": "Xiaomi",
        "os": "toco",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "kenzo",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX PRO",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "helium",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 3",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "ido",
        "hardware": "qcom"
    },
    {
        "model": "M2003J15SC",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "merlinnfc",
        "hardware": "mt6768"
    },
    {
        "model": "MI 6",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "409",
        "brand": "Xiaomi",
        "os": "sagit",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "helium",
        "hardware": "qcom"
    },
    {
        "model": "Mi-4c",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "libra",
        "hardware": "libra"
    },
    {
        "model": "MI 5C",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "meri",
        "hardware": "song"
    },
    {
        "model": "MI 8",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2248",
        "dpi": "360",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4X",
        "sdk": "28",
        "android_version": "9.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "Mi A1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "tissot_sprout",
        "hardware": "qcom"
    },
    {
        "model": "M2102J20SG",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "POCO",
        "os": "vayu",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 3",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "xiaomi",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 2",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "xiaomi",
        "os": "hermes",
        "hardware": "mt6795"
    },
    {
        "model": "Redmi 5",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1320",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "rosy",
        "hardware": "qcom"
    },
    {
        "model": "Mi 9T",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "352",
        "brand": "Xiaomi",
        "os": "davinci",
        "hardware": "qcom"
    },
    {
        "model": "Mi 4i",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "ferrari",
        "hardware": "qcom"
    },
    {
        "model": "M2101K7BNY",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "rosemary",
        "hardware": "mt6785"
    },
    {
        "model": "Redmi 3S",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "land",
        "hardware": "qcom"
    },
    {
        "model": "MI 8",
        "sdk": "28",
        "android_version": "9.0",
        "display": "1080x2248",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "dipper",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 7",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1520",
        "dpi": "290",
        "brand": "Xiaomi",
        "os": "onc",
        "hardware": "qcom"
    },
    {
        "model": "Mi 9T",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "davinci",
        "hardware": "qcom"
    },
    {
        "model": "MI 4LTE",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cancro_lte_ct",
        "hardware": "qcom"
    },
    {
        "model": "Mi MIX 2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "chiron",
        "hardware": "qcom"
    },
    {
        "model": "Mi Note 2",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "scorpio",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 8T",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "352",
        "brand": "Xiaomi",
        "os": "willow",
        "hardware": "qcom"
    },
    {
        "model": "M2006C3LG",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "Redmi",
        "os": "dandelion",
        "hardware": "mt6762"
    },
    {
        "model": "M2007J3SC",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "440",
        "brand": "Redmi",
        "os": "apollo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4A",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "rolex",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 7",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "403",
        "brand": "Xiaomi",
        "os": "lavender",
        "hardware": "qcom"
    },
    {
        "model": "M2003J15SC",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "merlinnfc",
        "hardware": "mt6768"
    },
    {
        "model": "MI PLAY",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "384",
        "brand": "xiaomi",
        "os": "lotus",
        "hardware": "mt6765"
    },
    {
        "model": "POCO F1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2246",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "beryllium",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 5 Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "500",
        "brand": "xiaomi",
        "os": "vince",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 2 Prime",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "hermes",
        "hardware": "mt6795"
    },
    {
        "model": "Redmi 7",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "224",
        "brand": "Xiaomi",
        "os": "onc",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 5",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "356",
        "brand": "Xiaomi",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "dandelion",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "250",
        "brand": "Redmi",
        "os": "dandelion",
        "hardware": "mt6762"
    },
    {
        "model": "Redmi Note 8",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "ginkgo",
        "hardware": "qcom"
    },
    {
        "model": "MiBOX3_PRO",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "kungfupanda",
        "hardware": "mt8173"
    },
    {
        "model": "Mi A2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "408",
        "brand": "xiaomi",
        "os": "jasmine_sprout",
        "hardware": "qcom"
    },
    {
        "model": "MI MAX",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "helium",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 6 Pro",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "sakura",
        "hardware": "qcom"
    },
    {
        "model": "MI 8 SE",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2244",
        "dpi": "365",
        "brand": "Xiaomi",
        "os": "sirius",
        "hardware": "qcom"
    },
    {
        "model": "Mi A3",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1560",
        "dpi": "256",
        "brand": "Xiaomi",
        "os": "laurel_sprout",
        "hardware": "qcom"
    },
    {
        "model": "MI 8 Lite",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "Xiaomi",
        "os": "platina",
        "hardware": "qcom"
    },
    {
        "model": "Redmi 4X",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "xiaomi",
        "hardware": "qcom"
    },
    {
        "model": "M2004J19C",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "galahad",
        "hardware": "mt6768"
    },
    {
        "model": "M2004J19C",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Redmi",
        "os": "lancelot",
        "hardware": "mt6768"
    },
    {
        "model": "MiTV4S",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "213",
        "brand": "Xiaomi",
        "os": "vforvendetta",
        "hardware": "mainz"
    },
    {
        "model": "Redmi Y2",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "336",
        "brand": "xiaomi",
        "os": "ysl",
        "hardware": "qcom"
    },
    {
        "model": "MI NOTE PRO",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "215",
        "brand": "Xiaomi",
        "os": "leo",
        "hardware": "qcom"
    },
    {
        "model": "Redmi Note 4",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "378",
        "brand": "Xiaomi",
        "os": "mido",
        "hardware": "qcom"
    },
    {
        "model": "HM NOTE 1LTE",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "dior",
        "hardware": "dior"
    }
]
asus = [
    {
        "model": "Nexus 7",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "google",
        "os": "flo",
        "hardware": "flo"
    },
    {
        "model": "ASUS_X008D",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_X008",
        "hardware": "mt6735"
    },
    {
        "model": "ASUS_I001D",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "asus",
        "os": "ASUS_I001_1",
        "hardware": "qcom"
    },
    {
        "model": "Nexus 7",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "google",
        "os": "deb",
        "hardware": "flo"
    },
    {
        "model": "ASUS_A002",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "476",
        "brand": "asus",
        "os": "ASUS_A002",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z017DA",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z017D_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X008DC",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_X008_1",
        "hardware": "mt6735"
    },
    {
        "model": "ASUS_Z00A",
        "sdk": "25",
        "android_version": "7.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "Z00A",
        "hardware": "mofd_v1"
    },
    {
        "model": "ASUS_X008D",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_X008",
        "hardware": "mt6735"
    },
    {
        "model": "ASUS_X018D",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X018_4",
        "hardware": "mt6755"
    },
    {
        "model": "ASUS_X008DC",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "272",
        "brand": "asus",
        "os": "ASUS_X008_1",
        "hardware": "mt6735"
    },
    {
        "model": "ASUS_X01BDA",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X01BD_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z012DC",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z012D",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z017D",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z017D_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00TD",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_2",
        "hardware": "qcom"
    },
    {
        "model": "P00C",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "160",
        "brand": "asus",
        "os": "P00C_2",
        "hardware": "mt8163"
    },
    {
        "model": "ASUS_I001DE",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "asus",
        "os": "ASUS_I001_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_I001DE",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "460",
        "brand": "asus",
        "os": "ASUS_I001_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00TDB",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_2",
        "hardware": "qcom"
    },
    {
        "model": "Z00D",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "288",
        "brand": "asus",
        "os": "ASUS_Z00D",
        "hardware": "redhookbay"
    },
    {
        "model": "MeMOPAD 10FHD Lte",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "google",
        "os": "deb",
        "hardware": "msm8960"
    },
    {
        "model": "ASUS_X008D",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_X008_1",
        "hardware": "mt6735"
    },
    {
        "model": "ASUS_Z012D",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z012D",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z016D",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "Z016",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00TDB",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_4",
        "hardware": "qcom"
    },
    {
        "model": "Z00D",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "288",
        "brand": "asus",
        "os": "ASUS_Z00D",
        "hardware": "redhookbay"
    },
    {
        "model": "ASUS_X008D",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "272",
        "brand": "asus",
        "os": "ASUS_X008_1",
        "hardware": "mt6735"
    },
    {
        "model": "ZB602KL",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "540",
        "brand": "asus",
        "os": "ASUS_X00T_6",
        "hardware": "qcom"
    },
    {
        "model": "ZE520KL",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z017D_1",
        "hardware": "qcom"
    },
    {
        "model": "P027",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "asus",
        "os": "P027",
        "hardware": "mt8173"
    },
    {
        "model": "Nexus 7 3G",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Google",
        "os": "tilapia",
        "hardware": "grouper"
    },
    {
        "model": "ASUS_X00TDB",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_2",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00GD",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "272",
        "brand": "asus",
        "os": "ASUS_X00G_1",
        "hardware": "mt6755"
    },
    {
        "model": "ZD552KL",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z01M_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00RD",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_X00R_3",
        "hardware": "qcom"
    },
    {
        "model": "Nexus 7 LTE",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Android",
        "os": "deb",
        "hardware": "flo"
    },
    {
        "model": "ASUS_A002",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "asus",
        "os": "ASUS_A002",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X018D",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X018_4",
        "hardware": "mt6755"
    },
    {
        "model": "Nexus 7",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1200x1920",
        "dpi": "420",
        "brand": "google",
        "os": "deb",
        "hardware": "flo"
    },
    {
        "model": "ASUS_X00TD",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_2",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X008DA",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "272",
        "brand": "asus",
        "os": "ASUS_X008",
        "hardware": "mt6735"
    },
    {
        "model": "Zenfone Max Pro M1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "427",
        "brand": "asus",
        "os": "ASUS_X00T_3",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00TD",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_4",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00TDB",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_4",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X018D",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_X018_4",
        "hardware": "mt6755"
    },
    {
        "model": "ASUS_Z012D",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z012D",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z012DA",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z012D",
        "hardware": "qcom"
    },
    {
        "model": "ZC551KL",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "Z01B_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z00LD",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_Z00L",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_I001DE",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "asus",
        "os": "ASUS_I001_1",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z012DB",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_Z012D",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_Z01QD",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "900x1600",
        "dpi": "240",
        "brand": "asus",
        "os": "ASUS_I001_1",
        "hardware": "qcom"
    },
    {
        "model": "ZenFone Max Pro M1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "420",
        "brand": "asus",
        "os": "ASUS_X00T_2",
        "hardware": "qcom"
    },
    {
        "model": "Zenfone Max Pro M1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "429",
        "brand": "asus",
        "os": "X00T",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00TD",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "asus",
        "os": "ASUS_X00T_3",
        "hardware": "qcom"
    },
    {
        "model": "ASUS_X00GD",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_X00G_1",
        "hardware": "mt6755"
    },
    {
        "model": "P00I",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "asus",
        "os": "P00I",
        "hardware": "qcom"
    },
    {
        "model": "P00A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "asus",
        "os": "P00A_2",
        "hardware": "mt8163"
    },
    {
        "model": "ASUS_Z012D",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "asus",
        "os": "ASUS_Z012D",
        "hardware": "qcom"
    }
]
google = [
    {
        "model": "Acer Chromebook 15 (C910 / CB5-571)",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "412x731",
        "dpi": "160",
        "brand": "google",
        "os": "yuna_cheets",
        "hardware": "cheets"
    },
    {
        "model": "octopus",
        "sdk": "28",
        "android_version": "9",
        "display": "651x1211",
        "dpi": "160",
        "brand": "google",
        "os": "octopus_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Acer Chromebook R11 (CB5-132T / C738T / CB3-132)",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "412x1366",
        "dpi": "160",
        "brand": "google",
        "os": "cyan_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Pixel 2 XL",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1440x2880",
        "dpi": "560",
        "brand": "google",
        "os": "taimen",
        "hardware": "taimen"
    },
    {
        "model": "Samsung Chromebook 3",
        "sdk": "28",
        "android_version": "9",
        "display": "688x1280",
        "dpi": "160",
        "brand": "google",
        "os": "celes_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Pixel 2 XL",
        "sdk": "30",
        "android_version": "11",
        "display": "1440x2880",
        "dpi": "495",
        "brand": "google",
        "os": "taimen",
        "hardware": "taimen"
    },
    {
        "model": "Pixel 2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "460",
        "brand": "google",
        "os": "walleye",
        "hardware": "walleye"
    },
    {
        "model": "Pixel 2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "google",
        "os": "walleye",
        "hardware": "walleye"
    },
    {
        "model": "Pixelbook",
        "sdk": "28",
        "android_version": "9",
        "display": "618x1098",
        "dpi": "240",
        "brand": "google",
        "os": "eve_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Pixel 2 XL",
        "sdk": "28",
        "android_version": "9.0",
        "display": "1080x2160",
        "dpi": "420",
        "brand": "Google",
        "os": "whyred",
        "hardware": "qcom"
    },
    {
        "model": "Pixel",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "google",
        "os": "sailfish",
        "hardware": "sailfish"
    },
    {
        "model": "Pixel 4 XL",
        "sdk": "33",
        "android_version": "13",
        "display": "1440x3040",
        "dpi": "612",
        "brand": "google",
        "os": "coral",
        "hardware": "coral"
    },
    {
        "model": "Pixel 6",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "google",
        "os": "oriole",
        "hardware": "oriole"
    },
    {
        "model": "Pixel 4 XL",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "google",
        "os": "coral",
        "hardware": "jp6"
    },
    {
        "model": "nami",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "412x1136",
        "dpi": "160",
        "brand": "google",
        "os": "nami_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Pixel 2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "google",
        "os": "walleye",
        "hardware": "walleye"
    },
    {
        "model": "Pixel XL",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1440x2560",
        "dpi": "418",
        "brand": "google",
        "os": "marlin",
        "hardware": "marlin"
    },
    {
        "model": "Samsung Chromebook 3",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "667x1187",
        "dpi": "176",
        "brand": "google",
        "os": "celes_cheets",
        "hardware": "cheets"
    },
    {
        "model": "coral",
        "sdk": "28",
        "android_version": "9",
        "display": "980x1823",
        "dpi": "160",
        "brand": "google",
        "os": "coral_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Pixel 3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "google",
        "os": "blueline",
        "hardware": "blueline"
    },
    {
        "model": "Pixel 2 XL",
        "sdk": "28",
        "android_version": "9",
        "display": "1440x2880",
        "dpi": "560",
        "brand": "google",
        "os": "taimen",
        "hardware": "taimen"
    },
    {
        "model": "Pixel 2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "356",
        "brand": "google",
        "os": "walleye",
        "hardware": "walleye"
    },
    {
        "model": "Pixel 2",
        "sdk": "23",
        "android_version": "8.0",
        "display": "480x854",
        "dpi": "213",
        "brand": "Google",
        "os": "Pixel 2",
        "hardware": "mt6735"
    },
    {
        "model": "octopus",
        "sdk": "28",
        "android_version": "9",
        "display": "688x1280",
        "dpi": "160",
        "brand": "google",
        "os": "octopus_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Pixel 4 XL",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "180",
        "brand": "google",
        "os": "coral",
        "hardware": "jp6"
    },
    {
        "model": "Pixel 4a (5G)",
        "sdk": "33",
        "android_version": "13",
        "display": "1080x2340",
        "dpi": "356",
        "brand": "google",
        "os": "bramble",
        "hardware": "bramble"
    },
    {
        "model": "Pixel 2 XL",
        "sdk": "29",
        "android_version": "10",
        "display": "1440x2880",
        "dpi": "612",
        "brand": "google",
        "os": "taimen",
        "hardware": "taimen"
    },
    {
        "model": "Mediatek MT8173 Chromebook",
        "sdk": "28",
        "android_version": "9",
        "display": "587x1092",
        "dpi": "160",
        "brand": "google",
        "os": "hana_cheets",
        "hardware": "cheets"
    },
    {
        "model": "Pixel 3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "420",
        "brand": "google",
        "os": "blueline",
        "hardware": "qcom"
    },
    {
        "model": "Pixel 2",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "google",
        "os": "walleye",
        "hardware": "walleye"
    },
    {
        "model": "Pixel 5a",
        "sdk": "33",
        "android_version": "13",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "google",
        "os": "barbet",
        "hardware": "barbet"
    },
    {
        "model": "Pixel 6 Pro",
        "sdk": "33",
        "android_version": "13",
        "display": "1440x3120",
        "dpi": "560",
        "brand": "google",
        "os": "raven",
        "hardware": "raven"
    },
    {
        "model": "Pixel 3",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "google",
        "os": "blueline",
        "hardware": "blueline"
    },
    {
        "model": "Pixel 4",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "google",
        "os": "flame",
        "hardware": "flame"
    },
    {
        "model": "Pixel 6",
        "sdk": "33",
        "android_version": "13",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "google",
        "os": "oriole",
        "hardware": "oriole"
    },
    {
        "model": "Pixel 4 XL(JP6s)",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "google",
        "os": "coral",
        "hardware": "jp6"
    },
    {
        "model": "Pixel XL",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "marlin",
        "hardware": "marlin"
    },
    {
        "model": "octopus",
        "sdk": "30",
        "android_version": "11",
        "display": "412x768",
        "dpi": "160",
        "brand": "google",
        "os": "octopus_cheets",
        "hardware": "bertha"
    },
    {
        "model": "sunfish",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "450",
        "brand": "OnePlus",
        "os": "OnePlus7",
        "hardware": "qcom"
    },
    {
        "model": "Chromebox Reference",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "412x900",
        "dpi": "160",
        "brand": "google",
        "os": "fizz_cheets",
        "hardware": "cheets"
    },
    {
        "model": "dedede",
        "sdk": "30",
        "android_version": "11",
        "display": "412x768",
        "dpi": "160",
        "brand": "google",
        "os": "dedede_cheets",
        "hardware": "bertha"
    },
    {
        "model": "Pixel XL",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "marlin",
        "hardware": "marlin"
    },
    {
        "model": "Android SDK built for x86",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "google",
        "os": "generic_x86",
        "hardware": "ranchu"
    },
    {
        "model": "Pixel",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "google",
        "os": "sailfish",
        "hardware": "sailfish"
    },
    {
        "model": "MBOX",
        "sdk": "22",
        "android_version": "11.1",
        "display": "720x1280",
        "dpi": "160",
        "brand": "google",
        "os": "walleye",
        "hardware": "amlogic"
    },
    {
        "model": "Pixel",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "google",
        "os": "sailfish",
        "hardware": "sailfish"
    },
    {
        "model": "Pixel XL",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "marlin",
        "hardware": "marlin"
    },
    {
        "model": "Pixel 6 Pro",
        "sdk": "31",
        "android_version": "12",
        "display": "1440x3120",
        "dpi": "560",
        "brand": "google",
        "os": "raven",
        "hardware": "raven"
    }
]
huawei = [
    {
        "model": "ATH-TL00H",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWATH",
        "hardware": "qcom"
    },
    {
        "model": "MRD-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWMRD-M1",
        "hardware": "mt6761"
    },
    {
        "model": "LYA-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWLYA",
        "hardware": "kirin980"
    },
    {
        "model": "MYA-U29",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWMYA-U6580",
        "hardware": "mt6580"
    },
    {
        "model": "AGS2-W09",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWAGS2",
        "hardware": "hi6250"
    },
    {
        "model": "MRX-AL09",
        "sdk": "29",
        "android_version": "10",
        "display": "1600x2560",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWMRX",
        "hardware": "kirin990"
    },
    {
        "model": "JKM-LX2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWJKM-H",
        "hardware": "kirin710"
    },
    {
        "model": "STF-L09S",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWSTF",
        "hardware": "hi3660"
    },
    {
        "model": "JAT-LX3",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1336",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWJAT-M",
        "hardware": "mt6765"
    },
    {
        "model": "INE-LX2r",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "HMA-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWHMA",
        "hardware": "kirin980"
    },
    {
        "model": "CUN-L22",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCUN-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "KOB-L09C100B279 ",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1223",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWKobe-Q",
        "hardware": "qcom"
    },
    {
        "model": "SCL-L21",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwSCL-Q",
        "hardware": "qcom"
    },
    {
        "model": "NEM-L21",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNNEM-H",
        "hardware": "hi6250"
    },
    {
        "model": "JSN-L21",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "INE-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "PLK-L01",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWPLK",
        "hardware": "hi3635"
    },
    {
        "model": "GRA-L09 ",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWGRA",
        "hardware": "hi3635"
    },
    {
        "model": "BAH-W09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWBAH-Q",
        "hardware": "qcom"
    },
    {
        "model": "Hol-U19",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "rainbow",
        "hardware": "mt6582"
    },
    {
        "model": "ALP-L09",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWALP",
        "hardware": "kirin970"
    },
    {
        "model": "MRD-LX1F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "272",
        "brand": "HUAWEI",
        "os": "HWMRD-M1",
        "hardware": "mt6761"
    },
    {
        "model": "VIE-L29",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWVIE",
        "hardware": "hi3650"
    },
    {
        "model": "LLD-AL10",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWLLD-H",
        "hardware": "hi6250"
    },
    {
        "model": "VNS-L31",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "PLK",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWPLK",
        "hardware": "hi3635"
    },
    {
        "model": "KOB-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1223",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWKobe-Q",
        "hardware": "qcom"
    },
    {
        "model": "NXT-L29",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWNXT",
        "hardware": "hi3650"
    },
    {
        "model": "KII-L22",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "HUAWEI",
        "os": "HWKII-Q",
        "hardware": "qcom"
    },
    {
        "model": "ALE-L21",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "C 8816",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1701",
        "hardware": "qcom"
    },
    {
        "model": "P8",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWGRA",
        "hardware": "hi3635"
    },
    {
        "model": "H710VL",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWH710VL-Q",
        "hardware": "qcom"
    },
    {
        "model": "hi6210sft",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "hi6210sft"
    },
    {
        "model": "RNE-L22",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWRNE",
        "hardware": "hi6250"
    },
    {
        "model": "H60-L04",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwH60",
        "hardware": "hi3630"
    },
    {
        "model": "Hauwei P8 lite",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "P7-L10",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwp7",
        "hardware": "hi6620oem"
    },
    {
        "model": "RIO-L01",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "hwRIO-L01",
        "hardware": "qcom"
    },
    {
        "model": "TAG-L21",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTAG-L6753",
        "hardware": "mt6735"
    },
    {
        "model": "ATU-L31",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWATU-QG",
        "hardware": "qcom"
    },
    {
        "model": "POT-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPOT-H",
        "hardware": "kirin710"
    },
    {
        "model": "HUAWEI P9 lite",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "336",
        "brand": "honor",
        "os": "hi6250",
        "hardware": "hi6250"
    },
    {
        "model": "KII-L21",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWKII-Q",
        "hardware": "qcom"
    },
    {
        "model": "Nexus 6P",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "angler",
        "hardware": "angler"
    },
    {
        "model": "MT7-TL10",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwmt7",
        "hardware": "hi3630"
    },
    {
        "model": "560-L01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWY560-L",
        "hardware": "qcom"
    },
    {
        "model": "VTR-L29",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVTR",
        "hardware": "hi3660"
    },
    {
        "model": "WAS-LX1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWWAS-H",
        "hardware": "hi6250"
    },
    {
        "model": "AGS-W09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "181",
        "brand": "HUAWEI",
        "os": "HWAGS-Q",
        "hardware": "qcom"
    },
    {
        "model": "LLD-L31",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWLLD-H",
        "hardware": "hi6250"
    },
    {
        "model": "CUN-U29",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCUN-U6582",
        "hardware": "mt6582"
    },
    {
        "model": "COL-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "540",
        "brand": "HONOR",
        "os": "HWCOL",
        "hardware": "kirin970"
    },
    {
        "model": "JAT-L41",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWJAT-M",
        "hardware": "mt6765"
    },
    {
        "model": "DUK-L09",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWDUK",
        "hardware": "hi3660"
    },
    {
        "model": "CAM-L22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1196",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCAM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "NEM-L51",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNNEM-H",
        "hardware": "hi6250"
    },
    {
        "model": "BLA-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWBLA",
        "hardware": "kirin970"
    },
    {
        "model": "LYO-L01",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWLYO-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "ATH-UL01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWATH",
        "hardware": "qcom"
    },
    {
        "model": "RIO-L01",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "hwRIO-L01",
        "hardware": "qcom"
    },
    {
        "model": "CHM-U01",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "unknown",
        "hardware": "hi6210sft"
    },
    {
        "model": "HRY-LX1T",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWHRY-HF",
        "hardware": "kirin710"
    },
    {
        "model": "COR-AL00",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWCOR",
        "hardware": "kirin970"
    },
    {
        "model": "TIT-AL00",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWTIT-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "BLA-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWBLA",
        "hardware": "kirin970"
    },
    {
        "model": "SCL-U31",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1196",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwSCLU-Q",
        "hardware": "qcom"
    },
    {
        "model": "KIW-L21",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "Y560-L01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "230",
        "brand": "HUAWEI",
        "os": "HWY560-L",
        "hardware": "qcom"
    },
    {
        "model": "MYA-L13",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWMYA-L6737",
        "hardware": "mt6735"
    },
    {
        "model": "CUN-L21",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCUN-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "RNE-L22",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWRNE",
        "hardware": "hi6250"
    },
    {
        "model": "TAG-L22",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTAG-L6753",
        "hardware": "mt6735"
    },
    {
        "model": "STK-LX3",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "VTR-L29",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVTR",
        "hardware": "hi3660"
    },
    {
        "model": "SNE-LX3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWSNE",
        "hardware": "kirin710"
    },
    {
        "model": "H60-L04",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwH60",
        "hardware": "hi3630"
    },
    {
        "model": "EML-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1496",
        "dpi": "272",
        "brand": "HUAWEI",
        "os": "HWEML",
        "hardware": "kirin970"
    },
    {
        "model": "BND-L21",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "JNY-LX2",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2310",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWJNY",
        "hardware": "kirin810"
    },
    {
        "model": "MAR-LX3Bm",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2312",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWMAR",
        "hardware": "kirin710"
    },
    {
        "model": "Y560-L01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWY560-L",
        "hardware": "qcom"
    },
    {
        "model": "SLA-L22",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWSLA-Q",
        "hardware": "qcom"
    },
    {
        "model": "VNS-L53 ",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "ALE-L21",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "MHA-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWMHA",
        "hardware": "hi3660"
    },
    {
        "model": "PAR-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWPAR",
        "hardware": "kirin970"
    },
    {
        "model": "BLL-L22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "DUA-L22",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWDUA-M",
        "hardware": "mt6739"
    },
    {
        "model": "INE-LX2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "YAL-L21",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWYAL",
        "hardware": "kirin980"
    },
    {
        "model": "AGS-L03",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "HWAGS-Q",
        "hardware": "qcom"
    },
    {
        "model": "JNY-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2310",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWJNY",
        "hardware": "kirin810"
    },
    {
        "model": "DLI-TL20",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWDLI-Q",
        "hardware": "qcom"
    },
    {
        "model": "H1711",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWH1711-Q",
        "hardware": "qcom"
    },
    {
        "model": "KOB-W09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWKobe-Q",
        "hardware": "qcom"
    },
    {
        "model": "BLL-L22",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "HUAWEI",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "TIT-AL00",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTIT-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "ALE-UL00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "Y5",
        "sdk": "23",
        "android_version": "6.1.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Huawei",
        "os": "y560",
        "hardware": "qcom"
    },
    {
        "model": "P20 Pro",
        "sdk": "22",
        "android_version": "8.1",
        "display": "480x960",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "P20 Pro",
        "hardware": "mt6580"
    },
    {
        "model": "BLN-L22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "BND-L21",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "JSN-L21",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "GEM-703L",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1200x1920",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWGemini",
        "hardware": "hi3635"
    },
    {
        "model": "NMO-L31",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWNMO-H",
        "hardware": "hi6250"
    },
    {
        "model": "ALE-L02",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "MHA-AL00",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWMHA",
        "hardware": "hi3660"
    },
    {
        "model": "AGS2-W09EEA",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWAGS2",
        "hardware": "hi6250"
    },
    {
        "model": "JSN-L22",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2340",
        "dpi": "540",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "ALE-L02",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "STK-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1560",
        "dpi": "272",
        "brand": "HONOR",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "cro-l22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWCRO-L6737M",
        "hardware": "mt6735"
    },
    {
        "model": "EVA-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWEVA",
        "hardware": "hi3650"
    },
    {
        "model": "ELE-L09",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWELE",
        "hardware": "kirin980"
    },
    {
        "model": "DUB-LX3",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWDUB-Q",
        "hardware": "qcom"
    },
    {
        "model": "JSN-L42",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "540",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "FIG-LA1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWFIG-H",
        "hardware": "hi6250"
    },
    {
        "model": "STK-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "KOB-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWKobe-Q",
        "hardware": "qcom"
    },
    {
        "model": "JSN-L22",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "HLK-AL00",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWHLK-H",
        "hardware": "kirin810"
    },
    {
        "model": "MAR-LX1A",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2312",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWMAR",
        "hardware": "kirin710"
    },
    {
        "model": "PRA-LX1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "ANE-LX1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWANE",
        "hardware": "hi6250"
    },
    {
        "model": "Y541-U02",
        "sdk": "21",
        "android_version": "4.4.2",
        "display": "480x854",
        "dpi": "240",
        "brand": "Samsung",
        "os": "SM-N900S",
        "hardware": "sc8830"
    },
    {
        "model": "RNE-L21",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWRNE",
        "hardware": "hi6250"
    },
    {
        "model": "ATH-Ulo1",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "TECNO",
        "os": "TECNO-C8",
        "hardware": "mt6735"
    },
    {
        "model": "PRA-TL10",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "ALE-L23",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "BGO-DL09",
        "sdk": "23",
        "android_version": "6.0",
        "display": "600x976",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "hwbgo",
        "hardware": "sc8830"
    },
    {
        "model": "STK-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "y5",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5nlte",
        "hardware": "qcom"
    },
    {
        "model": "ALE-L21",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "BLN-L21",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "400",
        "brand": "HONOR",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "FRD-L04",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWFRD",
        "hardware": "hi3650"
    },
    {
        "model": "INE-LX2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "BTV-DL09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1600x2560",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "hwbeethoven",
        "hardware": "hi3650"
    },
    {
        "model": "H1611",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "300",
        "brand": "HUAWEI",
        "os": "HWH1611-Q",
        "hardware": "qcom"
    },
    {
        "model": "CRO-L22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWCRO-L6737M",
        "hardware": "mt6735"
    },
    {
        "model": "EDI-AL10",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "HUAWEI",
        "os": "hwedison",
        "hardware": "hi3650"
    },
    {
        "model": "P6 Pro Lt",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWJMM",
        "hardware": "mt6735"
    },
    {
        "model": "P30 Pro",
        "sdk": "22",
        "android_version": "9.1",
        "display": "540x1140",
        "dpi": "240",
        "brand": "Android",
        "os": "P30 Pro",
        "hardware": "mt6580"
    },
    {
        "model": "Nexus 6P",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "angler",
        "hardware": "angler"
    },
    {
        "model": "FRD-L09",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWFRD",
        "hardware": "hi3650"
    },
    {
        "model": "WLZ-AL10",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWWLZ",
        "hardware": "kirin990"
    },
    {
        "model": "ATH-UL01",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWATH",
        "hardware": "qcom"
    },
    {
        "model": "Nexus 6P",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1440x2417",
        "dpi": "476",
        "brand": "google",
        "os": "angler",
        "hardware": "angler"
    },
    {
        "model": "MYA-L41",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWMYA-L6737",
        "hardware": "mt6735"
    },
    {
        "model": "STF-L09",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWSTF",
        "hardware": "hi3660"
    },
    {
        "model": "EDI-AL10",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "HUAWEI",
        "os": "hwedison",
        "hardware": "hi3650"
    },
    {
        "model": "CHC-U01",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwCHC-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "M2-A01L",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "hwliszt",
        "hardware": "hi3635"
    },
    {
        "model": "VNS-AL00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-Q",
        "hardware": "qcom"
    },
    {
        "model": "KII-L22",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWKII-Q",
        "hardware": "qcom"
    },
    {
        "model": "YAL-L41",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "411",
        "brand": "HONOR",
        "os": "HWYAL",
        "hardware": "kirin980"
    },
    {
        "model": "EDI-AL10",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "HUAWEI",
        "os": "hwedison",
        "hardware": "hi3650"
    },
    {
        "model": "RNE-L21",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "440",
        "brand": "HUAWEI",
        "os": "HWRNE",
        "hardware": "hi6250"
    },
    {
        "model": "H60-L02",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwH60",
        "hardware": "hi3630"
    },
    {
        "model": "Nexus 6P",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "angler",
        "hardware": "angler"
    },
    {
        "model": "BTV-DL09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1600x2560",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "hwbeethoven",
        "hardware": "hi3650"
    },
    {
        "model": "MAR-LX1A",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2312",
        "dpi": "540",
        "brand": "HUAWEI",
        "os": "HWMAR",
        "hardware": "kirin710"
    },
    {
        "model": "CRO-U00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWCRO-U6580M",
        "hardware": "mt6580"
    },
    {
        "model": "INE-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "JAT-LX3",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWJAT-M",
        "hardware": "mt6765"
    },
    {
        "model": "BG2-W09",
        "sdk": "23",
        "android_version": "6.0",
        "display": "600x976",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "hwbg2",
        "hardware": "mt8127"
    },
    {
        "model": "MHA-L29",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWMHA",
        "hardware": "hi3660"
    },
    {
        "model": "BLA-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "272",
        "brand": "HUAWEI",
        "os": "HWBLA",
        "hardware": "kirin970"
    },
    {
        "model": "HRY-LX1T",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWHRY-HF",
        "hardware": "kirin710"
    },
    {
        "model": "M2-801L",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWMozart",
        "hardware": "hi3635"
    },
    {
        "model": "DIG-AL00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWDIG-L8940",
        "hardware": "qcom"
    },
    {
        "model": "STK-L21",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "DUK-AL20",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "HONOR",
        "os": "HWDUK",
        "hardware": "hi3660"
    },
    {
        "model": "Nexus 6P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "angler",
        "hardware": "angler"
    },
    {
        "model": "HMA-AL00",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWHMA",
        "hardware": "kirin980"
    },
    {
        "model": "TRT-L21A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "303",
        "brand": "HUAWEI",
        "os": "HWTRT-Q",
        "hardware": "qcom"
    },
    {
        "model": "VNS-L31",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "STF-L09",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWSTF",
        "hardware": "hi3660"
    },
    {
        "model": "FRD-L19",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "honor",
        "os": "HWFRD",
        "hardware": "hi3650"
    },
    {
        "model": "SNE-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWSNE",
        "hardware": "kirin710"
    },
    {
        "model": "VOG-AL00",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVOG",
        "hardware": "kirin985"
    },
    {
        "model": "TIT-U02",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTIT-U6582",
        "hardware": "mt6582"
    },
    {
        "model": "BLN-L24",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "BND-L21",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "408",
        "brand": "HONOR",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "VOG-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVOG",
        "hardware": "kirin980"
    },
    {
        "model": "GRA-UL00",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWGRA",
        "hardware": "hi3635"
    },
    {
        "model": "JSN-L22",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "JAT-AL00",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWJAT-M",
        "hardware": "mt6765"
    },
    {
        "model": "EVR-AN00",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWEVR",
        "hardware": "kirin980"
    },
    {
        "model": "ANE-LX3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWANE",
        "hardware": "hi6250"
    },
    {
        "model": "EVA-L09",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWEVA",
        "hardware": "hi3650"
    },
    {
        "model": "GRA-L09",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWGRA",
        "hardware": "hi3635"
    },
    {
        "model": "DLI-L42",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWDLI-Q",
        "hardware": "qcom"
    },
    {
        "model": "NEM-L51",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNNEM-H",
        "hardware": "hi6250"
    },
    {
        "model": "JSN-L21",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "Che1-L04",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "Che1-L04",
        "hardware": "qcom"
    },
    {
        "model": "ANE-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWANE",
        "hardware": "hi6250"
    },
    {
        "model": "CLT-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2240",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWCLT",
        "hardware": "kirin970"
    },
    {
        "model": "X1 7.0",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1200x1920",
        "dpi": "400",
        "brand": "Huawei",
        "os": "hw7d501l",
        "hardware": "hi6620oem"
    },
    {
        "model": "VNS-AL00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "360",
        "brand": "HUAWEI",
        "os": "HWVNS-Q",
        "hardware": "qcom"
    },
    {
        "model": "COL-L29",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWCOL",
        "hardware": "kirin970"
    },
    {
        "model": "y538a1",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "221",
        "brand": "generic",
        "os": "y6",
        "hardware": "qcom"
    },
    {
        "model": "TRT-LX1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTRT-Q",
        "hardware": "qcom"
    },
    {
        "model": "STK-LX3",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "JDN-AL00",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwjdn",
        "hardware": "qcom"
    },
    {
        "model": "STK-LX3",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "CAM-L21",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCAM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "MT7-TL10",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Huawei",
        "os": "hwmt7",
        "hardware": "hi3630"
    },
    {
        "model": "WAS-LX1A",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWWAS-H",
        "hardware": "hi6250"
    },
    {
        "model": "BAH3-W09",
        "sdk": "29",
        "android_version": "10",
        "display": "1200x2000",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWBAH3",
        "hardware": "kirin810"
    },
    {
        "model": "HONOR 10 COL-L29",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWCOL",
        "hardware": "kirin970"
    },
    {
        "model": "Huawei",
        "sdk": "27",
        "android_version": "4.4.2",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Samsung",
        "os": "hwt1701",
        "hardware": "sc8830"
    },
    {
        "model": "LuA U22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "nikel",
        "hardware": "mt6797"
    },
    {
        "model": "LYO-L02",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWLYO-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "Che1-CL20",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Honor",
        "os": "Che1",
        "hardware": "qcom"
    },
    {
        "model": "P8 Lite",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "240",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "hi6210sft"
    },
    {
        "model": "hi6210sft",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "hi6210sft"
    },
    {
        "model": "LIO-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1176x2400",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWLIO",
        "hardware": "kirin990"
    },
    {
        "model": "TIT-L01",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTIT-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "CUN-U29",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCUN-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "STF-AL10",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWSTF",
        "hardware": "hi3660"
    },
    {
        "model": "VTR-AL00",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "Huawei",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "EVA-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "345",
        "brand": "HUAWEI",
        "os": "HWEVA",
        "hardware": "hi3650"
    },
    {
        "model": "G8",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "hwRIO-L01",
        "hardware": "qcom"
    },
    {
        "model": "RIO-L01",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "hwRIO-L01",
        "hardware": "qcom"
    },
    {
        "model": "ELE-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWELE",
        "hardware": "kirin980"
    },
    {
        "model": "HMA-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWHMA",
        "hardware": "kirin980"
    },
    {
        "model": "AGS-W09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "HWAGS-Q",
        "hardware": "qcom"
    },
    {
        "model": "VNS-L21",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "VTR-AL00",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVTR",
        "hardware": "hi3660"
    },
    {
        "model": "BG2-W09",
        "sdk": "23",
        "android_version": "6.0",
        "display": "600x1024",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "hwbg2",
        "hardware": "mt8127"
    },
    {
        "model": "GR5 (KII-L21)",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "unknown",
        "hardware": "unknown"
    },
    {
        "model": "INE-LX1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "LUA-U22",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWLUA-U6582",
        "hardware": "mt6582"
    },
    {
        "model": "NEM-L21",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "HONOR",
        "os": "HNNEM-H",
        "hardware": "hi6250"
    },
    {
        "model": "ALE-L02",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "COL-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "408",
        "brand": "HONOR",
        "os": "HWCOL",
        "hardware": "kirin970"
    },
    {
        "model": "PLK-L01",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWPLK",
        "hardware": "hi3635"
    },
    {
        "model": "CHM-U01",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "hi6210sft"
    },
    {
        "model": "p8",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWGRA",
        "hardware": "hi3635"
    },
    {
        "model": "STF-L09",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWSTF",
        "hardware": "hi3660"
    },
    {
        "model": "Y538",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Huawei",
        "os": "hwY538",
        "hardware": "qcom"
    },
    {
        "model": "FLA-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWFLA-H",
        "hardware": "hi6250"
    },
    {
        "model": "AUM-AL00",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWAUM-Q",
        "hardware": "qcom"
    },
    {
        "model": "COL-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWCOL",
        "hardware": "kirin970"
    },
    {
        "model": "VTR-AL00",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVTR",
        "hardware": "hi3660"
    },
    {
        "model": "KII-L21",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "unknown",
        "hardware": "unknown"
    },
    {
        "model": "VNS-L23",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "VKY-AL00",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "HUAWEI",
        "os": "HWVKY",
        "hardware": "hi3660"
    },
    {
        "model": "VTR-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVTR",
        "hardware": "hi3660"
    },
    {
        "model": "PE-TL10",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "Huawei",
        "os": "hwPE",
        "hardware": "hi3630"
    },
    {
        "model": "MT7-CL00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "400",
        "brand": "Huawei",
        "os": "hwmt7",
        "hardware": "hi3630"
    },
    {
        "model": "PRA-LA1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "BAH-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWBAH-Q",
        "hardware": "qcom"
    },
    {
        "model": "CHM-U01",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "290",
        "brand": "Honor",
        "os": "hwCHM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "PPA-LX2",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPPA-H",
        "hardware": "kirin710"
    },
    {
        "model": "PAR-AL00",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPAR",
        "hardware": "kirin970"
    },
    {
        "model": "G620S-L01",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "G620S-L01",
        "hardware": "qcom"
    },
    {
        "model": "ALE-L21",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "hi6210sft"
    },
    {
        "model": "EML-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWEML",
        "hardware": "kirin970"
    },
    {
        "model": "CAZ-AL10",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWCAZ",
        "hardware": "qcom"
    },
    {
        "model": "NXT-AL10",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWNXT",
        "hardware": "hi3650"
    },
    {
        "model": "BKK-LX2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWBKK-Q",
        "hardware": "qcom"
    },
    {
        "model": "AUM-L41",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWAUM-Q",
        "hardware": "qcom"
    },
    {
        "model": "JSN-L22",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "CHM-U01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Honor",
        "os": "hwCHM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "VOG-L09",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVOG",
        "hardware": "kirin980"
    },
    {
        "model": "LND-L29",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWLND-Q",
        "hardware": "qcom"
    },
    {
        "model": "RNE-L21",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWRNE",
        "hardware": "hi6250"
    },
    {
        "model": "BTV-DL09",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1600x2560",
        "dpi": "480",
        "brand": "Huawei",
        "os": "btv",
        "hardware": "hi3650"
    },
    {
        "model": "CHC-U01",
        "sdk": "23",
        "android_version": "6.0",
        "display": "795x1115",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwCHC-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "WAS-TL10",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWWAS-H",
        "hardware": "hi6250"
    },
    {
        "model": "MT7-TL10",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1794",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwmt7",
        "hardware": "hi3630"
    },
    {
        "model": "LYA-L09",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWLYA",
        "hardware": "kirin980"
    },
    {
        "model": "FRD-L19",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWFRD",
        "hardware": "hi3650"
    },
    {
        "model": "INE-LX1r",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "SCL-L32",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwSCL-Q",
        "hardware": "qcom"
    },
    {
        "model": "SCL-L04",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1196",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwSCL-Q",
        "hardware": "qcom"
    },
    {
        "model": "hi6250",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "AMN-LX9",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWAMN-M",
        "hardware": "mt6761"
    },
    {
        "model": "DLI-AL10",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWDLI-Q",
        "hardware": "qcom"
    },
    {
        "model": "V9 Plus",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "KIW-L22",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "AGS-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "181",
        "brand": "HUAWEI",
        "os": "HWAGS-Q",
        "hardware": "qcom"
    },
    {
        "model": "CAM-UL00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWCAM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "LUA-L01",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWLUA-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "GRACE",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWGRA",
        "hardware": "hi3635"
    },
    {
        "model": "LYA-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "540",
        "brand": "HUAWEI",
        "os": "HWLYA",
        "hardware": "kirin980"
    },
    {
        "model": "honor 4x",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "unknown"
    },
    {
        "model": "SNE-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWSNE",
        "hardware": "kirin710"
    },
    {
        "model": "CAN-L11",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "can",
        "hardware": "qcom"
    },
    {
        "model": "ALE-TL00",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "KIW-L22 (Honor 5x)",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "JDN-L01",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwjdn",
        "hardware": "qcom"
    },
    {
        "model": "AMN-LX9",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "272",
        "brand": "HUAWEI",
        "os": "HWAMN-M",
        "hardware": "mt6761"
    },
    {
        "model": "FRD-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWFRD",
        "hardware": "hi3650"
    },
    {
        "model": "AUM-L29",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWAUM-Q",
        "hardware": "qcom"
    },
    {
        "model": "BG2-U01",
        "sdk": "24",
        "android_version": "7.0",
        "display": "600x1024",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "HWBG2",
        "hardware": "sp7731g_1h10"
    },
    {
        "model": "JSN-L21",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "NXT-L29",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWNXT",
        "hardware": "hi3650"
    },
    {
        "model": "VNS-L21",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "ARE-AL00",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWARE-Q",
        "hardware": "qcom"
    },
    {
        "model": "P7-L10",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwp7",
        "hardware": "hi6620oem"
    },
    {
        "model": "LYA-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1440x3120",
        "dpi": "640",
        "brand": "HUAWEI",
        "os": "HWLYA",
        "hardware": "kirin980"
    },
    {
        "model": "TRT-L21A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTRT-Q",
        "hardware": "qcom"
    },
    {
        "model": "YAL-L21",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWYAL",
        "hardware": "kirin980"
    },
    {
        "model": "STF-AL10",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWSTF",
        "hardware": "hi3660"
    },
    {
        "model": "JKM-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWJKM-H",
        "hardware": "kirin710"
    },
    {
        "model": "ANE-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "540",
        "brand": "HUAWEI",
        "os": "HWANE",
        "hardware": "hi6250"
    },
    {
        "model": "BTV",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1600x2560",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "hwbeethoven",
        "hardware": "hi3650"
    },
    {
        "model": "JAT-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWJAT-M",
        "hardware": "mt6765"
    },
    {
        "model": "CAN-L11",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWCAN",
        "hardware": "qcom"
    },
    {
        "model": "AGS-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "HWAGS-Q",
        "hardware": "qcom"
    },
    {
        "model": "KII-L21",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWKII-Q",
        "hardware": "qcom"
    },
    {
        "model": "RNE-L22",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWRNE",
        "hardware": "hi6250"
    },
    {
        "model": "ELS-NX9",
        "sdk": "29",
        "android_version": "10",
        "display": "1200x2640",
        "dpi": "530",
        "brand": "HUAWEI",
        "os": "HWELS",
        "hardware": "kirin990"
    },
    {
        "model": "BND-L21",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "G7-L01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwG7-L01",
        "hardware": "qcom"
    },
    {
        "model": "Che2-L11",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Honor",
        "os": "hwChe2",
        "hardware": "hi6210sft"
    },
    {
        "model": "CHE-TL00H",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Honor",
        "os": "hnCHE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "BTV-DL09",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1600x2560",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "hwbeethoven",
        "hardware": "hi3650"
    },
    {
        "model": "KIW-L24",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "hi6210sft",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "hi6210sft"
    },
    {
        "model": "CLT-L29",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2240",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWCLT",
        "hardware": "kirin970"
    },
    {
        "model": "AMN-LX2",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "272",
        "brand": "HUAWEI",
        "os": "HWAMN-M",
        "hardware": "mt6761"
    },
    {
        "model": "DRA-LX2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWDRA-M",
        "hardware": "mt6739"
    },
    {
        "model": "FIG-LA1",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "360",
        "brand": "HUAWEI",
        "os": "HWFIG-H",
        "hardware": "hi6250"
    },
    {
        "model": "PRA-L21",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "WAS-LX1A",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2312",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWMAR",
        "hardware": "kirin710"
    },
    {
        "model": "JDN2-W09HN",
        "sdk": "28",
        "android_version": "9",
        "display": "1200x1920",
        "dpi": "360",
        "brand": "HONOR",
        "os": "HWJDN2",
        "hardware": "kirin710"
    },
    {
        "model": "VKY-L29",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "unknown",
        "os": "HWD189",
        "hardware": "unknown"
    },
    {
        "model": "YAL-AL00",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWYAL",
        "hardware": "kirin980"
    },
    {
        "model": "ATU-L22",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWATU-QG",
        "hardware": "qcom"
    },
    {
        "model": "VTR-L09",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVTR",
        "hardware": "hi3660"
    },
    {
        "model": "Y538",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x791",
        "dpi": "240",
        "brand": "Huawei",
        "os": "hwY538",
        "hardware": "qcom"
    },
    {
        "model": "ALE-L21",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "LYO-L21",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWLYO-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "BND-L21",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "SCL-L04",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwSCL-Q",
        "hardware": "qcom"
    },
    {
        "model": "TAG-L13",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWTAG-L6753",
        "hardware": "mt6735"
    },
    {
        "model": "MLA-L11",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWMLA",
        "hardware": "qcom"
    },
    {
        "model": "SLA-AL00",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWSLA-Q",
        "hardware": "qcom"
    },
    {
        "model": "HONOR-8",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Honor",
        "os": "frd",
        "hardware": "hi3650"
    },
    {
        "model": "MT7-L09",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwmt7",
        "hardware": "hi3630"
    },
    {
        "model": "Nexus 6P",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "google",
        "os": "angler",
        "hardware": "angler"
    },
    {
        "model": "CAG-L02",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWCAG-L6737M",
        "hardware": "mt6735"
    },
    {
        "model": "BLA-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWBLA",
        "hardware": "kirin970"
    },
    {
        "model": "STK-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "540",
        "brand": "HUAWEI",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "LLD-L21",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWLLD-H",
        "hardware": "hi6250"
    },
    {
        "model": "DRA-L21",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "360",
        "brand": "HUAWEI",
        "os": "HWDRA-M",
        "hardware": "mt6739"
    },
    {
        "model": "VIE-AL10",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "huawei",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "MYA-L22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWMYA-L6737",
        "hardware": "mt6735"
    },
    {
        "model": "BND-L34",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "DUK-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "HONOR",
        "os": "HWDUK",
        "hardware": "hi3660"
    },
    {
        "model": "HRY-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWHRY-H",
        "hardware": "kirin710"
    },
    {
        "model": "LDN-L21",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWLDN-Q",
        "hardware": "qcom"
    },
    {
        "model": "KIW-CL00",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "ARE-L22HN",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWARE-QC",
        "hardware": "qcom"
    },
    {
        "model": "H1611",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWH1611-Q",
        "hardware": "qcom"
    },
    {
        "model": "BG2-U03",
        "sdk": "24",
        "android_version": "7.0",
        "display": "600x1024",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "HWBG2",
        "hardware": "sp7731g_1h10"
    },
    {
        "model": "FIG-LA1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWFIG-H",
        "hardware": "hi6250"
    },
    {
        "model": "JAT-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWJAT-M",
        "hardware": "mt6765"
    },
    {
        "model": "p smart",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWFIG-H",
        "hardware": "hi6250"
    },
    {
        "model": "PRA-LX1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "BLN-L21",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "HONOR",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "BLN-L24",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "HONOR",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "G620S-L01",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "G620S-L01",
        "hardware": "qcom"
    },
    {
        "model": "TIT-L01",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HONOR",
        "os": "HWTIT-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "KOB-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "204",
        "brand": "HUAWEI",
        "os": "HWKobe-Q",
        "hardware": "qcom"
    },
    {
        "model": "MT7-TL10",
        "sdk": "23",
        "android_version": "8.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwmt7",
        "hardware": "hi3630"
    },
    {
        "model": "EVA-L19",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWEVA",
        "hardware": "hi3650"
    },
    {
        "model": "VNS-L31",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "469",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "CLT-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2240",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWCLT",
        "hardware": "kirin970"
    },
    {
        "model": "MAR-LX3Bm",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2312",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWMAR",
        "hardware": "kirin710"
    },
    {
        "model": "HWI-TL00",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWHWI",
        "hardware": "hi3660"
    },
    {
        "model": "KIW-L21",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "BGO-DL09",
        "sdk": "23",
        "android_version": "6.0",
        "display": "600x1024",
        "dpi": "213",
        "brand": "HUAWEI",
        "os": "hwbgo",
        "hardware": "sc8830"
    },
    {
        "model": "LUA-L02",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWLUA-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "/storage/emulated/0/Android/ANDROID.PERMISSION.TEST",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWDRA-M",
        "hardware": "mt6739"
    },
    {
        "model": "JDN-W09",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwjdn",
        "hardware": "qcom"
    },
    {
        "model": "SHT-W09",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1600x2560",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWSHT",
        "hardware": "hi3660"
    },
    {
        "model": "LIO-AN00",
        "sdk": "29",
        "android_version": "10",
        "display": "1176x2400",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWLIO",
        "hardware": "kirin990"
    },
    {
        "model": "Mate 20 Pro",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x960",
        "dpi": "240",
        "brand": "alps",
        "os": "Mate_20_Pro",
        "hardware": "mt6580"
    },
    {
        "model": "MT7-TL10",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Huawei",
        "os": "hwmt7",
        "hardware": "hi3630"
    },
    {
        "model": "BLA-L09",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWBLA",
        "hardware": "kirin970"
    },
    {
        "model": "YAL-L21",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWYAL",
        "hardware": "kirin980"
    },
    {
        "model": "G750-T01",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwG750-T01",
        "hardware": "mt6592"
    },
    {
        "model": "SCC-U21",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwSCC-Q",
        "hardware": "qcom"
    },
    {
        "model": "H60-L04",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwH60",
        "hardware": "hi3630"
    },
    {
        "model": "YAL-L41",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "419",
        "brand": "HONOR",
        "os": "HWYAL",
        "hardware": "kirin980"
    },
    {
        "model": "Che2-L11",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "280",
        "brand": "Honor",
        "os": "cherryplus",
        "hardware": "hi6210sft"
    },
    {
        "model": "GRA-L09",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1794",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWGRA",
        "hardware": "hi3635"
    },
    {
        "model": "CAM-L32",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCAM-Q",
        "hardware": "qcom"
    },
    {
        "model": "GEM-702L",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWGemini",
        "hardware": "hi3635"
    },
    {
        "model": "Y360",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x800",
        "dpi": "220",
        "brand": "Huawei",
        "os": "Huawei Y360",
        "hardware": "mt6582"
    },
    {
        "model": "EVR-L29",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2244",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWEVR",
        "hardware": "kirin980"
    },
    {
        "model": "MRD-LX1F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1336",
        "dpi": "272",
        "brand": "HUAWEI",
        "os": "HWMRD-M1",
        "hardware": "mt6761"
    },
    {
        "model": "PRA-LX2",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "ALE-L21",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "BLL-L22",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "PRA-LX1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "KIW-L24",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "SHT-W09",
        "sdk": "28",
        "android_version": "9",
        "display": "1600x2560",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWSHT",
        "hardware": "hi3660"
    },
    {
        "model": "MHA-L29",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "HUAWEI",
        "os": "HWMHA",
        "hardware": "hi3660"
    },
    {
        "model": "BLL-L22",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "P9 Plus",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "huawei",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "DUB-LX1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWDUB-Q",
        "hardware": "qcom"
    },
    {
        "model": "ANE-LX1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWANE",
        "hardware": "hi6250"
    },
    {
        "model": "ELE-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWELE",
        "hardware": "kirin980"
    },
    {
        "model": "DRA-LX2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "360",
        "brand": "HUAWEI",
        "os": "HWDRA-M",
        "hardware": "mt6739"
    },
    {
        "model": "SCL-U31",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwSCLU-Q",
        "hardware": "qcom"
    },
    {
        "model": "CHM-TL00H",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Honor",
        "os": "hwCHM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "H715BL",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWH715BL-Q",
        "hardware": "qcom"
    },
    {
        "model": "BND-L24",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "VNS-L21",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "STK-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWSTK-HF",
        "hardware": "kirin710"
    },
    {
        "model": "EVA-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "HUAWEI",
        "os": "HWEVA",
        "hardware": "hi3650"
    },
    {
        "model": "MAR-LX3A",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1734",
        "dpi": "360",
        "brand": "HUAWEI",
        "os": "HWMAR",
        "hardware": "kirin710"
    },
    {
        "model": "CHC-U01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwCHC-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "hi6210sft",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "hi6210sft",
        "os": "hi6210sft",
        "hardware": "hi6210sft"
    },
    {
        "model": "RNE-L22",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "293",
        "brand": "HUAWEI",
        "os": "HWRNE",
        "hardware": "hi6250"
    },
    {
        "model": "JSN-L22",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWJSN-H",
        "hardware": "kirin710"
    },
    {
        "model": "JKM-LX2",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "HUAWEI",
        "os": "HWJKM-H",
        "hardware": "kirin710"
    },
    {
        "model": "FLA-LX2",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWFLA-H",
        "hardware": "hi6250"
    },
    {
        "model": "ALE-L21",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "294",
        "brand": "Huawei",
        "os": "hwALE-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "PRA-LA1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWPRA-H",
        "hardware": "hi6250"
    },
    {
        "model": "T1 7.0",
        "sdk": "24",
        "android_version": "5.5.2",
        "display": "600x982",
        "dpi": "160",
        "brand": "Huawei",
        "os": "hwt1701",
        "hardware": "sc8830"
    },
    {
        "model": "CHM-U01",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Honor",
        "os": "hwCHM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "ANA-NX9",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWANA",
        "hardware": "kirin990"
    },
    {
        "model": "Che2-L11",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Honor",
        "os": "hwChe2",
        "hardware": "hi6210sft"
    },
    {
        "model": "P10 Plus",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "Huawei",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "LUA-L21",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWLUA-L6735",
        "hardware": "mt6735"
    },
    {
        "model": "Y5",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "480x854",
        "dpi": "240",
        "brand": "Huawei",
        "os": "y560",
        "hardware": "qcom"
    },
    {
        "model": "JNY-LX1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2310",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWJNY",
        "hardware": "kirin810"
    },
    {
        "model": "ANE-LX1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWANE",
        "hardware": "hi6250"
    },
    {
        "model": "BLN-L21",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "DUA-L22",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "360",
        "brand": "HONOR",
        "os": "HWDUA-M",
        "hardware": "mt6739"
    },
    {
        "model": "BLN-L21",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWBLN-H",
        "hardware": "hi6250"
    },
    {
        "model": "KIW-L24",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1794",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HNKIW-Q",
        "hardware": "qcom"
    },
    {
        "model": "LYA-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1440x3120",
        "dpi": "640",
        "brand": "HUAWEI",
        "os": "HWLYA",
        "hardware": "kirin980"
    },
    {
        "model": "YAL-AL00",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWYAL",
        "hardware": "kirin980"
    },
    {
        "model": "FRD-L02",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWFRD",
        "hardware": "hi3650"
    },
    {
        "model": "NXT-AL10",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "400",
        "brand": "HUAWEI",
        "os": "HWNXT",
        "hardware": "hi3650"
    },
    {
        "model": "SCL-L01",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "256",
        "brand": "Huawei",
        "os": "SCL-L01",
        "hardware": "qcom"
    },
    {
        "model": "EVA-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "259",
        "brand": "HUAWEI",
        "os": "HWEVA",
        "hardware": "hi3650"
    },
    {
        "model": "LDN-LX2",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWLDN-Q",
        "hardware": "qcom"
    },
    {
        "model": "FIG-LX1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWFIG-H",
        "hardware": "hi6250"
    },
    {
        "model": "STF-L09",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWSTF",
        "hardware": "hi3660"
    },
    {
        "model": "LLD-L31",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HONOR",
        "os": "HWLLD-H",
        "hardware": "hi6250"
    },
    {
        "model": "H60-L02",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Huawei",
        "os": "hwH60",
        "hardware": "hi3630"
    },
    {
        "model": "WAS-LX1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWWAS-H",
        "hardware": "hi6250"
    },
    {
        "model": "lotfi",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWCAM-H",
        "hardware": "hi6210sft"
    },
    {
        "model": "JDN2-W09",
        "sdk": "28",
        "android_version": "9",
        "display": "1200x1920",
        "dpi": "360",
        "brand": "HUAWEI",
        "os": "HWJDN2",
        "hardware": "kirin710"
    },
    {
        "model": "VNS-L22",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVNS-H",
        "hardware": "hi6250"
    },
    {
        "model": "LDN-LX3",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWLDN-Q",
        "hardware": "qcom"
    },
    {
        "model": "BND-L34",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWBND-H",
        "hardware": "hi6250"
    },
    {
        "model": "Nexus 6P",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1440x2560",
        "dpi": "476",
        "brand": "google",
        "os": "angler",
        "hardware": "angler"
    },
    {
        "model": "AGS2-L09",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWAGS2",
        "hardware": "hi6250"
    },
    {
        "model": "VOG-L29",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWVOG",
        "hardware": "kirin980"
    },
    {
        "model": "CRO-L03",
        "sdk": "23",
        "android_version": "6.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "HUAWEI",
        "os": "HWCRO-L6737M",
        "hardware": "mt6735"
    }
]
lenovo = [
    {
        "model": "Lenovo K920",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "Lenovo",
        "os": "kingdom_row",
        "hardware": "qcom"
    },
    {
        "model": "A536",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A536",
        "hardware": "sprout"
    },
    {
        "model": "TB-8704V",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "TB-8704V",
        "hardware": "qcom"
    },
    {
        "model": "S6000",
        "sdk": "22",
        "android_version": "5.12",
        "display": "800x1280",
        "dpi": "210",
        "brand": "联想/Lenovo",
        "os": "S6000",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo K50T5",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K50a40",
        "hardware": "mt6752"
    },
    {
        "model": "X1030X",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "MEDION",
        "os": "X1030X",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo Z90a40",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zoom_row",
        "hardware": "qcom"
    },
    {
        "model": "P70",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "P70",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo S60-a",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "sisleylr",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo X3c50",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "x3_row",
        "hardware": "qcom"
    },
    {
        "model": "Pixel XL",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "aio_otfp_m",
        "hardware": "mt6752"
    },
    {
        "model": "A6000",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "Kraft-A6000",
        "hardware": "qcom"
    },
    {
        "model": "3395CTO",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "768x1339",
        "dpi": "160",
        "brand": "Android-x86",
        "os": "x86_64",
        "hardware": "android_x86_64"
    },
    {
        "model": "Lenovo TAB 2 A8-50F",
        "sdk": "22",
        "android_version": "5.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "A8-50F",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo P2a42",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "P2a42",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-7104F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB7104F",
        "hardware": "mt8167"
    },
    {
        "model": "Lenovo A7000-a",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "300",
        "brand": "Lenovo",
        "os": "A7000-a",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo K53a48",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K53a48",
        "hardware": "qcom"
    },
    {
        "model": "a5500-HV",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "a5500",
        "os": "a5500-HV",
        "hardware": "mt6582"
    },
    {
        "model": "Lenovo A2016a40",
        "sdk": "23",
        "android_version": "6.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A2016a40",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TAB S8-50LC",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "S8-50LC",
        "hardware": "spark"
    },
    {
        "model": "Lenovo A7000-a",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A7000-a",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo P70-A",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "P70-A",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo TAB 2 A8-50LC",
        "sdk": "22",
        "android_version": "5.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "A8-50LC",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TAB 2 A10-70L",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1200x1920",
        "dpi": "280",
        "brand": "Lenovo",
        "os": "A10-70L",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo A7010a48",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "A7010a48",
        "hardware": "mt6735"
    },
    {
        "model": "YOGA Tablet 2 Pro-1380F",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1440x2560",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "YT2",
        "hardware": "byt_t_ffrd8"
    },
    {
        "model": "YOGA Tablet 2-830L",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "YT2",
        "hardware": "byt_t_ffrd8"
    },
    {
        "model": "Lenovo K50-t5",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "aio_otfp_m",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo TB-8504F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "TB-8504F",
        "hardware": "qcom"
    },
    {
        "model": "P1050X",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "MEDION",
        "os": "P1050X",
        "hardware": "medion_f1018"
    },
    {
        "model": "Lenovo K53b36",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K53b36",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-X505F",
        "sdk": "28",
        "android_version": "9",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB-X505F",
        "hardware": "qcom"
    },
    {
        "model": "L38111",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "kunlun2",
        "hardware": "qcom"
    },
    {
        "model": "L38111",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "454",
        "brand": "Lenovo",
        "os": "kunlun2",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A7600-m",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "aiocmcc_ttp",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo TAB 2 A7-30HC",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "A7-30HC",
        "hardware": "mt8382"
    },
    {
        "model": "Lenovo A6000",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "Kraft-A6000",
        "hardware": "qcom"
    },
    {
        "model": "T5",
        "sdk": "22",
        "android_version": "6.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "TXD",
        "os": "TXD",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo YT3-850M",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "YT3-850M",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo Z90-7",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zoom_fdd",
        "hardware": "qcom"
    },
    {
        "model": "P1061X",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "MEDION",
        "os": "P1061X",
        "hardware": "qcom"
    },
    {
        "model": "Vibe K5",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "280",
        "brand": "Lenovo",
        "os": "A6020a40",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A2016b30",
        "sdk": "23",
        "android_version": "6.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A2016b30",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo A6010",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A6010",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-8504X",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "TB-8504X",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A7600",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "aio_otfp",
        "hardware": "mt6752"
    },
    {
        "model": "L78011",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2246",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "jd2018",
        "hardware": "qcom"
    },
    {
        "model": "P1032X",
        "sdk": "21",
        "android_version": "5.0",
        "display": "800x1280",
        "dpi": "160",
        "brand": "MEDION",
        "os": "P1032X",
        "hardware": "medion_f1013"
    },
    {
        "model": "V1",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "lenovo",
        "os": "V1",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo TB-8703F",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "TB-8703F",
        "hardware": "qcom"
    },
    {
        "model": "MEDION X5004",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "MEDION",
        "os": "X5004",
        "hardware": "qcom"
    },
    {
        "model": "LIFETAB_S1034X",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "MEDION",
        "os": "lifetab_s1034x",
        "hardware": "anzhen4_mrd8_w"
    },
    {
        "model": "Lenovo K33a48",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K33a48",
        "hardware": "qcom"
    },
    {
        "model": "A6000",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "224",
        "brand": "Lenovo",
        "os": "a6000",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K50-t5",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "aio_otfp",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo TB2-X30F",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB2-X30F",
        "hardware": "qcom"
    },
    {
        "model": "K10e70",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "K10e70",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-X605F",
        "sdk": "28",
        "android_version": "9",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "X605F",
        "hardware": "qcom"
    },
    {
        "model": "3395CTO",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "768x1366",
        "dpi": "160",
        "brand": "Android-x86",
        "os": "android_x86_64",
        "hardware": "cm_android_x86_64"
    },
    {
        "model": "Lenovo TB-8504F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "TB-8504F",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo Z90-3",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zoom_tdd",
        "hardware": "qcom"
    },
    {
        "model": "S1035X",
        "sdk": "23",
        "android_version": "6.0",
        "display": "800x1280",
        "dpi": "160",
        "brand": "MEDION",
        "os": "S1035X",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo Z90a40",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zoom_row",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo Z90-7",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zoom_fdd",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo YT-X703F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1600x2560",
        "dpi": "272",
        "brand": "Lenovo",
        "os": "YT-X703F",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo S90-A",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "sisleyr",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo Z2",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "z2r",
        "hardware": "qcom"
    },
    {
        "model": "K520",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "seoul",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A2010-a",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "220",
        "brand": "LENOVO",
        "os": "A2010",
        "hardware": "mt6735"
    },
    {
        "model": "K50-T5",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "aio_otfp_m",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo A2010-a",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "220",
        "brand": "Micromax",
        "os": "A2010-a",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo S1a40",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "S1a40",
        "hardware": "mt6752"
    },
    {
        "model": "kali linux",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "kali linux",
        "os": "Kraft-A6000",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-8304F1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "TB-8304F1",
        "hardware": "mt8163"
    },
    {
        "model": "Lenovo A2010-a",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A2010-a",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo P1ma40",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "P1ma40",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TB-X704F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "X704F",
        "hardware": "qcom"
    },
    {
        "model": "A1010a20",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A1010a20",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo TB2-X30L",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB2-X30L",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A6020a46",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "A6020a46",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A1000",
        "sdk": "21",
        "android_version": "5.0",
        "display": "480x800",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A1000",
        "hardware": "sc8830"
    },
    {
        "model": "Lenovo TAB 2 A8-50F",
        "sdk": "22",
        "android_version": "5.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "A8-50F",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo A2580",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A2580",
        "hardware": "mt6735"
    },
    {
        "model": "Z90",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zoom",
        "hardware": "qcom"
    },
    {
        "model": "TAB 2 A10-70L",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A10-70L",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo TB3-850F",
        "sdk": "23",
        "android_version": "6.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "TB3-850F",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo X3a40",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "x3_row",
        "hardware": "qcom"
    },
    {
        "model": "A2010",
        "sdk": "23",
        "android_version": "6.0",
        "display": "480x854",
        "dpi": "220",
        "brand": "Senseit",
        "os": "A2016a40",
        "hardware": "mt6735"
    },
    {
        "model": "vibe p1 a42",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "P1a42",
        "hardware": "qcom"
    },
    {
        "model": "a850",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1560",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWINE",
        "hardware": "kirin710"
    },
    {
        "model": "Lenovo A7020a48",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "A7020a48",
        "hardware": "mt6755"
    },
    {
        "model": "Lenovo K30-T",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "Kraft-T",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-X606F",
        "sdk": "29",
        "android_version": "10",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "X606F",
        "hardware": "mt8768"
    },
    {
        "model": "Lenovo TB-X306F",
        "sdk": "29",
        "android_version": "10",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "X306F",
        "hardware": "mt8768"
    },
    {
        "model": "Lenovo K33a42",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K33a42",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB3-X70F",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "TB3-X70F",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TB-X605L",
        "sdk": "28",
        "android_version": "9",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "X605L",
        "hardware": "qcom"
    },
    {
        "model": "s90c",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "200",
        "brand": "Lenovo",
        "os": "S850",
        "hardware": "mt6582"
    },
    {
        "model": "Lenovo A2020a40",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "angus3A4",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-X304L",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "186",
        "brand": "Lenovo",
        "os": "X304L",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB3-X70L",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "TB3-X70L",
        "hardware": "mt6735"
    },
    {
        "model": "L38111",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "440",
        "brand": "Lenovo",
        "os": "kunlun2",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo YT3-X50F",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "YT3-X50F",
        "hardware": "qcom"
    },
    {
        "model": "K920 (ROW)",
        "sdk": "28",
        "android_version": "9",
        "display": "1440x2560",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "kingdom_row",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K50a40",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K50a40",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo X2-AP",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "X2-AP",
        "hardware": "mt6595"
    },
    {
        "model": "Lenovo X2-EU",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "X2-EU",
        "hardware": "mt6595"
    },
    {
        "model": "Lenovo A1010a20",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A1010a20",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo A536",
        "sdk": "26",
        "android_version": "8.0",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A536",
        "hardware": "mt6582"
    },
    {
        "model": "Lenovo TAB S8-50F",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "S8-50F",
        "hardware": "spark"
    },
    {
        "model": "A 536",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "320",
        "brand": "samsung",
        "os": "GT-I9500",
        "hardware": "mt6582"
    },
    {
        "model": "Lenovo A6020a40",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A6020a40",
        "hardware": "qcom"
    },
    {
        "model": "A7010a48",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "k5fpr",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TB2-X30F",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "800x1280",
        "dpi": "180",
        "brand": "Lenovo",
        "os": "TB2-X30F",
        "hardware": "qcom"
    },
    {
        "model": "L38011",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "k5",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K33a42",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K33a42",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K50a40",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K50a40",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo Vibe Z2",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "z2r",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K50-T5",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "aio_otfp",
        "hardware": "mt6752"
    },
    {
        "model": "L78121",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "jd20",
        "hardware": "qcom"
    },
    {
        "model": "E691X",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "213",
        "brand": "MEDION",
        "os": "E691X",
        "hardware": "mt6580"
    },
    {
        "model": "A1000",
        "sdk": "21",
        "android_version": "5.0",
        "display": "480x800",
        "dpi": "240",
        "brand": "LENOVO",
        "os": "A1000",
        "hardware": "sc8830"
    },
    {
        "model": "TB3-710I",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Lenovo TB3-710I",
        "os": "TB3-710I",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo TB2-X30F",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB2-X30F",
        "hardware": "qcom"
    },
    {
        "model": "LIFETAB_S1034X",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "MEDION",
        "os": "lifetab_s1034x",
        "hardware": "anzhen4_mrd8_w"
    },
    {
        "model": "Lenovo A7010a48",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "A7010a48",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo PB1-770M",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "PB1-770M",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB-7504X",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "TB-7504X",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TB-X304L",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "X304L",
        "hardware": "qcom"
    },
    {
        "model": "tab2 x30L",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "on5xelte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "TB3-710I",
        "sdk": "22",
        "android_version": "5.1",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB3-710I",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo A6010 smartphone",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A6010",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A2010",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A2010-a",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo P1a42",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "P1a42",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB3-850M",
        "sdk": "23",
        "android_version": "6.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "TB3-850M",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo A7000-a",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "hermes",
        "hardware": "mt6752"
    },
    {
        "model": "A889",
        "sdk": "22",
        "android_version": "9.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A889",
        "hardware": "mt6582"
    },
    {
        "model": "Lenovo X3a40",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "x3_row",
        "hardware": "qcom"
    },
    {
        "model": "BQ2NK",
        "sdk": "24",
        "android_version": "0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "6zv",
        "hardware": "jr5n6bj1"
    },
    {
        "model": "Lenovo TB-8505FS",
        "sdk": "29",
        "android_version": "10",
        "display": "800x1280",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "8505FS",
        "hardware": "mt8766"
    },
    {
        "model": "X1030X",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "MEDION",
        "os": "X1030X",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo A7000-a",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A7000-a",
        "hardware": "mt6752"
    },
    {
        "model": "a880",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "aio_otfp_m",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo P1ma40",
        "sdk": "22",
        "android_version": "7.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "P1ma40",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TB-X103F",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB-X103F",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K53a48",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "Lenovo",
        "os": "K53a48",
        "hardware": "qcom"
    },
    {
        "model": "L78051",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zippo",
        "hardware": "qcom"
    },
    {
        "model": "L78071",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "375",
        "brand": "Lenovo",
        "os": "jd2019",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo Z90-7",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "zoom_row",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB2-X30L",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB2-X30L",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A6020l36",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "A6020l36",
        "hardware": "qcom"
    },
    {
        "model": "A7010",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "A7010a48",
        "hardware": "mt6735"
    },
    {
        "model": "TB-X704V",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1200x1920",
        "dpi": "239",
        "brand": "Lenovo",
        "os": "X704V",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A6000",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "Kraft-A6000",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo PB1-750M",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "PB1-750M",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo P2a42",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "P2a42",
        "hardware": "qcom"
    },
    {
        "model": "A5000",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "294",
        "brand": "Lenovo",
        "os": "A5000",
        "hardware": "sprout"
    },
    {
        "model": "m9623",
        "sdk": "22",
        "android_version": "5.1",
        "display": "800x1280",
        "dpi": "210",
        "brand": "M9623",
        "os": "M9623",
        "hardware": "mt6580"
    },
    {
        "model": "flex 10",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "vivo",
        "os": "V3",
        "hardware": "qcom"
    },
    {
        "model": "A536",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "480x854",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "Lenovo A536",
        "hardware": "sprout"
    },
    {
        "model": "Lenovo K8 Note",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "lenovo",
        "os": "manning",
        "hardware": "mt6797"
    },
    {
        "model": "Tab2A7-10F",
        "sdk": "21",
        "android_version": "5.0",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "Tab2A7-10F",
        "hardware": "mt8127"
    },
    {
        "model": "Lenovo K920",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "Lenovo",
        "os": "kingdomt",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K3 Note",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K50a40",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo TAB S8-50F",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "S8-50F",
        "hardware": "spark"
    },
    {
        "model": "L78071",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "jd2019",
        "hardware": "qcom"
    },
    {
        "model": "1S16800367700CM",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "768x1366",
        "dpi": "160",
        "brand": "Android-x86",
        "os": "x86",
        "hardware": "android_x86"
    },
    {
        "model": "a2020a40",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "480x854",
        "dpi": "200",
        "brand": "Micromax",
        "os": "Q415",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TB3-730X",
        "sdk": "23",
        "android_version": "6.0",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "TB3-730X",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TAB 2 A8-50LC",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "800x1280",
        "dpi": "213",
        "brand": "Lenovo",
        "os": "A8-50LC",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TAB 2 A7-30GC",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "600x1024",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "A7-30GC",
        "hardware": "mt8382"
    },
    {
        "model": "Lenovo A6010 PLUS",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A6010",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A6600d40",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A6600d40",
        "hardware": "mt6735"
    },
    {
        "model": " A3500-H",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "800x1280",
        "dpi": "188",
        "brand": "Mediatek",
        "os": "Lenovo_a3500",
        "hardware": "mt6582"
    },
    {
        "model": "L18011",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "L18011",
        "hardware": "mt6739"
    },
    {
        "model": "Lenovo K10a40",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "K10a40",
        "hardware": "mt6735"
    },
    {
        "model": "L78011",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2246",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "jd2018",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A7600",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A7600",
        "hardware": "mt6752"
    },
    {
        "model": "Vibe P1m",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "P1ma40",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo K50-t5",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K50-t5",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo K53a48",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K53a48",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo PB2-670M",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "360",
        "brand": "Lenovo",
        "os": "PB2-670M",
        "hardware": "mt6735"
    },
    {
        "model": "Lenovo TB-X704L",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "X704L",
        "hardware": "qcom"
    },
    {
        "model": "A5000",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "294",
        "brand": "Highscreen",
        "os": "giraffe",
        "hardware": "sprout"
    },
    {
        "model": "Vibe P1",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "p1a42",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo YT3-X90L",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1600x2560",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "YT3",
        "hardware": "r2_cht_ffd"
    },
    {
        "model": "L78071",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "jd2019_row",
        "hardware": "qcom"
    },
    {
        "model": "/S6000",
        "sdk": "22",
        "android_version": "5.12",
        "display": "800x1280",
        "dpi": "210",
        "brand": "lenovo",
        "os": "lenovo",
        "hardware": "mt6580"
    },
    {
        "model": "P1040X",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "MEDION",
        "os": "P1050X",
        "hardware": "medion_g1006"
    },
    {
        "model": "Lenovo TAB 2 A10-70L",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A10-70L",
        "hardware": "mt6752"
    },
    {
        "model": "A7010a48",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "A7010a48",
        "hardware": "mt6735"
    },
    {
        "model": "S939",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "300",
        "brand": "Lenovo",
        "os": "S939",
        "hardware": "mt6592"
    },
    {
        "model": "Lenovo A5000",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "A5000",
        "hardware": "mt6582"
    },
    {
        "model": "T805C",
        "sdk": "22",
        "android_version": "5.1",
        "display": "800x1280",
        "dpi": "210",
        "brand": "Lenovo",
        "os": "T805C",
        "hardware": "mt6580"
    },
    {
        "model": "Lenovo K33a48",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K33a48",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo K53a48",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "K53a48",
        "hardware": "qcom"
    },
    {
        "model": "TAB 2 A10-70F",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A10-70F",
        "hardware": "mt6752"
    },
    {
        "model": "Lenovo TB-X104F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Lenovo",
        "os": "X104F",
        "hardware": "qcom"
    },
    {
        "model": "l38012",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1440",
        "dpi": "320",
        "brand": "Android",
        "os": "phhgsi_arm64_a",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo A760",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "lenovo",
        "os": "armani",
        "hardware": "qcom"
    },
    {
        "model": "K920",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1440x2560",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "kingdom_row",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TAB S8-50L",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "S8-50L",
        "hardware": "spark"
    },
    {
        "model": "Lenovo K8 Plus",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Lenovo",
        "os": "marino_f",
        "hardware": "mt6757"
    },
    {
        "model": "a6000",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "a6000",
        "hardware": "qcom"
    },
    {
        "model": "Lenovo TAB 2 A10-70F",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Lenovo",
        "os": "A10-70F",
        "hardware": "mt6752"
    }
]
oneplus = [
    {
        "model": "DE2118",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlusN200TMO",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "432",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "A0001",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONEPLUS A3000",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "oneplus3",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONE E1003",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus",
        "hardware": "qcom"
    },
    {
        "model": "de",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlusN200TMO",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "900x1600",
        "dpi": "240",
        "brand": "OnePlus",
        "os": "OnePlus5",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "380",
        "brand": "OnePlus",
        "os": "OnePlus3T",
        "hardware": "qcom"
    },
    {
        "model": "DE2118_11-C.16",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlusN200TMO",
        "hardware": "qcom"
    },
    {
        "model": "ONE E1003",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5010",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x2160",
        "dpi": "540",
        "brand": "OnePlus",
        "os": "OnePlus5T",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONEPLUS A6013",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus6T",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5010",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus5T",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6003",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "314",
        "brand": "OnePlus",
        "os": "OnePlus6",
        "hardware": "qcom"
    },
    {
        "model": "ONE A2001",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus2",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONE A2001",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus2",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3000",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5010",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus5T",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "440",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "A0001",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus3T",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "21",
        "android_version": "5.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus3T",
        "hardware": "qcom"
    },
    {
        "model": "BE2025",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "OnePlus",
        "os": "OnePlusN10METRO",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5010",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus5T",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6003",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2280",
        "dpi": "510",
        "brand": "OnePlus",
        "os": "OnePlus6",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6010",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "380",
        "brand": "OnePlus",
        "os": "OnePlus6T",
        "hardware": "qcom"
    },
    {
        "model": "BE2025",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlusN10METRO",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6000",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "380",
        "brand": "OnePlus",
        "os": "OnePlus6",
        "hardware": "qcom"
    },
    {
        "model": "GM1917",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "540",
        "brand": "OnePlus",
        "os": "OnePlus7Pro",
        "hardware": "qcom"
    },
    {
        "model": "HD1900",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus7T",
        "hardware": "qcom"
    },
    {
        "model": "GM1915",
        "sdk": "29",
        "android_version": "10",
        "display": "1440x3120",
        "dpi": "650",
        "brand": "OnePlus",
        "os": "OnePlus7ProTMO",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6010",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus6T",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "380",
        "brand": "OnePlus",
        "os": "OnePlus5",
        "hardware": "qcom"
    },
    {
        "model": "AC2001",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "Nord",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6013",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus6TSingle",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "ONEPLUS",
        "os": "A0001",
        "hardware": "qcom"
    },
    {
        "model": "7",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "guacamoleb",
        "hardware": "qcom"
    },
    {
        "model": "GM1913",
        "sdk": "29",
        "android_version": "10",
        "display": "1440x3120",
        "dpi": "560",
        "brand": "OnePlus",
        "os": "OnePlus7Pro",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus5",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus3T",
        "hardware": "qcom"
    },
    {
        "model": "ONE E1003",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "onyx",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6013",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "380",
        "brand": "OnePlus",
        "os": "OnePlus6T",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6003",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus6",
        "hardware": "qcom"
    },
    {
        "model": "7 Pro",
        "sdk": "28",
        "android_version": "9",
        "display": "1440x3120",
        "dpi": "476",
        "brand": "OnePlus",
        "os": "OnePlus7Pro",
        "hardware": "qcom"
    },
    {
        "model": "One",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "oneplus",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONEPLUS A3000",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "GM1901",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus7",
        "hardware": "qcom"
    },
    {
        "model": "GM1900",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus 7",
        "hardware": "qcom"
    },
    {
        "model": "Nord N10 5G",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "OnePlus",
        "os": "billie",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "A0001",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "OnePlus",
        "os": "OnePlus3",
        "hardware": "qcom"
    },
    {
        "model": "ONE A2003",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OnePlus",
        "os": "OnePlus2",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3003",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "384",
        "brand": "OnePlus",
        "os": "OnePlus3T",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5000",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus5",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A3010",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus3T",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A6013",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "OnePlus",
        "os": "OnePlus6T",
        "hardware": "qcom"
    },
    {
        "model": "A0001",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "ONEPLUS",
        "os": "A0001",
        "hardware": "bacon"
    },
    {
        "model": "ONEPLUS A5000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "240",
        "brand": "OnePlus",
        "os": "OnePlus5",
        "hardware": "qcom"
    },
    {
        "model": "ONEPLUS A5000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "240",
        "brand": "OnePlus",
        "os": "OnePlus5",
        "hardware": "qcom"
    }
]
oppo = [
    {
        "model": "f1s",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33w",
        "hardware": "mt6582"
    },
    {
        "model": "A33f",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33",
        "hardware": "qcom"
    },
    {
        "model": "A59s",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A59s",
        "hardware": "mt6755"
    },
    {
        "model": "CPH1823",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "OPPO",
        "os": "CPH1823",
        "hardware": "mt6771"
    },
    {
        "model": "A33m",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33m",
        "hardware": "qcom"
    },
    {
        "model": "CPH1937",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4B80L1",
        "hardware": "qcom"
    },
    {
        "model": "X9076",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "OPPO",
        "os": "X9076",
        "hardware": "qcom"
    },
    {
        "model": "CPH2239",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4F2F",
        "hardware": "mt6765"
    },
    {
        "model": "X9009",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "X9009",
        "hardware": "mt6755"
    },
    {
        "model": "CPH1723",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "OPPO",
        "os": "CPH1723",
        "hardware": "mt6763"
    },
    {
        "model": "A1603",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A1603",
        "hardware": "mt6582"
    },
    {
        "model": "R11s Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R11sPlus",
        "hardware": "qcom"
    },
    {
        "model": "CPH1609",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "CPH1609",
        "hardware": "mt6755"
    },
    {
        "model": "CPH1701",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1701",
        "hardware": "qcom"
    },
    {
        "model": "CPH1727",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "OPPO",
        "os": "CPH1727",
        "hardware": "mt6763"
    },
    {
        "model": "R9sk",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R9sk",
        "hardware": "qcom"
    },
    {
        "model": "A51w",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A51",
        "hardware": "qcom"
    },
    {
        "model": "CPH1909",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1909",
        "hardware": "mt6765"
    },
    {
        "model": "CPH2185",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4F2F",
        "hardware": "mt6765"
    },
    {
        "model": "CPH1825",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "OPPO",
        "os": "CPH1825",
        "hardware": "mt6771"
    },
    {
        "model": "CPH1907",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4B83L1",
        "hardware": "qcom"
    },
    {
        "model": "A37f",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A37f",
        "hardware": "qcom"
    },
    {
        "model": "A33fw",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33",
        "hardware": "qcom"
    },
    {
        "model": "CPH1803",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1803",
        "hardware": "qcom"
    },
    {
        "model": "A33m",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33",
        "hardware": "qcom"
    },
    {
        "model": "CPH2325",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP5303",
        "hardware": "mt6765"
    },
    {
        "model": "A33f color-os v2.1.01",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33",
        "hardware": "qcom"
    },
    {
        "model": "RMX1809",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "272",
        "brand": "OPPO",
        "os": "RMX1809",
        "hardware": "qcom"
    },
    {
        "model": "F1f",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "F1f",
        "hardware": "qcom"
    },
    {
        "model": "R7g",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Android",
        "os": "R7f",
        "hardware": "qcom"
    },
    {
        "model": "CPH1803",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "PBAT00",
        "hardware": "qcom"
    },
    {
        "model": "CPH2185",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "Redmi",
        "os": "angelica",
        "hardware": "mt6765"
    },
    {
        "model": "5.5",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33w",
        "hardware": "mt6582"
    },
    {
        "model": "CPH1933",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4B79L1",
        "hardware": "qcom"
    },
    {
        "model": "CPH1989",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4C4BL1",
        "hardware": "mt6771"
    },
    {
        "model": "CPH2239",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "360",
        "brand": "OPPO",
        "os": "OP4F2F",
        "hardware": "mt6765"
    },
    {
        "model": "R11 Plus",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R11Plus",
        "hardware": "qcom"
    },
    {
        "model": "PBCM10",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "OPPO",
        "os": "PBCM10",
        "hardware": "qcom"
    },
    {
        "model": "A33",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33",
        "hardware": "qcom"
    },
    {
        "model": "R7sm",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R7sm",
        "hardware": "qcom"
    },
    {
        "model": "CPH1907",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "408",
        "brand": "OPPO",
        "os": "OP4B83L1",
        "hardware": "qcom"
    },
    {
        "model": "CPH1825",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "OPPO",
        "os": "CPH1825",
        "hardware": "mt6771"
    },
    {
        "model": "CPH1937",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "272",
        "brand": "OPPO",
        "os": "OP4B80L1",
        "hardware": "qcom"
    },
    {
        "model": "R7Plus",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R7Plus",
        "hardware": "mt6795"
    },
    {
        "model": "A1601",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A1601",
        "hardware": "mt6755"
    },
    {
        "model": "CPH1729",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1440",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1729",
        "hardware": "mt6763"
    },
    {
        "model": "R7g",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R7f",
        "hardware": "qcom"
    },
    {
        "model": "R11s",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R11s",
        "hardware": "qcom"
    },
    {
        "model": "R7kf",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "R7f",
        "hardware": "qcom"
    },
    {
        "model": "CPH2247",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "540",
        "brand": "OPPO",
        "os": "OP4F7FL1",
        "hardware": "qcom"
    },
    {
        "model": "CPH1801",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1801",
        "hardware": "qcom"
    },
    {
        "model": "X9009",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "X9009",
        "hardware": "mt6755"
    },
    {
        "model": "A33wEX",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A1603",
        "hardware": "mt6582"
    },
    {
        "model": "A33w",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33w",
        "hardware": "mt6582"
    },
    {
        "model": "a5 2020",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A37f",
        "hardware": "qcom"
    },
    {
        "model": "_A33m",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A33m",
        "hardware": "qcom"
    },
    {
        "model": "CPH2293",
        "sdk": "33",
        "android_version": "13",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP52E1L1",
        "hardware": "mt6893"
    },
    {
        "model": "CPH2015",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4C7D",
        "hardware": "mt6765"
    },
    {
        "model": "X9006",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "X9006",
        "hardware": "qcom"
    },
    {
        "model": "A1601",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A1601",
        "hardware": "mt6755"
    },
    {
        "model": "CPH1907",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2400",
        "dpi": "408",
        "brand": "OPPO",
        "os": "OP4B83L1",
        "hardware": "qcom"
    },
    {
        "model": "CPH1920",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1920",
        "hardware": "mt6765"
    },
    {
        "model": "CPH1859",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "408",
        "brand": "OPPO",
        "os": "CPH1859",
        "hardware": "mt6771"
    },
    {
        "model": "CPH2059",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4C72L1",
        "hardware": "qcom"
    },
    {
        "model": "1201",
        "sdk": "22",
        "android_version": "5.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "OPPO",
        "os": "1201",
        "hardware": "mt6582"
    },
    {
        "model": "a33f",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "LYF",
        "os": "msm8909",
        "hardware": "qcom"
    },
    {
        "model": "A3S CPH-1803",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1803",
        "hardware": "qcom"
    },
    {
        "model": "CPH1931",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4B79L1",
        "hardware": "qcom"
    },
    {
        "model": "a33f+",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Lenovo",
        "os": "Kraft-A6000",
        "hardware": "qcom"
    },
    {
        "model": "R7sf",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R7sf",
        "hardware": "qcom"
    },
    {
        "model": "A31",
        "sdk": "23",
        "android_version": "8.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A31",
        "hardware": "qcom"
    },
    {
        "model": "A33f",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "200",
        "brand": "OPPO",
        "os": "A33",
        "hardware": "qcom"
    },
    {
        "model": "Find 5",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "find5",
        "hardware": "qcom"
    },
    {
        "model": "R7plusf",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R7Plusm",
        "hardware": "qcom"
    },
    {
        "model": "CPH1901",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "CPH1901",
        "hardware": "qcom"
    },
    {
        "model": "R11s Plus",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R11sPlus",
        "hardware": "qcom"
    },
    {
        "model": "CPH2217",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "408",
        "brand": "OPPO",
        "os": "OP4F43L1",
        "hardware": "mt6779"
    },
    {
        "model": "CPH2083",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4BFB",
        "hardware": "mt6765"
    },
    {
        "model": "F3",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "CPH2035",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4C5FL1",
        "hardware": "mt6779"
    },
    {
        "model": "CPH1989",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4C4BL1",
        "hardware": "mt6771"
    },
    {
        "model": "f11",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "alps",
        "os": "R10",
        "hardware": "mt6580"
    },
    {
        "model": "CPH1937",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4B80L1",
        "hardware": "qcom"
    },
    {
        "model": "Samsung s9",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A37f",
        "hardware": "qcom"
    },
    {
        "model": "CPH2239",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "a2corelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "CPH2127",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "272",
        "brand": "OPPO",
        "os": "OP4EFDL1",
        "hardware": "qcom"
    },
    {
        "model": "CPH2015",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1600",
        "dpi": "272",
        "brand": "OPPO",
        "os": "OP4C7D",
        "hardware": "mt6765"
    },
    {
        "model": "R7sfsg ",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R7sf",
        "hardware": "qcom"
    },
    {
        "model": "CPH2109",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4BA5L1",
        "hardware": "qcom"
    },
    {
        "model": "A59s",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A59m",
        "hardware": "mt6755"
    },
    {
        "model": "RMX1805",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "RMX1805",
        "hardware": "qcom"
    },
    {
        "model": "A59s",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A59",
        "hardware": "mt6755"
    },
    {
        "model": "CPH2219",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4F11L1",
        "hardware": "qcom"
    },
    {
        "model": "A37fw",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A37f",
        "hardware": "qcom"
    },
    {
        "model": "R7sf",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "OPPO",
        "os": "R7sf",
        "hardware": "qcom"
    },
    {
        "model": "RMX1811",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "OPPO",
        "os": "RMX1811",
        "hardware": "qcom"
    },
    {
        "model": "CPH2001",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4B9B",
        "hardware": "mt6771"
    },
    {
        "model": "cph2333",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "OPPO",
        "os": "OP4F2F",
        "hardware": "mt6765"
    },
    {
        "model": "PADM00",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "OPPO",
        "os": "PADM00",
        "hardware": "mt6771"
    },
    {
        "model": "CPH1725",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "OPPO",
        "os": "CPH1725",
        "hardware": "mt6763"
    }
]
realme = [
    {
        "model": "RMX1851",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Realme",
        "os": "RMX1851",
        "hardware": "qcom"
    },
    {
        "model": "RMX3511",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2408",
        "dpi": "480",
        "brand": "realme",
        "os": "RE87BAL1",
        "hardware": "ums9230_nico"
    },
    {
        "model": "RMX1911",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1600",
        "dpi": "320",
        "brand": "realme",
        "os": "RMX1911",
        "hardware": "qcom"
    },
    {
        "model": "RMX1931",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "408",
        "brand": "realme",
        "os": "RMX1931L1",
        "hardware": "qcom"
    },
    {
        "model": "RMX1941",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "OPPO",
        "os": "A37f",
        "hardware": "qcom"
    },
    {
        "model": "RMX2185",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "realme",
        "os": "RMX2185",
        "hardware": "mt6765"
    },
    {
        "model": "X2 Pro",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX1931",
        "hardware": "qcom"
    },
    {
        "model": "RMX2189",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "realme",
        "os": "RMX2189",
        "hardware": "mt6765"
    },
    {
        "model": "RMX3370",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RE879AL1",
        "hardware": "qcom"
    },
    {
        "model": "RMX1925",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "272",
        "brand": "realme",
        "os": "RMX1925",
        "hardware": "qcom"
    },
    {
        "model": "rmx 2185",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "realme",
        "os": "RMX2189",
        "hardware": "mt6765"
    },
    {
        "model": "RMX2086",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX2086L1",
        "hardware": "qcom"
    },
    {
        "model": "RMX2061",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX2061L1",
        "hardware": "qcom"
    },
    {
        "model": "RMX1941",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "Realme",
        "os": "RMX1941",
        "hardware": "mt6765"
    },
    {
        "model": "RMX2030",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "272",
        "brand": "realme",
        "os": "RMX2030",
        "hardware": "qcom"
    },
    {
        "model": "RMX1941",
        "sdk": "22",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "nook",
        "os": "zoom2",
        "hardware": "qcom"
    },
    {
        "model": "RMX1851",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "408",
        "brand": "Realme",
        "os": "RMX1851",
        "hardware": "qcom"
    },
    {
        "model": "RMX2020",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "320",
        "brand": "realme",
        "os": "RMX2020",
        "hardware": "mt6768"
    },
    {
        "model": "RMX1925",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1600",
        "dpi": "320",
        "brand": "realme",
        "os": "RMX1925",
        "hardware": "qcom"
    },
    {
        "model": "RMX2002",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX2002L1",
        "hardware": "mt6785"
    },
    {
        "model": "RMX1921",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX1921",
        "hardware": "qcom"
    },
    {
        "model": "RMX2061",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX2061L1",
        "hardware": "qcom"
    },
    {
        "model": "RMX2075",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX2075L1",
        "hardware": "qcom"
    },
    {
        "model": "RMX3121",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "320",
        "brand": "realme",
        "os": "RMX3121CN",
        "hardware": "mt6833"
    },
    {
        "model": "RMX2001",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2400",
        "dpi": "408",
        "brand": "realme",
        "os": "RMX2001L1",
        "hardware": "mt6785"
    },
    {
        "model": "RMX2063",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX2063L1",
        "hardware": "qcom"
    },
    {
        "model": "RMX1851",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "Realme",
        "os": "RMX1851",
        "hardware": "qcom"
    },
    {
        "model": "RMX3081",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "realme",
        "os": "RMX3081L1",
        "hardware": "qcom"
    }
]
samsung = [
    {
        "model": "SM-A505F",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SAMSUNG-SM-G930A",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroqlteatt",
        "hardware": "qcom"
    },
    {
        "model": "SM-N975U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A720S",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "a7y17lteskt",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-G615F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "j7maxlte",
        "hardware": "mt6757"
    },
    {
        "model": "SM-A716U",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1507",
        "dpi": "360",
        "brand": "samsung",
        "os": "a71xq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G973U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J330G",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3y17lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-N970U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "d1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J737P",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7topeltespr",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G996U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "samsung",
        "os": "t2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A910F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "270",
        "brand": "samsung",
        "os": "a9xproltesea",
        "hardware": "qcom"
    },
    {
        "model": "SM-A520W",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "405",
        "brand": "samsung",
        "os": "a5y17ltecan",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-G930F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": " ",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gta2slte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930W8",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "heroltebmc",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G930F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-N950F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2220",
        "dpi": "480",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G531H",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "grandprimeve3g",
        "hardware": "sc8830"
    },
    {
        "model": "SM-A528B",
        "sdk": "33",
        "android_version": "13",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "samsung",
        "os": "a52sxq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroqltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935T",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "hero2qltetmo",
        "hardware": "qcom"
    },
    {
        "model": "SM-J530FM",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A107F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a10s",
        "hardware": "mt6762"
    },
    {
        "model": "j3119s",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "440",
        "brand": "xiaomi",
        "os": "sakura_india",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G900F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "klte",
        "hardware": "qcom"
    },
    {
        "model": "SM-J700T1",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7eltemtr",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-N960U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "crownqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G970U1",
        "sdk": "31",
        "android_version": "12",
        "display": "952x2280",
        "dpi": "540",
        "brand": "samsung",
        "os": "beyond0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T815Y",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "210",
        "brand": "samsung",
        "os": "gts210lte",
        "hardware": "universal5433"
    },
    {
        "model": "SM-G960U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "starqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G955U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-G890A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "marinelteatt",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G955U1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x2220",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A530W",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "405",
        "brand": "samsung",
        "os": "jackpotltecan",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G610F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "on7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-T585",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gtaxllte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "GT-I9060I",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "480x800",
        "dpi": "200",
        "brand": "samsung",
        "os": "grandneove3g",
        "hardware": "sc8830"
    },
    {
        "model": "SM-J250F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "j2y18lte",
        "hardware": "qcom"
    },
    {
        "model": "SM-A725F",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "samsung",
        "os": "a72q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T818W",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "samsung",
        "os": "gts210veltecan",
        "hardware": "qcom"
    },
    {
        "model": "SM-M315F",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "m31",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-N950U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1440x2678",
        "dpi": "640",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "11 Pro Max",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "mt6580"
    },
    {
        "model": "SM-A305G",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "a30",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G900F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "klte",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-G930A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroqlteatt",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Verizon",
        "os": "heroqltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-T377W",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gteslte",
        "hardware": "universal3475"
    },
    {
        "model": "SM-N986U1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "c2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930W8",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroltebmc",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G950F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-J337U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j3toplteue",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-T510",
        "sdk": "28",
        "android_version": "9",
        "display": "900x1440",
        "dpi": "210",
        "brand": "samsung",
        "os": "gta3xlwifi",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G960F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-G970U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A730F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "jackpot2lte",
        "hardware": "qcom"
    },
    {
        "model": "SM-A032F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "320",
        "brand": "samsung",
        "os": "a3core",
        "hardware": "m168"
    },
    {
        "model": "SM-J610FN",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j6primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-J700T",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7eltetmo",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G570F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "on5xelte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G960F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-N975U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N981U",
        "sdk": "33",
        "android_version": "13",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "samsung",
        "os": "c1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A037U",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a03su",
        "hardware": "mt6765"
    },
    {
        "model": "SM-G781B",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "360",
        "brand": "samsung",
        "os": "r8q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A605FN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a6plte",
        "hardware": "qcom"
    },
    {
        "model": "SM-A720F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "a7y17lte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-J415F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j4primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-P585Y",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "samsung",
        "os": "gtanotexllte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "samsung j3",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j3xlteatt",
        "hardware": "universal3475"
    },
    {
        "model": "GT-I9300",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "m0",
        "hardware": "smdk4x12"
    },
    {
        "model": "SM-T350",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "768x1024",
        "dpi": "240",
        "brand": "samsung",
        "os": "gt58wifi",
        "hardware": "qcom"
    },
    {
        "model": "galaxy star",
        "sdk": "28",
        "android_version": "9",
        "display": "480x854",
        "dpi": "240",
        "brand": "Nokia",
        "os": "FRT",
        "hardware": "mt6735"
    },
    {
        "model": "SM-G965F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-G930U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroqlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-A505F",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-C7000",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "c7ltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-N986B",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "c2s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-G950F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G950U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "435",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A7100",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "a7xltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-G975U1",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "446",
        "brand": "samsung",
        "os": "beyond2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G998B",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "samsung",
        "os": "p3s",
        "hardware": "exynos2100"
    },
    {
        "model": "SM-J260T1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "234",
        "brand": "samsung",
        "os": "j2corepltemtr",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-J500M",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5lte",
        "hardware": "qcom"
    },
    {
        "model": "SM-F926U",
        "sdk": "32",
        "android_version": "12",
        "display": "1326x1656",
        "dpi": "360",
        "brand": "samsung",
        "os": "q2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A102U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a10e",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-A202F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1339",
        "dpi": "320",
        "brand": "samsung",
        "os": "a20e",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-T567V",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "200",
        "brand": "Verizon",
        "os": "gtelltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J600F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "j6lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J510FN",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5xnlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9500",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatqltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G965U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A515F",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a51",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-J337P",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3topeltespr",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-J727T1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popeltemtr",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A510F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "a5xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G960F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "GT-I9301I",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "s3ve3gxx",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-G935A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "hero2qlteatt",
        "hardware": "qcom"
    },
    {
        "model": "SM-A510F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "a5xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G9500",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-A720F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "a7y17lte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-A217M",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a21s",
        "hardware": "exynos850"
    },
    {
        "model": "SM-G950U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G998B",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "samsung",
        "os": "p3s",
        "hardware": "exynos2100"
    },
    {
        "model": "SM-A205U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-G960U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "starqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-S906U",
        "sdk": "33",
        "android_version": "13",
        "display": "1080x2340",
        "dpi": "450",
        "brand": "samsung",
        "os": "g0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A715F",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a71",
        "hardware": "qcom"
    },
    {
        "model": "SM-J327T1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3popeltemtr",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-N950F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-T377R4",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gtesqlteusc",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G970U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "beyond0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N976V",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2xq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G9350",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "hero2qltechn",
        "hardware": "qcom"
    },
    {
        "model": "GT-N7000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "256",
        "brand": "Samsung",
        "os": "GT-N7000",
        "hardware": "smdk4210"
    },
    {
        "model": "SC-01F",
        "sdk": "27",
        "android_version": "4.4.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "SC-01F",
        "hardware": "qcom"
    },
    {
        "model": "SM-G975U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A205F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-T530",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "samsung",
        "os": "matissewifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-J510FN",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "267",
        "brand": "samsung",
        "os": "j5xnlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9750",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1480",
        "dpi": "320",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935L",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "hero2ltelgt",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G975F",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond2",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-A750GN",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a7y18lte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G998U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "samsung",
        "os": "p3q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-P580",
        "sdk": "24",
        "android_version": "7.0",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gtanotexlwifikx",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J530F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j5y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G950FD",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G935F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G950U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroqlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-G9730",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N960U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "crownqltesq",
        "hardware": "qcom"
    },
    {
        "model": "sm-t815y ",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "samsung",
        "os": "gts3llte",
        "hardware": "universal5433"
    },
    {
        "model": "SM-A125F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1339",
        "dpi": "360",
        "brand": "samsung",
        "os": "a12",
        "hardware": "mt6765"
    },
    {
        "model": "SM-G986U1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "y2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A750GN",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "a7y18lte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-J710FQ",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A013M",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1480",
        "dpi": "320",
        "brand": "samsung",
        "os": "a01core",
        "hardware": "mt6739"
    },
    {
        "model": "SM-S134DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a03su",
        "hardware": "mt6765"
    },
    {
        "model": "GT-N7000",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "800x1280",
        "dpi": "256",
        "brand": "Samsung",
        "os": "GT-N7000",
        "hardware": "smdk4210"
    },
    {
        "model": "SM-A013G",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1480",
        "dpi": "320",
        "brand": "samsung",
        "os": "a01core",
        "hardware": "mt6739"
    },
    {
        "model": "SM-G970U1",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J510H",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5x3g",
        "hardware": "qcom"
    },
    {
        "model": "SM-T713",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "samsung",
        "os": "gts28vewifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-S908B",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2316",
        "dpi": "420",
        "brand": "samsung",
        "os": "b0s",
        "hardware": "s5e9925"
    },
    {
        "model": "SM-A515U",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1507",
        "dpi": "315",
        "brand": "samsung",
        "os": "a51",
        "hardware": "exynos9611"
    },
    {
        "model": "GT-N7000",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "320",
        "brand": "Samsung",
        "os": "GT-N7000",
        "hardware": "smdk4210"
    },
    {
        "model": "SM-G973U1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A750FN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a7y18lte",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-N975U1",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J327T1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "277",
        "brand": "samsung",
        "os": "j3popeltemtr",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G610F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "411",
        "brand": "samsung",
        "os": "on7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G930F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "360",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G975F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond2",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-G900F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "336",
        "brand": "samsung",
        "os": "klte",
        "hardware": "qcom"
    },
    {
        "model": "ts-m704a",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3topltetfntmo",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A105F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "250",
        "brand": "samsung",
        "os": "a10",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G903W",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "s5neoltecan",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "GT-N7100",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "t03g",
        "hardware": "smdk4x12"
    },
    {
        "model": "SM-A205F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-G570M",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "on5xelte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-J700P",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7ltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-A107F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "280",
        "brand": "samsung",
        "os": "a10s",
        "hardware": "mt6762"
    },
    {
        "model": "SM-S515DL",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a51",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-G960U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "starqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-N970U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "d1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T377T",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gtesltetmo",
        "hardware": "universal3475"
    },
    {
        "model": "SM-S260DL",
        "sdk": "28",
        "android_version": "9",
        "display": "405x720",
        "dpi": "180",
        "brand": "samsung",
        "os": "j2corepltetfntmo",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G950U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A217F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a21s",
        "hardware": "exynos850"
    },
    {
        "model": "SM-G996U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "samsung",
        "os": "t2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G610F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "on7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A205F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-N960F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-G955U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G973F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-A515F",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "315",
        "brand": "samsung",
        "os": "a51",
        "hardware": "exynos9611"
    },
    {
        "model": "Galaxy s9",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "motorola",
        "os": "ali",
        "hardware": "qcom"
    },
    {
        "model": "SM-A530N",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G9860",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "y2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A705FN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1507",
        "dpi": "315",
        "brand": "samsung",
        "os": "a70q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G960F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-G930FD",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-A910F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a9xproltesea",
        "hardware": "qcom"
    },
    {
        "model": "SM-A710F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "405",
        "brand": "samsung",
        "os": "a7xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-A505FN",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-G925T",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "zeroltetmo",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "GT-I9505",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "384",
        "brand": "samsung",
        "os": "jflte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N900",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1440x2560",
        "dpi": "480",
        "brand": "samsung",
        "os": "trltetmo",
        "hardware": "qcom"
    },
    {
        "model": "SM-N920T",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "nobleltetmo",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-N960F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-N975F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-S908B",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2316",
        "dpi": "450",
        "brand": "samsung",
        "os": "b0s",
        "hardware": "s5e9925"
    },
    {
        "model": "SM-J327R7",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3poplteacg",
        "hardware": "qcom"
    },
    {
        "model": "SM-A102U",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "360",
        "brand": "samsung",
        "os": "a10e",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A715F",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "315",
        "brand": "samsung",
        "os": "a71",
        "hardware": "qcom"
    },
    {
        "model": "SM-N920V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Verizon",
        "os": "nobleltevzw",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-A105G",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a10",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-A127F",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1600",
        "dpi": "320",
        "brand": "samsung",
        "os": "a12s",
        "hardware": "exynos850"
    },
    {
        "model": "SM-N920C",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "noblelte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "sm-g532f",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-J510FN",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j5xnlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-T290",
        "sdk": "30",
        "android_version": "11",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gtowifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-A022M",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a02",
        "hardware": "mt6739"
    },
    {
        "model": "SM-A102U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1339",
        "dpi": "360",
        "brand": "samsung",
        "os": "a10e",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-A205U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-N981B",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "c1s",
        "hardware": "exynos990"
    },
    {
        "model": "A51",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "lge",
        "os": "cv3",
        "hardware": "cv3"
    },
    {
        "model": "SM-A105G",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a10",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-N9860",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1544",
        "dpi": "280",
        "brand": "samsung",
        "os": "c2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T710",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "240",
        "brand": "samsung",
        "os": "gts28wifi",
        "hardware": "universal5433"
    },
    {
        "model": "SM-A515U",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a51",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-G965F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-C710F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "jadelte",
        "hardware": "mt6757"
    },
    {
        "model": "SM-A320FL",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a3y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-T818V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "Verizon",
        "os": "gts210veltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-T510",
        "sdk": "28",
        "android_version": "9",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gta3xlwifi",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G920I",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "zeroflte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "GT-I9515",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "jfvelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-S205DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-A115F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a11q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "282",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-J330F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "274",
        "brand": "samsung",
        "os": "j3y17lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A205U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "300",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-A225F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a22",
        "hardware": "mt6769t"
    },
    {
        "model": "SM-t377A",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "a01q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T825",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "210",
        "brand": "samsung",
        "os": "gts3llte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930V",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "Verizon",
        "os": "heroqltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-A215U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a21",
        "hardware": "mt6765"
    },
    {
        "model": "SM-G570Y",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "on5xelte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-J730G",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G6100",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "on7xltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-G9006V",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "384",
        "brand": "samsung",
        "os": "klte",
        "hardware": "qcom"
    },
    {
        "model": "sm-j320a",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3xlteatt",
        "hardware": "universal3475"
    },
    {
        "model": "SM-N960F",
        "sdk": "28",
        "android_version": "9",
        "display": "608x1080",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-N960U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "crownqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-G891A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "poseidonlteatt",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-S111DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "320",
        "brand": "samsung",
        "os": "a01q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T560NU",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "140",
        "brand": "samsung",
        "os": "gtelwifiue",
        "hardware": "qcom"
    },
    {
        "model": "SM-T580",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "900x1440",
        "dpi": "160",
        "brand": "samsung",
        "os": "gtaxlwifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A505FN",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-N960F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-A600FN",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a6lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "s5neoltevl",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "259",
        "brand": "samsung",
        "os": "s5neoltecan",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G610F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "314",
        "brand": "samsung",
        "os": "on7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J260F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "j2corelte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G781U",
        "sdk": "30",
        "android_version": "11",
        "display": "810x2009",
        "dpi": "360",
        "brand": "samsung",
        "os": "r8q",
        "hardware": "qcom"
    },
    {
        "model": "GT-I9195",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "serranoltexx",
        "hardware": "qcom"
    },
    {
        "model": "SM-M127F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "m12",
        "hardware": "exynos850"
    },
    {
        "model": "SM-A310F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a3xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-S506DL",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-G965U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "411",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "note 30 plus",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "320",
        "brand": "samsung",
        "os": "a10e",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-S102DL",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a10e",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-M215F",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "m21",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-G935FD",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G955U1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "dream2qlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-A022F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "360",
        "brand": "samsung",
        "os": "a02",
        "hardware": "mt6739"
    },
    {
        "model": "SM-N9005",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "540x960",
        "dpi": "160",
        "brand": "samsung",
        "os": "hlte",
        "hardware": "samsungexynox8895"
    },
    {
        "model": "SM-J727P",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-J710MN/DS",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N920P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "nobleltespr",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G950F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G900M",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "klte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G892U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "cruiserltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J610FN",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "238",
        "brand": "samsung",
        "os": "j6primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N900",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "ha3g",
        "hardware": "universal5420"
    },
    {
        "model": "SM-G955F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-N950F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G988U1",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "z3q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T719",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "360",
        "brand": "samsung",
        "os": "gts28velte",
        "hardware": "qcom"
    },
    {
        "model": "g975",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "c2s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-A530W",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "jackpotltecan",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G930F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G991U",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "o1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J701MT",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7velte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N920I",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "noblelte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-T580",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gtaxlwifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G950F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-N975U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J727P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "256",
        "brand": "samsung",
        "os": "j7popltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-G928T",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "245",
        "brand": "samsung",
        "os": "zenltetmo",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G9880",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "z3q",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-G935A",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2qlteatt",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-J600F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j6lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G986B",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "y2s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-N975U",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "314",
        "brand": "samsung",
        "os": "hero2qlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-A530F",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "jackpotlte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G950F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A910F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a9xproltesea",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A125F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a12",
        "hardware": "mt6765"
    },
    {
        "model": "SM-G955U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J415F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j4primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-A300F",
        "sdk": "29",
        "android_version": "10",
        "display": "540x960",
        "dpi": "234",
        "brand": "Samsung",
        "os": "a3ltexx",
        "hardware": "qcom"
    },
    {
        "model": "SM-J727VPP",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "Verizon",
        "os": "j7popltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-G960U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2220",
        "dpi": "450",
        "brand": "samsung",
        "os": "starqltesq",
        "hardware": "qcom"
    },
    {
        "model": "Note 8",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1520",
        "dpi": "320",
        "brand": "Xiaomi",
        "os": "olivelite",
        "hardware": "qcom"
    },
    {
        "model": "SM-G615F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "j7maxlte",
        "hardware": "mt6757"
    },
    {
        "model": "SM-G975F",
        "sdk": "28",
        "android_version": "9",
        "display": "607x1080",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond2",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-G925F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "Samsung",
        "os": "zerolte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-A205U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-J701F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7velte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A530W",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "jackpotltecan",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-N9005",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hltexx",
        "hardware": "qcom"
    },
    {
        "model": "SM-N960F",
        "sdk": "28",
        "android_version": "9",
        "display": "1440x2960",
        "dpi": "560",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-J600F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j6lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G955U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SCV38",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "KDDI",
        "os": "SCV38",
        "hardware": "qcom"
    },
    {
        "model": "SM-J330G",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3y17lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-J727V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Verizon",
        "os": "j7popltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-S367VL",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3topeltetfnvzw",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-J700M",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a3xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G950F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A107F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a10s",
        "hardware": "mt6762"
    },
    {
        "model": "SM-J600G/DS",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j6lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N950U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-A320FL",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a3y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N975F",
        "sdk": "28",
        "android_version": "9.0",
        "display": "720x1560",
        "dpi": "240",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-J730G",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G920F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "zeroflte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G950N",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamlteks",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A125F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "360",
        "brand": "samsung",
        "os": "a12",
        "hardware": "mt6765"
    },
    {
        "model": "SM-A505FM",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "405",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-N950U",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A920F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "270",
        "brand": "samsung",
        "os": "a9y18qlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-X200",
        "sdk": "31",
        "android_version": "12",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "samsung",
        "os": "gta8wifi",
        "hardware": "ums512_25c10"
    },
    {
        "model": "SM-T820",
        "sdk": "28",
        "android_version": "9",
        "display": "1152x1536",
        "dpi": "210",
        "brand": "samsung",
        "os": "gts3lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-T380",
        "sdk": "28",
        "android_version": "9",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gta2swifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-T555",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "768x1024",
        "dpi": "160",
        "brand": "samsung",
        "os": "T555XXU1CQJ5",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-G930AZ",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroqlteaio",
        "hardware": "qcom"
    },
    {
        "model": "SM-C7000",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "c7ltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-G981B",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "samsung",
        "os": "x1s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-N9500",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5xnlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G970F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1560",
        "dpi": "320",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-A136U",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1600",
        "dpi": "300",
        "brand": "samsung",
        "os": "a13x",
        "hardware": "mt6833"
    },
    {
        "model": "SM-J727T",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popeltetmo",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "GT-I9301I",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "s3ve3g",
        "hardware": "qcom"
    },
    {
        "model": "SM-G920F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "samsung",
        "os": "zeroflte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-J327T",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3popeltetmo",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-N900T",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hltetmo",
        "hardware": "qcom"
    },
    {
        "model": "SM-A015F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a01q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G928L",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "zenltelgt",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-T350",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "768x1024",
        "dpi": "144",
        "brand": "samsung",
        "os": "gt58wifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-J730G",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A9100",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a9xproltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-J730F",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N975U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A520F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a5y17lte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-G930U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "heroqlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-N960F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-G965W",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2qltecs",
        "hardware": "qcom"
    },
    {
        "model": "SM-J400F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "271",
        "brand": "samsung",
        "os": "j4lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-J730GM",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SAMSUNG-SM-T817A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "240",
        "brand": "samsung",
        "os": "gts210lteatt",
        "hardware": "universal5433"
    },
    {
        "model": "SM-G930P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "heroqltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-N981U",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "c1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A207F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1339",
        "dpi": "320",
        "brand": "samsung",
        "os": "a20s",
        "hardware": "qcom"
    },
    {
        "model": "Note10+",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1480",
        "dpi": "320",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-J727AZ",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "271",
        "brand": "samsung",
        "os": "j7popelteaio",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G955F",
        "sdk": "29",
        "android_version": "10",
        "display": "1440x2960",
        "dpi": "480",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SAMSUNG-SM-G891A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "poseidonlteatt",
        "hardware": "qcom"
    },
    {
        "model": "SM-A725F",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "OPPO",
        "os": "OP4BA5L1",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "GT-I9300",
        "sdk": "25",
        "android_version": "7.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "m0",
        "hardware": "smdk4x12"
    },
    {
        "model": "SM-A205F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-A520F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "a5y17lte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-S767VL",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7topeltetfnvzw",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-F926B",
        "sdk": "32",
        "android_version": "12",
        "display": "1326x1656",
        "dpi": "360",
        "brand": "samsung",
        "os": "q2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x2220",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A107M",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a10s",
        "hardware": "mt6762"
    },
    {
        "model": "SM-G935F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-J260A",
        "sdk": "28",
        "android_version": "9",
        "display": "405x720",
        "dpi": "180",
        "brand": "samsung",
        "os": "j2coreplteatt",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A536U",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "338",
        "brand": "samsung",
        "os": "a53x",
        "hardware": "s5e8825"
    },
    {
        "model": "SM-A405FN",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a40",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-J701F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j6lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-975l",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j3topeltespr",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "GT-i9301i",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "s3ve3g",
        "hardware": "qcom"
    },
    {
        "model": "SM-G998U",
        "sdk": "28",
        "android_version": "9.0",
        "display": "720x1600",
        "dpi": "320",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-S536DL",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "324",
        "brand": "samsung",
        "os": "a53x",
        "hardware": "s5e8825"
    },
    {
        "model": "SM-A205U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-J337VPP",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "250",
        "brand": "Verizon",
        "os": "j3topeltevzw",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-A520F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "a5y17lte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-G930W8",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroltebmc",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G981U1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "x1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950U1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "greatqlteue",
        "hardware": "qcom"
    },
    {
        "model": "GT-P7500",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "Samsung",
        "os": "p4",
        "hardware": "p3"
    },
    {
        "model": "SM-N960F",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1080",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-T350",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "768x1024",
        "dpi": "160",
        "brand": "samsung",
        "os": "gt58wifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-T733",
        "sdk": "31",
        "android_version": "12",
        "display": "1200x1920",
        "dpi": "255",
        "brand": "samsung",
        "os": "gts7fewifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "288",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A720F",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "jackpotlte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-T820",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "184",
        "brand": "samsung",
        "os": "gts3lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-M317F",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "338",
        "brand": "samsung",
        "os": "m31s",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-T580",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "samsung",
        "os": "gtaxlwifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G955U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2960",
        "dpi": "560",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A115U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a11q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-A207F",
        "sdk": "29",
        "android_version": "9",
        "display": "1440x2960",
        "dpi": "560",
        "brand": "samsung",
        "os": "a20s",
        "hardware": "qualcommsdm450"
    },
    {
        "model": "SM-G970F",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond0",
        "hardware": "exynos9820"
    },
    {
        "model": "SCV38",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "473",
        "brand": "KDDI",
        "os": "SCV38",
        "hardware": "qcom"
    },
    {
        "model": "SM-G960F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "510",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-A505U",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-A037G",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a03s",
        "hardware": "mt6765"
    },
    {
        "model": "SM-G955U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-N981U1",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "samsung",
        "os": "c1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G9700UD ",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j3toplteatt",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A320F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a3y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J727P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7popltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-G615F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "j7maxlte",
        "hardware": "mt6757"
    },
    {
        "model": "SM-J730FM",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "285",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A730F",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "jackpot2lte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-J701M",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7velte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N7505",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "hllte",
        "hardware": "universal5260"
    },
    {
        "model": "SM-G965U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J260A",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "j2coreplteatt",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G935T",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2qltetmo",
        "hardware": "qcom"
    },
    {
        "model": "SM-N920T",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "nobleltetmo",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G988U1",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1600",
        "dpi": "279",
        "brand": "samsung",
        "os": "z3q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2678",
        "dpi": "640",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-X200",
        "sdk": "30",
        "android_version": "11",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "samsung",
        "os": "gta8wifi",
        "hardware": "ums512_wifionly"
    },
    {
        "model": "SM-T350",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "768x1024",
        "dpi": "128",
        "brand": "samsung",
        "os": "gt58wifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-T500",
        "sdk": "30",
        "android_version": "11",
        "display": "1200x2000",
        "dpi": "240",
        "brand": "samsung",
        "os": "gta4lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-T720",
        "sdk": "28",
        "android_version": "9",
        "display": "1200x1920",
        "dpi": "266",
        "brand": "samsung",
        "os": "gts4lvwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-A202F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a20e",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-T510",
        "sdk": "30",
        "android_version": "11",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gta3xlwifi",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-G920FD",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "621",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G935V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "Verizon",
        "os": "hero2qltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-A115AZ",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a11q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T585",
        "sdk": "24",
        "android_version": "7.0",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gtaxllte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J337A",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3toplteatt",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-C710F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "jadelte",
        "hardware": "mt6757"
    },
    {
        "model": "SM-A037M",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a03s",
        "hardware": "mt6765"
    },
    {
        "model": "SM-G935U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "hero2qlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-N970U1",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "d1q",
        "hardware": "qcom"
    },
    {
        "model": "GT-I9300",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "290",
        "brand": "samsung",
        "os": "m0",
        "hardware": "smdk4x12"
    },
    {
        "model": "SAMSUNG-SM-J320A",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3xlteatt",
        "hardware": "universal3475"
    },
    {
        "model": "SM-A505F",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-G390F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "xcover4lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-P600",
        "sdk": "25",
        "android_version": "7.1",
        "display": "1600x2560",
        "dpi": "320",
        "brand": "samsung",
        "os": "n1awifi",
        "hardware": "universal5420"
    },
    {
        "model": "SM-G610F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "810x1440",
        "dpi": "332",
        "brand": "samsung",
        "os": "on7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G965U1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2qlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9200",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "nobleltehk",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G930V",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Verizon",
        "os": "heroqltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G973U1",
        "sdk": "28",
        "android_version": "9",
        "display": "608x1080",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9508",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x2220",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatqltecmcc",
        "hardware": "qcom"
    },
    {
        "model": "Xs Max",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "mt6580"
    },
    {
        "model": "SM-M105M",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "m10lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N985F",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "c2s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-G955U1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2qlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G998U1",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "samsung",
        "os": "p3q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N910V",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "Verizon",
        "os": "trltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-S757BL",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7topltetfntmo",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-T595",
        "sdk": "28",
        "android_version": "9",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gta2xllte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N960U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "crownqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J530FM",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j5y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G955U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x2220",
        "dpi": "480",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G975U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J710F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7xeltexx",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A526U",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "315",
        "brand": "samsung",
        "os": "a52xq",
        "hardware": "qcom"
    },
    {
        "model": "SM-T217S",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "600x1024",
        "dpi": "160",
        "brand": "samsung",
        "os": "lt02ltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G955F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-S115DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a11q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G975F",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "beyond2",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-G950F",
        "sdk": "28",
        "android_version": "9",
        "display": "1440x2678",
        "dpi": "560",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G925I",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "zerolte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-S115DL",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a11q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G960F",
        "sdk": "28",
        "android_version": "9",
        "display": "1440x2960",
        "dpi": "640",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-S124DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "320",
        "brand": "samsung",
        "os": "a02q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G6100",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "on7xltechn",
        "hardware": "qcom"
    },
    {
        "model": "Samsung Galaxy J7 Refine ",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7topeltespr",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-A705FN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a70q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G900T",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "kltetmo",
        "hardware": "qcom"
    },
    {
        "model": "SM-A510F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "330",
        "brand": "samsung",
        "os": "a5xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-J260T1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "270",
        "brand": "samsung",
        "os": "j2corepltemtr",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A510M",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a5xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G935FD",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G973F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond1",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-T320",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1600x2560",
        "dpi": "320",
        "brand": "samsung",
        "os": "mondrianwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955W",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dream2qltecan",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G975F",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond2",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-N950U1",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatqlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-T835",
        "sdk": "29",
        "android_version": "10",
        "display": "1287x2059",
        "dpi": "290",
        "brand": "samsung",
        "os": "gts4llte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935W8",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "hero2ltebmc",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G900F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "klte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G973F",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1520",
        "dpi": "280",
        "brand": "samsung",
        "os": "beyond1",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-G9650",
        "sdk": "29",
        "android_version": "10",
        "display": "1440x2960",
        "dpi": "600",
        "brand": "samsung",
        "os": "star2qltechn",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-J320A",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3xlteatt",
        "hardware": "universal3475"
    },
    {
        "model": "SM-T561",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "800x1280",
        "dpi": "200",
        "brand": "samsung",
        "os": "gtel3g",
        "hardware": "sc8830"
    },
    {
        "model": "SM-G973U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9005",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-T580",
        "sdk": "24",
        "android_version": "7.0",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gtaxlwifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N950F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G930V",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "Verizon",
        "os": "heroqltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Verizon",
        "os": "hero2qltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-J700T1",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j7eltemtr",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-N970U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "samsung",
        "os": "d1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G780F",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "360",
        "brand": "samsung",
        "os": "r8s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-G930U",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "450",
        "brand": "samsung",
        "os": "heroqlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-T510",
        "sdk": "29",
        "android_version": "10",
        "display": "900x1440",
        "dpi": "210",
        "brand": "samsung",
        "os": "gta3xlwifi",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-G975F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond0",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-T830",
        "sdk": "29",
        "android_version": "10",
        "display": "1600x2560",
        "dpi": "256",
        "brand": "samsung",
        "os": "gts4lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-A105F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a10",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-T380",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gta2swifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-N920C",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "noblelte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-T387T",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gtasliteltetmo",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-J730F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "j7lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "384",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J330FN",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3y17lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A515F",
        "sdk": "33",
        "android_version": "13",
        "display": "810x1800",
        "dpi": "315",
        "brand": "samsung",
        "os": "a51",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-A037F",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1600",
        "dpi": "300",
        "brand": "samsung",
        "os": "a03s",
        "hardware": "mt6765"
    },
    {
        "model": "SM-A305FN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a30",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-A750FN",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a7y18lte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G920F",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "Samsung",
        "os": "zeroflte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-T819",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "samsung",
        "os": "gts210velte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G970U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G986U",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2008",
        "dpi": "450",
        "brand": "samsung",
        "os": "y2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T830",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "samsung",
        "os": "gts4lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-T830",
        "sdk": "28",
        "android_version": "9",
        "display": "1200x1920",
        "dpi": "270",
        "brand": "samsung",
        "os": "gts4lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-A205U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-A025U",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a02q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A605FN",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a6plte",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-J727AZ",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popelteaio",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G988U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "420",
        "brand": "samsung",
        "os": "z3q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Verizon",
        "os": "heroqltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-G530H",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "540x960",
        "dpi": "216",
        "brand": "samsung",
        "os": "fortunave3g",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950F",
        "sdk": "32",
        "android_version": "12",
        "display": "1440x2960",
        "dpi": "560",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-N920I",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "noblelte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G973U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T580",
        "sdk": "24",
        "android_version": "7.0",
        "display": "900x1440",
        "dpi": "160",
        "brand": "samsung",
        "os": "gtaxlwifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N770F",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "360",
        "brand": "samsung",
        "os": "r7",
        "hardware": "exynos9810"
    },
    {
        "model": "SM-G9200",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "zerofltechn",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-T710",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "210",
        "brand": "samsung",
        "os": "gts28wifi",
        "hardware": "universal5433"
    },
    {
        "model": "SM-G960F",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1440",
        "dpi": "320",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "mt6580"
    },
    {
        "model": "SM-J700H",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7e3g",
        "hardware": "universal3475"
    },
    {
        "model": "SAMSUNG-SM-J327A",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3popelteatt",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A127F",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1600",
        "dpi": "300",
        "brand": "samsung",
        "os": "a12s",
        "hardware": "exynos850"
    },
    {
        "model": "GT-I8160",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "480x800",
        "dpi": "240",
        "brand": "samsung",
        "os": "codina",
        "hardware": "samsungcodina"
    },
    {
        "model": "SM-N975F",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2s",
        "hardware": "exynos9825"
    },
    {
        "model": "SM-G950W",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqltecan",
        "hardware": "qcom"
    },
    {
        "model": "Nexus 10",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1600x2560",
        "dpi": "320",
        "brand": "Google",
        "os": "manta",
        "hardware": "manta"
    },
    {
        "model": "SM-S124DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1600",
        "dpi": "280",
        "brand": "samsung",
        "os": "a02q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935P",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "hero2qltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-A510F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "405",
        "brand": "samsung",
        "os": "a5xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G975F",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2008",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond2",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-T355Y",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "768x1024",
        "dpi": "160",
        "brand": "samsung",
        "os": "gt58lte",
        "hardware": "qcom"
    },
    {
        "model": "SM-J610F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j6primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G975U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1080",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J710F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A022F",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a02",
        "hardware": "mt6739"
    },
    {
        "model": "SM-T377R4",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "samsung",
        "os": "gtesqlteusc",
        "hardware": "qcom"
    },
    {
        "model": "SM-T820",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "240",
        "brand": "samsung",
        "os": "gts3lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1440x2678",
        "dpi": "560",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A705FN",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a70q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J260T1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "j2corepltemtr",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G6200",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2160",
        "dpi": "432",
        "brand": "samsung",
        "os": "Phoenix",
        "hardware": "qcom"
    },
    {
        "model": "SM-J320V",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Verizon",
        "os": "j3ltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-S205DL",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-A605FN",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a6plte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G991U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "samsung",
        "os": "o1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-M515F",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1507",
        "dpi": "338",
        "brand": "samsung",
        "os": "m51",
        "hardware": "qcom"
    },
    {
        "model": "SM-T550",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "768x1024",
        "dpi": "160",
        "brand": "samsung",
        "os": "gt510wifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-J700T",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7eltetmo",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G991B",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "510",
        "brand": "samsung",
        "os": "o1s",
        "hardware": "exynos2100"
    },
    {
        "model": "SM-N976B",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2008",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2x",
        "hardware": "exynos9825"
    },
    {
        "model": "SM-G950U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A500F",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "288",
        "brand": "samsung",
        "os": "a5ulte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A405FM",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "a40",
        "hardware": "exynos7904"
    },
    {
        "model": "SAMSUNG-SM-J327A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3popelteatt",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-T510",
        "sdk": "29",
        "android_version": "10",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gta3xlwifi",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-A505FN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "405",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-A720F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a7y17lte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-A520F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "a5y17lte",
        "hardware": "samsungexynos7880"
    },
    {
        "model": "SM-G965U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G960F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-J337P",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j3topeltespr",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-J710MN",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G960F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1339",
        "dpi": "320",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-G900H",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "k3gxx",
        "hardware": "universal5422"
    },
    {
        "model": "SM-J337A",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3toplteatt",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A125U",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a12u",
        "hardware": "mt6765"
    },
    {
        "model": "SM-J727VPP",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Verizon",
        "os": "j7popltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SPH-L600",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "240",
        "brand": "samsung",
        "os": "meliusltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9005",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9200",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "samsung",
        "os": "nobleltehk",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G965F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-J415GN",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j4primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-J710FN",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "on7xreflte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-S367VL",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j3topeltetfnvzw",
        "hardware": "exynos7885"
    },
    {
        "model": "SCV38",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "472",
        "brand": "KDDI",
        "os": "SCV38",
        "hardware": "qcom"
    },
    {
        "model": "SM-J710F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G920F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "zeroflte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-J610F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j6primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-M307FN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "m30s",
        "hardware": "exynos9611"
    },
    {
        "model": "SM-A705W",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a70q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "star2qlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950U",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G9550",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dream2qltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-J610F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "j6primelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N920K",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "nobleltektt",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-N986B",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2008",
        "dpi": "320",
        "brand": "samsung",
        "os": "c2s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-G935P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2qltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-T377W",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gtesltebmc",
        "hardware": "universal3475"
    },
    {
        "model": "SM-T561",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "800x1280",
        "dpi": "180",
        "brand": "samsung",
        "os": "gtel3g",
        "hardware": "sc8830"
    },
    {
        "model": "SM-G985F",
        "sdk": "28",
        "android_version": "9.0",
        "display": "720x1600",
        "dpi": "320",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-A730F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "jackpot2lte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G950U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-N950U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "419",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-N910F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "samsung",
        "os": "trltexx",
        "hardware": "qcom"
    },
    {
        "model": "SM-G781B",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "338",
        "brand": "samsung",
        "os": "r8q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J701F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7velte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-S260DL",
        "sdk": "28",
        "android_version": "9",
        "display": "405x720",
        "dpi": "203",
        "brand": "samsung",
        "os": "j2corepltetfntmo",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G996B",
        "sdk": "28",
        "android_version": "9.0",
        "display": "720x1600",
        "dpi": "320",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-G960F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "starlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-S205DL",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-J337AZ",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3toplteaio",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A102U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "a10e",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G925F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "zerolte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G965F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-S127DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a12u",
        "hardware": "mt6765"
    },
    {
        "model": "SM-J701F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7velte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G998U1",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "p3q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J327VPP",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "Verizon",
        "os": "j3popltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-N920P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "nobleltespr",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-A310F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Samsung",
        "os": "a3xeltexx",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-A505FN",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-G615FU",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "j7maxlte",
        "hardware": "mt6757"
    },
    {
        "model": "SM-N950F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-J337VPP",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Verizon",
        "os": "j3topeltevzw",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G955F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-G920P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "zerofltespr",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SPH-L710",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "d2spr",
        "hardware": "qcom"
    },
    {
        "model": "sch-i679",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownqlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-A505F",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1507",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-J260AZ",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "j2coreplteaio",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A725F",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "315",
        "brand": "samsung",
        "os": "a72q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A710F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "a7xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-A202F",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a20e",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-N976V",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2xq",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-S902L",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "kltetfnvzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950N",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatlteks",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-S215DL",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a21",
        "hardware": "mt6765"
    },
    {
        "model": "SM-N975F",
        "sdk": "28",
        "android_version": "9.0",
        "display": "720x1560",
        "dpi": "320",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-N975U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J737VPP",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "Verizon",
        "os": "j7topeltevzw",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G925W8",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "zeroltebmc",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G973U",
        "sdk": "28",
        "android_version": "9",
        "display": "608x1080",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935R4",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "samsung",
        "os": "hero2qlteusc",
        "hardware": "qcom"
    },
    {
        "model": "SM-J400F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j4lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-N960U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J600G",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "j6lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "http://www.specdevice.com",
        "sdk": "30",
        "android_version": "11",
        "display": "1200x2000",
        "dpi": "240",
        "brand": "samsung",
        "os": "gta4lwifi",
        "hardware": "qcom"
    },
    {
        "model": "SAMSUNG-SM-G925A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "zerolteatt",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-T290",
        "sdk": "29",
        "android_version": "10",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gtowifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "hero2qltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950U",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G973F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-G935F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "419",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G9880",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "z3q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J701F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7velte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-T819",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1536x2048",
        "dpi": "320",
        "brand": "samsung",
        "os": "gts210velte",
        "hardware": "qcom"
    },
    {
        "model": "GT-I9505",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "jfltexx",
        "hardware": "qcom"
    },
    {
        "model": "s10",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a30s",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-J327T1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j3popeltemtr",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A136U",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a13x",
        "hardware": "mt6833"
    },
    {
        "model": "SM-G955F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A115A",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "a11q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J727VPP",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Verizon",
        "os": "j7popltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-J730F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SAMSUNG-SM-J727AZ",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popelteaio",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-N950F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1440x2560",
        "dpi": "560",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-S111DL",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a01q",
        "hardware": "qcom"
    },
    {
        "model": "SM-J250F/DS",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "j2y18lte",
        "hardware": "qcom"
    },
    {
        "model": "GT-I9000",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "600x1024",
        "dpi": "160",
        "brand": "samsung",
        "os": "GT-I9000",
        "hardware": "sun8iw11p1"
    },
    {
        "model": "SM-M305M",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "m30lte",
        "hardware": "exynos7904"
    },
    {
        "model": "SM-S124DL",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a02q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935V",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Verizon",
        "os": "hero2qltevzw",
        "hardware": "qcom"
    },
    {
        "model": "SM-T380",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gta2swifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1480",
        "dpi": "280",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "GT-I9295",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "jactivelte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G935F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G920V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Verizon",
        "os": "zerofltevzw",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G991U1",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "408",
        "brand": "samsung",
        "os": "o1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J730FM",
        "sdk": "24",
        "android_version": "7.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "j7y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-S367VL",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3topeltetfnvzw",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-T350",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "768x1024",
        "dpi": "210",
        "brand": "samsung",
        "os": "gt58wifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dreamlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-J727P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j7popltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-T810",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1152x1536",
        "dpi": "240",
        "brand": "samsung",
        "os": "gts210wifi",
        "hardware": "universal5433"
    },
    {
        "model": "GT-I9100",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "480x800",
        "dpi": "240",
        "brand": "Samsung",
        "os": "GT-I9100",
        "hardware": "smdk4210"
    },
    {
        "model": "SM-G900R4",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "432",
        "brand": "samsung",
        "os": "klteusc",
        "hardware": "qcom"
    },
    {
        "model": "SM-J400G",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j4lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-J727P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-J530F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j5y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G973U1",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G955U",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-N960U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-J337VPP",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "Verizon",
        "os": "j3topeltevzw",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-G780F",
        "sdk": "33",
        "android_version": "13",
        "display": "810x1800",
        "dpi": "360",
        "brand": "samsung",
        "os": "r8s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-G935F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G975U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "beyond2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A510F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "a5xelte",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-A530F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "jackpotlte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SAMSUNG-SM-N920A",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "noblelteatt",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-A920F",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a9y18qlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-J710F",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-S102DL",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a10e",
        "hardware": "exynos7884B"
    },
    {
        "model": "SM-G930F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2lte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-A260G",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "540x960",
        "dpi": "240",
        "brand": "samsung",
        "os": "a2corelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "Galaxy S21 Ultra",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "HUAWEI",
        "os": "HWDUB-Q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T350",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "768x1024",
        "dpi": "180",
        "brand": "samsung",
        "os": "gt58wifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G985F",
        "sdk": "28",
        "android_version": "10.0",
        "display": "720x1560",
        "dpi": "320",
        "brand": "samsung",
        "os": "beyond1q",
        "hardware": "mt6580"
    },
    {
        "model": "SM-G611F",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "on7xreflte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G955F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "dream2lte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-J327T1",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j3popeltemtr",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G975U1",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1520",
        "dpi": "280",
        "brand": "samsung",
        "os": "beyond2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N960F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "crownlte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-A015AZ",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "a01q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G570F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "on5xelte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G970U",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "450",
        "brand": "samsung",
        "os": "beyond0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G965U1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "star2qlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-A326U",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1339",
        "dpi": "300",
        "brand": "samsung",
        "os": "a32x",
        "hardware": "mt6853"
    },
    {
        "model": "SM-J710F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "samsung",
        "os": "j7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J737T",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7topltetmo",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-T580",
        "sdk": "24",
        "android_version": "7.0",
        "display": "900x1440",
        "dpi": "240",
        "brand": "samsung",
        "os": "gtaxlwifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-T580",
        "sdk": "24",
        "android_version": "7.0",
        "display": "900x1440",
        "dpi": "210",
        "brand": "samsung",
        "os": "gtaxlwifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J727T1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "j7popeltemtr",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G935W8",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2ltebmc",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-G930P",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "heroqltespr",
        "hardware": "qcom"
    },
    {
        "model": "SM-G981U",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2009",
        "dpi": "480",
        "brand": "samsung",
        "os": "x1q",
        "hardware": "qcom"
    },
    {
        "model": "Galaxy j7 star 4512",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1520",
        "dpi": "360",
        "brand": "motorola",
        "os": "ocean",
        "hardware": "qcom"
    },
    {
        "model": "SM-G928F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "zenlte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G996U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "480",
        "brand": "samsung",
        "os": "t2q",
        "hardware": "qcom"
    },
    {
        "model": "GT-I9505",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "432",
        "brand": "samsung",
        "os": "jfltexx",
        "hardware": "qcom"
    },
    {
        "model": "SM-A205U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-J727T",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popeltetmo",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-T390",
        "sdk": "28",
        "android_version": "9",
        "display": "600x960",
        "dpi": "160",
        "brand": "samsung",
        "os": "gtactive2wifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G986B",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2678",
        "dpi": "450",
        "brand": "samsung",
        "os": "y2s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-N920V",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "Verizon",
        "os": "nobleltevzw",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G965F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "star2lte",
        "hardware": "samsungexynos9810"
    },
    {
        "model": "SM-N975F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2s",
        "hardware": "exynos9825"
    },
    {
        "model": "SM-N975F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2s",
        "hardware": "exynos9825"
    },
    {
        "model": "SM-G610G",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "810x1440",
        "dpi": "360",
        "brand": "samsung",
        "os": "on7xelte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G925F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "zerolte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-N950U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-F711U",
        "sdk": "32",
        "android_version": "12",
        "display": "1080x2640",
        "dpi": "480",
        "brand": "samsung",
        "os": "b2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "454",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-G930F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "herolte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-T595",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "900x1440",
        "dpi": "180",
        "brand": "samsung",
        "os": "gta2xllte",
        "hardware": "qcom"
    },
    {
        "model": "SM-J530F",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5y17lte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-A015AZ",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "a01q",
        "hardware": "qcom"
    },
    {
        "model": "SM-G928P",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "280",
        "brand": "samsung",
        "os": "zenltespr",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-J337V",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Verizon",
        "os": "j3topeltevzw",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G935F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1440x2560",
        "dpi": "448",
        "brand": "samsung",
        "os": "hero2ltexx",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "SM-N770F",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1507",
        "dpi": "315",
        "brand": "samsung",
        "os": "r7",
        "hardware": "exynos9810"
    },
    {
        "model": "SM-G930F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "gracerlte",
        "hardware": "samsungexynos8890"
    },
    {
        "model": "UN65NU7200",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "greatqlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-J330F",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3y17lte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-A730F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "jackpot2lte",
        "hardware": "samsungexynos7885"
    },
    {
        "model": "SM-J500FN",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j5nlte",
        "hardware": "qcom"
    },
    {
        "model": "SM-T290",
        "sdk": "28",
        "android_version": "9",
        "display": "800x1280",
        "dpi": "213",
        "brand": "samsung",
        "os": "gtowifi",
        "hardware": "qcom"
    },
    {
        "model": "SM-G950U1",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqlteue",
        "hardware": "qcom"
    },
    {
        "model": "SM-A526W",
        "sdk": "31",
        "android_version": "12",
        "display": "810x1800",
        "dpi": "315",
        "brand": "samsung",
        "os": "a52xq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A528B",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a52sxq",
        "hardware": "qcom"
    },
    {
        "model": "SM-N9208",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "noblelte",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-A405FN",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1440",
        "dpi": "405",
        "brand": "samsung",
        "os": "a40",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-895",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2190",
        "dpi": "480",
        "brand": "samsung",
        "os": "d1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-S506DL",
        "sdk": "30",
        "android_version": "11",
        "display": "810x1506",
        "dpi": "315",
        "brand": "samsung",
        "os": "a50",
        "hardware": "exynos9610"
    },
    {
        "model": "SM-S205DL",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "306",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-T560NU",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "800x1280",
        "dpi": "160",
        "brand": "samsung",
        "os": "gtelwifiue",
        "hardware": "qcom"
    },
    {
        "model": "SM-A805N",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1280",
        "dpi": "240",
        "brand": "samsung",
        "os": "aosp",
        "hardware": "android_x86"
    },
    {
        "model": "SM-N981U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2400",
        "dpi": "450",
        "brand": "samsung",
        "os": "c1q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A750GN",
        "sdk": "29",
        "android_version": "10",
        "display": "810x1440",
        "dpi": "315",
        "brand": "samsung",
        "os": "a7y18lte",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G950U",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "dreamqltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-A705W",
        "sdk": "28",
        "android_version": "9",
        "display": "810x1800",
        "dpi": "315",
        "brand": "samsung",
        "os": "a70q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N975U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2280",
        "dpi": "420",
        "brand": "samsung",
        "os": "d2q",
        "hardware": "qcom"
    },
    {
        "model": "SM-N950F",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "SM-A520F",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "a5xeltexx",
        "hardware": "samsungexynos7580"
    },
    {
        "model": "SM-G935T",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2qltetmo",
        "hardware": "qcom"
    },
    {
        "model": "SM-J727T1",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7popeltemtr",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-J701M",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j7velte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "galexy a10e",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "motorola",
        "os": "hannah",
        "hardware": "qcom"
    },
    {
        "model": "SM-N910C",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1440x2560",
        "dpi": "448",
        "brand": "samsung",
        "os": "treltexx",
        "hardware": "universal5433"
    },
    {
        "model": "SM-A025U",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1339",
        "dpi": "280",
        "brand": "samsung",
        "os": "a02q",
        "hardware": "qcom"
    },
    {
        "model": "SM-A205U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1339",
        "dpi": "180",
        "brand": "samsung",
        "os": "a20p",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-S367VL",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "j3topeltetfnvzw",
        "hardware": "exynos7885"
    },
    {
        "model": "SM-G960W",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "starqltecs",
        "hardware": "qcom"
    },
    {
        "model": "SM-G780F",
        "sdk": "30",
        "android_version": "11",
        "display": "810x2009",
        "dpi": "360",
        "brand": "samsung",
        "os": "r8s",
        "hardware": "exynos990"
    },
    {
        "model": "SM-N975F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2009",
        "dpi": "450",
        "brand": "samsung",
        "os": "d2s",
        "hardware": "exynos9825"
    },
    {
        "model": "SM-G570F",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "on5xelte",
        "hardware": "samsungexynos7570"
    },
    {
        "model": "SM-G970F",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "samsung",
        "os": "beyond0",
        "hardware": "exynos9820"
    },
    {
        "model": "SM-S901U",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2340",
        "dpi": "420",
        "brand": "samsung",
        "os": "r0q",
        "hardware": "qcom"
    },
    {
        "model": "SM-T390",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "600x960",
        "dpi": "160",
        "brand": "samsung",
        "os": "gtactive2wifi",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "galaxy j2",
        "sdk": "80",
        "android_version": "6.0.2",
        "display": "480x854",
        "dpi": "240",
        "brand": "OPPO",
        "os": "A11w",
        "hardware": "mt6582"
    },
    {
        "model": "SM-G965U",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "samsung",
        "os": "star2qltesq",
        "hardware": "qcom"
    },
    {
        "model": "SM-T585",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "samsung",
        "os": "gtaxllte",
        "hardware": "samsungexynos7870"
    },
    {
        "model": "SM-G920W8",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "samsung",
        "os": "zerofltebmc",
        "hardware": "samsungexynos7420"
    },
    {
        "model": "SM-G9350",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "hero2qltechn",
        "hardware": "qcom"
    },
    {
        "model": "SM-J530",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "samsung",
        "os": "a5y17lte",
        "hardware": "samsungexynos7880"
    }
]
sony = [
    {
        "model": "Xperia S",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "nozomi",
        "hardware": "semc"
    },
    {
        "model": "H8324",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "Sony",
        "os": "H8324",
        "hardware": "qcom"
    },
    {
        "model": "Xperia XZ Premium, G8142, G8141, SO-04K, SO-04J",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Xiaomi",
        "os": "cancro",
        "hardware": "qcom"
    },
    {
        "model": "C6903",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6903",
        "hardware": "qcom"
    },
    {
        "model": "Xperia L",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Sony",
        "os": "taoshan",
        "hardware": "qcom"
    },
    {
        "model": "C6833",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Sony",
        "os": "C6833",
        "hardware": "qcom"
    },
    {
        "model": "E6885",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6603",
        "hardware": "qcom"
    },
    {
        "model": "SO-03H",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "docomo",
        "os": "SO-03H",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z2",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "sirius",
        "hardware": "qcom"
    },
    {
        "model": "Xperia x",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "HUAWEI",
        "os": "HWRIO",
        "hardware": "qcom"
    },
    {
        "model": "SO-04G",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "docomo",
        "os": "SO-04G",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z1",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "honami",
        "hardware": "qcom"
    },
    {
        "model": "XQ-AU52",
        "sdk": "31",
        "android_version": "12",
        "display": "1080x2520",
        "dpi": "356",
        "brand": "Sony",
        "os": "XQ-AU52",
        "hardware": "qcom"
    },
    {
        "model": "E6883",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6883",
        "hardware": "qcom"
    },
    {
        "model": "D6603",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "asus",
        "os": "ASUS_Z002",
        "hardware": "redhookbay"
    },
    {
        "model": "F8331",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "F8331",
        "hardware": "qcom"
    },
    {
        "model": "E6533",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6533",
        "hardware": "qcom"
    },
    {
        "model": "C2105",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "480x854",
        "dpi": "240",
        "brand": "Sony",
        "os": "unknown",
        "hardware": "qcom"
    },
    {
        "model": "SGP521",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Sony",
        "os": "SGP521",
        "hardware": "qcom"
    },
    {
        "model": "F3112",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "272",
        "brand": "Sony",
        "os": "F3112",
        "hardware": "mt6755"
    },
    {
        "model": "D6653",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6653",
        "hardware": "qcom"
    },
    {
        "model": "D6653",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6653",
        "hardware": "qcom"
    },
    {
        "model": "D6603",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6603",
        "hardware": "qcom"
    },
    {
        "model": "D6633",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6633",
        "hardware": "qcom"
    },
    {
        "model": "H4213",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "H4213",
        "hardware": "qcom"
    },
    {
        "model": "C6902",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6902",
        "hardware": "qcom"
    },
    {
        "model": "H3223",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "H3223",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "yuga",
        "hardware": "qcom"
    },
    {
        "model": "D5803",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "D5803",
        "hardware": "qcom"
    },
    {
        "model": "XF75",
        "sdk": "30",
        "android_version": "11",
        "display": "1440x3168",
        "dpi": "720",
        "brand": "OnePlus",
        "os": "OnePlus8Pro",
        "hardware": "qcom"
    },
    {
        "model": "D6603",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6603",
        "hardware": "qcom"
    },
    {
        "model": "C3",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2502",
        "hardware": "qcom"
    },
    {
        "model": "E6653",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6653",
        "hardware": "qcom"
    },
    {
        "model": "F5121",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "F5121",
        "hardware": "qcom"
    },
    {
        "model": "D6503",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "480x854",
        "dpi": "190",
        "brand": "Sony",
        "os": "D6503",
        "hardware": "mt6582"
    },
    {
        "model": "C6903",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1794",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6903",
        "hardware": "qcom"
    },
    {
        "model": "C6503",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6503",
        "hardware": "qcom"
    },
    {
        "model": "G8141",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1877",
        "dpi": "236",
        "brand": "Sony",
        "os": "G8141",
        "hardware": "qcom"
    },
    {
        "model": "E2303",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E2303",
        "hardware": "qcom"
    },
    {
        "model": "D2305",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2305",
        "hardware": "qcom"
    },
    {
        "model": "E5823",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1196",
        "dpi": "320",
        "brand": "Sony",
        "os": "E5823",
        "hardware": "qcom"
    },
    {
        "model": "F3311",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "F3311",
        "hardware": "mt6735"
    },
    {
        "model": "C6603",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1794",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6603",
        "hardware": "qcom"
    },
    {
        "model": "E6553",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6553",
        "hardware": "qcom"
    },
    {
        "model": "E5823",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E5823",
        "hardware": "qcom"
    },
    {
        "model": "D6503",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6503",
        "hardware": "qcom"
    },
    {
        "model": "D2302",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2302",
        "hardware": "qcom"
    },
    {
        "model": "F8331",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "F8331",
        "hardware": "qcom"
    },
    {
        "model": "C6802",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Sony",
        "os": "C6802",
        "hardware": "qcom"
    },
    {
        "model": "Xperia XZs",
        "sdk": "22",
        "android_version": "5.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "unknown",
        "sdk": "24",
        "android_version": "7.0",
        "display": "1440x2560",
        "dpi": "640",
        "brand": "Sony",
        "os": "kagura",
        "hardware": "elsa"
    },
    {
        "model": "D2302",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2302",
        "hardware": "eagle"
    },
    {
        "model": "D6503",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "370",
        "brand": "Sony",
        "os": "D6503",
        "hardware": "qcom"
    },
    {
        "model": "E5333",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E5333",
        "hardware": "mt6752"
    },
    {
        "model": "Xperia Z1",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x1920",
        "dpi": "336",
        "brand": "Sony",
        "os": "honami",
        "hardware": "qcom"
    },
    {
        "model": "D6563",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6563",
        "hardware": "qcom"
    },
    {
        "model": "E5803",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E5803",
        "hardware": "qcom"
    },
    {
        "model": "C6802",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Sony",
        "os": "C6802",
        "hardware": "qcom"
    },
    {
        "model": "E6653",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6653",
        "hardware": "qcom"
    },
    {
        "model": "F3111",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "F3111",
        "hardware": "mt6755"
    },
    {
        "model": "H4113",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "Sony",
        "os": "H4113",
        "hardware": "qcom"
    },
    {
        "model": "D6603",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1794",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6603",
        "hardware": "qcom"
    },
    {
        "model": "F8132",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "F8132",
        "hardware": "qcom"
    },
    {
        "model": "G8142",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "Sony",
        "os": "G8142",
        "hardware": "qcom"
    },
    {
        "model": "XQ-AU52",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2520",
        "dpi": "420",
        "brand": "Sony",
        "os": "XQ-AU52",
        "hardware": "qcom"
    },
    {
        "model": "F8342",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "401",
        "brand": "Samsung",
        "os": "hero2qlteatt",
        "hardware": "qcom"
    },
    {
        "model": "H3123",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "H3123",
        "hardware": "qcom"
    },
    {
        "model": "D6633",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6633",
        "hardware": "qcom"
    },
    {
        "model": "G8441",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "G8441",
        "hardware": "qcom"
    },
    {
        "model": "D5803",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "D5803",
        "hardware": "qcom"
    },
    {
        "model": "E6653",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1776",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6653",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z3 Compact",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "D5803",
        "hardware": "qcom"
    },
    {
        "model": "C6502",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6502",
        "hardware": "qcom"
    },
    {
        "model": "E5563",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E5563",
        "hardware": "mt6752"
    },
    {
        "model": "C6603",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6603",
        "hardware": "qcom"
    },
    {
        "model": "C2104",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "480x854",
        "dpi": "240",
        "brand": "Sony",
        "os": "unknown",
        "hardware": "qcom"
    },
    {
        "model": "D6503",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6503",
        "hardware": "qcom"
    },
    {
        "model": "E2312",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E2312",
        "hardware": "qcom"
    },
    {
        "model": "F3313",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "F3313",
        "hardware": "mt6735"
    },
    {
        "model": "D6603",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6603",
        "hardware": "qcom"
    },
    {
        "model": "H4113",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1776",
        "dpi": "480",
        "brand": "Sony",
        "os": "H4113",
        "hardware": "qcom"
    },
    {
        "model": "SGP321",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Sony",
        "os": "SGP321",
        "hardware": "qcom"
    },
    {
        "model": "D5503",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "D5503",
        "hardware": "qcom"
    },
    {
        "model": "C6902",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6902",
        "hardware": "qcom"
    },
    {
        "model": "C5502",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "C5502",
        "hardware": "qcom"
    },
    {
        "model": "E6653",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "441",
        "brand": "Sony",
        "os": "E6653",
        "hardware": "qcom"
    },
    {
        "model": "F3116",
        "sdk": "23",
        "android_version": "6.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "F3116",
        "hardware": "mt6755"
    },
    {
        "model": "E6653",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "240",
        "brand": "Sony",
        "os": "E6653",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z2",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "KDDI",
        "os": "SOL25",
        "hardware": "qcom"
    },
    {
        "model": "D5322",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Sony",
        "os": "D5322",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z1",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "honami",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "yuga",
        "hardware": "qcom"
    },
    {
        "model": "D2533",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2533",
        "hardware": "qcom"
    },
    {
        "model": "G3412",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "G3412",
        "hardware": "mt6757"
    },
    {
        "model": "D5803",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "335",
        "brand": "Sony",
        "os": "D5803",
        "hardware": "qcom"
    },
    {
        "model": "G8141",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "Sony",
        "os": "G8141",
        "hardware": "qcom"
    },
    {
        "model": "SGP312",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Sony",
        "os": "SGP312",
        "hardware": "qcom"
    },
    {
        "model": "C5503",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "C5503",
        "hardware": "qcom"
    },
    {
        "model": "F3115",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "Sony",
        "os": "F3115",
        "hardware": "mt6755"
    },
    {
        "model": "G3112",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "720x1280",
        "dpi": "360",
        "brand": "Sony",
        "os": "G3112",
        "hardware": "mt6757"
    },
    {
        "model": "C6806_GPe",
        "sdk": "21",
        "android_version": "5.0",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Sony",
        "os": "C6806",
        "hardware": "qcom"
    },
    {
        "model": "SO-04G",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "240",
        "brand": "docomo",
        "os": "SO-04G",
        "hardware": "qcom"
    },
    {
        "model": "SGP312",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1200x1920",
        "dpi": "240",
        "brand": "Sony",
        "os": "SGP312",
        "hardware": "qcom"
    },
    {
        "model": "SGP712",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1600x2560",
        "dpi": "320",
        "brand": "Sony",
        "os": "SGP712",
        "hardware": "qcom"
    },
    {
        "model": "D5503",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "D5503",
        "hardware": "qcom"
    },
    {
        "model": "E2303",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E2303",
        "hardware": "qcom"
    },
    {
        "model": "F8131",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "F8131",
        "hardware": "qcom"
    },
    {
        "model": "D2303",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2303",
        "hardware": "qcom"
    },
    {
        "model": "C6833",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "320",
        "brand": "Sony",
        "os": "C6833",
        "hardware": "qcom"
    },
    {
        "model": "E5333",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E5333",
        "hardware": "mt6752"
    },
    {
        "model": "E6653",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6653",
        "hardware": "qcom"
    },
    {
        "model": "E5663",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E5663",
        "hardware": "mt6795"
    },
    {
        "model": "D6603",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "leo",
        "hardware": "qcom"
    },
    {
        "model": "D6503",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6503",
        "hardware": "qcom"
    },
    {
        "model": "C6603",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6603",
        "hardware": "qcom"
    },
    {
        "model": "D6708",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "verizon",
        "os": "D6708",
        "hardware": "qcom"
    },
    {
        "model": "Xperia SP",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "huashan",
        "hardware": "qcom"
    },
    {
        "model": "Xperia acro S",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "hikari",
        "hardware": "semc"
    },
    {
        "model": "E5563",
        "sdk": "22",
        "android_version": "5.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E5563",
        "hardware": "mt6752"
    },
    {
        "model": "E6883",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6883",
        "hardware": "qcom"
    },
    {
        "model": "E2306",
        "sdk": "21",
        "android_version": "5.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E2306",
        "hardware": "qcom"
    },
    {
        "model": "E6883",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1794",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6883",
        "hardware": "qcom"
    },
    {
        "model": "H8216",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2160",
        "dpi": "408",
        "brand": "Sony",
        "os": "H8216",
        "hardware": "qcom"
    },
    {
        "model": "C6903",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "C6903",
        "hardware": "qcom"
    },
    {
        "model": "D2502",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2502",
        "hardware": "qcom"
    },
    {
        "model": "SGP771",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "1600x2560",
        "dpi": "320",
        "brand": "Sony",
        "os": "SGP771",
        "hardware": "qcom"
    },
    {
        "model": "E6853",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E6853",
        "hardware": "qcom"
    },
    {
        "model": "SGP621",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1200x1920",
        "dpi": "320",
        "brand": "Sony",
        "os": "SGP621",
        "hardware": "qcom"
    },
    {
        "model": "G8341",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "540",
        "brand": "Sony",
        "os": "G8341",
        "hardware": "qcom"
    },
    {
        "model": "G3311",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "G3311",
        "hardware": "mt6735"
    },
    {
        "model": "D6503",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1776",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6503",
        "hardware": "qcom"
    },
    {
        "model": "E5603",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E5603",
        "hardware": "mt6795"
    },
    {
        "model": "D6502",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6502",
        "hardware": "qcom"
    },
    {
        "model": "E5823",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E5823",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z3C",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "z3c",
        "hardware": "qcom"
    },
    {
        "model": "E5823",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E5823",
        "hardware": "qcom"
    },
    {
        "model": "F3211",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "F3211",
        "hardware": "mt6755"
    },
    {
        "model": "C1905",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "480x854",
        "dpi": "240",
        "brand": "Sony",
        "os": "C1905",
        "hardware": "qcom"
    },
    {
        "model": "D6653",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6653",
        "hardware": "qcom"
    },
    {
        "model": "D2533",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Sony",
        "os": "D2533",
        "hardware": "qcom"
    },
    {
        "model": "E5823",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "720x1280",
        "dpi": "360",
        "brand": "Sony",
        "os": "E5823",
        "hardware": "qcom"
    },
    {
        "model": "E2312",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "E2312",
        "hardware": "qcom"
    },
    {
        "model": "F8332",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "F8332",
        "hardware": "qcom"
    },
    {
        "model": "cube 5.0_2GB",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "320",
        "brand": "XOLO",
        "os": "cube_5_0_2GB",
        "hardware": "mt6582"
    },
    {
        "model": "XZ Premium",
        "sdk": "22",
        "android_version": "5.1",
        "display": "540x960",
        "dpi": "240",
        "brand": "Sony",
        "os": "gxq6580_weg_l",
        "hardware": "mt6580"
    },
    {
        "model": "D6603",
        "sdk": "26",
        "android_version": "8.0.0",
        "display": "1080x1920",
        "dpi": "420",
        "brand": "samsung",
        "os": "greatlte",
        "hardware": "samsungexynos8895"
    },
    {
        "model": "Xperia Z1 Compact",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "amami",
        "hardware": "qcom"
    },
    {
        "model": "Z3",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "D6603",
        "hardware": "qcom"
    },
    {
        "model": "Xperia Z3 d6603",
        "sdk": "22",
        "android_version": "5.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "z3",
        "hardware": "qcom"
    },
    {
        "model": "D5803",
        "sdk": "23",
        "android_version": "6.0.1",
        "display": "720x1280",
        "dpi": "320",
        "brand": "Sony",
        "os": "D5803",
        "hardware": "qcom"
    },
    {
        "model": "H8276",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2160",
        "dpi": "480",
        "brand": "Sony",
        "os": "H8276",
        "hardware": "qcom"
    },
    {
        "model": "E5303",
        "sdk": "23",
        "android_version": "6.0",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "Sony",
        "os": "E5303",
        "hardware": "mt6752"
    },
    {
        "model": "G8142",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x1920",
        "dpi": "408",
        "brand": "Sony",
        "os": "G8142",
        "hardware": "qcom"
    },
    {
        "model": "D5322",
        "sdk": "21",
        "android_version": "5.0.2",
        "display": "720x1280",
        "dpi": "240",
        "brand": "Sony",
        "os": "D5322",
        "hardware": "qcom"
    }
]
vivo = [
    {
        "model": "X21A",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "vivo",
        "os": "PD1728",
        "hardware": "qcom"
    },
    {
        "model": "V2024",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "vivo",
        "os": "1920",
        "hardware": "qcom"
    },
    {
        "model": "Y81S",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "1808",
        "hardware": "mt6762"
    },
    {
        "model": "1901",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1544",
        "dpi": "320",
        "brand": "vivo",
        "os": "1901",
        "hardware": "mt6762"
    },
    {
        "model": "V2041",
        "sdk": "30",
        "android_version": "11",
        "display": "1080x2408",
        "dpi": "440",
        "brand": "vivo",
        "os": "2041",
        "hardware": "mt6833"
    },
    {
        "model": "V1934A",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "vivo",
        "os": "PD1934",
        "hardware": "mt6768"
    },
    {
        "model": "V2028",
        "sdk": "31",
        "android_version": "12",
        "display": "720x1600",
        "dpi": "300",
        "brand": "vivo",
        "os": "2028",
        "hardware": "qcom"
    },
    {
        "model": "1723",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "vivo",
        "os": "1723",
        "hardware": "qcom"
    },
    {
        "model": "1906",
        "sdk": "30",
        "android_version": "11",
        "display": "720x1544",
        "dpi": "320",
        "brand": "vivo",
        "os": "1906",
        "hardware": "qcom"
    },
    {
        "model": "1806",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "vivo",
        "os": "1806",
        "hardware": "mt6771"
    },
    {
        "model": "1808",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "1808",
        "hardware": "mt6762"
    },
    {
        "model": "1907",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "vivo",
        "os": "1907",
        "hardware": "mt6768"
    },
    {
        "model": "X9",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "vivo",
        "os": "PD1616",
        "hardware": "qcom"
    },
    {
        "model": "1812",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "288",
        "brand": "vivo",
        "os": "1812",
        "hardware": "mt6761"
    },
    {
        "model": "1724",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1440",
        "dpi": "320",
        "brand": "vivo",
        "os": "PD1731",
        "hardware": "qcom"
    },
    {
        "model": "X9i",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "vivo",
        "os": "PD1624",
        "hardware": "qcom"
    },
    {
        "model": "1901_19",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1544",
        "dpi": "320",
        "brand": "vivo",
        "os": "1901",
        "hardware": "mt6762"
    },
    {
        "model": "1812",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "1812",
        "hardware": "mt6761"
    },
    {
        "model": "1815",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "1815",
        "hardware": "mt6762"
    },
    {
        "model": "Xplay6L",
        "sdk": "25",
        "android_version": "7.1.1",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "vivo",
        "os": "PD1610",
        "hardware": "qcom"
    },
    {
        "model": "1806",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "vivo",
        "os": "1806",
        "hardware": "mt6771"
    },
    {
        "model": "1902",
        "sdk": "28",
        "android_version": "9",
        "display": "720x1544",
        "dpi": "320",
        "brand": "vivo",
        "os": "1902",
        "hardware": "mt6765"
    },
    {
        "model": "1727",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "vivo",
        "os": "1727ID",
        "hardware": "qcom"
    },
    {
        "model": "1820",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "303",
        "brand": "vivo",
        "os": "1820",
        "hardware": "mt6762"
    },
    {
        "model": "1811",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "1811",
        "hardware": "qcom"
    },
    {
        "model": "X9L",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "1080x1920",
        "dpi": "480",
        "brand": "vivo",
        "os": "PD1616",
        "hardware": "qcom"
    },
    {
        "model": "1716",
        "sdk": "25",
        "android_version": "7.1.2",
        "display": "720x1440",
        "dpi": "320",
        "brand": "vivo",
        "os": "1716",
        "hardware": "qcom"
    },
    {
        "model": "v17",
        "sdk": "28",
        "android_version": "9",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "vivo",
        "os": "1723CF",
        "hardware": "qcom"
    },
    {
        "model": "1814",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "1814",
        "hardware": "mt6762"
    },
    {
        "model": "1612",
        "sdk": "24",
        "android_version": "7.0",
        "display": "720x1280",
        "dpi": "320",
        "brand": "vivo",
        "os": "1601",
        "hardware": "mt6755"
    },
    {
        "model": "V1732A",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "PD1732",
        "hardware": "mt6762"
    },
    {
        "model": "1804",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "vivo",
        "os": "1804",
        "hardware": "qcom"
    },
    {
        "model": "1806",
        "sdk": "27",
        "android_version": "8.1.0",
        "display": "1080x2280",
        "dpi": "480",
        "brand": "vivo",
        "os": "1806",
        "hardware": "mt6771"
    },
    {
        "model": "2015",
        "sdk": "29",
        "android_version": "10",
        "display": "720x1520",
        "dpi": "320",
        "brand": "vivo",
        "os": "2015",
        "hardware": "mt6765"
    },
    {
        "model": "1951",
        "sdk": "29",
        "android_version": "10",
        "display": "1080x2340",
        "dpi": "480",
        "brand": "vivo",
        "os": "1951",
        "hardware": "qcom"
    }
]

versions = [
    {
        "version": "5.0.8",
        "code": "1376634"
    },
    {
        "version": "5.1.7",
        "code": "2218950"
    },
    {
        "version": "6.10.1",
        "code": "5257472"
    },
    {
        "version": "6.11.2",
        "code": "5547416"
    },
    {
        "version": "6.12.0",
        "code": "5856007"
    },
    {
        "version": "6.12.1",
        "code": "5879188"
    },
    {
        "version": "6.12.2",
        "code": "5914807"
    },
    {
        "version": "6.13.0",
        "code": "6189164"
    },
    {
        "version": "6.13.1",
        "code": "6208041"
    },
    {
        "version": "6.13.3",
        "code": "6280649"
    },
    {
        "version": "6.14.0",
        "code": "6323749"
    },
    {
        "version": "6.14.0",
        "code": "6456473"
    },
    {
        "version": "6.14.1",
        "code": "6527593"
    },
    {
        "version": "6.15.0",
        "code": "6648672"
    },
    {
        "version": "6.15.0",
        "code": "6809797"
    },
    {
        "version": "6.15.0",
        "code": "6891295"
    },
    {
        "version": "6.16.0",
        "code": "7097676"
    },
    {
        "version": "6.16.0",
        "code": "7186551"
    },
    {
        "version": "6.16.0",
        "code": "7274492"
    },
    {
        "version": "6.16.1",
        "code": "7369808"
    },
    {
        "version": "6.17.0",
        "code": "7483428"
    },
    {
        "version": "6.17.0",
        "code": "7713781"
    },
    {
        "version": "6.17.1",
        "code": "7792671"
    },
    {
        "version": "6.18.0",
        "code": "8031086"
    },
    {
        "version": "6.18.0",
        "code": "8133161"
    },
    {
        "version": "6.18.0",
        "code": "8241704"
    },
    {
        "version": "6.18.0",
        "code": "8317903"
    },
    {
        "version": "6.19.0",
        "code": "8582325"
    },
    {
        "version": "6.19.0",
        "code": "8700864"
    },
    {
        "version": "6.19.0",
        "code": "8847895"
    },
    {
        "version": "6.19.0",
        "code": "8886221"
    },
    {
        "version": "6.20.0",
        "code": "9204850"
    },
    {
        "version": "6.20.0",
        "code": "9353187"
    },
    {
        "version": "6.20.1",
        "code": "9409530"
    },
    {
        "version": "6.20.1",
        "code": "9476507"
    },
    {
        "version": "6.20.2",
        "code": "9494173"
    },
    {
        "version": "6.21.0",
        "code": "9627240"
    },
    {
        "version": "6.21.0",
        "code": "9804755"
    },
    {
        "version": "6.21.0",
        "code": "9921663"
    },
    {
        "version": "6.21.2",
        "code": "9956336"
    },
    {
        "version": "6.21.2",
        "code": "9956337"
    },
    {
        "version": "6.22.0",
        "code": "10227271"
    },
    {
        "version": "6.22.0",
        "code": "10368623"
    },
    {
        "version": "6.22.0",
        "code": "10529824"
    },
    {
        "version": "6.22.0",
        "code": "10569317"
    },
    {
        "version": "6.23.0",
        "code": "10886602"
    },
    {
        "version": "6.23.0",
        "code": "11001525"
    },
    {
        "version": "6.23.0",
        "code": "11152246"
    },
    {
        "version": "6.23.0",
        "code": "11152254"
    },
    {
        "version": "6.24.0",
        "code": "11467175"
    },
    {
        "version": "6.24.0",
        "code": "11628516"
    },
    {
        "version": "6.24.0",
        "code": "11776170"
    },
    {
        "version": "7.0.0",
        "code": "12080497"
    },
    {
        "version": "7.0.0",
        "code": "12103120"
    },
    {
        "version": "7.1.0",
        "code": "12138101"
    },
    {
        "version": "7.1.0",
        "code": "12399039"
    },
    {
        "version": "7.1.1",
        "code": "12505108"
    },
    {
        "version": "7.2.0",
        "code": "12678588"
    },
    {
        "version": "7.2.0",
        "code": "12894558"
    },
    {
        "version": "7.2.0",
        "code": "12953501"
    },
    {
        "version": "7.2.1",
        "code": "12998762"
    },
    {
        "version": "7.2.2",
        "code": "13167125"
    },
    {
        "version": "7.2.3",
        "code": "13175448"
    },
    {
        "version": "7.2.4",
        "code": "13207465"
    },
    {
        "version": "7.3.0",
        "code": "13211814"
    },
    {
        "version": "7.3.0",
        "code": "13252488"
    },
    {
        "version": "7.3.0",
        "code": "13328396"
    },
    {
        "version": "7.3.0",
        "code": "13357693"
    },
    {
        "version": "7.3.0",
        "code": "13428238"
    },
    {
        "version": "7.3.0",
        "code": "13447540"
    },
    {
        "version": "7.3.0",
        "code": "13447541"
    },
    {
        "version": "7.4.0",
        "code": "13617090"
    },
    {
        "version": "7.4.0",
        "code": "13673128"
    },
    {
        "version": "7.3.1",
        "code": "13678552"
    },
    {
        "version": "7.4.0",
        "code": "13688692"
    },
    {
        "version": "7.4.0",
        "code": "13806513"
    },
    {
        "version": "7.4.0",
        "code": "13841095"
    },
    {
        "version": "7.5.0",
        "code": "14047999"
    },
    {
        "version": "7.5.0",
        "code": "14082771"
    },
    {
        "version": "7.5.0",
        "code": "14135411"
    },
    {
        "version": "7.5.0",
        "code": "14240471"
    },
    {
        "version": "7.5.0",
        "code": "14276131"
    },
    {
        "version": "7.5.1",
        "code": "14510519"
    },
    {
        "version": "7.5.2",
        "code": "14547085"
    },
    {
        "version": "7.6.0",
        "code": "14592506"
    },
    {
        "version": "7.6.0",
        "code": "14649552"
    },
    {
        "version": "7.6.0",
        "code": "14708479"
    },
    {
        "version": "7.7.0",
        "code": "14945148"
    },
    {
        "version": "7.7.0",
        "code": "14997179"
    },
    {
        "version": "7.6.1",
        "code": "14996309"
    },
    {
        "version": "7.7.0",
        "code": "15049153"
    },
    {
        "version": "7.7.0",
        "code": "15123498"
    },
    {
        "version": "7.7.0",
        "code": "15235526"
    },
    {
        "version": "7.8.0",
        "code": "15435389"
    },
    {
        "version": "7.8.0",
        "code": "15552925"
    },
    {
        "version": "7.8.0",
        "code": "15655929"
    },
    {
        "version": "7.8.0",
        "code": "15677960"
    },
    {
        "version": "7.8.0",
        "code": "15693177"
    },
    {
        "version": "7.9.0",
        "code": "15997156"
    },
    {
        "version": "7.9.0",
        "code": "16085896"
    },
    {
        "version": "7.9.0",
        "code": "16288123"
    },
    {
        "version": "7.9.0",
        "code": "16414541"
    },
    {
        "version": "7.9.0",
        "code": "16414543"
    },
    {
        "version": "7.9.2",
        "code": "16553907"
    },
    {
        "version": "7.9.1",
        "code": "16508983"
    },
    {
        "version": "7.9.1",
        "code": "16508986"
    },
    {
        "version": "7.10.0",
        "code": "16732668"
    },
    {
        "version": "7.10.0",
        "code": "16838479"
    },
    {
        "version": "7.10.0",
        "code": "16887320"
    },
    {
        "version": "7.10.0",
        "code": "17047892"
    },
    {
        "version": "7.11.0",
        "code": "17371373"
    },
    {
        "version": "7.11.0",
        "code": "17476525"
    },
    {
        "version": "7.11.0",
        "code": "17639608"
    },
    {
        "version": "7.11.0",
        "code": "17690090"
    },
    {
        "version": "7.11.0",
        "code": "17712920"
    },
    {
        "version": "7.11.0",
        "code": "17712926"
    },
    {
        "version": "7.11.1",
        "code": "17776137"
    },
    {
        "version": "7.12.0",
        "code": "18020870"
    },
    {
        "version": "7.12.0",
        "code": "18187053"
    },
    {
        "version": "7.12.0",
        "code": "18297871"
    },
    {
        "version": "7.12.0",
        "code": "18317857"
    },
    {
        "version": "7.12.1",
        "code": "18439029"
    },
    {
        "version": "7.12.1",
        "code": "18439032"
    },
    {
        "version": "7.13.0",
        "code": "18650373"
    },
    {
        "version": "7.13.0",
        "code": "18770142"
    },
    {
        "version": "7.13.0",
        "code": "18906164"
    },
    {
        "version": "7.13.0",
        "code": "18986441"
    },
    {
        "version": "7.13.0",
        "code": "19013743"
    },
    {
        "version": "7.13.1",
        "code": "19276019"
    },
    {
        "version": "7.14.0",
        "code": "19528317"
    },
    {
        "version": "7.14.0",
        "code": "19767666"
    },
    {
        "version": "7.14.0",
        "code": "19890715"
    },
    {
        "version": "7.14.0",
        "code": "20014569"
    },
    {
        "version": "7.14.0",
        "code": "20120481"
    },
    {
        "version": "7.14.0",
        "code": "20151314"
    },
    {
        "version": "7.14.0",
        "code": "20151320"
    },
    {
        "version": "7.15.0",
        "code": "20543579"
    },
    {
        "version": "7.15.0",
        "code": "20660854"
    },
    {
        "version": "7.15.0",
        "code": "20770943"
    },
    {
        "version": "7.15.0",
        "code": "20808502"
    },
    {
        "version": "7.15.0",
        "code": "20808504"
    },
    {
        "version": "7.16.0",
        "code": "21388836"
    },
    {
        "version": "7.16.0",
        "code": "21388876"
    },
    {
        "version": "7.16.0",
        "code": "21578176"
    },
    {
        "version": "7.16.0",
        "code": "21966528"
    },
    {
        "version": "7.16.0",
        "code": "22038485"
    },
    {
        "version": "7.17.0",
        "code": "23162604"
    },
    {
        "version": "7.17.0",
        "code": "23265084"
    },
    {
        "version": "7.17.0",
        "code": "23322199"
    },
    {
        "version": "7.17.0",
        "code": "23322206"
    },
    {
        "version": "7.18.0",
        "code": "24086480"
    },
    {
        "version": "7.18.0",
        "code": "24302095"
    },
    {
        "version": "7.18.0",
        "code": "24595347"
    },
    {
        "version": "7.18.0",
        "code": "24809118"
    },
    {
        "version": "7.18.0",
        "code": "24863788"
    },
    {
        "version": "7.18.1",
        "code": "25055364"
    },
    {
        "version": "7.18.2",
        "code": "25119635"
    },
    {
        "version": "7.18.2",
        "code": "25119636"
    },
    {
        "version": "7.19.0",
        "code": "25297122"
    },
    {
        "version": "7.19.0",
        "code": "25297129"
    },
    {
        "version": "7.19.0",
        "code": "25453447"
    },
    {
        "version": "7.19.0",
        "code": "25704759"
    },
    {
        "version": "7.19.0",
        "code": "25704772"
    },
    {
        "version": "7.19.0",
        "code": "25872807"
    },
    {
        "version": "7.19.0",
        "code": "25936825"
    },
    {
        "version": "7.19.1",
        "code": "26404397"
    },
    {
        "version": "7.19.1",
        "code": "26404404"
    },
    {
        "version": "7.20.0",
        "code": "26443138"
    },
    {
        "version": "7.20.0",
        "code": "26681339"
    },
    {
        "version": "7.20.0",
        "code": "26875547"
    },
    {
        "version": "7.20.0",
        "code": "27025861"
    },
    {
        "version": "7.20.0",
        "code": "27037564"
    },
    {
        "version": "7.20.0",
        "code": "27105654"
    },
    {
        "version": "8.0.0",
        "code": "27630442"
    },
    {
        "version": "8.0.0",
        "code": "27923403"
    },
    {
        "version": "8.0.0",
        "code": "27923434"
    },
    {
        "version": "7.21.0",
        "code": "28414909"
    },
    {
        "version": "7.21.0",
        "code": "28414923"
    },
    {
        "version": "7.21.1",
        "code": "28735170"
    },
    {
        "version": "7.22.0",
        "code": "28741243"
    },
    {
        "version": "7.22.0",
        "code": "28902140"
    },
    {
        "version": "7.22.0",
        "code": "29136038"
    },
    {
        "version": "8.0.0",
        "code": "29687306"
    },
    {
        "version": "8.0.0",
        "code": "29687307"
    },
    {
        "version": "8.0.0",
        "code": "29687308"
    },
    {
        "version": "8.0.0",
        "code": "29687309"
    },
    {
        "version": "8.1.0",
        "code": "30051248"
    },
    {
        "version": "8.1.0",
        "code": "30064543"
    },
    {
        "version": "8.1.0",
        "code": "30122962"
    },
    {
        "version": "8.1.0",
        "code": "30278352"
    },
    {
        "version": "8.1.0",
        "code": "30278354"
    },
    {
        "version": "8.2.0",
        "code": "30538609"
    },
    {
        "version": "8.2.0",
        "code": "30706772"
    },
    {
        "version": "8.2.0",
        "code": "30903420"
    },
    {
        "version": "8.2.0",
        "code": "30992010"
    },
    {
        "version": "8.2.0",
        "code": "30992015"
    },
    {
        "version": "8.2.0",
        "code": "30992021"
    },
    {
        "version": "8.3.0",
        "code": "31441110"
    },
    {
        "version": "8.3.0",
        "code": "31606904"
    },
    {
        "version": "8.3.0",
        "code": "31896301"
    },
    {
        "version": "8.3.0",
        "code": "31938068"
    },
    {
        "version": "8.4.0",
        "code": "32405865"
    },
    {
        "version": "8.4.0",
        "code": "32673414"
    },
    {
        "version": "8.4.0",
        "code": "32821114"
    },
    {
        "version": "8.4.0",
        "code": "32875821"
    },
    {
        "version": "8.4.0",
        "code": "32875826"
    },
    {
        "version": "8.4.0",
        "code": "32875829"
    },
    {
        "version": "8.4.0",
        "code": "32875831"
    },
    {
        "version": "8.5.0",
        "code": "33361487"
    },
    {
        "version": "8.5.0",
        "code": "33516302"
    },
    {
        "version": "8.5.0",
        "code": "33696654"
    },
    {
        "version": "8.5.0",
        "code": "33737790"
    },
    {
        "version": "8.5.1",
        "code": "33918520"
    },
    {
        "version": "8.5.1",
        "code": "33918522"
    },
    {
        "version": "8.5.1",
        "code": "33918523"
    },
    {
        "version": "8.5.1",
        "code": "33918528"
    },
    {
        "version": "8.5.1",
        "code": "33918531"
    },
    {
        "version": "9.0.0",
        "code": "34525903"
    },
    {
        "version": "9.0.0",
        "code": "34814732"
    },
    {
        "version": "9.0.0",
        "code": "34840905"
    },
    {
        "version": "8.5.2",
        "code": "34875509"
    },
    {
        "version": "8.5.2",
        "code": "34875513"
    },
    {
        "version": "8.5.2",
        "code": "34875519"
    },
    {
        "version": "8.5.2",
        "code": "34875525"
    },
    {
        "version": "9.0.0",
        "code": "34920046"
    },
    {
        "version": "9.0.0",
        "code": "34920050"
    },
    {
        "version": "9.0.0",
        "code": "35221413"
    },
    {
        "version": "9.0.0",
        "code": "35221427"
    },
    {
        "version": "9.0.0",
        "code": "35221453"
    },
    {
        "version": "9.1.0",
        "code": "35367610"
    },
    {
        "version": "9.0.1",
        "code": "35440028"
    },
    {
        "version": "9.0.1",
        "code": "35440030"
    },
    {
        "version": "9.0.1",
        "code": "35440031"
    },
    {
        "version": "9.0.1",
        "code": "35440032"
    },
    {
        "version": "9.0.1",
        "code": "35440033"
    },
    {
        "version": "9.1.0",
        "code": "35469529"
    },
    {
        "version": "9.1.0",
        "code": "35686917"
    },
    {
        "version": "9.1.0",
        "code": "35795937"
    },
    {
        "version": "9.1.0",
        "code": "35795940"
    },
    {
        "version": "9.1.5",
        "code": "35935469"
    },
    {
        "version": "9.1.5",
        "code": "36302796"
    },
    {
        "version": "9.1.5",
        "code": "36425083"
    },
    {
        "version": "9.2.0",
        "code": "36507662"
    },
    {
        "version": "9.1.5",
        "code": "36531351"
    },
    {
        "version": "9.1.5",
        "code": "36531355"
    },
    {
        "version": "9.1.5",
        "code": "36531359"
    },
    {
        "version": "9.1.5",
        "code": "36531364"
    },
    {
        "version": "9.1.5",
        "code": "36531368"
    },
    {
        "version": "9.2.0",
        "code": "36656231"
    },
    {
        "version": "9.2.0",
        "code": "36751260"
    },
    {
        "version": "9.2.0",
        "code": "36903624"
    },
    {
        "version": "9.2.0",
        "code": "37023763"
    },
    {
        "version": "9.2.0",
        "code": "37023764"
    },
    {
        "version": "9.2.0",
        "code": "37023765"
    },
    {
        "version": "9.2.0",
        "code": "37023766"
    },
    {
        "version": "9.2.0",
        "code": "37023767"
    },
    {
        "version": "9.2.5",
        "code": "37108327"
    },
    {
        "version": "9.2.5",
        "code": "37331386"
    },
    {
        "version": "9.2.5",
        "code": "37581779"
    },
    {
        "version": "9.2.5",
        "code": "37581798"
    },
    {
        "version": "9.2.5",
        "code": "37581809"
    },
    {
        "version": "9.2.5",
        "code": "37581824"
    },
    {
        "version": "9.2.5",
        "code": "37734551"
    },
    {
        "version": "9.2.5",
        "code": "37734553"
    },
    {
        "version": "9.2.5",
        "code": "37734555"
    },
    {
        "version": "9.2.5",
        "code": "37734557"
    },
    {
        "version": "9.2.5",
        "code": "37734562"
    },
    {
        "version": "9.3.0",
        "code": "37737123"
    },
    {
        "version": "9.3.0",
        "code": "37837196"
    },
    {
        "version": "9.3.5",
        "code": "38334689"
    },
    {
        "version": "9.3.0",
        "code": "38376122"
    },
    {
        "version": "9.3.0",
        "code": "38376123"
    },
    {
        "version": "9.3.0",
        "code": "38376124"
    },
    {
        "version": "9.3.0",
        "code": "38376125"
    },
    {
        "version": "9.3.0",
        "code": "38376126"
    },
    {
        "version": "9.3.5",
        "code": "38484906"
    },
    {
        "version": "9.3.5",
        "code": "38612508"
    },
    {
        "version": "9.3.5",
        "code": "38802257"
    },
    {
        "version": "9.3.5",
        "code": "38802274"
    },
    {
        "version": "9.3.5",
        "code": "38802287"
    },
    {
        "version": "9.3.5",
        "code": "38802302"
    },
    {
        "version": "9.3.5",
        "code": "38802318"
    },
    {
        "version": "9.4.0",
        "code": "38922625"
    },
    {
        "version": "9.4.0",
        "code": "39213970"
    },
    {
        "version": "9.4.0",
        "code": "39432129"
    },
    {
        "version": "9.4.0",
        "code": "39471614"
    },
    {
        "version": "9.4.0",
        "code": "39471620"
    },
    {
        "version": "9.4.0",
        "code": "39471625"
    },
    {
        "version": "9.4.0",
        "code": "39471633"
    },
    {
        "version": "9.4.0",
        "code": "39471643"
    },
    {
        "version": "9.4.5",
        "code": "39617613"
    },
    {
        "version": "9.4.5",
        "code": "40012791"
    },
    {
        "version": "9.4.5",
        "code": "40012799"
    },
    {
        "version": "9.4.5",
        "code": "40012805"
    },
    {
        "version": "9.4.5",
        "code": "40012815"
    },
    {
        "version": "9.4.5",
        "code": "40012823"
    },
    {
        "version": "9.5.0",
        "code": "40103626"
    },
    {
        "version": "9.4.5",
        "code": "40190548"
    },
    {
        "version": "9.4.5",
        "code": "40190549"
    },
    {
        "version": "9.4.5",
        "code": "40190551"
    },
    {
        "version": "9.4.5",
        "code": "40190552"
    },
    {
        "version": "9.4.5",
        "code": "40190553"
    },
    {
        "version": "9.5.0",
        "code": "40515338"
    },
    {
        "version": "9.5.0",
        "code": "40619016"
    },
    {
        "version": "9.5.5",
        "code": "40758520"
    },
    {
        "version": "9.5.0",
        "code": "40714450"
    },
    {
        "version": "9.5.0",
        "code": "40714452"
    },
    {
        "version": "9.5.0",
        "code": "40714453"
    },
    {
        "version": "9.5.0",
        "code": "40714455"
    },
    {
        "version": "9.5.0",
        "code": "40714457"
    },
    {
        "version": "9.5.5",
        "code": "40849471"
    },
    {
        "version": "9.5.5",
        "code": "41032480"
    },
    {
        "version": "9.5.5",
        "code": "41194573"
    },
    {
        "version": "9.5.5",
        "code": "41194580"
    },
    {
        "version": "9.5.5",
        "code": "41194594"
    },
    {
        "version": "9.5.5",
        "code": "41194600"
    },
    {
        "version": "9.5.5",
        "code": "41194607"
    },
    {
        "version": "9.6.0",
        "code": "41377320"
    },
    {
        "version": "9.6.0",
        "code": "41567516"
    },
    {
        "version": "9.6.0",
        "code": "41774323"
    },
    {
        "version": "9.6.0",
        "code": "41774332"
    },
    {
        "version": "9.6.0",
        "code": "41774345"
    },
    {
        "version": "9.6.0",
        "code": "41774362"
    },
    {
        "version": "9.6.0",
        "code": "41774376"
    },
    {
        "version": "9.6.5",
        "code": "41972110"
    },
    {
        "version": "9.6.6",
        "code": "42208365"
    },
    {
        "version": "9.6.6",
        "code": "42286962"
    },
    {
        "version": "9.6.6",
        "code": "42286970"
    },
    {
        "version": "9.6.6",
        "code": "42286974"
    },
    {
        "version": "9.6.6",
        "code": "42286977"
    },
    {
        "version": "9.6.6",
        "code": "42286981"
    },
    {
        "version": "9.7.0",
        "code": "42365116"
    },
    {
        "version": "9.7.0",
        "code": "42447991"
    },
    {
        "version": "9.6.7",
        "code": "42539520"
    },
    {
        "version": "9.6.7",
        "code": "42539538"
    },
    {
        "version": "9.6.7",
        "code": "42539549"
    },
    {
        "version": "9.6.7",
        "code": "42539553"
    },
    {
        "version": "9.6.7",
        "code": "42539561"
    },
    {
        "version": "9.7.0",
        "code": "42643097"
    },
    {
        "version": "9.7.0",
        "code": "42643116"
    },
    {
        "version": "9.7.5",
        "code": "42871859"
    },
    {
        "version": "9.7.0",
        "code": "42797737"
    },
    {
        "version": "9.7.0",
        "code": "42797741"
    },
    {
        "version": "9.7.0",
        "code": "42797743"
    },
    {
        "version": "9.7.0",
        "code": "42797747"
    },
    {
        "version": "9.7.0",
        "code": "42797748"
    },
    {
        "version": "9.7.5",
        "code": "43080327"
    },
    {
        "version": "9.7.5",
        "code": "43298789"
    },
    {
        "version": "9.7.5",
        "code": "43298790"
    },
    {
        "version": "9.7.5",
        "code": "43298791"
    },
    {
        "version": "9.7.5",
        "code": "43298793"
    },
    {
        "version": "9.7.5",
        "code": "43298795"
    },
    {
        "version": "9.8.0",
        "code": "43510707"
    },
    {
        "version": "9.8.0",
        "code": "43510715"
    },
    {
        "version": "9.8.0",
        "code": "43604896"
    },
    {
        "version": "9.8.0",
        "code": "43604907"
    },
    {
        "version": "9.8.0",
        "code": "43704314"
    },
    {
        "version": "9.8.0",
        "code": "43704318"
    },
    {
        "version": "9.8.0",
        "code": "43917443"
    },
    {
        "version": "9.8.0",
        "code": "43917444"
    },
    {
        "version": "9.8.0",
        "code": "43917446"
    },
    {
        "version": "9.8.0",
        "code": "43917447"
    },
    {
        "version": "9.8.0",
        "code": "43917449"
    },
    {
        "version": "9.8.5",
        "code": "44104157"
    },
    {
        "version": "9.8.5",
        "code": "44149188"
    },
    {
        "version": "9.8.5",
        "code": "44222990"
    },
    {
        "version": "9.8.5",
        "code": "44223008"
    },
    {
        "version": "10.0.0",
        "code": "44319907"
    },
    {
        "version": "10.0.0",
        "code": "44319910"
    },
    {
        "version": "10.0.0",
        "code": "44319911"
    },
    {
        "version": "10.0.0",
        "code": "44319915"
    },
    {
        "version": "10.0.0",
        "code": "44319920"
    },
    {
        "version": "10.0.1",
        "code": "44361668"
    },
    {
        "version": "10.0.1",
        "code": "44361672"
    },
    {
        "version": "10.0.1",
        "code": "44361676"
    },
    {
        "version": "10.0.1",
        "code": "44361680"
    },
    {
        "version": "10.0.1",
        "code": "44361682"
    },
    {
        "version": "10.1.0",
        "code": "44497026"
    },
    {
        "version": "10.1.0",
        "code": "44497027"
    },
    {
        "version": "10.1.0",
        "code": "44770801"
    },
    {
        "version": "10.1.0",
        "code": "44770804"
    },
    {
        "version": "10.1.0",
        "code": "44934675"
    },
    {
        "version": "10.1.0",
        "code": "44934691"
    },
    {
        "version": "10.1.0",
        "code": "45007214"
    },
    {
        "version": "10.1.0",
        "code": "45007216"
    },
    {
        "version": "10.1.0",
        "code": "45007217"
    },
    {
        "version": "10.1.0",
        "code": "45007218"
    },
    {
        "version": "10.1.0",
        "code": "45007220"
    },
    {
        "version": "10.2.0",
        "code": "45437335"
    },
    {
        "version": "10.2.0",
        "code": "45437336"
    },
    {
        "version": "10.2.0",
        "code": "45601630"
    },
    {
        "version": "10.2.0",
        "code": "45601632"
    },
    {
        "version": "10.2.0",
        "code": "45798832"
    },
    {
        "version": "10.2.0",
        "code": "45798835"
    },
    {
        "version": "10.2.0",
        "code": "45798836"
    },
    {
        "version": "10.2.0",
        "code": "45798839"
    },
    {
        "version": "10.2.1",
        "code": "45907261"
    },
    {
        "version": "10.2.1",
        "code": "45907267"
    },
    {
        "version": "10.2.1",
        "code": "45907273"
    },
    {
        "version": "10.2.1",
        "code": "45907284"
    },
    {
        "version": "10.2.1",
        "code": "45907288"
    },
    {
        "version": "10.3.0",
        "code": "45969864"
    },
    {
        "version": "10.3.0",
        "code": "45969869"
    },
    {
        "version": "10.3.0",
        "code": "46070702"
    },
    {
        "version": "10.3.0",
        "code": "46070704"
    },
    {
        "version": "10.3.0",
        "code": "46218777"
    },
    {
        "version": "10.3.0",
        "code": "46218778"
    },
    {
        "version": "10.3.0",
        "code": "46270752"
    },
    {
        "version": "10.3.0",
        "code": "46270753"
    },
    {
        "version": "10.3.0",
        "code": "46270754"
    },
    {
        "version": "10.3.0",
        "code": "46270755"
    },
    {
        "version": "10.3.0",
        "code": "46270756"
    },
    {
        "version": "10.3.0",
        "code": "46247777"
    },
    {
        "version": "10.3.0",
        "code": "46247778"
    },
    {
        "version": "10.3.1",
        "code": "46341238"
    },
    {
        "version": "10.3.1",
        "code": "46341239"
    },
    {
        "version": "10.3.1",
        "code": "46341240"
    },
    {
        "version": "10.3.1",
        "code": "46341241"
    },
    {
        "version": "10.3.1",
        "code": "46341242"
    },
    {
        "version": "10.3.2",
        "code": "46395470"
    },
    {
        "version": "10.3.2",
        "code": "46395471"
    },
    {
        "version": "10.3.2",
        "code": "46395472"
    },
    {
        "version": "10.3.2",
        "code": "46395473"
    },
    {
        "version": "10.3.2",
        "code": "46395474"
    },
    {
        "version": "10.4.0",
        "code": "47206831"
    },
    {
        "version": "10.4.0",
        "code": "47206840"
    },
    {
        "version": "10.4.0",
        "code": "47395669"
    },
    {
        "version": "10.4.0",
        "code": "47395670"
    },
    {
        "version": "10.4.0",
        "code": "47718693"
    },
    {
        "version": "10.4.0",
        "code": "47718694"
    },
    {
        "version": "10.4.0",
        "code": "47718695"
    },
    {
        "version": "10.4.0",
        "code": "47718697"
    },
    {
        "version": "10.4.0",
        "code": "47718698"
    },
    {
        "version": "10.5.0",
        "code": "47743792"
    },
    {
        "version": "10.5.0",
        "code": "47743794"
    },
    {
        "version": "10.5.0",
        "code": "47884297"
    },
    {
        "version": "10.5.0",
        "code": "47884298"
    },
    {
        "version": "10.5.0",
        "code": "47997334"
    },
    {
        "version": "10.5.0",
        "code": "47997341"
    },
    {
        "version": "10.5.0",
        "code": "48149419"
    },
    {
        "version": "10.5.0",
        "code": "48149423"
    },
    {
        "version": "10.5.0",
        "code": "48149427"
    },
    {
        "version": "10.6.0",
        "code": "48258064"
    },
    {
        "version": "10.6.0",
        "code": "48258070"
    },
    {
        "version": "10.5.1",
        "code": "48243304"
    },
    {
        "version": "10.5.1",
        "code": "48243312"
    },
    {
        "version": "10.5.1",
        "code": "48243317"
    },
    {
        "version": "10.5.1",
        "code": "48243321"
    },
    {
        "version": "10.5.1",
        "code": "48243323"
    },
    {
        "version": "10.7.0",
        "code": "48743563"
    },
    {
        "version": "10.7.0",
        "code": "48743568"
    },
    {
        "version": "10.6.0",
        "code": "48697431"
    },
    {
        "version": "10.6.0",
        "code": "48697435"
    },
    {
        "version": "10.6.0",
        "code": "48697436"
    },
    {
        "version": "10.6.0",
        "code": "48697439"
    },
    {
        "version": "10.6.0",
        "code": "48697441"
    },
    {
        "version": "10.7.0",
        "code": "48891032"
    },
    {
        "version": "10.7.0",
        "code": "48891034"
    },
    {
        "version": "10.7.0",
        "code": "49080654"
    },
    {
        "version": "10.7.0",
        "code": "49080656"
    },
    {
        "version": "10.7.0",
        "code": "49254538"
    },
    {
        "version": "10.7.0",
        "code": "49254549"
    },
    {
        "version": "10.7.0",
        "code": "49254554"
    },
    {
        "version": "10.7.0",
        "code": "49254558"
    },
    {
        "version": "10.7.0",
        "code": "49400166"
    },
    {
        "version": "10.7.0",
        "code": "49400167"
    },
    {
        "version": "10.7.0",
        "code": "49400168"
    },
    {
        "version": "10.7.0",
        "code": "49400170"
    },
    {
        "version": "10.7.0",
        "code": "49400171"
    },
    {
        "version": "10.8.0",
        "code": "49403860"
    },
    {
        "version": "10.8.0",
        "code": "49403864"
    },
    {
        "version": "10.8.0",
        "code": "49510731"
    },
    {
        "version": "10.8.0",
        "code": "49510733"
    },
    {
        "version": "10.8.0",
        "code": "49708876"
    },
    {
        "version": "10.8.0",
        "code": "49708877"
    },
    {
        "version": "10.8.0",
        "code": "49833220"
    },
    {
        "version": "10.8.0",
        "code": "49833230"
    },
    {
        "version": "10.9.0",
        "code": "50021166"
    },
    {
        "version": "10.9.0",
        "code": "50021174"
    },
    {
        "version": "10.9.0",
        "code": "50141465"
    },
    {
        "version": "10.9.0",
        "code": "50141466"
    },
    {
        "version": "10.9.0",
        "code": "50297872"
    },
    {
        "version": "10.9.0",
        "code": "50297873"
    },
    {
        "version": "10.9.0",
        "code": "50452424"
    },
    {
        "version": "10.9.0",
        "code": "50452425"
    },
    {
        "version": "10.9.0",
        "code": "50452427"
    },
    {
        "version": "10.9.0",
        "code": "50452428"
    },
    {
        "version": "10.9.0",
        "code": "50452429"
    },
    {
        "version": "10.10.0",
        "code": "50548149"
    },
    {
        "version": "10.10.0",
        "code": "50548168"
    },
    {
        "version": "10.10.0",
        "code": "50790484"
    },
    {
        "version": "10.10.0",
        "code": "50790487"
    },
    {
        "version": "10.10.0",
        "code": "50984356"
    },
    {
        "version": "10.10.0",
        "code": "50984359"
    },
    {
        "version": "10.10.0",
        "code": "50984364"
    },
    {
        "version": "10.10.0",
        "code": "50984366"
    },
    {
        "version": "10.10.0",
        "code": "50984369"
    },
    {
        "version": "10.11.0",
        "code": "51083247"
    },
    {
        "version": "10.11.0",
        "code": "51083248"
    },
    {
        "version": "10.11.0",
        "code": "51205381"
    },
    {
        "version": "10.11.0",
        "code": "51205384"
    },
    {
        "version": "10.11.0",
        "code": "51519100"
    },
    {
        "version": "10.11.0",
        "code": "51519101"
    },
    {
        "version": "10.11.0",
        "code": "51631979"
    },
    {
        "version": "10.11.0",
        "code": "51631980"
    },
    {
        "version": "10.11.0",
        "code": "51631981"
    },
    {
        "version": "10.11.0",
        "code": "51631982"
    },
    {
        "version": "10.11.0",
        "code": "51631983"
    },
    {
        "version": "10.12.0",
        "code": "51780259"
    },
    {
        "version": "10.12.0",
        "code": "51780265"
    },
    {
        "version": "10.12.0",
        "code": "52328590"
    },
    {
        "version": "10.12.0",
        "code": "52328593"
    },
    {
        "version": "10.12.0",
        "code": "52418251"
    },
    {
        "version": "10.12.0",
        "code": "52418252"
    },
    {
        "version": "10.12.0",
        "code": "52418253"
    },
    {
        "version": "10.12.0",
        "code": "52418254"
    },
    {
        "version": "10.12.0",
        "code": "52418256"
    },
    {
        "version": "10.13.0",
        "code": "52629400"
    },
    {
        "version": "10.13.0",
        "code": "52629403"
    },
    {
        "version": "10.13.0",
        "code": "52858524"
    },
    {
        "version": "10.13.0",
        "code": "52858527"
    },
    {
        "version": "10.13.0",
        "code": "53070968"
    },
    {
        "version": "10.13.0",
        "code": "53070969"
    },
    {
        "version": "10.13.0",
        "code": "53070973"
    },
    {
        "version": "10.13.0",
        "code": "53070974"
    },
    {
        "version": "10.13.0",
        "code": "53070975"
    },
    {
        "version": "10.14.0",
        "code": "53199629"
    },
    {
        "version": "10.14.0",
        "code": "53199630"
    },
    {
        "version": "10.14.0",
        "code": "53676094"
    },
    {
        "version": "10.14.0",
        "code": "53676095"
    },
    {
        "version": "10.14.0",
        "code": "53734041"
    },
    {
        "version": "10.14.0",
        "code": "53734042"
    },
    {
        "version": "10.14.0",
        "code": "53734043"
    },
    {
        "version": "10.14.0",
        "code": "53734044"
    },
    {
        "version": "10.14.0",
        "code": "53734045"
    },
    {
        "version": "10.15.0",
        "code": "53863829"
    },
    {
        "version": "10.15.0",
        "code": "53863830"
    },
    {
        "version": "10.15.0",
        "code": "53997300"
    },
    {
        "version": "10.15.0",
        "code": "53997343"
    },
    {
        "version": "10.15.0",
        "code": "54119071"
    },
    {
        "version": "10.15.0",
        "code": "54119096"
    },
    {
        "version": "10.15.0",
        "code": "54375389"
    },
    {
        "version": "10.15.0",
        "code": "54375392"
    },
    {
        "version": "10.15.0",
        "code": "54375395"
    },
    {
        "version": "10.15.0",
        "code": "54375396"
    },
    {
        "version": "10.15.0",
        "code": "54375399"
    },
    {
        "version": "10.16.0",
        "code": "54495181"
    },
    {
        "version": "10.16.0",
        "code": "54495185"
    },
    {
        "version": "10.16.0",
        "code": "54682050"
    },
    {
        "version": "10.16.0",
        "code": "54682051"
    },
    {
        "version": "10.16.0",
        "code": "54942119"
    },
    {
        "version": "10.16.0",
        "code": "54942122"
    },
    {
        "version": "10.16.0",
        "code": "54942124"
    },
    {
        "version": "10.16.0",
        "code": "54942127"
    },
    {
        "version": "10.16.0",
        "code": "54942129"
    },
    {
        "version": "10.17.0",
        "code": "55090834"
    },
    {
        "version": "10.17.0",
        "code": "55090838"
    },
    {
        "version": "10.16.1",
        "code": "55125670"
    },
    {
        "version": "10.16.1",
        "code": "55125673"
    },
    {
        "version": "10.16.1",
        "code": "55125674"
    },
    {
        "version": "10.16.1",
        "code": "55125676"
    },
    {
        "version": "10.16.1",
        "code": "55125678"
    },
    {
        "version": "10.17.0",
        "code": "55285007"
    },
    {
        "version": "10.17.0",
        "code": "55285008"
    },
    {
        "version": "10.18.0",
        "code": "55548043"
    },
    {
        "version": "10.18.0",
        "code": "55548048"
    },
    {
        "version": "10.18.0",
        "code": "55692557"
    },
    {
        "version": "10.18.0",
        "code": "55692558"
    },
    {
        "version": "10.17.0",
        "code": "55521848"
    },
    {
        "version": "10.17.0",
        "code": "55521855"
    },
    {
        "version": "10.17.0",
        "code": "55521859"
    },
    {
        "version": "10.17.0",
        "code": "55521864"
    },
    {
        "version": "10.17.0",
        "code": "55521867"
    },
    {
        "version": "10.18.0",
        "code": "55835624"
    },
    {
        "version": "10.18.0",
        "code": "55835627"
    },
    {
        "version": "10.18.0",
        "code": "56145866"
    },
    {
        "version": "10.18.0",
        "code": "56145872"
    },
    {
        "version": "10.18.0",
        "code": "56145876"
    },
    {
        "version": "10.18.0",
        "code": "56145882"
    },
    {
        "version": "10.18.0",
        "code": "56145885"
    },
    {
        "version": "10.19.0",
        "code": "56213387"
    },
    {
        "version": "10.19.0",
        "code": "56213388"
    },
    {
        "version": "10.19.0",
        "code": "56443993"
    },
    {
        "version": "10.19.0",
        "code": "56443995"
    },
    {
        "version": "10.20.0",
        "code": "56912606"
    },
    {
        "version": "10.20.0",
        "code": "56912623"
    },
    {
        "version": "10.19.0",
        "code": "56878869"
    },
    {
        "version": "10.19.0",
        "code": "56878870"
    },
    {
        "version": "10.19.0",
        "code": "56878872"
    },
    {
        "version": "10.19.0",
        "code": "56878873"
    },
    {
        "version": "10.19.0",
        "code": "56878874"
    },
    {
        "version": "10.20.0",
        "code": "57156154"
    },
    {
        "version": "10.19.1",
        "code": "57202585"
    },
    {
        "version": "10.19.1",
        "code": "57202587"
    },
    {
        "version": "10.19.1",
        "code": "57202589"
    },
    {
        "version": "10.19.1",
        "code": "57202593"
    },
    {
        "version": "10.19.1",
        "code": "57202594"
    },
    {
        "version": "10.20.0",
        "code": "57282578"
    },
    {
        "version": "10.20.0",
        "code": "57635236"
    },
    {
        "version": "10.20.0",
        "code": "57635237"
    },
    {
        "version": "10.20.0",
        "code": "57635239"
    },
    {
        "version": "10.20.0",
        "code": "57635240"
    },
    {
        "version": "10.20.0",
        "code": "57635242"
    },
    {
        "version": "10.21.0",
        "code": "57657864"
    },
    {
        "version": "10.21.0",
        "code": "57657867"
    },
    {
        "version": "10.21.0",
        "code": "57734943"
    },
    {
        "version": "10.21.0",
        "code": "57734949"
    },
    {
        "version": "10.21.0",
        "code": "57869439"
    },
    {
        "version": "10.20.0",
        "code": "57944455"
    },
    {
        "version": "10.20.0",
        "code": "57944458"
    },
    {
        "version": "10.20.0",
        "code": "57944460"
    },
    {
        "version": "10.20.0",
        "code": "57944461"
    },
    {
        "version": "10.20.0",
        "code": "57944462"
    },
    {
        "version": "10.21.0",
        "code": "58100880"
    },
    {
        "version": "10.21.0",
        "code": "58213091"
    },
    {
        "version": "10.21.0",
        "code": "58256051"
    },
    {
        "version": "10.21.0",
        "code": "58302827"
    },
    {
        "version": "10.21.0",
        "code": "58302830"
    },
    {
        "version": "10.21.0",
        "code": "58302835"
    },
    {
        "version": "10.21.0",
        "code": "58302845"
    },
    {
        "version": "10.21.0",
        "code": "58302850"
    },
    {
        "version": "10.22.0",
        "code": "58304237"
    },
    {
        "version": "10.22.0",
        "code": "58357921"
    },
    {
        "version": "10.22.0",
        "code": "58532222"
    },
    {
        "version": "10.22.0",
        "code": "58532223"
    },
    {
        "version": "10.22.0",
        "code": "58775268"
    },
    {
        "version": "10.23.0",
        "code": "58962121"
    },
    {
        "version": "10.23.0",
        "code": "58962122"
    },
    {
        "version": "10.22.0",
        "code": "58956666"
    },
    {
        "version": "10.22.0",
        "code": "58956671"
    },
    {
        "version": "10.22.0",
        "code": "58956676"
    },
    {
        "version": "10.22.0",
        "code": "58956681"
    },
    {
        "version": "10.22.0",
        "code": "58956686"
    },
    {
        "version": "10.23.0",
        "code": "59181096"
    },
    {
        "version": "10.23.0",
        "code": "59181101"
    },
    {
        "version": "10.23.0",
        "code": "59451976"
    },
    {
        "version": "10.23.0",
        "code": "59451977"
    },
    {
        "version": "10.23.0",
        "code": "59820928"
    },
    {
        "version": "10.23.0",
        "code": "59820929"
    },
    {
        "version": "10.23.0",
        "code": "59820930"
    },
    {
        "version": "10.23.0",
        "code": "59820931"
    },
    {
        "version": "10.23.0",
        "code": "59820932"
    },
    {
        "version": "10.24.0",
        "code": "59839734"
    },
    {
        "version": "10.24.0",
        "code": "59839740"
    },
    {
        "version": "10.24.0",
        "code": "60173967"
    },
    {
        "version": "10.24.0",
        "code": "60173968"
    },
    {
        "version": "10.24.0",
        "code": "60335755"
    },
    {
        "version": "10.24.0",
        "code": "60335756"
    },
    {
        "version": "10.24.0",
        "code": "60335757"
    },
    {
        "version": "10.24.0",
        "code": "60335759"
    },
    {
        "version": "10.24.0",
        "code": "60335760"
    },
    {
        "version": "10.25.0",
        "code": "60531488"
    },
    {
        "version": "10.25.0",
        "code": "60531492"
    },
    {
        "version": "10.25.0",
        "code": "60813718"
    },
    {
        "version": "10.25.0",
        "code": "60813721"
    },
    {
        "version": "10.25.0",
        "code": "61294052"
    },
    {
        "version": "10.25.0",
        "code": "61294066"
    },
    {
        "version": "10.25.0",
        "code": "61294071"
    },
    {
        "version": "10.25.0",
        "code": "61294077"
    },
    {
        "version": "10.25.1",
        "code": "61475277"
    },
    {
        "version": "10.25.1",
        "code": "61475280"
    },
    {
        "version": "10.25.1",
        "code": "61475288"
    },
    {
        "version": "10.25.1",
        "code": "61475291"
    },
    {
        "version": "10.25.1",
        "code": "61475296"
    },
    {
        "version": "10.26.0",
        "code": "61586286"
    },
    {
        "version": "10.26.0",
        "code": "61586287"
    },
    {
        "version": "10.26.0",
        "code": "61947337"
    },
    {
        "version": "10.26.0",
        "code": "61947338"
    },
    {
        "version": "10.26.0",
        "code": "62257637"
    },
    {
        "version": "10.26.0",
        "code": "62257640"
    },
    {
        "version": "10.26.0",
        "code": "62257644"
    },
    {
        "version": "10.26.0",
        "code": "62257646"
    },
    {
        "version": "10.26.0",
        "code": "62257650"
    },
    {
        "version": "10.27.0",
        "code": "62259341"
    },
    {
        "version": "10.27.0",
        "code": "62259359"
    },
    {
        "version": "10.27.0",
        "code": "62642849"
    },
    {
        "version": "10.27.0",
        "code": "62642853"
    },
    {
        "version": "10.27.0",
        "code": "63111915"
    },
    {
        "version": "10.27.0",
        "code": "63111925"
    },
    {
        "version": "10.27.0",
        "code": "63251605"
    },
    {
        "version": "10.27.0",
        "code": "63251606"
    },
    {
        "version": "10.27.0",
        "code": "63251608"
    },
    {
        "version": "10.27.0",
        "code": "63251609"
    },
    {
        "version": "10.28.0",
        "code": "63419392"
    },
    {
        "version": "10.28.0",
        "code": "63419393"
    },
    {
        "version": "10.27.1",
        "code": "63323422"
    },
    {
        "version": "10.27.1",
        "code": "63323428"
    },
    {
        "version": "10.27.1",
        "code": "63323436"
    },
    {
        "version": "10.27.1",
        "code": "63323440"
    },
    {
        "version": "10.27.1",
        "code": "63323444"
    },
    {
        "version": "10.28.0",
        "code": "63594885"
    },
    {
        "version": "10.28.0",
        "code": "63594893"
    },
    {
        "version": "10.28.0",
        "code": "63904419"
    },
    {
        "version": "10.28.0",
        "code": "63904426"
    },
    {
        "version": "10.29.0",
        "code": "64175345"
    },
    {
        "version": "10.29.0",
        "code": "64175358"
    },
    {
        "version": "10.28.0",
        "code": "64172492"
    },
    {
        "version": "10.28.0",
        "code": "64172494"
    },
    {
        "version": "10.28.0",
        "code": "64172495"
    },
    {
        "version": "10.28.0",
        "code": "64172496"
    },
    {
        "version": "10.29.0",
        "code": "64311028"
    },
    {
        "version": "10.29.0",
        "code": "64311032"
    },
    {
        "version": "10.29.0",
        "code": "64549041"
    },
    {
        "version": "10.29.0",
        "code": "64549042"
    },
    {
        "version": "10.30.0",
        "code": "64667761"
    },
    {
        "version": "10.30.0",
        "code": "64667765"
    },
    {
        "version": "10.29.0",
        "code": "64630924"
    },
    {
        "version": "10.29.0",
        "code": "64630925"
    },
    {
        "version": "10.29.0",
        "code": "64630926"
    },
    {
        "version": "10.29.0",
        "code": "64630927"
    },
    {
        "version": "10.29.0",
        "code": "64630928"
    },
    {
        "version": "10.30.0",
        "code": "64866812"
    },
    {
        "version": "10.30.0",
        "code": "64866813"
    },
    {
        "version": "10.30.0",
        "code": "65118902"
    },
    {
        "version": "10.30.0",
        "code": "65118908"
    },
    {
        "version": "10.31.0",
        "code": "65305970"
    },
    {
        "version": "10.31.0",
        "code": "65305972"
    },
    {
        "version": "10.30.0",
        "code": "65303574"
    },
    {
        "version": "10.30.0",
        "code": "65303577"
    },
    {
        "version": "10.30.0",
        "code": "65303583"
    },
    {
        "version": "10.30.0",
        "code": "65303587"
    },
    {
        "version": "10.30.0",
        "code": "65303594"
    },
    {
        "version": "10.31.0",
        "code": "65633900"
    },
    {
        "version": "10.31.0",
        "code": "65633903"
    },
    {
        "version": "10.31.0",
        "code": "65804388"
    },
    {
        "version": "10.32.0",
        "code": "66029662"
    },
    {
        "version": "10.32.0",
        "code": "66029667"
    },
    {
        "version": "10.31.0",
        "code": "65992940"
    },
    {
        "version": "10.31.0",
        "code": "65992946"
    },
    {
        "version": "10.32.0",
        "code": "66264811"
    },
    {
        "version": "10.32.0",
        "code": "66264815"
    },
    {
        "version": "10.32.0",
        "code": "66468522"
    },
    {
        "version": "10.32.0",
        "code": "66468523"
    },
    {
        "version": "10.32.0",
        "code": "66699482"
    },
    {
        "version": "10.32.0",
        "code": "66699486"
    },
    {
        "version": "10.32.0",
        "code": "66699490"
    },
    {
        "version": "10.32.0",
        "code": "66699494"
    },
    {
        "version": "10.32.0",
        "code": "66699497"
    },
    {
        "version": "10.33.0",
        "code": "66749790"
    },
    {
        "version": "10.33.0",
        "code": "66749792"
    },
    {
        "version": "10.33.0",
        "code": "66983342"
    },
    {
        "version": "10.33.0",
        "code": "66983344"
    },
    {
        "version": "10.33.0",
        "code": "67304244"
    },
    {
        "version": "10.33.0",
        "code": "67410771"
    },
    {
        "version": "10.33.0",
        "code": "67410777"
    },
    {
        "version": "10.34.0",
        "code": "67463976"
    },
    {
        "version": "10.34.0",
        "code": "67463983"
    },
    {
        "version": "10.34.0",
        "code": "67697991"
    },
    {
        "version": "10.34.0",
        "code": "67697992"
    },
    {
        "version": "10.34.0",
        "code": "67963312"
    },
    {
        "version": "10.34.0",
        "code": "68173476"
    },
    {
        "version": "10.34.0",
        "code": "68173479"
    },
    {
        "version": "10.34.0",
        "code": "68173485"
    },
    {
        "version": "10.34.0",
        "code": "68173486"
    },
    {
        "version": "11.0.0.1.20",
        "code": "68204375"
    },
    {
        "version": "11.0.0.1.20",
        "code": "68204377"
    },
    {
        "version": "11.0.0.3.20",
        "code": "68521637"
    },
    {
        "version": "11.0.0.11.20",
        "code": "68850559"
    },
    {
        "version": "11.0.0.11.20",
        "code": "68850571"
    },
    {
        "version": "12.0.0.2.91",
        "code": "69259749"
    },
    {
        "version": "12.0.0.2.91",
        "code": "69259751"
    },
    {
        "version": "12.0.0.4.91",
        "code": "69460266"
    },
    {
        "version": "12.0.0.4.91",
        "code": "69460272"
    },
    {
        "version": "11.0.0.12.20",
        "code": "69139027"
    },
    {
        "version": "11.0.0.12.20",
        "code": "69139039"
    },
    {
        "version": "12.0.0.5.91",
        "code": "69724093"
    },
    {
        "version": "12.0.0.5.91",
        "code": "69724098"
    },
    {
        "version": "13.0.0.1.91",
        "code": "69989691"
    },
    {
        "version": "12.0.0.7.91",
        "code": "69950856"
    },
    {
        "version": "12.0.0.7.91",
        "code": "69950857"
    },
    {
        "version": "12.0.0.7.91",
        "code": "69950860"
    },
    {
        "version": "12.0.0.7.91",
        "code": "69950867"
    },
    {
        "version": "12.0.0.7.91",
        "code": "69950874"
    },
    {
        "version": "13.0.0.4.91",
        "code": "70301197"
    },
    {
        "version": "13.0.0.4.91",
        "code": "70301206"
    },
    {
        "version": "13.0.0.6.91",
        "code": "70565432"
    },
    {
        "version": "13.0.0.6.91",
        "code": "70565437"
    },
    {
        "version": "14.0.0.1.91",
        "code": "70866341"
    },
    {
        "version": "14.0.0.1.91",
        "code": "70866342"
    },
    {
        "version": "14.0.0.4.91",
        "code": "71023044"
    },
    {
        "version": "14.0.0.4.91",
        "code": "71023055"
    },
    {
        "version": "13.0.0.7.91",
        "code": "70864846"
    },
    {
        "version": "13.0.0.7.91",
        "code": "70864847"
    },
    {
        "version": "13.0.0.7.91",
        "code": "70864849"
    },
    {
        "version": "14.0.0.7.91",
        "code": "71313408"
    },
    {
        "version": "14.0.0.7.91",
        "code": "71313420"
    },
    {
        "version": "14.0.0.10.91",
        "code": "71607485"
    },
    {
        "version": "15.0.0.2.90",
        "code": "71609170"
    },
    {
        "version": "15.0.0.2.90",
        "code": "71609177"
    },
    {
        "version": "15.0.0.5.90",
        "code": "71869745"
    },
    {
        "version": "15.0.0.9.90",
        "code": "72058304"
    },
    {
        "version": "15.0.0.9.90",
        "code": "72058307"
    },
    {
        "version": "15.0.0.11.90",
        "code": "72211476"
    },
    {
        "version": "15.0.0.11.90",
        "code": "72211477"
    },
    {
        "version": "15.0.0.11.90",
        "code": "72211479"
    },
    {
        "version": "15.0.0.11.90",
        "code": "72211480"
    },
    {
        "version": "15.0.0.11.90",
        "code": "72211482"
    },
    {
        "version": "16.0.0.1.90",
        "code": "72230930"
    },
    {
        "version": "16.0.0.1.90",
        "code": "72230933"
    },
    {
        "version": "16.0.0.5.90",
        "code": "72555085"
    },
    {
        "version": "16.0.0.5.90",
        "code": "72555089"
    },
    {
        "version": "16.0.0.11.90",
        "code": "72975638"
    },
    {
        "version": "16.0.0.11.90",
        "code": "72975639"
    },
    {
        "version": "17.0.0.2.91",
        "code": "73135859"
    },
    {
        "version": "17.0.0.2.91",
        "code": "73135860"
    },
    {
        "version": "16.0.0.13.90",
        "code": "73134433"
    },
    {
        "version": "17.0.0.5.91",
        "code": "73424839"
    },
    {
        "version": "17.0.0.5.91",
        "code": "73424841"
    },
    {
        "version": "17.0.0.14.91",
        "code": "73754320"
    },
    {
        "version": "18.0.0.1.85",
        "code": "74019914"
    },
    {
        "version": "18.0.0.1.85",
        "code": "74019915"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998917"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998918"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998923"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998925"
    },
    {
        "version": "18.0.0.8.85",
        "code": "74316861"
    },
    {
        "version": "18.0.0.8.85",
        "code": "74316868"
    },
    {
        "version": "18.0.0.14.85",
        "code": "74588139"
    },
    {
        "version": "18.0.0.14.85",
        "code": "74588140"
    },
    {
        "version": "18.0.0.16.85",
        "code": "74766563"
    },
    {
        "version": "19.0.0.2.91",
        "code": "74850287"
    },
    {
        "version": "19.0.0.2.91",
        "code": "74850294"
    },
    {
        "version": "18.0.0.18.85",
        "code": "74848591"
    },
    {
        "version": "18.0.0.18.85",
        "code": "74848595"
    },
    {
        "version": "19.0.0.6.91",
        "code": "75154623"
    },
    {
        "version": "19.0.0.6.91",
        "code": "75154632"
    },
    {
        "version": "19.0.0.12.91",
        "code": "75440931"
    },
    {
        "version": "19.0.0.29.91",
        "code": "75739465"
    },
    {
        "version": "19.1.0.31.91",
        "code": "75767742"
    },
    {
        "version": "19.1.0.31.91",
        "code": "75767744"
    },
    {
        "version": "20.0.0.10.75",
        "code": "75875218"
    },
    {
        "version": "20.0.0.10.75",
        "code": "75875222"
    },
    {
        "version": "20.0.0.19.75",
        "code": "76055392"
    },
    {
        "version": "20.0.0.19.75",
        "code": "76055394"
    },
    {
        "version": "20.0.0.29.75",
        "code": "76440357"
    },
    {
        "version": "20.0.0.29.75",
        "code": "76440359"
    },
    {
        "version": "20.0.0.29.75",
        "code": "76734047"
    },
    {
        "version": "20.0.0.29.75",
        "code": "76734048"
    },
    {
        "version": "21.0.0.1.62",
        "code": "76769970"
    },
    {
        "version": "21.0.0.1.62",
        "code": "76769971"
    },
    {
        "version": "21.0.0.3.62",
        "code": "77131847"
    },
    {
        "version": "21.0.0.3.62",
        "code": "77131854"
    },
    {
        "version": "21.0.0.8.62",
        "code": "77472097"
    },
    {
        "version": "21.0.0.11.62",
        "code": "77790084"
    },
    {
        "version": "21.0.0.11.62",
        "code": "77790086"
    },
    {
        "version": "21.0.0.11.62",
        "code": "77790087"
    },
    {
        "version": "22.0.0.3.68",
        "code": "77973636"
    },
    {
        "version": "22.0.0.3.68",
        "code": "77973642"
    },
    {
        "version": "22.0.0.8.68",
        "code": "78246422"
    },
    {
        "version": "22.0.0.8.68",
        "code": "78246423"
    },
    {
        "version": "22.0.0.15.68",
        "code": "78610143"
    },
    {
        "version": "22.0.0.15.68",
        "code": "78610144"
    },
    {
        "version": "23.0.0.2.135",
        "code": "78983804"
    },
    {
        "version": "23.0.0.2.135",
        "code": "78983806"
    },
    {
        "version": "22.0.0.17.68",
        "code": "78982742"
    },
    {
        "version": "23.0.0.6.135",
        "code": "79369968"
    },
    {
        "version": "23.0.0.6.135",
        "code": "79369974"
    },
    {
        "version": "23.0.0.12.135",
        "code": "79757769"
    },
    {
        "version": "24.0.0.2.201",
        "code": "80132351"
    },
    {
        "version": "24.0.0.8.201",
        "code": "80489717"
    },
    {
        "version": "24.0.0.11.201",
        "code": "80851216"
    },
    {
        "version": "24.0.0.12.201",
        "code": "81140472"
    },
    {
        "version": "24.0.0.12.201",
        "code": "81140473"
    },
    {
        "version": "24.0.0.12.201",
        "code": "81140474"
    },
    {
        "version": "25.0.0.1.136",
        "code": "81947967"
    },
    {
        "version": "23.0.0.14.135",
        "code": "80125192"
    },
    {
        "version": "23.0.0.14.135",
        "code": "80125193"
    },
    {
        "version": "23.0.0.14.135",
        "code": "80125195"
    },
    {
        "version": "25.0.0.11.136",
        "code": "82293528"
    },
    {
        "version": "25.0.0.20.136",
        "code": "82660880"
    },
    {
        "version": "25.0.0.26.136",
        "code": "83072241"
    },
    {
        "version": "26.0.0.1.86",
        "code": "83085573"
    },
    {
        "version": "26.0.0.5.86",
        "code": "83486950"
    },
    {
        "version": "26.0.0.10.86",
        "code": "83827592"
    },
    {
        "version": "27.0.0.2.97",
        "code": "84125290"
    },
    {
        "version": "26.0.0.13.86",
        "code": "84116174"
    },
    {
        "version": "26.0.0.13.86",
        "code": "84116177"
    },
    {
        "version": "27.0.0.7.97",
        "code": "84433655"
    },
    {
        "version": "27.0.0.9.97",
        "code": "84725370"
    },
    {
        "version": "27.0.0.11.97",
        "code": "84946932"
    },
    {
        "version": "28.0.0.2.284",
        "code": "86924497"
    },
    {
        "version": "28.0.0.2.284",
        "code": "86924501"
    },
    {
        "version": "28.0.0.6.284",
        "code": "87350500"
    },
    {
        "version": "28.0.0.7.284",
        "code": "87568511"
    },
    {
        "version": "28.0.0.7.284",
        "code": "87949185"
    },
    {
        "version": "28.0.0.7.284",
        "code": "87949189"
    },
    {
        "version": "29.0.0.1.95",
        "code": "87956739"
    },
    {
        "version": "29.0.0.3.95",
        "code": "88139205"
    },
    {
        "version": "29.0.0.7.95",
        "code": "88511992"
    },
    {
        "version": "29.0.0.13.95",
        "code": "88934931"
    },
    {
        "version": "30.0.0.1.95",
        "code": "88948234"
    },
    {
        "version": "30.0.0.5.95",
        "code": "89272429"
    },
    {
        "version": "30.0.0.10.95",
        "code": "89553885"
    },
    {
        "version": "31.0.0.1.94",
        "code": "89872911"
    },
    {
        "version": "30.0.0.12.95",
        "code": "89867442"
    },
    {
        "version": "30.0.0.12.95",
        "code": "89867443"
    },
    {
        "version": "31.0.0.4.94",
        "code": "90206733"
    },
    {
        "version": "31.0.0.9.94",
        "code": "90539500"
    },
    {
        "version": "31.0.0.10.94",
        "code": "90841959"
    },
    {
        "version": "31.0.0.10.94",
        "code": "90841964"
    },
    {
        "version": "32.0.0.1.94",
        "code": "90848911"
    },
    {
        "version": "32.0.0.7.94",
        "code": "91196699"
    },
    {
        "version": "32.0.0.14.94",
        "code": "91537601"
    },
    {
        "version": "32.0.0.16.94",
        "code": "91882539"
    },
    {
        "version": "33.0.0.1.92",
        "code": "91910106"
    },
    {
        "version": "33.0.0.5.92",
        "code": "92383910"
    },
    {
        "version": "33.0.0.8.92",
        "code": "92605898"
    },
    {
        "version": "33.0.0.11.92",
        "code": "93117667"
    },
    {
        "version": "33.0.0.11.92",
        "code": "93117670"
    },
    {
        "version": "34.0.0.3.93",
        "code": "93134846"
    },
    {
        "version": "34.0.0.4.93",
        "code": "93321235"
    },
    {
        "version": "34.0.0.10.93",
        "code": "93684092"
    },
    {
        "version": "34.0.0.12.93",
        "code": "94080606"
    },
    {
        "version": "34.0.0.12.93",
        "code": "94080607"
    },
    {
        "version": "35.0.0.3.96",
        "code": "94112298"
    },
    {
        "version": "35.0.0.7.96",
        "code": "94500659"
    },
    {
        "version": "35.0.0.14.96",
        "code": "94961862"
    },
    {
        "version": "35.0.0.20.96",
        "code": "95414345"
    },
    {
        "version": "35.0.0.20.96",
        "code": "95414346"
    },
    {
        "version": "35.0.0.20.96",
        "code": "95414347"
    },
    {
        "version": "36.0.0.3.91",
        "code": "95434759"
    },
    {
        "version": "36.0.0.7.91",
        "code": "95829521"
    },
    {
        "version": "36.0.0.13.91",
        "code": "96258630"
    },
    {
        "version": "36.0.0.13.91",
        "code": "96794591"
    },
    {
        "version": "36.0.0.13.91",
        "code": "96794592"
    },
    {
        "version": "37.0.0.5.97",
        "code": "96940945"
    },
    {
        "version": "37.0.0.9.97",
        "code": "97235966"
    },
    {
        "version": "37.0.0.15.97",
        "code": "97757337"
    },
    {
        "version": "37.0.0.21.97",
        "code": "98288239"
    },
    {
        "version": "37.0.0.21.97",
        "code": "98288242"
    },
    {
        "version": "38.0.0.3.95",
        "code": "98301249"
    },
    {
        "version": "38.0.0.7.95",
        "code": "98766551"
    },
    {
        "version": "38.0.0.12.95",
        "code": "99353302"
    },
    {
        "version": "38.0.0.13.95",
        "code": "99640905"
    },
    {
        "version": "38.0.0.13.95",
        "code": "99640911"
    },
    {
        "version": "39.0.0.4.93",
        "code": "99668514"
    },
    {
        "version": "39.0.0.12.93",
        "code": "100120602"
    },
    {
        "version": "39.0.0.16.93",
        "code": "100521966"
    },
    {
        "version": "40.0.0.3.95",
        "code": "101012706"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986890"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986893"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986894"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986896"
    },
    {
        "version": "40.0.0.7.95",
        "code": "101435484"
    },
    {
        "version": "40.0.0.12.95",
        "code": "101784049"
    },
    {
        "version": "41.0.0.10.92",
        "code": "102994842"
    },
    {
        "version": "42.0.0.2.95",
        "code": "103543967"
    },
    {
        "version": "42.0.0.17.95",
        "code": "104284665"
    },
    {
        "version": "42.0.0.19.95",
        "code": "104766886"
    },
    {
        "version": "42.0.0.19.95",
        "code": "104766893"
    },
    {
        "version": "42.0.0.19.95",
        "code": "104766900"
    },
    {
        "version": "42.0.0.19.95",
        "code": "104766912"
    },
    {
        "version": "43.0.0.9.97",
        "code": "105430182"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842048"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842051"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842053"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842058"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092308"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092318"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092322"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092339"
    },
    {
        "version": "45.0.0.17.93",
        "code": "108357720"
    },
    {
        "version": "45.0.0.17.93",
        "code": "108357722"
    },
    {
        "version": "46.0.0.15.96",
        "code": "109556223"
    },
    {
        "version": "46.0.0.15.96",
        "code": "109556226"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937437"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937441"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937448"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937453"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937463"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021127"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021130"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021131"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021134"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249548"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249561"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249569"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249580"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622421"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622426"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622429"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622435"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746524"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746525"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746527"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746528"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746533"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211351"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211358"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211364"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211374"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994873"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994876"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994877"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994879"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756940"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756947"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756948"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756953"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539695"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539687"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539698"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539703"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539706"
    },
    {
        "version": "55.0.0.12.79",
        "code": "118342006"
    },
    {
        "version": "55.0.0.12.79",
        "code": "118342010"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104795"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104798"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104802"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104804"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875220"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875222"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875225"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875229"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875235"
    },
    {
        "version": "58.0.0.12.73",
        "code": "120662547"
    },
    {
        "version": "58.0.0.12.73",
        "code": "120662550"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451786"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451799"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451810"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451814"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206595"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206601"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206608"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206624"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206636"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338241"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338243"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338247"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338251"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338255"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103719"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103729"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103748"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103756"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790714"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790715"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790716"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790722"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790725"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124583932"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124583960"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124584015"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124584019"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398466"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398467"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398468"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398471"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398474"
    },
    {
        "version": "65.0.0.12.86",
        "code": "126223508"
    },
    {
        "version": "65.0.0.12.86",
        "code": "126223536"
    },
    {
        "version": "65.0.0.12.86",
        "code": "126223544"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127048992"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127049016"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127049038"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127049053"
    },
    {
        "version": "67.0.0.24.100",
        "code": "128028364"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079974"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079975"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079976"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079984"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079991"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676139"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676143"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676146"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676156"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676160"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611414"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611415"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611416"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611419"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611421"
    },
    {
        "version": "70.0.0.21.98",
        "code": "130528344"
    },
    {
        "version": "70.0.0.21.98",
        "code": "130528499"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580482"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580484"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580485"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580488"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580490"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223236"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223237"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223239"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223240"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223243"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223245"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081622"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081640"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081644"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081648"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081649"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081655"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633067"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633068"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633072"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633074"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666554"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666556"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666564"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666566"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374885"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374887"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374890"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374896"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374904"
    },
    {
        "version": "76.0.0.15.395",
        "code": "138226743"
    },
    {
        "version": "76.0.0.15.395",
        "code": "138226752"
    },
    {
        "version": "76.0.0.15.395",
        "code": "138226758"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237606"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237622"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237645"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237670"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237687"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906542"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906547"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906556"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906564"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906580"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906597"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973934"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973935"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973940"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973941"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973942"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753087"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753091"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753097"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753099"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841905"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841908"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841909"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841911"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841917"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841921"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841922"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631572"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631574"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631575"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631576"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612578"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612596"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612598"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612600"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652085"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652086"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652094"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652096"
    },
    {
        "version": "85.0.0.21.100",
        "code": "146536611"
    },
    {
        "version": "85.0.0.21.100",
        "code": "146536612"
    },
    {
        "version": "85.0.0.21.100",
        "code": "146536619"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985641"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985644"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985665"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985667"
    },
    {
        "version": "86.0.0.24.87",
        "code": "147375127"
    },
    {
        "version": "86.0.0.24.87",
        "code": "147375143"
    },
    {
        "version": "87.0.0.18.99",
        "code": "148324036"
    },
    {
        "version": "87.0.0.18.99",
        "code": "148324039"
    },
    {
        "version": "87.0.0.18.99",
        "code": "148324051"
    },
    {
        "version": "88.0.0.14.99",
        "code": "149350048"
    },
    {
        "version": "88.0.0.14.99",
        "code": "149350061"
    },
    {
        "version": "89.0.0.21.101",
        "code": "150338063"
    },
    {
        "version": "89.0.0.21.101",
        "code": "150338067"
    },
    {
        "version": "90.0.0.18.110",
        "code": "151414267"
    },
    {
        "version": "90.0.0.18.110",
        "code": "151414270"
    },
    {
        "version": "90.0.0.18.110",
        "code": "151414277"
    },
    {
        "version": "91.0.0.18.118",
        "code": "152367488"
    },
    {
        "version": "91.0.0.18.118",
        "code": "152367502"
    },
    {
        "version": "92.0.0.15.114",
        "code": "153386777"
    },
    {
        "version": "92.0.0.15.114",
        "code": "153386779"
    },
    {
        "version": "92.0.0.15.114",
        "code": "153386780"
    },
    {
        "version": "93.1.0.19.102",
        "code": "154400376"
    },
    {
        "version": "93.1.0.19.102",
        "code": "154400383"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374049"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374077"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374080"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374104"
    },
    {
        "version": "95.0.0.21.124",
        "code": "156514146"
    },
    {
        "version": "95.0.0.21.124",
        "code": "156514151"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405369"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405371"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405376"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405377"
    },
    {
        "version": "97.0.0.32.119",
        "code": "158441903"
    },
    {
        "version": "97.0.0.32.119",
        "code": "158441917"
    },
    {
        "version": "98.0.0.15.119",
        "code": "159526671"
    },
    {
        "version": "98.0.0.15.119",
        "code": "159526764"
    },
    {
        "version": "98.0.0.15.119",
        "code": "159526788"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497901"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497902"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497913"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497915"
    },
    {
        "version": "101.0.0.15.120",
        "code": "162439022"
    },
    {
        "version": "101.0.0.15.120",
        "code": "162439038"
    },
    {
        "version": "101.0.0.15.120",
        "code": "162439040"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478660"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478663"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478664"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478665"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478671"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478672"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022067"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022069"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022072"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022084"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022088"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022089"
    },
    {
        "version": "103.0.0.15.119",
        "code": "163988652"
    },
    {
        "version": "103.0.0.15.119",
        "code": "163988658"
    },
    {
        "version": "103.0.0.15.119",
        "code": "163988664"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094470"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094522"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094526"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094533"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094537"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094539"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094540"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165030898"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165030942"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165030945"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165031087"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165031107"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165031108"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149662"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149665"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149669"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149709"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149717"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149725"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338369"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338371"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338511"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338514"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338559"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338564"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361624"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361627"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361634"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361635"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474954"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474957"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474965"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474968"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693915"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693940"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693970"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693979"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693982"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693985"
    },
    {
        "version": "110.0.0.16.119",
        "code": "171727776"
    },
    {
        "version": "110.0.0.16.119",
        "code": "171727777"
    },
    {
        "version": "110.0.0.16.119",
        "code": "171727795"
    },
    {
        "version": "110.0.0.16.119",
        "code": "171727797"
    },
    {
        "version": "110.0.0.16.119",
        "code": "171727798"
    },
    {
        "version": "111.0.0.24.152",
        "code": "172894482"
    },
    {
        "version": "111.1.0.25.152",
        "code": "173238718"
    },
    {
        "version": "111.1.0.25.152",
        "code": "173238731"
    },
    {
        "version": "111.1.0.25.152",
        "code": "173238732"
    },
    {
        "version": "112.0.0.29.121",
        "code": "174081646"
    },
    {
        "version": "112.0.0.29.121",
        "code": "174081672"
    },
    {
        "version": "112.0.0.29.121",
        "code": "174081674"
    },
    {
        "version": "113.0.0.38.122",
        "code": "175504952"
    },
    {
        "version": "113.0.0.38.122",
        "code": "175504966"
    },
    {
        "version": "113.0.0.38.122",
        "code": "175504968"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649420"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649426"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649435"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649442"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649504"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649511"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649519"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649525"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574582"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574590"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574593"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574596"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574628"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574630"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574640"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574641"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770652"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770654"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770659"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770663"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770667"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770724"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770729"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770732"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770737"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155059"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155084"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155088"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155096"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155097"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155098"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155099"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322757"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322760"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322800"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322810"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322811"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322814"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496401"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496405"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496406"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496409"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496411"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496429"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496433"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496434"
    },
    {
        "version": "118.0.0.28.122",
        "code": "181496437"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747374"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747388"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747397"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747399"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747400"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747402"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982954"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982956"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982971"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982976"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982986"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982991"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183983005"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203672"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203673"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203693"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203705"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203706"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203708"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203710"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682680"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682681"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682682"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682684"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682694"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682695"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682698"
    },
    {
        "version": "122.0.0.29.238",
        "code": "187682700"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791631"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791648"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791669"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791674"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791681"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791692"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791703"
    },
    {
        "version": "124.0.0.17.473",
        "code": "192992558"
    },
    {
        "version": "124.0.0.17.473",
        "code": "192992563"
    },
    {
        "version": "124.0.0.17.473",
        "code": "192992565"
    },
    {
        "version": "124.0.0.17.473",
        "code": "192992577"
    },
    {
        "version": "124.0.0.17.473",
        "code": "192992578"
    },
    {
        "version": "124.0.0.17.473",
        "code": "192992579"
    },
    {
        "version": "124.0.0.17.473",
        "code": "192992583"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383407"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383411"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383413"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383426"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383428"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383430"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383433"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435525"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435540"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435547"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435560"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435561"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435566"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435577"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643798"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643799"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643801"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643803"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643814"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643820"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643821"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643822"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643823"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643826"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825079"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825083"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825084"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825108"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825186"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825208"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825223"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825234"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825244"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825260"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825268"
    },
    {
        "version": "128.0.0.26.128",
        "code": "197825286"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325880"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325883"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325886"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325890"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325897"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325907"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325909"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325911"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325912"
    },
    {
        "version": "129.0.0.29.119",
        "code": "199325914"
    },
    {
        "version": "130.0.0.31.121",
        "code": "200395940"
    },
    {
        "version": "130.0.0.31.121",
        "code": "200395971"
    },
    {
        "version": "130.0.0.31.121",
        "code": "200396014"
    },
    {
        "version": "130.0.0.31.121",
        "code": "200396019"
    },
    {
        "version": "130.0.0.31.121",
        "code": "200396023"
    },
    {
        "version": "130.0.0.31.121",
        "code": "200396029"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201576811"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201576921"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201576967"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201576977"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201576995"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201576999"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201577005"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201577185"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201577192"
    },
    {
        "version": "131.0.0.23.116",
        "code": "201577196"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775819"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775898"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775906"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775922"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775926"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775951"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775966"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775970"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775973"
    },
    {
        "version": "131.0.0.25.116",
        "code": "201775975"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766582"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766599"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766600"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766603"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766605"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766609"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766610"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766612"
    },
    {
        "version": "132.0.0.26.134",
        "code": "202766613"
    },
    {
        "version": "133.0.0.32.120",
        "code": "204019451"
    },
    {
        "version": "133.0.0.32.120",
        "code": "204019456"
    },
    {
        "version": "133.0.0.32.120",
        "code": "204019466"
    },
    {
        "version": "133.0.0.32.120",
        "code": "204019468"
    },
    {
        "version": "133.0.0.32.120",
        "code": "204019471"
    },
    {
        "version": "133.0.0.32.120",
        "code": "204019472"
    },
    {
        "version": "133.0.0.32.120",
        "code": "204019473"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280527"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280529"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280531"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280537"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280538"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280539"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280542"
    },
    {
        "version": "134.0.0.26.121",
        "code": "205280545"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670913"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670914"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670916"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670917"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670920"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670922"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670923"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670924"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670926"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670927"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670929"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670931"
    },
    {
        "version": "135.0.0.28.119",
        "code": "206670932"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061688"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061692"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061696"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061698"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061712"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061718"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061721"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061725"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061728"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061730"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061732"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061734"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061737"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061739"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061741"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061744"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061746"
    },
    {
        "version": "136.0.0.34.124",
        "code": "208061749"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143676"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143691"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143700"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143712"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143726"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143737"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143878"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143881"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143896"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143903"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143913"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143922"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143935"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143944"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143954"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143957"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143963"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143970"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143976"
    },
    {
        "version": "137.0.0.34.123",
        "code": "209143981"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180491"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180493"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180508"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180509"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180510"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180512"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180513"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180514"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180517"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180518"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180519"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180521"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180522"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180523"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180524"
    },
    {
        "version": "138.0.0.28.117",
        "code": "210180526"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399327"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399328"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399329"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399332"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399335"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399336"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399337"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399339"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399340"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399341"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399342"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399345"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399346"
    },
    {
        "version": "139.0.0.33.121",
        "code": "211399349"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676866"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676869"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676872"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676875"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676878"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676881"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676886"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676890"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676893"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676895"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676898"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676901"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676902"
    },
    {
        "version": "140.0.0.30.126",
        "code": "212676903"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245185"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245221"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245228"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245271"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245280"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245288"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245295"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245304"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245312"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245319"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245325"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245336"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245346"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245350"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245354"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245358"
    },
    {
        "version": "141.0.0.32.118",
        "code": "214245362"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464381"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464382"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464385"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464389"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464390"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464393"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464395"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464396"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464397"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464398"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464400"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464401"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464403"
    },
    {
        "version": "142.0.0.34.110",
        "code": "215464404"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817269"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817273"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817280"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817286"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817296"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817299"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817305"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817318"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817325"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817331"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817344"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817357"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817367"
    },
    {
        "version": "143.0.0.25.121",
        "code": "216817379"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948947"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948952"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948956"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948959"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948964"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948968"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948971"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948974"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948979"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948980"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948981"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948982"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948984"
    },
    {
        "version": "144.0.0.25.119",
        "code": "217948985"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308713"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308717"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308721"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308726"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308730"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308733"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308736"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308740"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308748"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308754"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308759"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308763"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308771"
    },
    {
        "version": "145.0.0.32.119",
        "code": "219308774"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221133998"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134002"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134005"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134009"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134012"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134015"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134018"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134023"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134026"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134029"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134032"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134037"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134039"
    },
    {
        "version": "146.0.0.27.125",
        "code": "221134042"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283620"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283621"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283623"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283624"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283625"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283627"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283628"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283629"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283630"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283631"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283632"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283634"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283635"
    },
    {
        "version": "147.0.0.42.124",
        "code": "225283636"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227298996"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299005"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299012"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299021"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299027"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299034"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299041"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299048"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299055"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299060"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299063"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299064"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299068"
    },
    {
        "version": "148.0.0.33.121",
        "code": "227299085"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970678"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970681"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970683"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970687"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970689"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970693"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970694"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970697"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970702"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970705"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970707"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970710"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970713"
    },
    {
        "version": "149.0.0.25.120",
        "code": "228970716"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877663"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877668"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877671"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877674"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877678"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877684"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877689"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877694"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877700"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877705"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877709"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877713"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877718"
    },
    {
        "version": "150.0.0.33.120",
        "code": "230877726"
    },
    {
        "version": "151.0.0.21.120",
        "code": "232088854"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232867959"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232867964"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232867967"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232867971"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232867993"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232867997"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868001"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868005"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868009"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868012"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868015"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868018"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868021"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868024"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868027"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868031"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868034"
    },
    {
        "version": "151.0.0.23.120",
        "code": "232868038"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847224"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847226"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847227"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847229"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847230"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847233"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847234"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847235"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847236"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847238"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847239"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847240"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847241"
    },
    {
        "version": "152.0.0.25.117",
        "code": "234847242"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572319"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572326"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572331"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572337"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572344"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572349"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572355"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572362"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572367"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572372"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572377"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572383"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572388"
    },
    {
        "version": "153.0.0.34.96",
        "code": "236572396"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093938"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093943"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093946"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093948"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093954"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093960"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093966"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093974"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093982"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093987"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093993"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238093999"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238094010"
    },
    {
        "version": "154.0.0.32.123",
        "code": "238094015"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490544"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490546"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490548"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490550"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490551"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490553"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490555"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490557"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490558"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490563"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490565"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490568"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490569"
    },
    {
        "version": "155.0.0.37.107",
        "code": "239490573"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726384"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726392"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726407"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726416"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726426"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726436"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726452"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726468"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726471"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726476"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726484"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726491"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726499"
    },
    {
        "version": "156.0.0.26.109",
        "code": "240726511"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168922"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168923"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168925"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168928"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168931"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168933"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168935"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168936"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168938"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168939"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168941"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168943"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168945"
    },
    {
        "version": "157.0.0.37.120",
        "code": "242168948"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646244"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646246"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646248"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646252"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646255"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646261"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646263"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646264"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646266"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646267"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646269"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646273"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646279"
    },
    {
        "version": "158.0.0.30.123",
        "code": "243646280"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196047"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196050"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196055"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196061"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196063"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196068"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196070"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196075"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196077"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196082"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196084"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196087"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196089"
    },
    {
        "version": "159.0.0.40.122",
        "code": "245196091"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889061"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889062"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889063"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889064"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889065"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889067"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889068"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889069"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889071"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889072"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889073"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889074"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889075"
    },
    {
        "version": "160.0.0.25.132",
        "code": "246889077"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310203"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310205"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310206"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310208"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310210"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310211"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310212"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310213"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310215"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310216"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310220"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310221"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310224"
    },
    {
        "version": "161.0.0.37.121",
        "code": "248310225"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507580"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507582"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507585"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507588"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507592"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507595"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507599"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507605"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507606"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507607"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507608"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507610"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507611"
    },
    {
        "version": "162.0.0.42.125",
        "code": "249507615"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742099"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742101"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742102"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742103"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742105"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742106"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742107"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742108"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742110"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742111"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742113"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742115"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742117"
    },
    {
        "version": "163.0.0.45.122",
        "code": "250742119"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055911"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055918"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055925"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055927"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055936"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055944"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055945"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055948"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055951"
    },
    {
        "version": "164.0.0.46.123",
        "code": "252055957"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447806"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447809"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447811"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447814"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447816"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447817"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447818"
    },
    {
        "version": "165.1.0.29.119",
        "code": "253447819"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777468"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777469"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777470"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777471"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777472"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777473"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777474"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777475"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777476"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777477"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777478"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777479"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777480"
    },
    {
        "version": "166.0.0.37.245",
        "code": "255777481"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959606"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959608"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959610"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959614"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959617"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959620"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959626"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959629"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959632"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959635"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959637"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959640"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959641"
    },
    {
        "version": "166.0.0.41.245",
        "code": "255959643"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099147"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099151"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099153"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099156"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099157"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099190"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099192"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099196"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099199"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099204"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099205"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099208"
    },
    {
        "version": "166.1.0.42.245",
        "code": "256099211"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966583"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966586"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966587"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966589"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966590"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966592"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966593"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966594"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966625"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966626"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966628"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966629"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966631"
    },
    {
        "version": "167.0.0.24.120",
        "code": "256966633"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829100"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829102"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829103"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829104"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829105"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829107"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829109"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829110"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829111"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829113"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829115"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829116"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829117"
    },
    {
        "version": "167.1.0.25.120",
        "code": "259829118"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079758"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079759"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079760"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079761"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079762"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079764"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079765"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079766"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079767"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079768"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079769"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079771"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079772"
    },
    {
        "version": "168.0.0.40.355",
        "code": "261079774"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372422"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372423"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372424"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372425"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372426"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372427"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372428"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372429"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372430"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372431"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372432"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372433"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372435"
    },
    {
        "version": "169.0.0.28.135",
        "code": "262372436"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886984"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886985"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886986"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886987"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886988"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886989"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886990"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886991"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886992"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886993"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886995"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886996"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886998"
    },
    {
        "version": "169.1.0.29.135",
        "code": "262886999"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009009"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009011"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009013"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009019"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009021"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009023"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009024"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009026"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009028"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009030"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009049"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009052"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009054"
    },
    {
        "version": "169.3.0.30.135",
        "code": "264009055"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397319"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397320"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397321"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397322"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397327"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397329"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397334"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397337"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397338"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397343"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397344"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397348"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397351"
    },
    {
        "version": "170.0.0.30.474",
        "code": "267397357"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925697"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925702"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925705"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925708"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925714"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925718"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925724"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925726"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925729"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925733"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925737"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925742"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925745"
    },
    {
        "version": "170.2.0.30.474",
        "code": "267925747"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773220"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773225"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773227"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773233"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773239"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773272"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773274"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773276"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773283"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773286"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773287"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773290"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773295"
    },
    {
        "version": "171.0.0.29.121",
        "code": "268773297"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790785"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790788"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790789"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790792"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790795"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790796"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790798"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790799"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790800"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790803"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790805"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790807"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790810"
    },
    {
        "version": "172.0.0.21.123",
        "code": "269790811"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182262"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182263"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182265"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182266"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182267"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182268"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182270"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182273"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182274"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182276"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182277"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182279"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182280"
    },
    {
        "version": "173.0.0.39.120",
        "code": "271182282"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382089"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382091"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382093"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382095"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382098"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382099"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382100"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382101"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382103"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382106"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382110"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382111"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382115"
    },
    {
        "version": "174.0.0.31.132",
        "code": "272382117"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728769"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728778"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728787"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728798"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728806"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728813"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728820"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728826"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728828"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728832"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728833"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728838"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728842"
    },
    {
        "version": "175.0.0.23.119",
        "code": "273728846"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907082"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907087"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907088"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907093"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907098"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907101"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907103"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907106"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907107"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907108"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907111"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907112"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907115"
    },
    {
        "version": "175.1.0.25.119",
        "code": "273907117"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774853"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774857"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774862"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774869"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774875"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774884"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774891"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774895"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774900"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774904"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774908"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774914"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774918"
    },
    {
        "version": "176.0.0.38.116",
        "code": "274774922"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276027952"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276027963"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276027967"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028005"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028009"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028013"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028017"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028020"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028026"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028029"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028032"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028033"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028037"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028040"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028045"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028050"
    },
    {
        "version": "177.0.0.30.119",
        "code": "276028053"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249210"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249226"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249227"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249234"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249235"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249237"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249238"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249240"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249241"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249242"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249244"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249245"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249248"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249249"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249250"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249251"
    },
    {
        "version": "178.1.0.37.123",
        "code": "277249252"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625412"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625414"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625416"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625420"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625423"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625429"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625431"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625435"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625440"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625444"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625447"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625451"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625454"
    },
    {
        "version": "179.0.0.31.132",
        "code": "278625456"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996057"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996058"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996059"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996060"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996061"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996062"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996063"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996064"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996065"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996067"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996068"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996070"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996071"
    },
    {
        "version": "180.0.0.31.119",
        "code": "279996072"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579016"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579020"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579021"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579023"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579025"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579026"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579027"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579029"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579030"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579031"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579032"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579033"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579034"
    },
    {
        "version": "181.0.0.33.117",
        "code": "281579036"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072560"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072562"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072567"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072571"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072574"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072576"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072580"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072582"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072585"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072587"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072590"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072592"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072593"
    },
    {
        "version": "182.0.0.29.124",
        "code": "283072597"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459210"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459211"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459212"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459213"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459214"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459215"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459218"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459220"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459221"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459223"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459224"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459225"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459228"
    },
    {
        "version": "183.0.0.40.116",
        "code": "284459229"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855788"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855790"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855791"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855793"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855795"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855796"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855797"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855798"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855800"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855802"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855803"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855804"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855805"
    },
    {
        "version": "184.0.0.30.117",
        "code": "285855806"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287420968"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287420971"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287420974"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287420979"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287420997"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421005"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421012"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421015"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421017"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421019"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421023"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421026"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421028"
    },
    {
        "version": "185.0.0.38.116",
        "code": "287421032"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682395"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682396"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682397"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682398"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682399"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682400"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682401"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682402"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682403"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682405"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682406"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682407"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682408"
    },
    {
        "version": "186.0.0.36.128",
        "code": "288682410"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692181"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692183"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692185"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692186"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692188"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692190"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692192"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692195"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692196"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692197"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692198"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692200"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692202"
    },
    {
        "version": "187.0.0.32.120",
        "code": "289692203"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080139"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080146"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080153"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080157"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080163"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080168"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080169"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080174"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080178"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080183"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080186"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080190"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080194"
    },
    {
        "version": "188.0.0.35.124",
        "code": "292080197"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853426"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853429"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853431"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853435"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853440"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853447"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853452"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853463"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853467"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853473"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853475"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853478"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853481"
    },
    {
        "version": "189.0.0.41.121",
        "code": "293853483"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813903"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813904"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813906"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813912"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813914"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813915"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813918"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813919"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813921"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813922"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813925"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813947"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813952"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813957"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813978"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813983"
    },
    {
        "version": "190.0.0.36.119",
        "code": "295813984"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117880"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117905"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117925"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117927"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117956"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117961"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117966"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117969"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117972"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117973"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117974"
    },
    {
        "version": "191.0.0.40.124",
        "code": "297117976"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313644"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313648"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313654"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313658"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313662"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313668"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313672"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313674"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313675"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313677"
    },
    {
        "version": "191.1.0.41.124",
        "code": "297313678"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419552"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419558"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419561"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419565"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419581"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419601"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419614"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419638"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419656"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419684"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419715"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419744"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419767"
    },
    {
        "version": "192.0.0.35.123",
        "code": "298419792"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078984"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078985"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078986"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078988"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078989"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078990"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078992"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078994"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078996"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078997"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078998"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300078999"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300079001"
    },
    {
        "version": "193.0.0.45.120",
        "code": "300079004"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484470"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484471"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484472"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484473"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484474"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484475"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484477"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484478"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484479"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484481"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484483"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484484"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484485"
    },
    {
        "version": "194.0.0.36.172",
        "code": "301484486"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733750"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733752"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733755"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733757"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733759"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733761"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733763"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733765"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733767"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733769"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733770"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733772"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733773"
    },
    {
        "version": "195.0.0.31.123",
        "code": "302733775"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101658"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101659"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101660"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101661"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101662"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101664"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101665"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101666"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101667"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101668"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101669"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101670"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101671"
    },
    {
        "version": "196.0.0.32.126",
        "code": "304101673"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478153"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478159"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478165"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478169"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478175"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478185"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478193"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478201"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478203"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478207"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478211"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478212"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478215"
    },
    {
        "version": "197.0.0.26.119",
        "code": "305478217"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053294"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053295"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053297"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053298"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053300"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053303"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053305"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053310"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053313"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053315"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053317"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053320"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053323"
    },
    {
        "version": "198.0.0.32.120",
        "code": "307053326"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427612"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427615"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427618"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427624"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427626"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427628"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427631"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427633"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427638"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427642"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427644"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427647"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427650"
    },
    {
        "version": "199.0.0.34.119",
        "code": "308427652"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633560"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633564"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633567"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633570"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633575"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633579"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633583"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633588"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633594"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633598"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633599"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633605"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633607"
    },
    {
        "version": "199.1.0.34.119",
        "code": "308633611"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093348"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093354"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093357"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093361"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093362"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093364"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093368"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093373"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093375"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093376"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093377"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093378"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093382"
    },
    {
        "version": "200.0.0.29.121",
        "code": "310093383"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560183"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560191"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560208"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560250"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560301"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560353"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560404"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560436"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560475"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560516"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560561"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560584"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560627"
    },
    {
        "version": "200.1.0.29.121",
        "code": "310560654"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311618547"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311618712"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311618945"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619304"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619575"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619709"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619753"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619798"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619826"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619851"
    },
    {
        "version": "201.0.0.26.112",
        "code": "311619871"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303531"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303532"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303533"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303534"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303535"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303536"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303537"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303538"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303539"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303540"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303541"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303542"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303543"
    },
    {
        "version": "203.0.0.29.118",
        "code": "320303544"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403563"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403564"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403565"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403566"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403567"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403568"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403569"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403570"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403571"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403572"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403573"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403574"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403575"
    },
    {
        "version": "204.0.0.30.119",
        "code": "320403576"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503757"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503758"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503759"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503760"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503761"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503762"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503763"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503764"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503765"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503766"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503767"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503768"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503769"
    },
    {
        "version": "205.0.0.34.114",
        "code": "320503770"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603758"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603761"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603763"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603766"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603767"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603768"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603769"
    },
    {
        "version": "206.0.0.34.121",
        "code": "320603770"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603789"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603790"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603793"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603795"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603798"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603799"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603800"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603801"
    },
    {
        "version": "206.1.0.34.121",
        "code": "320603802"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703917"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703918"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703920"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703921"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703923"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703926"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703927"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703928"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703929"
    },
    {
        "version": "207.0.0.39.120",
        "code": "320703930"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804001"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804002"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804003"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804004"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804005"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804006"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804007"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804008"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804009"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804010"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804011"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804012"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804013"
    },
    {
        "version": "208.0.0.32.135",
        "code": "320804014"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903297"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903298"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903299"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903300"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903301"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903302"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903303"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903304"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903305"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903306"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903307"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903308"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903309"
    },
    {
        "version": "209.0.0.21.119",
        "code": "320903310"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002465"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002466"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002467"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002468"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002469"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002470"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002471"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002472"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002473"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002474"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002475"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002476"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002477"
    },
    {
        "version": "210.0.0.28.71",
        "code": "321002478"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103505"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103506"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103507"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103508"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103509"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103510"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103511"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103512"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103513"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103514"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103515"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103516"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103517"
    },
    {
        "version": "211.0.0.33.117",
        "code": "321103518"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203905"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203906"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203907"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203908"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203909"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203910"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203911"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203912"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203913"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203914"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203915"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203916"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203917"
    },
    {
        "version": "212.0.0.38.119",
        "code": "321203918"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303807"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303808"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303809"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303810"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303811"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303812"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303813"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303814"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303815"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303816"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303817"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303818"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303819"
    },
    {
        "version": "213.0.0.29.120",
        "code": "321303820"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403727"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403728"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403729"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403730"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403731"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403732"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403733"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403734"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403735"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403736"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403737"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403738"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403739"
    },
    {
        "version": "214.0.0.27.120",
        "code": "321403740"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403847"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403848"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403849"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403850"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403851"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403852"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403853"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403854"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403855"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403856"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403857"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403858"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403859"
    },
    {
        "version": "214.1.0.29.120",
        "code": "321403860"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604976"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604977"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604978"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604979"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604980"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604981"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604982"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604983"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604984"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604985"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604986"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604987"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604988"
    },
    {
        "version": "215.0.0.27.359",
        "code": "321604989"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703944"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703945"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703946"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703947"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703948"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703949"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703950"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703951"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703952"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703953"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703954"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703955"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703956"
    },
    {
        "version": "216.0.0.20.137",
        "code": "321703957"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704028"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704029"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704030"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704031"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704032"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704033"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704034"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704035"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704036"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704037"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704038"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704039"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704040"
    },
    {
        "version": "216.1.0.21.137",
        "code": "321704041"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711989"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711990"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711991"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711992"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711993"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711994"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711995"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711996"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711997"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711998"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322711999"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322712000"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322712001"
    },
    {
        "version": "217.0.0.15.474",
        "code": "322712002"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803421"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803422"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803423"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803424"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803425"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803426"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803427"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803428"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803429"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803430"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803431"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803432"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803433"
    },
    {
        "version": "218.0.0.19.108",
        "code": "322803434"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903320"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903323"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903324"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903325"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903328"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903329"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903330"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903331"
    },
    {
        "version": "219.0.0.12.117",
        "code": "322903332"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003439"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003440"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003441"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003442"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003443"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003444"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003445"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003446"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003447"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003448"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003449"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003450"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003451"
    },
    {
        "version": "220.0.0.16.115",
        "code": "323003452"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103555"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103556"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103557"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103558"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103559"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103560"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103561"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103562"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103563"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103564"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103565"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103566"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103567"
    },
    {
        "version": "221.0.0.16.118",
        "code": "323103568"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203439"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203440"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203441"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203442"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203443"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203444"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203445"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203446"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203447"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203448"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203449"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203450"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203451"
    },
    {
        "version": "222.0.0.15.114",
        "code": "323203452"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303134"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303135"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303137"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303139"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303140"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303141"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303143"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303144"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303145"
    },
    {
        "version": "223.0.0.14.103",
        "code": "323303146"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303175"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303176"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303177"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303178"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303179"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303180"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303181"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303182"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303183"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303184"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303185"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303186"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303187"
    },
    {
        "version": "223.1.0.14.103",
        "code": "323303188"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403631"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403632"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403633"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403634"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403635"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403636"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403637"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403638"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403639"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403640"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403641"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403642"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403643"
    },
    {
        "version": "224.0.0.20.116",
        "code": "323403644"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403673"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403674"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403675"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403676"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403677"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403678"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403679"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403681"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403682"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403683"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403684"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403685"
    },
    {
        "version": "224.1.0.20.116",
        "code": "323403686"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403715"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403716"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403717"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403718"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403719"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403720"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403721"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403722"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403723"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403724"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403725"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403726"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403727"
    },
    {
        "version": "224.2.0.20.116",
        "code": "323403728"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503565"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503566"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503567"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503568"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503569"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503570"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503571"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503572"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503573"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503574"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503575"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503576"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503577"
    },
    {
        "version": "225.0.0.19.115",
        "code": "323503578"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603749"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603750"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603751"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603752"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603753"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603754"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603755"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603756"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603757"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603758"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603759"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603760"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603761"
    },
    {
        "version": "226.0.0.16.117",
        "code": "323603762"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603805"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603806"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603807"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603808"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603809"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603810"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603811"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603812"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603813"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603814"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603815"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603816"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603817"
    },
    {
        "version": "226.1.0.16.117",
        "code": "323603818"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703783"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703785"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703789"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703790"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703811"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703812"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703818"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703819"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703820"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703821"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703822"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703823"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703824"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703825"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703826"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703827"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703828"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703829"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703830"
    },
    {
        "version": "227.0.0.12.117",
        "code": "323703831"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801211"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801212"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801213"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801229"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801233"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801234"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801240"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801241"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801242"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801243"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801244"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801245"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801246"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801247"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801248"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801249"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801250"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801251"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801252"
    },
    {
        "version": "228.0.0.15.111",
        "code": "362801253"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904832"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904836"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904837"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904854"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904858"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904859"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904860"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904865"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904866"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904867"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904868"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904869"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904870"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904871"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904872"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904873"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904874"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904875"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904876"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904877"
    },
    {
        "version": "229.0.0.17.118",
        "code": "362904878"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004964"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004965"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004966"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004967"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004968"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004969"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004970"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004971"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004972"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004973"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004974"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004975"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004976"
    },
    {
        "version": "230.0.0.20.108",
        "code": "363004977"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363104995"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363104996"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363104997"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363104998"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363104999"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105000"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105001"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105002"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105003"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105004"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105005"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105006"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105007"
    },
    {
        "version": "231.0.0.18.113",
        "code": "363105008"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204577"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204586"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204587"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204608"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204609"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204611"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204615"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204616"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204617"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204618"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204619"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204620"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204621"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204622"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204623"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204624"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204625"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204626"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204627"
    },
    {
        "version": "232.0.0.16.114",
        "code": "363204628"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304194"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304198"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304200"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304214"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304216"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304220"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304225"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304226"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304227"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304228"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304229"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304230"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304231"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304232"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304233"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304234"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304235"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304236"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304237"
    },
    {
        "version": "233.0.0.13.112",
        "code": "363304238"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404943"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404948"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404952"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404953"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404984"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404988"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404989"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404990"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404993"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404994"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404995"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404996"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404997"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404998"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363404999"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363405000"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363405001"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363405002"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363405003"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363405004"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363405005"
    },
    {
        "version": "234.0.0.19.113",
        "code": "363405006"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504936"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504937"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504938"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504939"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504940"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504941"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504942"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504943"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504944"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504945"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504946"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504947"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504948"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504949"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504976"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504982"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504983"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504988"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504989"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504990"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504991"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504992"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504993"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504994"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504995"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504996"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504997"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504998"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363504999"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363505000"
    },
    {
        "version": "235.0.0.21.107",
        "code": "363505001"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605018"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605019"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605020"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605021"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605022"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605023"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605024"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605025"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605026"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605027"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605028"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605029"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605030"
    },
    {
        "version": "236.0.0.20.109",
        "code": "363605031"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704276"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704280"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704281"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704310"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704315"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704317"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704319"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704322"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704323"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704324"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704325"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704326"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704327"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704328"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704329"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704330"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704331"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704332"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704333"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704334"
    },
    {
        "version": "237.0.0.14.102",
        "code": "363704335"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804570"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804571"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804602"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804606"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804607"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804612"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804613"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804614"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804615"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804616"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804617"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804618"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804619"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804620"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804621"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804622"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804623"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804624"
    },
    {
        "version": "238.0.0.14.112",
        "code": "363804625"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904653"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904656"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904658"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904662"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904663"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904692"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904698"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904699"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904704"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904705"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904706"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904707"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904708"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904709"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904710"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904711"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904712"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904713"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904714"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904715"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904716"
    },
    {
        "version": "239.0.0.14.111",
        "code": "363904717"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004813"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004820"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004822"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004852"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004856"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004862"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004863"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004864"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004865"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004866"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004867"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004868"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004869"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004870"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004871"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004872"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004873"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004874"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364004875"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364104374"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364104714"
    },
    {
        "version": "240.2.0.18.107",
        "code": "364105084"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105300"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105304"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105305"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105336"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105340"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105341"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105342"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105346"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105347"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105348"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105349"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105350"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105351"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105352"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105353"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105354"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105355"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105356"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105357"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105358"
    },
    {
        "version": "241.1.0.18.114",
        "code": "364105359"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204530"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204531"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204533"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204562"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204566"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204567"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204568"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204572"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204573"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204574"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204575"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204576"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204577"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204578"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204579"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204580"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204581"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204582"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204583"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204584"
    },
    {
        "version": "242.0.0.16.111",
        "code": "364204585"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304742"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304743"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304778"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304784"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304785"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304786"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304787"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304788"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304789"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304790"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304791"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304792"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304793"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304794"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304795"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304796"
    },
    {
        "version": "243.0.0.16.111",
        "code": "364304797"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404772"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404776"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404777"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404803"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404808"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404812"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404813"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404818"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404819"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404820"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404821"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404822"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404823"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404824"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404825"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404826"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404827"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404828"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404829"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404830"
    },
    {
        "version": "244.0.0.17.110",
        "code": "364404831"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364404976"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364404980"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364404981"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405007"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405012"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405016"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405017"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405022"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405023"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405024"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405025"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405026"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405027"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405028"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405029"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405030"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405031"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405032"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405033"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405034"
    },
    {
        "version": "244.1.0.19.110",
        "code": "364405035"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504797"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504802"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504806"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504807"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504809"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504838"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504842"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504843"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504848"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504849"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504850"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504851"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504852"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504853"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504854"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504855"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504856"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504857"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504858"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504859"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504860"
    },
    {
        "version": "245.0.0.18.108",
        "code": "364504861"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604706"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604710"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604711"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604752"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604753"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604754"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604755"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604756"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604757"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604758"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604759"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604760"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604761"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604762"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604763"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604764"
    },
    {
        "version": "246.0.0.16.113",
        "code": "364604765"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604774"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604778"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604779"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604820"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604821"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604822"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604823"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604824"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604825"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604826"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604827"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604828"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604829"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604830"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604831"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604832"
    },
    {
        "version": "246.1.0.16.113",
        "code": "364604833"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704800"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704801"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704827"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704836"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704837"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704842"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704843"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704844"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704845"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704846"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704847"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704848"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704849"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704850"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704851"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704852"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704853"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704854"
    },
    {
        "version": "247.0.0.17.113",
        "code": "364704855"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804710"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804736"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804746"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804747"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804753"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804754"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804755"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804756"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804758"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804759"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804760"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804761"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804762"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804763"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804764"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364804765"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364903549"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364903715"
    },
    {
        "version": "248.0.0.17.109",
        "code": "364904259"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904786"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904787"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904818"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904822"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904823"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904824"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904828"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904829"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904830"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904831"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904832"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904833"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904834"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904835"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904836"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904837"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904838"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904839"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904840"
    },
    {
        "version": "249.0.0.20.105",
        "code": "364904841"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365004977"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365004980"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365004986"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365004987"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005022"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005023"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005024"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005028"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005029"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005030"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005031"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005032"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005033"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005034"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005035"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005036"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005037"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005038"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005039"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005040"
    },
    {
        "version": "250.0.0.21.109",
        "code": "365005041"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104326"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104330"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104366"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104367"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104372"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104373"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104374"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104375"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104376"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104377"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104378"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104379"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104380"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104381"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104382"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104383"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104384"
    },
    {
        "version": "251.0.0.11.106",
        "code": "365104385"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104394"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104398"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104399"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104434"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104440"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104441"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104442"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104443"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104444"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104445"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104446"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104447"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104448"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104449"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104450"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104451"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104452"
    },
    {
        "version": "251.1.0.11.106",
        "code": "365104453"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204770"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204776"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204777"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204778"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204808"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204812"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204813"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204818"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204819"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204820"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204821"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204822"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204823"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204824"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204825"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204826"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204827"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204828"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204829"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204830"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365204831"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365303827"
    },
    {
        "version": "252.0.0.17.111",
        "code": "365304877"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305059"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305062"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305066"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305067"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305093"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305108"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305109"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305110"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305112"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305114"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305117"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305118"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305119"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305120"
    },
    {
        "version": "253.0.0.23.114",
        "code": "365305121"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405108"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405109"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405144"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405150"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405151"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405152"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405153"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405154"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405155"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405156"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405157"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405158"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405159"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405160"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405161"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405162"
    },
    {
        "version": "254.0.0.19.109",
        "code": "365405163"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505400"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505401"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505406"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505407"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505408"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505409"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505410"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505411"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505412"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505413"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505414"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505415"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505416"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505417"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505418"
    },
    {
        "version": "255.0.0.17.102",
        "code": "365505419"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505428"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505432"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505433"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505434"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505435"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505459"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505464"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505468"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505469"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505474"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505475"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505476"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505477"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505478"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505479"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505480"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505481"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505482"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505483"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505484"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505485"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505486"
    },
    {
        "version": "255.1.0.17.102",
        "code": "365505487"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365604974"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365604978"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365604979"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605009"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605014"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605016"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605020"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605021"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605022"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605023"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605024"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605025"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605026"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605027"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605028"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605029"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605030"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605031"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605032"
    },
    {
        "version": "256.0.0.18.105",
        "code": "365605033"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705092"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705093"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705124"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705128"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705135"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705138"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705140"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705144"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705145"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705146"
    },
    {
        "version": "257.0.0.16.110",
        "code": "365705147"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705352"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705353"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705393"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705396"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705398"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705402"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705403"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705408"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705409"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705410"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705411"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705412"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705413"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705414"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705415"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705416"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705417"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705418"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705419"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705420"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365705421"
    },
    {
        "version": "257.1.0.16.110",
        "code": "365804487"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805460"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805472"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805473"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805474"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805475"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805476"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805477"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805478"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805479"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805480"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805481"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805482"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805483"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805484"
    },
    {
        "version": "258.0.0.26.100",
        "code": "365805485"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805490"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805492"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805493"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805498"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805499"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805528"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805530"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805534"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805535"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805540"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805541"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805542"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805543"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805544"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805545"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805546"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805547"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805548"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805549"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805550"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805551"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805552"
    },
    {
        "version": "258.1.0.26.100",
        "code": "365805553"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905812"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905813"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905814"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905815"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905816"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905817"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905818"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905819"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905820"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905821"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905822"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905823"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905824"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905825"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905829"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905832"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905834"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905838"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905869"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905874"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905875"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905880"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905881"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905882"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905883"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905884"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905885"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905886"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905887"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905888"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905889"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905890"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905891"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905892"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905893"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005340"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005341"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005342"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005346"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005347"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005376"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005377"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005378"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005382"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005388"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005389"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005390"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005391"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005392"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005393"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005394"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005395"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005396"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005397"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005398"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005399"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005400"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005401"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905812"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905813"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905814"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905815"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905816"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905817"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905818"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905819"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905820"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905821"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905822"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905823"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905824"
    },
    {
        "version": "259.0.0.29.104",
        "code": "365905825"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905829"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905832"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905834"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905838"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905869"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905874"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905875"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905880"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905881"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905882"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905883"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905884"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905885"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905886"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905887"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905888"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905889"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905890"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905891"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905892"
    },
    {
        "version": "259.1.0.29.104",
        "code": "365905893"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005340"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005341"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005342"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005346"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005347"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005376"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005377"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005378"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005382"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005388"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005389"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005390"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005391"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005392"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005393"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005394"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005395"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005396"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005397"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005398"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005399"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005400"
    },
    {
        "version": "260.0.0.23.115",
        "code": "366005401"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105462"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105466"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105467"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105493"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105496"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105502"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105508"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105509"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105510"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105511"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105512"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105513"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105514"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105515"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105516"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105517"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105518"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105519"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105520"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366105521"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366216265"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366216469"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366216535"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366216539"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366216607"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366216971"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366216975"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366217179"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366217247"
    },
    {
        "version": "261.0.0.21.111",
        "code": "366217383"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217699"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217700"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217702"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217706"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217707"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217735"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217736"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217737"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217743"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217747"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217750"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217751"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217752"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217753"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217754"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217756"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217757"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217758"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217759"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217760"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217761"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217762"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366217763"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366308253"
    },
    {
        "version": "262.0.0.24.327",
        "code": "366308457"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308706"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308707"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308708"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308712"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308742"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308748"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308749"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308753"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308756"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308757"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308758"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308759"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308760"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308762"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308763"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308764"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308765"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308766"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308767"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308768"
    },
    {
        "version": "263.0.0.19.104",
        "code": "366308769"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308842"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308843"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308844"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308848"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308878"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308884"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308885"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308889"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308892"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308893"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308894"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308895"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308896"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308898"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308899"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308900"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308901"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308902"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308903"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308904"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366308905"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366408445"
    },
    {
        "version": "263.2.0.19.104",
        "code": "366408853"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409643"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409646"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409647"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409648"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409682"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409683"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409684"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409688"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409689"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409693"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409696"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409697"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409698"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409699"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409700"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409702"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409703"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409704"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409705"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409706"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409707"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409708"
    },
    {
        "version": "264.0.0.22.106",
        "code": "366409709"
    }
]
versions_old = [
    {
        "version": "5.0.8",
        "code": "1376634"
    },
    {
        "version": "5.1.7",
        "code": "2218950"
    },
    {
        "version": "6.10.1",
        "code": "5257472"
    },
    {
        "version": "6.11.2",
        "code": "5547416"
    },
    {
        "version": "6.12.0",
        "code": "5856007"
    },
    {
        "version": "6.12.1",
        "code": "5879188"
    },
    {
        "version": "6.12.2",
        "code": "5914807"
    },
    {
        "version": "6.13.0",
        "code": "6189164"
    },
    {
        "version": "6.13.1",
        "code": "6208041"
    },
    {
        "version": "6.13.3",
        "code": "6280649"
    },
    {
        "version": "6.14.0",
        "code": "6323749"
    },
    {
        "version": "6.14.0",
        "code": "6456473"
    },
    {
        "version": "6.14.1",
        "code": "6527593"
    },
    {
        "version": "6.15.0",
        "code": "6648672"
    },
    {
        "version": "6.15.0",
        "code": "6809797"
    },
    {
        "version": "6.15.0",
        "code": "6891295"
    },
    {
        "version": "6.16.0",
        "code": "7097676"
    },
    {
        "version": "6.16.0",
        "code": "7186551"
    },
    {
        "version": "6.16.0",
        "code": "7274492"
    },
    {
        "version": "6.16.1",
        "code": "7369808"
    },
    {
        "version": "6.17.0",
        "code": "7483428"
    },
    {
        "version": "6.17.0",
        "code": "7713781"
    },
    {
        "version": "6.17.1",
        "code": "7792671"
    },
    {
        "version": "6.18.0",
        "code": "8031086"
    },
    {
        "version": "6.18.0",
        "code": "8133161"
    },
    {
        "version": "6.18.0",
        "code": "8241704"
    },
    {
        "version": "6.18.0",
        "code": "8317903"
    },
    {
        "version": "6.19.0",
        "code": "8582325"
    },
    {
        "version": "6.19.0",
        "code": "8700864"
    },
    {
        "version": "6.19.0",
        "code": "8847895"
    },
    {
        "version": "6.19.0",
        "code": "8886221"
    },
    {
        "version": "6.20.0",
        "code": "9204850"
    },
    {
        "version": "6.20.0",
        "code": "9353187"
    },
    {
        "version": "6.20.1",
        "code": "9409530"
    },
    {
        "version": "6.20.1",
        "code": "9476507"
    },
    {
        "version": "6.20.2",
        "code": "9494173"
    },
    {
        "version": "6.21.0",
        "code": "9627240"
    },
    {
        "version": "6.21.0",
        "code": "9804755"
    },
    {
        "version": "6.21.0",
        "code": "9921663"
    },
    {
        "version": "6.21.2",
        "code": "9956336"
    },
    {
        "version": "6.21.2",
        "code": "9956337"
    },
    {
        "version": "6.22.0",
        "code": "10227271"
    },
    {
        "version": "6.22.0",
        "code": "10368623"
    },
    {
        "version": "6.22.0",
        "code": "10529824"
    },
    {
        "version": "6.22.0",
        "code": "10569317"
    },
    {
        "version": "6.23.0",
        "code": "10886602"
    },
    {
        "version": "6.23.0",
        "code": "11001525"
    },
    {
        "version": "6.23.0",
        "code": "11152246"
    },
    {
        "version": "6.23.0",
        "code": "11152254"
    },
    {
        "version": "6.24.0",
        "code": "11467175"
    },
    {
        "version": "6.24.0",
        "code": "11628516"
    },
    {
        "version": "6.24.0",
        "code": "11776170"
    },
    {
        "version": "7.0.0",
        "code": "12080497"
    },
    {
        "version": "7.0.0",
        "code": "12103120"
    },
    {
        "version": "7.1.0",
        "code": "12138101"
    },
    {
        "version": "7.1.0",
        "code": "12399039"
    },
    {
        "version": "7.1.1",
        "code": "12505108"
    },
    {
        "version": "7.2.0",
        "code": "12678588"
    },
    {
        "version": "7.2.0",
        "code": "12894558"
    },
    {
        "version": "7.2.0",
        "code": "12953501"
    },
    {
        "version": "7.2.1",
        "code": "12998762"
    },
    {
        "version": "7.2.2",
        "code": "13167125"
    },
    {
        "version": "7.2.3",
        "code": "13175448"
    },
    {
        "version": "7.2.4",
        "code": "13207465"
    },
    {
        "version": "7.3.0",
        "code": "13211814"
    },
    {
        "version": "7.3.0",
        "code": "13252488"
    },
    {
        "version": "7.3.0",
        "code": "13328396"
    },
    {
        "version": "7.3.0",
        "code": "13357693"
    },
    {
        "version": "7.3.0",
        "code": "13428238"
    },
    {
        "version": "7.3.0",
        "code": "13447540"
    },
    {
        "version": "7.3.0",
        "code": "13447541"
    },
    {
        "version": "7.4.0",
        "code": "13617090"
    },
    {
        "version": "7.4.0",
        "code": "13673128"
    },
    {
        "version": "7.3.1",
        "code": "13678552"
    },
    {
        "version": "7.4.0",
        "code": "13688692"
    },
    {
        "version": "7.4.0",
        "code": "13806513"
    },
    {
        "version": "7.4.0",
        "code": "13841095"
    },
    {
        "version": "7.5.0",
        "code": "14047999"
    },
    {
        "version": "7.5.0",
        "code": "14082771"
    },
    {
        "version": "7.5.0",
        "code": "14135411"
    },
    {
        "version": "7.5.0",
        "code": "14240471"
    },
    {
        "version": "7.5.0",
        "code": "14276131"
    },
    {
        "version": "7.5.1",
        "code": "14510519"
    },
    {
        "version": "7.5.2",
        "code": "14547085"
    },
    {
        "version": "7.6.0",
        "code": "14592506"
    },
    {
        "version": "7.6.0",
        "code": "14649552"
    },
    {
        "version": "7.6.0",
        "code": "14708479"
    },
    {
        "version": "7.7.0",
        "code": "14945148"
    },
    {
        "version": "7.7.0",
        "code": "14997179"
    },
    {
        "version": "7.6.1",
        "code": "14996309"
    },
    {
        "version": "7.7.0",
        "code": "15049153"
    },
    {
        "version": "7.7.0",
        "code": "15123498"
    },
    {
        "version": "7.7.0",
        "code": "15235526"
    },
    {
        "version": "7.8.0",
        "code": "15435389"
    },
    {
        "version": "7.8.0",
        "code": "15552925"
    },
    {
        "version": "7.8.0",
        "code": "15655929"
    },
    {
        "version": "7.8.0",
        "code": "15677960"
    },
    {
        "version": "7.8.0",
        "code": "15693177"
    },
    {
        "version": "7.9.0",
        "code": "15997156"
    },
    {
        "version": "7.9.0",
        "code": "16085896"
    },
    {
        "version": "7.9.0",
        "code": "16288123"
    },
    {
        "version": "7.9.0",
        "code": "16414541"
    },
    {
        "version": "7.9.0",
        "code": "16414543"
    },
    {
        "version": "7.9.2",
        "code": "16553907"
    },
    {
        "version": "7.9.1",
        "code": "16508983"
    },
    {
        "version": "7.9.1",
        "code": "16508986"
    },
    {
        "version": "7.10.0",
        "code": "16732668"
    },
    {
        "version": "7.10.0",
        "code": "16838479"
    },
    {
        "version": "7.10.0",
        "code": "16887320"
    },
    {
        "version": "7.10.0",
        "code": "17047892"
    },
    {
        "version": "7.11.0",
        "code": "17371373"
    },
    {
        "version": "7.11.0",
        "code": "17476525"
    },
    {
        "version": "7.11.0",
        "code": "17639608"
    },
    {
        "version": "7.11.0",
        "code": "17690090"
    },
    {
        "version": "7.11.0",
        "code": "17712920"
    },
    {
        "version": "7.11.0",
        "code": "17712926"
    },
    {
        "version": "7.11.1",
        "code": "17776137"
    },
    {
        "version": "7.12.0",
        "code": "18020870"
    },
    {
        "version": "7.12.0",
        "code": "18187053"
    },
    {
        "version": "7.12.0",
        "code": "18297871"
    },
    {
        "version": "7.12.0",
        "code": "18317857"
    },
    {
        "version": "7.12.1",
        "code": "18439029"
    },
    {
        "version": "7.12.1",
        "code": "18439032"
    },
    {
        "version": "7.13.0",
        "code": "18650373"
    },
    {
        "version": "7.13.0",
        "code": "18770142"
    },
    {
        "version": "7.13.0",
        "code": "18906164"
    },
    {
        "version": "7.13.0",
        "code": "18986441"
    },
    {
        "version": "7.13.0",
        "code": "19013743"
    },
    {
        "version": "7.13.1",
        "code": "19276019"
    },
    {
        "version": "7.14.0",
        "code": "19528317"
    },
    {
        "version": "7.14.0",
        "code": "19767666"
    },
    {
        "version": "7.14.0",
        "code": "19890715"
    },
    {
        "version": "7.14.0",
        "code": "20014569"
    },
    {
        "version": "7.14.0",
        "code": "20120481"
    },
    {
        "version": "7.14.0",
        "code": "20151314"
    },
    {
        "version": "7.14.0",
        "code": "20151320"
    },
    {
        "version": "7.15.0",
        "code": "20543579"
    },
    {
        "version": "7.15.0",
        "code": "20660854"
    },
    {
        "version": "7.15.0",
        "code": "20770943"
    },
    {
        "version": "7.15.0",
        "code": "20808502"
    },
    {
        "version": "7.15.0",
        "code": "20808504"
    },
    {
        "version": "7.16.0",
        "code": "21388836"
    },
    {
        "version": "7.16.0",
        "code": "21388876"
    },
    {
        "version": "7.16.0",
        "code": "21578176"
    },
    {
        "version": "7.16.0",
        "code": "21966528"
    },
    {
        "version": "7.16.0",
        "code": "22038485"
    },
    {
        "version": "7.17.0",
        "code": "23162604"
    },
    {
        "version": "7.17.0",
        "code": "23265084"
    },
    {
        "version": "7.17.0",
        "code": "23322199"
    },
    {
        "version": "7.17.0",
        "code": "23322206"
    },
    {
        "version": "7.18.0",
        "code": "24086480"
    },
    {
        "version": "7.18.0",
        "code": "24302095"
    },
    {
        "version": "7.18.0",
        "code": "24595347"
    },
    {
        "version": "7.18.0",
        "code": "24809118"
    },
    {
        "version": "7.18.0",
        "code": "24863788"
    },
    {
        "version": "7.18.1",
        "code": "25055364"
    },
    {
        "version": "7.18.2",
        "code": "25119635"
    },
    {
        "version": "7.18.2",
        "code": "25119636"
    },
    {
        "version": "7.19.0",
        "code": "25297122"
    },
    {
        "version": "7.19.0",
        "code": "25297129"
    },
    {
        "version": "7.19.0",
        "code": "25453447"
    },
    {
        "version": "7.19.0",
        "code": "25704759"
    },
    {
        "version": "7.19.0",
        "code": "25704772"
    },
    {
        "version": "7.19.0",
        "code": "25872807"
    },
    {
        "version": "7.19.0",
        "code": "25936825"
    },
    {
        "version": "7.19.1",
        "code": "26404397"
    },
    {
        "version": "7.19.1",
        "code": "26404404"
    },
    {
        "version": "7.20.0",
        "code": "26443138"
    },
    {
        "version": "7.20.0",
        "code": "26681339"
    },
    {
        "version": "7.20.0",
        "code": "26875547"
    },
    {
        "version": "7.20.0",
        "code": "27025861"
    },
    {
        "version": "7.20.0",
        "code": "27037564"
    },
    {
        "version": "7.20.0",
        "code": "27105654"
    },
    {
        "version": "8.0.0",
        "code": "27630442"
    },
    {
        "version": "8.0.0",
        "code": "27923403"
    },
    {
        "version": "8.0.0",
        "code": "27923434"
    },
    {
        "version": "7.21.0",
        "code": "28414909"
    },
    {
        "version": "7.21.0",
        "code": "28414923"
    },
    {
        "version": "7.21.1",
        "code": "28735170"
    },
    {
        "version": "7.22.0",
        "code": "28741243"
    },
    {
        "version": "7.22.0",
        "code": "28902140"
    },
    {
        "version": "7.22.0",
        "code": "29136038"
    },
    {
        "version": "8.0.0",
        "code": "29687306"
    },
    {
        "version": "8.0.0",
        "code": "29687307"
    },
    {
        "version": "8.0.0",
        "code": "29687308"
    },
    {
        "version": "8.0.0",
        "code": "29687309"
    },
    {
        "version": "8.1.0",
        "code": "30051248"
    },
    {
        "version": "8.1.0",
        "code": "30064543"
    },
    {
        "version": "8.1.0",
        "code": "30122962"
    },
    {
        "version": "8.1.0",
        "code": "30278352"
    },
    {
        "version": "8.1.0",
        "code": "30278354"
    },
    {
        "version": "8.2.0",
        "code": "30538609"
    },
    {
        "version": "8.2.0",
        "code": "30706772"
    },
    {
        "version": "8.2.0",
        "code": "30903420"
    },
    {
        "version": "8.2.0",
        "code": "30992010"
    },
    {
        "version": "8.2.0",
        "code": "30992015"
    },
    {
        "version": "8.2.0",
        "code": "30992021"
    },
    {
        "version": "8.3.0",
        "code": "31441110"
    },
    {
        "version": "8.3.0",
        "code": "31606904"
    },
    {
        "version": "8.3.0",
        "code": "31896301"
    },
    {
        "version": "8.3.0",
        "code": "31938068"
    },
    {
        "version": "8.4.0",
        "code": "32405865"
    },
    {
        "version": "8.4.0",
        "code": "32673414"
    },
    {
        "version": "8.4.0",
        "code": "32821114"
    },
    {
        "version": "8.4.0",
        "code": "32875821"
    },
    {
        "version": "8.4.0",
        "code": "32875826"
    },
    {
        "version": "8.4.0",
        "code": "32875829"
    },
    {
        "version": "8.4.0",
        "code": "32875831"
    },
    {
        "version": "8.5.0",
        "code": "33361487"
    },
    {
        "version": "8.5.0",
        "code": "33516302"
    },
    {
        "version": "8.5.0",
        "code": "33696654"
    },
    {
        "version": "8.5.0",
        "code": "33737790"
    },
    {
        "version": "8.5.1",
        "code": "33918520"
    },
    {
        "version": "8.5.1",
        "code": "33918522"
    },
    {
        "version": "8.5.1",
        "code": "33918523"
    },
    {
        "version": "8.5.1",
        "code": "33918528"
    },
    {
        "version": "8.5.1",
        "code": "33918531"
    },
    {
        "version": "9.0.0",
        "code": "34525903"
    },
    {
        "version": "9.0.0",
        "code": "34814732"
    },
    {
        "version": "9.0.0",
        "code": "34840905"
    },
    {
        "version": "9.0.0",
        "code": "34920046"
    },
    {
        "version": "9.0.0",
        "code": "34920050"
    },
    {
        "version": "9.0.0",
        "code": "35221413"
    },
    {
        "version": "9.0.0",
        "code": "35221427"
    },
    {
        "version": "9.0.0",
        "code": "35221453"
    },
    {
        "version": "9.1.0",
        "code": "35367610"
    },
    {
        "version": "9.0.1",
        "code": "35440028"
    },
    {
        "version": "9.0.1",
        "code": "35440030"
    },
    {
        "version": "9.0.1",
        "code": "35440031"
    },
    {
        "version": "9.0.1",
        "code": "35440032"
    },
    {
        "version": "9.0.1",
        "code": "35440033"
    },
    {
        "version": "9.1.0",
        "code": "35469529"
    },
    {
        "version": "9.1.0",
        "code": "35686917"
    },
    {
        "version": "9.1.0",
        "code": "35795937"
    },
    {
        "version": "9.1.0",
        "code": "35795940"
    },
    {
        "version": "9.1.5",
        "code": "35935469"
    },
    {
        "version": "9.1.5",
        "code": "36302796"
    },
    {
        "version": "9.1.5",
        "code": "36425083"
    },
    {
        "version": "9.2.0",
        "code": "36507662"
    },
    {
        "version": "9.1.5",
        "code": "36531351"
    },
    {
        "version": "9.1.5",
        "code": "36531355"
    },
    {
        "version": "9.1.5",
        "code": "36531359"
    },
    {
        "version": "9.1.5",
        "code": "36531364"
    },
    {
        "version": "9.1.5",
        "code": "36531368"
    },
    {
        "version": "9.2.0",
        "code": "36656231"
    },
    {
        "version": "9.2.0",
        "code": "36751260"
    },
    {
        "version": "9.2.0",
        "code": "36903624"
    },
    {
        "version": "9.2.0",
        "code": "37023764"
    },
    {
        "version": "9.2.0",
        "code": "37023765"
    },
    {
        "version": "9.2.0",
        "code": "37023766"
    },
    {
        "version": "9.2.0",
        "code": "37023767"
    },
    {
        "version": "9.2.5",
        "code": "37108327"
    },
    {
        "version": "9.2.5",
        "code": "37331386"
    },
    {
        "version": "9.2.5",
        "code": "37581779"
    },
    {
        "version": "9.2.5",
        "code": "37581798"
    },
    {
        "version": "9.2.5",
        "code": "37581809"
    },
    {
        "version": "9.2.5",
        "code": "37581824"
    },
    {
        "version": "9.2.5",
        "code": "37734551"
    },
    {
        "version": "9.2.5",
        "code": "37734553"
    },
    {
        "version": "9.2.5",
        "code": "37734555"
    },
    {
        "version": "9.2.5",
        "code": "37734557"
    },
    {
        "version": "9.2.5",
        "code": "37734562"
    },
    {
        "version": "9.3.5",
        "code": "38334689"
    },
    {
        "version": "9.3.5",
        "code": "38484906"
    },
    {
        "version": "9.3.5",
        "code": "38612508"
    },
    {
        "version": "9.3.5",
        "code": "38802257"
    },
    {
        "version": "9.3.5",
        "code": "38802274"
    },
    {
        "version": "9.3.5",
        "code": "38802287"
    },
    {
        "version": "9.3.5",
        "code": "38802302"
    },
    {
        "version": "9.3.5",
        "code": "38802318"
    },
    {
        "version": "9.4.0",
        "code": "38922625"
    },
    {
        "version": "9.4.0",
        "code": "39213970"
    },
    {
        "version": "9.4.0",
        "code": "39432129"
    },
    {
        "version": "9.4.0",
        "code": "39471614"
    },
    {
        "version": "9.4.0",
        "code": "39471620"
    },
    {
        "version": "9.4.0",
        "code": "39471625"
    },
    {
        "version": "9.4.0",
        "code": "39471633"
    },
    {
        "version": "9.4.0",
        "code": "39471643"
    },
    {
        "version": "9.4.5",
        "code": "39617613"
    },
    {
        "version": "9.4.5",
        "code": "40012791"
    },
    {
        "version": "9.4.5",
        "code": "40012799"
    },
    {
        "version": "9.4.5",
        "code": "40012805"
    },
    {
        "version": "9.4.5",
        "code": "40012815"
    },
    {
        "version": "9.4.5",
        "code": "40012823"
    },
    {
        "version": "9.5.0",
        "code": "40103626"
    },
    {
        "version": "9.4.5",
        "code": "40190548"
    },
    {
        "version": "9.4.5",
        "code": "40190549"
    },
    {
        "version": "9.4.5",
        "code": "40190551"
    },
    {
        "version": "9.4.5",
        "code": "40190552"
    },
    {
        "version": "9.4.5",
        "code": "40190553"
    },
    {
        "version": "9.5.0",
        "code": "40515338"
    },
    {
        "version": "9.5.0",
        "code": "40619016"
    },
    {
        "version": "9.5.5",
        "code": "40758520"
    },
    {
        "version": "9.5.0",
        "code": "40714450"
    },
    {
        "version": "9.5.0",
        "code": "40714452"
    },
    {
        "version": "9.5.0",
        "code": "40714453"
    },
    {
        "version": "9.5.0",
        "code": "40714455"
    },
    {
        "version": "9.5.0",
        "code": "40714457"
    },
    {
        "version": "9.5.5",
        "code": "40849471"
    },
    {
        "version": "9.5.5",
        "code": "41032480"
    },
    {
        "version": "9.5.5",
        "code": "41194573"
    },
    {
        "version": "9.5.5",
        "code": "41194580"
    },
    {
        "version": "9.5.5",
        "code": "41194594"
    },
    {
        "version": "9.5.5",
        "code": "41194600"
    },
    {
        "version": "9.5.5",
        "code": "41194607"
    },
    {
        "version": "9.6.0",
        "code": "41377320"
    },
    {
        "version": "9.6.0",
        "code": "41567516"
    },
    {
        "version": "9.6.0",
        "code": "41774323"
    },
    {
        "version": "9.6.0",
        "code": "41774332"
    },
    {
        "version": "9.6.0",
        "code": "41774345"
    },
    {
        "version": "9.6.0",
        "code": "41774362"
    },
    {
        "version": "9.6.0",
        "code": "41774376"
    },
    {
        "version": "9.6.5",
        "code": "41972110"
    },
    {
        "version": "9.6.6",
        "code": "42208365"
    },
    {
        "version": "9.6.6",
        "code": "42286962"
    },
    {
        "version": "9.6.6",
        "code": "42286970"
    },
    {
        "version": "9.6.6",
        "code": "42286974"
    },
    {
        "version": "9.6.6",
        "code": "42286977"
    },
    {
        "version": "9.6.6",
        "code": "42286981"
    },
    {
        "version": "9.7.0",
        "code": "42365116"
    },
    {
        "version": "9.7.0",
        "code": "42447991"
    },
    {
        "version": "9.6.7",
        "code": "42539520"
    },
    {
        "version": "9.6.7",
        "code": "42539538"
    },
    {
        "version": "9.6.7",
        "code": "42539549"
    },
    {
        "version": "9.6.7",
        "code": "42539553"
    },
    {
        "version": "9.6.7",
        "code": "42539561"
    },
    {
        "version": "9.7.0",
        "code": "42643097"
    },
    {
        "version": "9.7.0",
        "code": "42643116"
    },
    {
        "version": "9.7.5",
        "code": "42871859"
    },
    {
        "version": "9.7.0",
        "code": "42797737"
    },
    {
        "version": "9.7.0",
        "code": "42797741"
    },
    {
        "version": "9.7.0",
        "code": "42797743"
    },
    {
        "version": "9.7.0",
        "code": "42797747"
    },
    {
        "version": "9.7.0",
        "code": "42797748"
    },
    {
        "version": "9.7.5",
        "code": "43080327"
    },
    {
        "version": "9.7.5",
        "code": "43298789"
    },
    {
        "version": "9.7.5",
        "code": "43298790"
    },
    {
        "version": "9.7.5",
        "code": "43298791"
    },
    {
        "version": "9.7.5",
        "code": "43298793"
    },
    {
        "version": "9.7.5",
        "code": "43298795"
    },
    {
        "version": "9.8.0",
        "code": "43510707"
    },
    {
        "version": "9.8.0",
        "code": "43510715"
    },
    {
        "version": "9.8.0",
        "code": "43604896"
    },
    {
        "version": "9.8.0",
        "code": "43604907"
    },
    {
        "version": "9.8.0",
        "code": "43704314"
    },
    {
        "version": "9.8.0",
        "code": "43704318"
    },
    {
        "version": "9.8.0",
        "code": "43917443"
    },
    {
        "version": "9.8.0",
        "code": "43917444"
    },
    {
        "version": "9.8.0",
        "code": "43917446"
    },
    {
        "version": "9.8.0",
        "code": "43917447"
    },
    {
        "version": "9.8.0",
        "code": "43917449"
    },
    {
        "version": "9.8.5",
        "code": "44104157"
    },
    {
        "version": "9.8.5",
        "code": "44149188"
    },
    {
        "version": "9.8.5",
        "code": "44222990"
    },
    {
        "version": "9.8.5",
        "code": "44223008"
    },
    {
        "version": "10.0.0",
        "code": "44319907"
    },
    {
        "version": "10.0.0",
        "code": "44319910"
    },
    {
        "version": "10.0.0",
        "code": "44319911"
    },
    {
        "version": "10.0.0",
        "code": "44319915"
    },
    {
        "version": "10.0.0",
        "code": "44319920"
    },
    {
        "version": "10.0.1",
        "code": "44361668"
    },
    {
        "version": "10.0.1",
        "code": "44361672"
    },
    {
        "version": "10.0.1",
        "code": "44361676"
    },
    {
        "version": "10.0.1",
        "code": "44361680"
    },
    {
        "version": "10.0.1",
        "code": "44361682"
    },
    {
        "version": "10.1.0",
        "code": "44497026"
    },
    {
        "version": "10.1.0",
        "code": "44497027"
    },
    {
        "version": "10.1.0",
        "code": "44770801"
    },
    {
        "version": "10.1.0",
        "code": "44770804"
    },
    {
        "version": "10.1.0",
        "code": "44934675"
    },
    {
        "version": "10.1.0",
        "code": "44934691"
    },
    {
        "version": "10.1.0",
        "code": "45007214"
    },
    {
        "version": "10.1.0",
        "code": "45007216"
    },
    {
        "version": "10.1.0",
        "code": "45007217"
    },
    {
        "version": "10.1.0",
        "code": "45007218"
    },
    {
        "version": "10.1.0",
        "code": "45007220"
    },
    {
        "version": "10.2.0",
        "code": "45437335"
    },
    {
        "version": "10.2.0",
        "code": "45437336"
    },
    {
        "version": "10.2.0",
        "code": "45601630"
    },
    {
        "version": "10.2.0",
        "code": "45601632"
    },
    {
        "version": "10.2.0",
        "code": "45798832"
    },
    {
        "version": "10.2.0",
        "code": "45798835"
    },
    {
        "version": "10.2.0",
        "code": "45798836"
    },
    {
        "version": "10.2.0",
        "code": "45798839"
    },
    {
        "version": "10.2.1",
        "code": "45907261"
    },
    {
        "version": "10.2.1",
        "code": "45907267"
    },
    {
        "version": "10.2.1",
        "code": "45907273"
    },
    {
        "version": "10.2.1",
        "code": "45907284"
    },
    {
        "version": "10.2.1",
        "code": "45907288"
    },
    {
        "version": "10.3.1",
        "code": "46341238"
    },
    {
        "version": "10.3.1",
        "code": "46341239"
    },
    {
        "version": "10.3.1",
        "code": "46341240"
    },
    {
        "version": "10.3.1",
        "code": "46341241"
    },
    {
        "version": "10.3.1",
        "code": "46341242"
    },
    {
        "version": "10.3.2",
        "code": "46395470"
    },
    {
        "version": "10.3.2",
        "code": "46395471"
    },
    {
        "version": "10.3.2",
        "code": "46395472"
    },
    {
        "version": "10.3.2",
        "code": "46395473"
    },
    {
        "version": "10.3.2",
        "code": "46395474"
    },
    {
        "version": "10.4.0",
        "code": "47206831"
    },
    {
        "version": "10.4.0",
        "code": "47206840"
    },
    {
        "version": "10.4.0",
        "code": "47395669"
    },
    {
        "version": "10.4.0",
        "code": "47395670"
    },
    {
        "version": "10.4.0",
        "code": "47718693"
    },
    {
        "version": "10.4.0",
        "code": "47718694"
    },
    {
        "version": "10.4.0",
        "code": "47718695"
    },
    {
        "version": "10.4.0",
        "code": "47718697"
    },
    {
        "version": "10.4.0",
        "code": "47718698"
    },
    {
        "version": "10.5.0",
        "code": "47743792"
    },
    {
        "version": "10.5.0",
        "code": "47743794"
    },
    {
        "version": "10.5.0",
        "code": "47884297"
    },
    {
        "version": "10.5.0",
        "code": "47884298"
    },
    {
        "version": "10.5.0",
        "code": "47997334"
    },
    {
        "version": "10.5.0",
        "code": "47997341"
    },
    {
        "version": "10.5.0",
        "code": "48149419"
    },
    {
        "version": "10.5.0",
        "code": "48149423"
    },
    {
        "version": "10.5.0",
        "code": "48149427"
    },
    {
        "version": "10.6.0",
        "code": "48258064"
    },
    {
        "version": "10.6.0",
        "code": "48258070"
    },
    {
        "version": "10.5.1",
        "code": "48243304"
    },
    {
        "version": "10.5.1",
        "code": "48243312"
    },
    {
        "version": "10.5.1",
        "code": "48243317"
    },
    {
        "version": "10.5.1",
        "code": "48243321"
    },
    {
        "version": "10.5.1",
        "code": "48243323"
    },
    {
        "version": "10.7.0",
        "code": "48743563"
    },
    {
        "version": "10.7.0",
        "code": "48743568"
    },
    {
        "version": "10.6.0",
        "code": "48697431"
    },
    {
        "version": "10.6.0",
        "code": "48697435"
    },
    {
        "version": "10.6.0",
        "code": "48697436"
    },
    {
        "version": "10.6.0",
        "code": "48697439"
    },
    {
        "version": "10.6.0",
        "code": "48697441"
    },
    {
        "version": "10.7.0",
        "code": "48891032"
    },
    {
        "version": "10.7.0",
        "code": "48891034"
    },
    {
        "version": "10.7.0",
        "code": "49080654"
    },
    {
        "version": "10.7.0",
        "code": "49080656"
    },
    {
        "version": "10.7.0",
        "code": "49254538"
    },
    {
        "version": "10.7.0",
        "code": "49254549"
    },
    {
        "version": "10.7.0",
        "code": "49254554"
    },
    {
        "version": "10.7.0",
        "code": "49254558"
    },
    {
        "version": "10.7.0",
        "code": "49400166"
    },
    {
        "version": "10.7.0",
        "code": "49400167"
    },
    {
        "version": "10.7.0",
        "code": "49400168"
    },
    {
        "version": "10.7.0",
        "code": "49400170"
    },
    {
        "version": "10.7.0",
        "code": "49400171"
    },
    {
        "version": "10.8.0",
        "code": "49403860"
    },
    {
        "version": "10.8.0",
        "code": "49403864"
    },
    {
        "version": "10.8.0",
        "code": "49510731"
    },
    {
        "version": "10.8.0",
        "code": "49510733"
    },
    {
        "version": "10.8.0",
        "code": "49708876"
    },
    {
        "version": "10.8.0",
        "code": "49708877"
    },
    {
        "version": "10.8.0",
        "code": "49833220"
    },
    {
        "version": "10.8.0",
        "code": "49833230"
    },
    {
        "version": "10.10.0",
        "code": "50548149"
    },
    {
        "version": "10.10.0",
        "code": "50548168"
    },
    {
        "version": "10.10.0",
        "code": "50790484"
    },
    {
        "version": "10.10.0",
        "code": "50790487"
    },
    {
        "version": "10.10.0",
        "code": "50984356"
    },
    {
        "version": "10.10.0",
        "code": "50984359"
    },
    {
        "version": "10.10.0",
        "code": "50984364"
    },
    {
        "version": "10.10.0",
        "code": "50984366"
    },
    {
        "version": "10.10.0",
        "code": "50984369"
    },
    {
        "version": "10.11.0",
        "code": "51083247"
    },
    {
        "version": "10.11.0",
        "code": "51083248"
    },
    {
        "version": "10.11.0",
        "code": "51205381"
    },
    {
        "version": "10.11.0",
        "code": "51205384"
    },
    {
        "version": "10.11.0",
        "code": "51519100"
    },
    {
        "version": "10.11.0",
        "code": "51519101"
    },
    {
        "version": "10.11.0",
        "code": "51631979"
    },
    {
        "version": "10.11.0",
        "code": "51631980"
    },
    {
        "version": "10.11.0",
        "code": "51631981"
    },
    {
        "version": "10.11.0",
        "code": "51631982"
    },
    {
        "version": "10.11.0",
        "code": "51631983"
    },
    {
        "version": "10.12.0",
        "code": "51780259"
    },
    {
        "version": "10.12.0",
        "code": "51780265"
    },
    {
        "version": "10.12.0",
        "code": "52328590"
    },
    {
        "version": "10.12.0",
        "code": "52328593"
    },
    {
        "version": "10.12.0",
        "code": "52418251"
    },
    {
        "version": "10.12.0",
        "code": "52418252"
    },
    {
        "version": "10.12.0",
        "code": "52418253"
    },
    {
        "version": "10.12.0",
        "code": "52418254"
    },
    {
        "version": "10.12.0",
        "code": "52418256"
    },
    {
        "version": "10.13.0",
        "code": "52629400"
    },
    {
        "version": "10.13.0",
        "code": "52629403"
    },
    {
        "version": "10.13.0",
        "code": "52858524"
    },
    {
        "version": "10.13.0",
        "code": "52858527"
    },
    {
        "version": "10.13.0",
        "code": "53070968"
    },
    {
        "version": "10.13.0",
        "code": "53070969"
    },
    {
        "version": "10.13.0",
        "code": "53070973"
    },
    {
        "version": "10.13.0",
        "code": "53070974"
    },
    {
        "version": "10.13.0",
        "code": "53070975"
    },
    {
        "version": "10.14.0",
        "code": "53199629"
    },
    {
        "version": "10.14.0",
        "code": "53199630"
    },
    {
        "version": "10.14.0",
        "code": "53676094"
    },
    {
        "version": "10.14.0",
        "code": "53676095"
    },
    {
        "version": "10.14.0",
        "code": "53734041"
    },
    {
        "version": "10.14.0",
        "code": "53734042"
    },
    {
        "version": "10.14.0",
        "code": "53734043"
    },
    {
        "version": "10.14.0",
        "code": "53734044"
    },
    {
        "version": "10.14.0",
        "code": "53734045"
    },
    {
        "version": "10.15.0",
        "code": "53863829"
    },
    {
        "version": "10.15.0",
        "code": "53863830"
    },
    {
        "version": "10.15.0",
        "code": "53997300"
    },
    {
        "version": "10.15.0",
        "code": "53997343"
    },
    {
        "version": "10.15.0",
        "code": "54119071"
    },
    {
        "version": "10.15.0",
        "code": "54119096"
    },
    {
        "version": "10.15.0",
        "code": "54375389"
    },
    {
        "version": "10.15.0",
        "code": "54375392"
    },
    {
        "version": "10.15.0",
        "code": "54375395"
    },
    {
        "version": "10.15.0",
        "code": "54375396"
    },
    {
        "version": "10.15.0",
        "code": "54375399"
    },
    {
        "version": "10.17.0",
        "code": "55090834"
    },
    {
        "version": "10.17.0",
        "code": "55090838"
    },
    {
        "version": "10.16.1",
        "code": "55125670"
    },
    {
        "version": "10.16.1",
        "code": "55125673"
    },
    {
        "version": "10.16.1",
        "code": "55125674"
    },
    {
        "version": "10.16.1",
        "code": "55125676"
    },
    {
        "version": "10.16.1",
        "code": "55125678"
    },
    {
        "version": "10.17.0",
        "code": "55285007"
    },
    {
        "version": "10.17.0",
        "code": "55285008"
    },
    {
        "version": "10.18.0",
        "code": "55548043"
    },
    {
        "version": "10.18.0",
        "code": "55548048"
    },
    {
        "version": "10.18.0",
        "code": "55692557"
    },
    {
        "version": "10.18.0",
        "code": "55692558"
    },
    {
        "version": "10.17.0",
        "code": "55521848"
    },
    {
        "version": "10.17.0",
        "code": "55521855"
    },
    {
        "version": "10.17.0",
        "code": "55521859"
    },
    {
        "version": "10.17.0",
        "code": "55521864"
    },
    {
        "version": "10.17.0",
        "code": "55521867"
    },
    {
        "version": "10.18.0",
        "code": "55835624"
    },
    {
        "version": "10.18.0",
        "code": "55835627"
    },
    {
        "version": "10.18.0",
        "code": "56145866"
    },
    {
        "version": "10.18.0",
        "code": "56145872"
    },
    {
        "version": "10.18.0",
        "code": "56145876"
    },
    {
        "version": "10.18.0",
        "code": "56145882"
    },
    {
        "version": "10.18.0",
        "code": "56145885"
    },
    {
        "version": "10.19.0",
        "code": "56213387"
    },
    {
        "version": "10.19.0",
        "code": "56213388"
    },
    {
        "version": "10.19.0",
        "code": "56443993"
    },
    {
        "version": "10.19.0",
        "code": "56443995"
    },
    {
        "version": "10.20.0",
        "code": "56912606"
    },
    {
        "version": "10.20.0",
        "code": "56912623"
    },
    {
        "version": "10.19.0",
        "code": "56878869"
    },
    {
        "version": "10.19.0",
        "code": "56878870"
    },
    {
        "version": "10.19.0",
        "code": "56878872"
    },
    {
        "version": "10.19.0",
        "code": "56878873"
    },
    {
        "version": "10.19.0",
        "code": "56878874"
    },
    {
        "version": "10.20.0",
        "code": "57156154"
    },
    {
        "version": "10.19.1",
        "code": "57202585"
    },
    {
        "version": "10.19.1",
        "code": "57202587"
    },
    {
        "version": "10.19.1",
        "code": "57202589"
    },
    {
        "version": "10.19.1",
        "code": "57202593"
    },
    {
        "version": "10.19.1",
        "code": "57202594"
    },
    {
        "version": "10.20.0",
        "code": "57282578"
    },
    {
        "version": "10.20.0",
        "code": "57635236"
    },
    {
        "version": "10.20.0",
        "code": "57635237"
    },
    {
        "version": "10.20.0",
        "code": "57635239"
    },
    {
        "version": "10.20.0",
        "code": "57635240"
    },
    {
        "version": "10.20.0",
        "code": "57635242"
    },
    {
        "version": "10.21.0",
        "code": "57657864"
    },
    {
        "version": "10.21.0",
        "code": "57657867"
    },
    {
        "version": "10.21.0",
        "code": "57734943"
    },
    {
        "version": "10.21.0",
        "code": "57734949"
    },
    {
        "version": "10.21.0",
        "code": "57869439"
    },
    {
        "version": "10.20.0",
        "code": "57944455"
    },
    {
        "version": "10.20.0",
        "code": "57944458"
    },
    {
        "version": "10.20.0",
        "code": "57944460"
    },
    {
        "version": "10.20.0",
        "code": "57944461"
    },
    {
        "version": "10.20.0",
        "code": "57944462"
    },
    {
        "version": "10.21.0",
        "code": "58100880"
    },
    {
        "version": "10.21.0",
        "code": "58213091"
    },
    {
        "version": "10.21.0",
        "code": "58256051"
    },
    {
        "version": "10.21.0",
        "code": "58302827"
    },
    {
        "version": "10.21.0",
        "code": "58302830"
    },
    {
        "version": "10.21.0",
        "code": "58302835"
    },
    {
        "version": "10.21.0",
        "code": "58302845"
    },
    {
        "version": "10.21.0",
        "code": "58302850"
    },
    {
        "version": "10.22.0",
        "code": "58304237"
    },
    {
        "version": "10.22.0",
        "code": "58357921"
    },
    {
        "version": "10.22.0",
        "code": "58532222"
    },
    {
        "version": "10.22.0",
        "code": "58532223"
    },
    {
        "version": "10.22.0",
        "code": "58775268"
    },
    {
        "version": "10.23.0",
        "code": "58962121"
    },
    {
        "version": "10.23.0",
        "code": "58962122"
    },
    {
        "version": "10.22.0",
        "code": "58956666"
    },
    {
        "version": "10.22.0",
        "code": "58956671"
    },
    {
        "version": "10.22.0",
        "code": "58956676"
    },
    {
        "version": "10.22.0",
        "code": "58956681"
    },
    {
        "version": "10.22.0",
        "code": "58956686"
    },
    {
        "version": "10.23.0",
        "code": "59181096"
    },
    {
        "version": "10.23.0",
        "code": "59181101"
    },
    {
        "version": "10.23.0",
        "code": "59451976"
    },
    {
        "version": "10.23.0",
        "code": "59451977"
    },
    {
        "version": "10.23.0",
        "code": "59820928"
    },
    {
        "version": "10.23.0",
        "code": "59820929"
    },
    {
        "version": "10.23.0",
        "code": "59820930"
    },
    {
        "version": "10.23.0",
        "code": "59820931"
    },
    {
        "version": "10.23.0",
        "code": "59820932"
    },
    {
        "version": "10.24.0",
        "code": "59839734"
    },
    {
        "version": "10.24.0",
        "code": "59839740"
    },
    {
        "version": "10.24.0",
        "code": "60173967"
    },
    {
        "version": "10.24.0",
        "code": "60173968"
    },
    {
        "version": "10.24.0",
        "code": "60335755"
    },
    {
        "version": "10.24.0",
        "code": "60335756"
    },
    {
        "version": "10.24.0",
        "code": "60335757"
    },
    {
        "version": "10.24.0",
        "code": "60335759"
    },
    {
        "version": "10.24.0",
        "code": "60335760"
    },
    {
        "version": "10.25.0",
        "code": "60531488"
    },
    {
        "version": "10.25.0",
        "code": "60531492"
    },
    {
        "version": "10.25.0",
        "code": "60813718"
    },
    {
        "version": "10.25.0",
        "code": "60813721"
    },
    {
        "version": "10.25.0",
        "code": "61294052"
    },
    {
        "version": "10.25.0",
        "code": "61294066"
    },
    {
        "version": "10.25.0",
        "code": "61294071"
    },
    {
        "version": "10.25.0",
        "code": "61294077"
    },
    {
        "version": "10.25.1",
        "code": "61475277"
    },
    {
        "version": "10.25.1",
        "code": "61475280"
    },
    {
        "version": "10.25.1",
        "code": "61475288"
    },
    {
        "version": "10.25.1",
        "code": "61475291"
    },
    {
        "version": "10.25.1",
        "code": "61475296"
    },
    {
        "version": "10.26.0",
        "code": "61586286"
    },
    {
        "version": "10.26.0",
        "code": "61586287"
    },
    {
        "version": "10.26.0",
        "code": "61947337"
    },
    {
        "version": "10.26.0",
        "code": "61947338"
    },
    {
        "version": "10.26.0",
        "code": "62257637"
    },
    {
        "version": "10.26.0",
        "code": "62257640"
    },
    {
        "version": "10.26.0",
        "code": "62257644"
    },
    {
        "version": "10.26.0",
        "code": "62257646"
    },
    {
        "version": "10.26.0",
        "code": "62257650"
    },
    {
        "version": "10.27.0",
        "code": "62259341"
    },
    {
        "version": "10.27.0",
        "code": "62259359"
    },
    {
        "version": "10.27.0",
        "code": "62642849"
    },
    {
        "version": "10.27.0",
        "code": "62642853"
    },
    {
        "version": "10.27.0",
        "code": "63111915"
    },
    {
        "version": "10.27.0",
        "code": "63111925"
    },
    {
        "version": "10.27.0",
        "code": "63251605"
    },
    {
        "version": "10.27.0",
        "code": "63251606"
    },
    {
        "version": "10.27.0",
        "code": "63251608"
    },
    {
        "version": "10.27.0",
        "code": "63251609"
    },
    {
        "version": "10.28.0",
        "code": "63419392"
    },
    {
        "version": "10.28.0",
        "code": "63419393"
    },
    {
        "version": "10.27.1",
        "code": "63323422"
    },
    {
        "version": "10.27.1",
        "code": "63323428"
    },
    {
        "version": "10.27.1",
        "code": "63323436"
    },
    {
        "version": "10.27.1",
        "code": "63323440"
    },
    {
        "version": "10.27.1",
        "code": "63323444"
    },
    {
        "version": "10.28.0",
        "code": "63594885"
    },
    {
        "version": "10.28.0",
        "code": "63594893"
    },
    {
        "version": "10.28.0",
        "code": "63904419"
    },
    {
        "version": "10.28.0",
        "code": "63904426"
    },
    {
        "version": "10.29.0",
        "code": "64175345"
    },
    {
        "version": "10.29.0",
        "code": "64175358"
    },
    {
        "version": "10.28.0",
        "code": "64172492"
    },
    {
        "version": "10.28.0",
        "code": "64172494"
    },
    {
        "version": "10.28.0",
        "code": "64172495"
    },
    {
        "version": "10.28.0",
        "code": "64172496"
    },
    {
        "version": "10.29.0",
        "code": "64311028"
    },
    {
        "version": "10.29.0",
        "code": "64311032"
    },
    {
        "version": "10.29.0",
        "code": "64549041"
    },
    {
        "version": "10.29.0",
        "code": "64549042"
    },
    {
        "version": "10.30.0",
        "code": "64667761"
    },
    {
        "version": "10.30.0",
        "code": "64667765"
    },
    {
        "version": "10.29.0",
        "code": "64630924"
    },
    {
        "version": "10.29.0",
        "code": "64630925"
    },
    {
        "version": "10.29.0",
        "code": "64630926"
    },
    {
        "version": "10.29.0",
        "code": "64630927"
    },
    {
        "version": "10.29.0",
        "code": "64630928"
    },
    {
        "version": "10.30.0",
        "code": "64866812"
    },
    {
        "version": "10.30.0",
        "code": "64866813"
    },
    {
        "version": "10.30.0",
        "code": "65118902"
    },
    {
        "version": "10.30.0",
        "code": "65118908"
    },
    {
        "version": "10.31.0",
        "code": "65305970"
    },
    {
        "version": "10.31.0",
        "code": "65305972"
    },
    {
        "version": "10.30.0",
        "code": "65303574"
    },
    {
        "version": "10.30.0",
        "code": "65303577"
    },
    {
        "version": "10.30.0",
        "code": "65303583"
    },
    {
        "version": "10.30.0",
        "code": "65303587"
    },
    {
        "version": "10.30.0",
        "code": "65303594"
    },
    {
        "version": "10.31.0",
        "code": "65633900"
    },
    {
        "version": "10.31.0",
        "code": "65633903"
    },
    {
        "version": "10.31.0",
        "code": "65804388"
    },
    {
        "version": "10.32.0",
        "code": "66029662"
    },
    {
        "version": "10.32.0",
        "code": "66029667"
    },
    {
        "version": "10.31.0",
        "code": "65992940"
    },
    {
        "version": "10.31.0",
        "code": "65992946"
    },
    {
        "version": "10.32.0",
        "code": "66264811"
    },
    {
        "version": "10.32.0",
        "code": "66264815"
    },
    {
        "version": "10.32.0",
        "code": "66468522"
    },
    {
        "version": "10.32.0",
        "code": "66468523"
    },
    {
        "version": "10.32.0",
        "code": "66699482"
    },
    {
        "version": "10.32.0",
        "code": "66699486"
    },
    {
        "version": "10.32.0",
        "code": "66699490"
    },
    {
        "version": "10.32.0",
        "code": "66699494"
    },
    {
        "version": "10.32.0",
        "code": "66699497"
    },
    {
        "version": "10.33.0",
        "code": "66749790"
    },
    {
        "version": "10.33.0",
        "code": "66749792"
    },
    {
        "version": "10.33.0",
        "code": "66983342"
    },
    {
        "version": "10.33.0",
        "code": "66983344"
    },
    {
        "version": "10.33.0",
        "code": "67304244"
    },
    {
        "version": "10.33.0",
        "code": "67410771"
    },
    {
        "version": "10.33.0",
        "code": "67410777"
    },
    {
        "version": "10.34.0",
        "code": "67463976"
    },
    {
        "version": "10.34.0",
        "code": "67463983"
    },
    {
        "version": "10.34.0",
        "code": "67697991"
    },
    {
        "version": "10.34.0",
        "code": "67697992"
    },
    {
        "version": "10.34.0",
        "code": "67963312"
    },
    {
        "version": "10.34.0",
        "code": "68173476"
    },
    {
        "version": "10.34.0",
        "code": "68173479"
    },
    {
        "version": "10.34.0",
        "code": "68173485"
    },
    {
        "version": "10.34.0",
        "code": "68173486"
    },
    {
        "version": "11.0.0.3.20",
        "code": "68521637"
    },
    {
        "version": "11.0.0.11.20",
        "code": "68850559"
    },
    {
        "version": "11.0.0.11.20",
        "code": "68850571"
    },
    {
        "version": "12.0.0.4.91",
        "code": "69460266"
    },
    {
        "version": "12.0.0.4.91",
        "code": "69460272"
    },
    {
        "version": "11.0.0.12.20",
        "code": "69139027"
    },
    {
        "version": "11.0.0.12.20",
        "code": "69139039"
    },
    {
        "version": "12.0.0.5.91",
        "code": "69724093"
    },
    {
        "version": "12.0.0.5.91",
        "code": "69724098"
    },
    {
        "version": "13.0.0.1.91",
        "code": "69989691"
    },
    {
        "version": "13.0.0.4.91",
        "code": "70301197"
    },
    {
        "version": "13.0.0.4.91",
        "code": "70301206"
    },
    {
        "version": "13.0.0.6.91",
        "code": "70565432"
    },
    {
        "version": "13.0.0.6.91",
        "code": "70565437"
    },
    {
        "version": "14.0.0.1.91",
        "code": "70866341"
    },
    {
        "version": "14.0.0.1.91",
        "code": "70866342"
    },
    {
        "version": "14.0.0.4.91",
        "code": "71023044"
    },
    {
        "version": "14.0.0.4.91",
        "code": "71023055"
    },
    {
        "version": "13.0.0.7.91",
        "code": "70864846"
    },
    {
        "version": "13.0.0.7.91",
        "code": "70864847"
    },
    {
        "version": "13.0.0.7.91",
        "code": "70864849"
    },
    {
        "version": "14.0.0.7.91",
        "code": "71313408"
    },
    {
        "version": "14.0.0.7.91",
        "code": "71313420"
    },
    {
        "version": "14.0.0.10.91",
        "code": "71607485"
    },
    {
        "version": "15.0.0.2.90",
        "code": "71609170"
    },
    {
        "version": "15.0.0.2.90",
        "code": "71609177"
    },
    {
        "version": "15.0.0.5.90",
        "code": "71869745"
    },
    {
        "version": "16.0.0.1.90",
        "code": "72230930"
    },
    {
        "version": "16.0.0.1.90",
        "code": "72230933"
    },
    {
        "version": "16.0.0.5.90",
        "code": "72555085"
    },
    {
        "version": "16.0.0.5.90",
        "code": "72555089"
    },
    {
        "version": "16.0.0.11.90",
        "code": "72975638"
    },
    {
        "version": "16.0.0.11.90",
        "code": "72975639"
    },
    {
        "version": "17.0.0.2.91",
        "code": "73135859"
    },
    {
        "version": "17.0.0.2.91",
        "code": "73135860"
    },
    {
        "version": "16.0.0.13.90",
        "code": "73134433"
    },
    {
        "version": "17.0.0.5.91",
        "code": "73424839"
    },
    {
        "version": "17.0.0.5.91",
        "code": "73424841"
    },
    {
        "version": "17.0.0.14.91",
        "code": "73754320"
    },
    {
        "version": "18.0.0.1.85",
        "code": "74019914"
    },
    {
        "version": "18.0.0.1.85",
        "code": "74019915"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998917"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998918"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998923"
    },
    {
        "version": "17.0.0.15.91",
        "code": "73998925"
    },
    {
        "version": "18.0.0.8.85",
        "code": "74316861"
    },
    {
        "version": "18.0.0.8.85",
        "code": "74316868"
    },
    {
        "version": "18.0.0.14.85",
        "code": "74588139"
    },
    {
        "version": "18.0.0.14.85",
        "code": "74588140"
    },
    {
        "version": "18.0.0.16.85",
        "code": "74766563"
    },
    {
        "version": "19.0.0.2.91",
        "code": "74850287"
    },
    {
        "version": "19.0.0.2.91",
        "code": "74850294"
    },
    {
        "version": "18.0.0.18.85",
        "code": "74848591"
    },
    {
        "version": "18.0.0.18.85",
        "code": "74848595"
    },
    {
        "version": "19.0.0.6.91",
        "code": "75154623"
    },
    {
        "version": "19.0.0.6.91",
        "code": "75154632"
    },
    {
        "version": "19.0.0.12.91",
        "code": "75440931"
    },
    {
        "version": "19.0.0.29.91",
        "code": "75739465"
    },
    {
        "version": "19.1.0.31.91",
        "code": "75767742"
    },
    {
        "version": "19.1.0.31.91",
        "code": "75767744"
    },
    {
        "version": "21.0.0.1.62",
        "code": "76769970"
    },
    {
        "version": "21.0.0.1.62",
        "code": "76769971"
    },
    {
        "version": "21.0.0.3.62",
        "code": "77131847"
    },
    {
        "version": "21.0.0.3.62",
        "code": "77131854"
    },
    {
        "version": "21.0.0.8.62",
        "code": "77472097"
    },
    {
        "version": "21.0.0.11.62",
        "code": "77790084"
    },
    {
        "version": "21.0.0.11.62",
        "code": "77790086"
    },
    {
        "version": "21.0.0.11.62",
        "code": "77790087"
    },
    {
        "version": "22.0.0.3.68",
        "code": "77973636"
    },
    {
        "version": "22.0.0.3.68",
        "code": "77973642"
    },
    {
        "version": "22.0.0.8.68",
        "code": "78246422"
    },
    {
        "version": "22.0.0.8.68",
        "code": "78246423"
    },
    {
        "version": "22.0.0.15.68",
        "code": "78610143"
    },
    {
        "version": "22.0.0.15.68",
        "code": "78610144"
    },
    {
        "version": "23.0.0.2.135",
        "code": "78983804"
    },
    {
        "version": "23.0.0.2.135",
        "code": "78983806"
    },
    {
        "version": "22.0.0.17.68",
        "code": "78982742"
    },
    {
        "version": "23.0.0.6.135",
        "code": "79369968"
    },
    {
        "version": "23.0.0.6.135",
        "code": "79369974"
    },
    {
        "version": "23.0.0.12.135",
        "code": "79757769"
    },
    {
        "version": "24.0.0.2.201",
        "code": "80132351"
    },
    {
        "version": "24.0.0.8.201",
        "code": "80489717"
    },
    {
        "version": "24.0.0.12.201",
        "code": "81140472"
    },
    {
        "version": "24.0.0.12.201",
        "code": "81140473"
    },
    {
        "version": "24.0.0.12.201",
        "code": "81140474"
    },
    {
        "version": "25.0.0.1.136",
        "code": "81947967"
    },
    {
        "version": "23.0.0.14.135",
        "code": "80125192"
    },
    {
        "version": "23.0.0.14.135",
        "code": "80125193"
    },
    {
        "version": "23.0.0.14.135",
        "code": "80125195"
    },
    {
        "version": "25.0.0.11.136",
        "code": "82293528"
    },
    {
        "version": "25.0.0.20.136",
        "code": "82660880"
    },
    {
        "version": "25.0.0.26.136",
        "code": "83072241"
    },
    {
        "version": "26.0.0.1.86",
        "code": "83085573"
    },
    {
        "version": "26.0.0.5.86",
        "code": "83486950"
    },
    {
        "version": "26.0.0.10.86",
        "code": "83827592"
    },
    {
        "version": "27.0.0.2.97",
        "code": "84125290"
    },
    {
        "version": "26.0.0.13.86",
        "code": "84116174"
    },
    {
        "version": "26.0.0.13.86",
        "code": "84116177"
    },
    {
        "version": "27.0.0.7.97",
        "code": "84433655"
    },
    {
        "version": "27.0.0.9.97",
        "code": "84725370"
    },
    {
        "version": "27.0.0.11.97",
        "code": "84946932"
    },
    {
        "version": "28.0.0.2.284",
        "code": "86924497"
    },
    {
        "version": "28.0.0.2.284",
        "code": "86924501"
    },
    {
        "version": "28.0.0.6.284",
        "code": "87350500"
    },
    {
        "version": "28.0.0.7.284",
        "code": "87568511"
    },
    {
        "version": "28.0.0.7.284",
        "code": "87949185"
    },
    {
        "version": "28.0.0.7.284",
        "code": "87949189"
    },
    {
        "version": "29.0.0.1.95",
        "code": "87956739"
    },
    {
        "version": "29.0.0.3.95",
        "code": "88139205"
    },
    {
        "version": "29.0.0.7.95",
        "code": "88511992"
    },
    {
        "version": "29.0.0.13.95",
        "code": "88934931"
    },
    {
        "version": "30.0.0.1.95",
        "code": "88948234"
    },
    {
        "version": "30.0.0.5.95",
        "code": "89272429"
    },
    {
        "version": "31.0.0.1.94",
        "code": "89872911"
    },
    {
        "version": "30.0.0.12.95",
        "code": "89867442"
    },
    {
        "version": "30.0.0.12.95",
        "code": "89867443"
    },
    {
        "version": "31.0.0.4.94",
        "code": "90206733"
    },
    {
        "version": "31.0.0.9.94",
        "code": "90539500"
    },
    {
        "version": "31.0.0.10.94",
        "code": "90841959"
    },
    {
        "version": "31.0.0.10.94",
        "code": "90841964"
    },
    {
        "version": "32.0.0.1.94",
        "code": "90848911"
    },
    {
        "version": "32.0.0.7.94",
        "code": "91196699"
    },
    {
        "version": "32.0.0.14.94",
        "code": "91537601"
    },
    {
        "version": "32.0.0.16.94",
        "code": "91882539"
    },
    {
        "version": "33.0.0.1.92",
        "code": "91910106"
    },
    {
        "version": "33.0.0.5.92",
        "code": "92383910"
    },
    {
        "version": "33.0.0.8.92",
        "code": "92605898"
    },
    {
        "version": "33.0.0.11.92",
        "code": "93117667"
    },
    {
        "version": "33.0.0.11.92",
        "code": "93117670"
    },
    {
        "version": "34.0.0.3.93",
        "code": "93134846"
    },
    {
        "version": "34.0.0.4.93",
        "code": "93321235"
    },
    {
        "version": "34.0.0.10.93",
        "code": "93684092"
    },
    {
        "version": "34.0.0.12.93",
        "code": "94080606"
    },
    {
        "version": "34.0.0.12.93",
        "code": "94080607"
    },
    {
        "version": "35.0.0.3.96",
        "code": "94112298"
    },
    {
        "version": "35.0.0.7.96",
        "code": "94500659"
    },
    {
        "version": "35.0.0.14.96",
        "code": "94961862"
    },
    {
        "version": "35.0.0.20.96",
        "code": "95414345"
    },
    {
        "version": "35.0.0.20.96",
        "code": "95414346"
    },
    {
        "version": "35.0.0.20.96",
        "code": "95414347"
    },
    {
        "version": "36.0.0.3.91",
        "code": "95434759"
    },
    {
        "version": "36.0.0.7.91",
        "code": "95829521"
    },
    {
        "version": "36.0.0.13.91",
        "code": "96258630"
    },
    {
        "version": "36.0.0.13.91",
        "code": "96794591"
    },
    {
        "version": "36.0.0.13.91",
        "code": "96794592"
    },
    {
        "version": "37.0.0.5.97",
        "code": "96940945"
    },
    {
        "version": "37.0.0.9.97",
        "code": "97235966"
    },
    {
        "version": "37.0.0.15.97",
        "code": "97757337"
    },
    {
        "version": "37.0.0.21.97",
        "code": "98288239"
    },
    {
        "version": "37.0.0.21.97",
        "code": "98288242"
    },
    {
        "version": "38.0.0.3.95",
        "code": "98301249"
    },
    {
        "version": "38.0.0.7.95",
        "code": "98766551"
    },
    {
        "version": "38.0.0.12.95",
        "code": "99353302"
    },
    {
        "version": "38.0.0.13.95",
        "code": "99640905"
    },
    {
        "version": "38.0.0.13.95",
        "code": "99640911"
    },
    {
        "version": "39.0.0.4.93",
        "code": "99668514"
    },
    {
        "version": "39.0.0.12.93",
        "code": "100120602"
    },
    {
        "version": "39.0.0.16.93",
        "code": "100521966"
    },
    {
        "version": "40.0.0.3.95",
        "code": "101012706"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986890"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986893"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986894"
    },
    {
        "version": "39.0.0.19.93",
        "code": "100986896"
    },
    {
        "version": "40.0.0.7.95",
        "code": "101435484"
    },
    {
        "version": "40.0.0.12.95",
        "code": "101784049"
    },
    {
        "version": "41.0.0.10.92",
        "code": "102994842"
    },
    {
        "version": "42.0.0.2.95",
        "code": "103543967"
    },
    {
        "version": "42.0.0.17.95",
        "code": "104284665"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842048"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842051"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842053"
    },
    {
        "version": "43.0.0.10.97",
        "code": "105842058"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092308"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092318"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092322"
    },
    {
        "version": "44.0.0.9.93",
        "code": "107092339"
    },
    {
        "version": "45.0.0.17.93",
        "code": "108357720"
    },
    {
        "version": "45.0.0.17.93",
        "code": "108357722"
    },
    {
        "version": "46.0.0.15.96",
        "code": "109556223"
    },
    {
        "version": "46.0.0.15.96",
        "code": "109556226"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937437"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937441"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937448"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937453"
    },
    {
        "version": "47.0.0.16.96",
        "code": "110937463"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021127"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021130"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021131"
    },
    {
        "version": "48.0.0.15.98",
        "code": "112021134"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249548"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249561"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249569"
    },
    {
        "version": "49.0.0.15.89",
        "code": "113249580"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622421"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622426"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622429"
    },
    {
        "version": "50.0.0.41.119",
        "code": "114622435"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746524"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746525"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746527"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746528"
    },
    {
        "version": "50.1.0.43.119",
        "code": "114746533"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211351"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211358"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211364"
    },
    {
        "version": "51.0.0.20.85",
        "code": "115211374"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994873"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994876"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994877"
    },
    {
        "version": "52.0.0.8.83",
        "code": "115994879"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756940"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756947"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756948"
    },
    {
        "version": "53.0.0.13.84",
        "code": "116756953"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539695"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539687"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539698"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539703"
    },
    {
        "version": "54.0.0.14.82",
        "code": "117539706"
    },
    {
        "version": "55.0.0.12.79",
        "code": "118342006"
    },
    {
        "version": "55.0.0.12.79",
        "code": "118342010"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104795"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104798"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104802"
    },
    {
        "version": "56.0.0.13.78",
        "code": "119104804"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875220"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875222"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875225"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875229"
    },
    {
        "version": "57.0.0.9.80",
        "code": "119875235"
    },
    {
        "version": "58.0.0.12.73",
        "code": "120662547"
    },
    {
        "version": "58.0.0.12.73",
        "code": "120662550"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451786"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451799"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451810"
    },
    {
        "version": "59.0.0.23.76",
        "code": "121451814"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206595"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206601"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206608"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206624"
    },
    {
        "version": "60.0.0.16.79",
        "code": "122206636"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338241"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338243"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338247"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338251"
    },
    {
        "version": "60.1.0.17.79",
        "code": "122338255"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103719"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103729"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103748"
    },
    {
        "version": "61.0.0.19.86",
        "code": "123103756"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790714"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790715"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790716"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790722"
    },
    {
        "version": "62.0.0.19.93",
        "code": "123790725"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124583932"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124583960"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124584015"
    },
    {
        "version": "63.0.0.17.94",
        "code": "124584019"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398466"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398467"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398468"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398471"
    },
    {
        "version": "64.0.0.14.96",
        "code": "125398474"
    },
    {
        "version": "65.0.0.12.86",
        "code": "126223508"
    },
    {
        "version": "65.0.0.12.86",
        "code": "126223536"
    },
    {
        "version": "65.0.0.12.86",
        "code": "126223544"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127048992"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127049016"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127049038"
    },
    {
        "version": "66.0.0.11.101",
        "code": "127049053"
    },
    {
        "version": "67.0.0.24.100",
        "code": "128028364"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079974"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079975"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079976"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079984"
    },
    {
        "version": "67.0.0.25.100",
        "code": "128079991"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676139"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676143"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676146"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676156"
    },
    {
        "version": "68.0.0.11.99",
        "code": "128676160"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611414"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611415"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611416"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611419"
    },
    {
        "version": "69.0.0.30.95",
        "code": "129611421"
    },
    {
        "version": "70.0.0.21.98",
        "code": "130528344"
    },
    {
        "version": "70.0.0.21.98",
        "code": "130528499"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580482"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580484"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580485"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580488"
    },
    {
        "version": "70.0.0.22.98",
        "code": "130580490"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223236"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223237"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223239"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223240"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223243"
    },
    {
        "version": "71.0.0.18.102",
        "code": "131223245"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081622"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081640"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081644"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081648"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081649"
    },
    {
        "version": "72.0.0.21.98",
        "code": "132081655"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633067"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633068"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633072"
    },
    {
        "version": "73.0.0.22.185",
        "code": "133633074"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666554"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666556"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666564"
    },
    {
        "version": "74.0.0.21.99",
        "code": "134666566"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374885"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374887"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374890"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374896"
    },
    {
        "version": "75.0.0.23.99",
        "code": "135374904"
    },
    {
        "version": "76.0.0.15.395",
        "code": "138226743"
    },
    {
        "version": "76.0.0.15.395",
        "code": "138226752"
    },
    {
        "version": "76.0.0.15.395",
        "code": "138226758"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237606"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237645"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237670"
    },
    {
        "version": "77.0.0.20.113",
        "code": "139237687"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906542"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906547"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906556"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906564"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906580"
    },
    {
        "version": "78.0.0.11.104",
        "code": "139906597"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973934"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973935"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973940"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973941"
    },
    {
        "version": "79.0.0.21.101",
        "code": "140973942"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753087"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753091"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753097"
    },
    {
        "version": "80.0.0.14.110",
        "code": "141753099"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841905"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841908"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841909"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841911"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841917"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841921"
    },
    {
        "version": "81.0.0.15.91",
        "code": "142841922"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631572"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631574"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631575"
    },
    {
        "version": "82.0.0.13.119",
        "code": "143631576"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612578"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612596"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612598"
    },
    {
        "version": "83.0.0.20.111",
        "code": "144612600"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652085"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652086"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652094"
    },
    {
        "version": "84.0.0.21.105",
        "code": "145652096"
    },
    {
        "version": "85.0.0.21.100",
        "code": "146536611"
    },
    {
        "version": "85.0.0.21.100",
        "code": "146536612"
    },
    {
        "version": "85.0.0.21.100",
        "code": "146536619"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985641"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985644"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985665"
    },
    {
        "version": "86.0.0.19.87",
        "code": "146985667"
    },
    {
        "version": "86.0.0.24.87",
        "code": "147375127"
    },
    {
        "version": "86.0.0.24.87",
        "code": "147375143"
    },
    {
        "version": "87.0.0.18.99",
        "code": "148324036"
    },
    {
        "version": "87.0.0.18.99",
        "code": "148324039"
    },
    {
        "version": "87.0.0.18.99",
        "code": "148324051"
    },
    {
        "version": "88.0.0.14.99",
        "code": "149350048"
    },
    {
        "version": "88.0.0.14.99",
        "code": "149350061"
    },
    {
        "version": "90.0.0.18.110",
        "code": "151414267"
    },
    {
        "version": "90.0.0.18.110",
        "code": "151414270"
    },
    {
        "version": "90.0.0.18.110",
        "code": "151414277"
    },
    {
        "version": "91.0.0.18.118",
        "code": "152367488"
    },
    {
        "version": "91.0.0.18.118",
        "code": "152367502"
    },
    {
        "version": "92.0.0.15.114",
        "code": "153386777"
    },
    {
        "version": "92.0.0.15.114",
        "code": "153386779"
    },
    {
        "version": "92.0.0.15.114",
        "code": "153386780"
    },
    {
        "version": "93.1.0.19.102",
        "code": "154400376"
    },
    {
        "version": "93.1.0.19.102",
        "code": "154400383"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374049"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374077"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374080"
    },
    {
        "version": "94.0.0.22.116",
        "code": "155374104"
    },
    {
        "version": "95.0.0.21.124",
        "code": "156514146"
    },
    {
        "version": "95.0.0.21.124",
        "code": "156514151"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405369"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405371"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405376"
    },
    {
        "version": "96.0.0.28.114",
        "code": "157405377"
    },
    {
        "version": "97.0.0.32.119",
        "code": "158441903"
    },
    {
        "version": "97.0.0.32.119",
        "code": "158441917"
    },
    {
        "version": "98.0.0.15.119",
        "code": "159526671"
    },
    {
        "version": "98.0.0.15.119",
        "code": "159526764"
    },
    {
        "version": "98.0.0.15.119",
        "code": "159526788"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497901"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497902"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497913"
    },
    {
        "version": "99.0.0.32.182",
        "code": "160497915"
    },
    {
        "version": "101.0.0.15.120",
        "code": "162439022"
    },
    {
        "version": "101.0.0.15.120",
        "code": "162439038"
    },
    {
        "version": "101.0.0.15.120",
        "code": "162439040"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478660"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478663"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478664"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478665"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478671"
    },
    {
        "version": "100.0.0.17.129",
        "code": "161478672"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022067"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022069"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022072"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022084"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022088"
    },
    {
        "version": "102.0.0.20.117",
        "code": "163022089"
    },
    {
        "version": "103.0.0.15.119",
        "code": "163988652"
    },
    {
        "version": "103.0.0.15.119",
        "code": "163988658"
    },
    {
        "version": "103.0.0.15.119",
        "code": "163988664"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094470"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094522"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094526"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094533"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094537"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094539"
    },
    {
        "version": "103.1.0.15.119",
        "code": "164094540"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165030898"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165030942"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165030945"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165031087"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165031107"
    },
    {
        "version": "104.0.0.21.118",
        "code": "165031108"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149662"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149665"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149669"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149709"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149717"
    },
    {
        "version": "105.0.0.18.119",
        "code": "166149725"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338369"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338371"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338511"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338514"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338559"
    },
    {
        "version": "106.0.0.24.118",
        "code": "167338564"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361624"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361627"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361634"
    },
    {
        "version": "107.0.0.27.121",
        "code": "168361635"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474954"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474957"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474965"
    },
    {
        "version": "108.0.0.23.119",
        "code": "169474968"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693915"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693940"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693970"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693979"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693982"
    },
    {
        "version": "109.0.0.18.124",
        "code": "170693985"
    },
    {
        "version": "111.0.0.24.152",
        "code": "172894482"
    },
    {
        "version": "111.1.0.25.152",
        "code": "173238718"
    },
    {
        "version": "111.1.0.25.152",
        "code": "173238731"
    },
    {
        "version": "111.1.0.25.152",
        "code": "173238732"
    },
    {
        "version": "112.0.0.29.121",
        "code": "174081646"
    },
    {
        "version": "112.0.0.29.121",
        "code": "174081672"
    },
    {
        "version": "112.0.0.29.121",
        "code": "174081674"
    },
    {
        "version": "113.0.0.38.122",
        "code": "175504952"
    },
    {
        "version": "113.0.0.38.122",
        "code": "175504966"
    },
    {
        "version": "113.0.0.38.122",
        "code": "175504968"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649420"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649426"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649435"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649442"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649504"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649511"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649519"
    },
    {
        "version": "114.0.0.38.120",
        "code": "176649525"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574582"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574590"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574593"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574596"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574628"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574630"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574640"
    },
    {
        "version": "113.0.0.39.122",
        "code": "175574641"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770652"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770654"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770659"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770663"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770667"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770724"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770729"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770732"
    },
    {
        "version": "115.0.0.26.111",
        "code": "177770737"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155059"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155084"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155088"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155096"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155097"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155098"
    },
    {
        "version": "116.0.0.34.121",
        "code": "179155099"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322757"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322760"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322800"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322810"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322811"
    },
    {
        "version": "117.0.0.28.123",
        "code": "180322814"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747374"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747388"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747397"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747399"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747400"
    },
    {
        "version": "119.0.0.33.147",
        "code": "182747402"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982954"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982956"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982971"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982976"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982986"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183982991"
    },
    {
        "version": "120.0.0.29.118",
        "code": "183983005"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203672"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203673"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203693"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203705"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203706"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203708"
    },
    {
        "version": "121.0.0.29.119",
        "code": "185203710"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791631"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791648"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791669"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791674"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791681"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791692"
    },
    {
        "version": "123.0.0.21.114",
        "code": "188791703"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383407"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383411"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383413"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383426"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383428"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383430"
    },
    {
        "version": "125.0.0.20.126",
        "code": "194383433"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435525"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435540"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435547"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435560"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435561"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435566"
    },
    {
        "version": "126.0.0.25.121",
        "code": "195435577"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643798"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643799"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643801"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643803"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643814"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643820"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643821"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643822"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643823"
    },
    {
        "version": "127.0.0.30.121",
        "code": "196643826"
    }
]

mobileUA = {
    "xiaomi": xiaomi,
    "asus": asus,
    "google": google,
    "huawei": huawei,
    "lenovo": lenovo,
    "oneplus": oneplus,
    "oppo": oppo,
    "realme": realme,
    "samsung": samsung,
    "sony": sony,
    "vivo": vivo,
}

fakeua = UserAgent(browsers=['chrome'])


def id_generator(self, size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


uax = []


def uaio(vers, fixed_version_code=[], dump=False):
    APPS = versions_old if vers == "old" else versions
    APP = random.choice(fixed_version_code if len(
        fixed_version_code) > 0 else APPS)
    auo = random.choice(random.choice(mobileUA['xiaomi'] if dump else uax))
    return f"Instagram {APP['version']} Android ({auo['sdk']}/{auo['android_version']}; {auo['dpi']}dpi; {auo['display']}; {auo['brand']}; {auo['model']}; {auo['os']}; {auo['hardware']}; in_ID; {APP['code']})"
