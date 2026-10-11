from pathlib import Path

from decouple import Config, Csv, RepositoryEnv

ENV_FILE = Path(__file__).resolve().parent / ".env"
config = Config(RepositoryEnv(str(ENV_FILE)))

BLOG_SECRET_KEY = config("BLOG_SECRET_KEY")
BLOG_ALLOWED_HOSTS = config(
    "BLOG_ALLOWED_HOSTS",
    default="localhost,127.0.0.1",
    cast=Csv(),
)

BLOG_DB_NAME = config("BLOG_DB_NAME", default="blog_api")
BLOG_DB_USER = config("BLOG_DB_USER", default="postgres")
BLOG_DB_PASSWORD = config("BLOG_DB_PASSWORD", default="")
BLOG_DB_HOST = config("BLOG_DB_HOST", default="localhost")
BLOG_DB_PORT = config("BLOG_DB_PORT", default=5432, cast=int)
