import asana

# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

# CONSTRUCT ASANA CLIENT
client = asana.Client.access_token(personal_access_token)
print(client)

# Set things up to send the name of this script to us to show that you succeeded! This is optional.
client.options['client_name'] = "hello_world_python"

# Get your user info
me = client.users.me()
print(me)

# # GET PROJECTS THAT YOU ARE WORKING ON
curl - X GET https: // app.asana.com/api/1.0/projects
print(project)

# Print out your information
print("Hello world! " + "My name is " + me['name'] + "!")
print("You are currently working on a project: ")
