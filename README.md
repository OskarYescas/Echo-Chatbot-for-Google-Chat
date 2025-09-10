Google Chat EchoBot on Cloud Run
This project provides a minimalistic Python implementation of a Google Chat bot that greets users and echoes their messages back to them. It's designed to be deployed as a serverless container on Google Cloud Run and integrates directly with the Google Chat API.

Core Technologies
- Python 3
- Google Cloud Run
- Google Chat API

Prerequisites
Before you begin, ensure you have the following:

- A Google Cloud project with billing enabled.
- A Google Workspace account with permissions to configure Chat apps.
- The gcloud CLI installed and configured, or you can perform the equivalent steps via the Google Cloud Console.

Step 1: Enable Required APIs
You need to enable the Cloud Run, Cloud Build, and Google Chat APIs for your project.

Bash on CLoudShell:
gcloud services enable run.googleapis.com cloudbuild.googleapis.com chat.googleapis.com

Step 2: Deploy the EchoBot to Cloud Run
1. Navigate to the Cloud Run section of the Google Cloud Console.
2. Click Create Service.
3. Choose Use an inline editor to create a function for the source.
4. Configure the service with the following settings:
          - Service name: Give your bot a name (e.g., echobot-service).
          - Region: Select a region of your choice.
          - Authentication: Select Allow public access. This is crucial for Google Chat to be able to reach your service.
          - Ingress control: Select All.
5. Click "Next" to go to the code editor. Paste the Python code from the section below.
6. Click Deploy. Once the deployment is complete, copy the service URL. You will need it for the next step.

Step 3: Configure the Google Chat API
1. Navigate to the Google Chat API page in the Google Cloud Console.
2. Click on the Configuration tab.
3. Fill out the Application info section:
          - App name: The name users will see in Google Chat (e.g., EchoBot).
          - Avatar URL: A public URL for an icon.
          - Description: A short description of your bot.
4. Crucial Step: Ensure the checkbox for "Build this Chat as a Workspace add-on" is NOT checked. This was a key source of issues.
5. Configure the Interactive features:
          - Enable Interactive features: Set the toggle to ON.
          - Functionality: Check "Join spaces and group conversations" so the bot can be used in rooms.
6. Configure the Connection settings:
          - Select HTTP endpoint URL.
          - HTTP endpoint URL: Paste the URL you copied from your deployed Cloud Run service.
          - Authentication Audience: Paste the exact same URL from your Cloud Run service into this field. This is a mandatory requirement.
7. Configure Visibility: Set the visibility for your app, either to specific users/groups or to your entire domain.
8. Click Save. It may take a few minutes for the settings to apply.

Step 4: Add the Bot Code
Paste the main.py & requirements.txt into the Cloud Run inline editor during the deployment step.

Step 5: Test Your Bot
1. Open Google Chat.
2. Click the + sign to start a new chat and find your bot by the name you configured (e.g., EchoBot).
3. Send it a message. It should echo your message back!
4. You can also add it to a Space by typing @YourBotName and adding it to the room. It should respond with "Hi!".
