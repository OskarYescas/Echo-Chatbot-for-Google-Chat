Requirements:
- Google Workspace environment
- Google Cloud Project with billing enabled
- Cloud Run Admin API Needed
- Enable permisions as prompted


To make the bot fully operational the following should be configured.
1. You must have a working Google Workspace environment with active users.
2. Create a project (Or select one you're going to use) which has billing enable.
3. Create a cloud run function.
          3.1. Any name you want
          3.2 Any region of your convenience
          3.3 Runtime Python 3.x
          3.4 Allow public access
          3.5 Request based billing
          3.6 Allow direct access ti your service from the internet
4. Enable Google Chat API
          4.1 On configuration tab, configure your app as pleased.
          4.2 Important: Interactive features ON; Join spaces and group conversations ON; HTTP endpoint URL;
          4.3 Trigger > Use a Common HTTP enpoint URL for all triggers > Add the URL from could Run function
