# # Import SQLAlchemy and other modules from your Flask application
# from app import db  # Replace 'app' with the actual name of your Flask app instance
# from config import Config  # Import your configuration if necessary
# from sqlalchemy import create_engine  # Import create_engine from SQLAlchemy

# # Create a SQLAlchemy engine using the connection URL from your config
# connection_url = Config.SQLALCHEMY_DATABASE_URI

# try:
#     # Create a SQLAlchemy engine using the connection URL
#     engine = create_engine(connection_url)
    
#     # Test the connection by connecting to the database
#     with engine.connect() as connection:
#         print("Connected to the database successfully!")

    

# except Exception as e:
#     print(f"Error connecting to the database: {str(e)}")


