# cPanel Deployment

## Pulling Changes from `main`
- Go to Git version control from the interactiveart dashboard
    
    ![](git.PNG)
- Click `Manage` for the interactive-art repo

    ![](git_manage.PNG)
- Click the `Pull or Deploy` tab
- Click `Update from Remote` 
- Finally click `Deploy HEAD Commit`
    - This follows the commands in the `.cpanel.yml` file, which just copies the files from the repo to its appropriate place and restarts the server

## Installing New Python Packages
If there are any new Python dependencies take the following steps
- Go to the python app

    ![](python.PNG)
- Click the edit symbol

    ![](python_edit.PNG)
- Click `Run Pip Install` for `requirements.txt`

    ![](install.PNG)
- Finally click `Restart`

    ![](restart.PNG)

## Clearing Cache
If major changes were made to the backend we want to clear the cache because the precomputed results will be inconsistent. To do so:
- Type in `clear_cache.py` in the execute python script section of the python app then click `Run Script`

    ![](clear.PNG)