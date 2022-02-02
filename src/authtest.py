import os 

from google.cloud import storage

credential_path ="C:/Users/wnsn0/Documents/boreal-album-340112-defd948aaca6.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
