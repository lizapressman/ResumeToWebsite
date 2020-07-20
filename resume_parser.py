from pyresparser import ResumeParser

data = ResumeParser('/Users/lizapressman/Documents/ResumeToWebsite/resume.pdf').get_extracted_data()

print(data)

for key in data:
    print(key)
    print(data.get(key))

# ask user to verify and change information on front end side
# update/fix data on submit from user

website = open('website.html', 'w')

message = f"""
<html>
    <head></head>
    <body>
        <h1>Name: {data.get("name")}</h1>
        <p>Email: {data.get("email")}</p>
    </body>
</html>
"""

website.write(message)
website.close()
