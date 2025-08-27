from app.cli import main_menu
from app.database import Base, engine

# Create tables
Base.metadata.create_all(engine)

# Start CLI
if __name__ == "__main__":
    main_menu()
