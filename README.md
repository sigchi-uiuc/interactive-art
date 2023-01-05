# interactive-art

## Development

### Install node packages
```
npm install
```

### Run UI on `http://localhost:8080/`
```
npm run serve
```

### Run Backend from `http://localhost:4000/`
```
cd server
python app.py
```

## Putting Changes Into Production
- `npm run build`
- Then commit and push your changes (including the `dist` folder)
- submit a pull request to the main brain
- To make changes live at `https://interactiveart.web.illinois.edu` those with cPanel access need to follow [these steps](docs/cpanel.md)

### Note on API location on server
The backend can be accessed at https://backend.interactiveart.web.illinois.edu which is specified in the .env file
When running the frontend locally,it automatically proxies to the backend running locally
