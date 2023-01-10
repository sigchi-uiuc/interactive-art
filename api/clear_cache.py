from flask_caching import Cache
from app import app, cache_config

cache = Cache()

def main():
    cache.init_app(app, config=cache_config)

    with app.app_context():
        cache.clear()
    
    # make sure gitignore file stays in folder
    f = open("cache/.gitignore", "w")
    f.write("*\n!.gitignore")
    f.close()

if __name__ == '__main__':
    main()