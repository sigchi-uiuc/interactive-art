# interactive-art

## Development

### Run Frontend locally on port `8080`
```
npm install
npm run serve
```
Go to http://localhost:8080/

### Run Backend locally on port `5000`
```
pip install -r requirements.txt
cd api
python app.py
```
Go to http://localhost:5000/

### Backend Caching
To speed up the backend we currently have file system caching implemented. This makes sure that anything already computed is retrieved from the `cache` folder and not computed again
- results will be cached forever in the filesystem unless cleared
- to clear the cache run `python clear_cache.py` in the `api` folder
- to clear the cache on the server see these [instructions](docs/cpanel.md#clearing-cache)

## Putting Changes Into Production
- Run `npm run build`
- If you added any Python dependencies for the api run `pip freeze > requirements.txt` from the root of the project
- Commit and push your changes (including the `dist` folder and `requirements.txt`)
- Submit a pull request to the [main brain](https://github.com/sigchi-uiuc/interactive-art)
- To make changes live at https://interactiveart.web.illinois.edu those with cPanel access need to follow [these steps](docs/cpanel.md)

### Note on API location on server
- When running the frontend locally, requests are automatically proxied to the backend running locally (see above)
- Once deployed, the frontend automatically makes requests to https://backend.interactiveart.web.illinois.edu as specified in the `.env` file
