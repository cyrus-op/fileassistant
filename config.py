import os

BOTTOKEN = os.environ.get("BOTTOKEN", "")
APIID = int(os.environ.get("APIID", ))
APIHASH = os.environ.get("APIHASH", "")
DOWNLOADPATH = os.environ.get("DOWNLOADPATH", "Downloads/")
USERNAME = "@LazyURLUpload_Bot"

"""
If you using VPS, edit like this:

BOTTOKEN = "123456:xxxx"
APIID = 6
APIHASH = eb06d4abfb49dc3eeb1aeb98ae0f581e
DOWNLOADPATH = "Downloads/"
USERNAME = "@LazyURLUpload_Bot"
"""
