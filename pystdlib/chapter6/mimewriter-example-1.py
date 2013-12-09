import MimeWriter, quopri, base64, StringIO, sys

TEXT = """
here comes the image you asked for. hope
it's what you expected.
"""

FILE = "samples/sample.jpg"

file = sys.stdout

mime = MimeWriter.MimeWriter(file)
mime.addheader("Mime-Version", "1.0")
mime.startmultipartbody("mixed")

# add a text message
part = mime.nextpart()
part.addheader("Content-Transfer-Encoding", "quoted-printable")
part.startbody("text/plain")

quopri.encode(StringIO.StringIO(TEXT), file, 0)

# add an image
part = mime.nextpart()
part.addheader("Content-Transfer-Encoding", "base64")
part.startbody("image/jpeg")

base64.encode(open(FILE, "rb"), file)

mime.lastpart()
