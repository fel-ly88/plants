# Plant Management System

A comprehensive plant management application with both CLI and web interfaces for tracking your plants, watering schedules, and plant care history.

## 🌱 Features

- **Plant Management**: Add, update, and organize your plants
- **Category System**: Organize plants by categories (Indoor, Outdoor, Succulents, etc.)
- **Watering Tracking**: Record watering sessions and track amounts
- **Watering History**: View complete watering history for each plant
- **CLI Interface**: Command-line interface for quick plant management
- **Web Interface**: React-based frontend for visual plant management
- **Database Storage**: SQLite database for persistent data storage

## 📁 Project Structure

```
fel3/plants/
├── backend/                 # Python backend with CLI
│   ├── app/
│   │   ├── cli.py          # Command-line interface
│   │   ├── models.py       # Database models
│   │   ├── database.py     # Database configuration
│   │   └── utils.py        # Utility functions
│   ├── run.py              # Main entry point for CLI
│   ├── Pipfile             # Python dependencies
│   └── plants.db           # SQLite database
├── frontend/               # React frontend
│   ├── src/                # React source code
│   ├── public/             # Static assets
│   └── package.json        # Node.js dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+
- pipenv (for Python dependency management)

### Backend Setup (CLI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pipenv install
   ```

3. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

4. Run the CLI application:
   ```bash
   python run.py
   ```

### Frontend Setup (Web Interface)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Open your browser to `http://localhost:3000`

## 🖥️ CLI Usage

The CLI provides a menu-driven interface with the following options:

### Main Menu
```
=== Plant Management CLI ===
1. Add new plant
2. List all plants
3. Update plant details
4. Record watering
5. List watering history
6. Add new category
7. Exit
```

### Adding a Plant
1. Select option 1 from the main menu
2. Enter plant details:
   - Plant name
   - Species
   - Location
   - Watering frequency (in days)
   - Category (from existing categories)

### Recording Watering
1. Select option 4 from the main menu
2. Choose a plant from the list
3. Enter the amount of water (in liters)
4. The current date is automatically recorded

### Viewing Watering History
1. Select option 5 from the main menu
2. Choose a plant from the list
3. View all watering records with dates and amounts

## 🗄️ Database Schema

### Categories Table
- `id`: Primary key
- `name`: Category name (unique)
- `description`: Category description

### Plants Table
- `id`: Primary key
- `name`: Plant name
- `species`: Plant species
- `location`: Where the plant is located
- `watering_frequency`: Days between watering
- `category_id`: Foreign key to categories

### Waterings Table
- `id`: Primary key
- `plant_id`: Foreign key to plants
- `date`: Date of watering
- `amount`: Amount of water in liters

## 🛠️ Development

### Backend Dependencies
- Flask: Web framework
- SQLAlchemy: ORM for database operations
- Click: CLI framework
- Python-dotenv: Environment variable management

### Frontend Dependencies
- React: Frontend framework
- React Router: Navigation
- Bootstrap: UI components
- Tailwind CSS: Utility-first CSS
- FontAwesome: Icons

### Running Tests
```bash
# Backend tests
cd backend
pipenv run pytest

# Frontend tests
cd frontend
npm test
```

## 📝 Example Usage

### CLI Example Session
```
=== Plant Management CLI ===
1. Add new plant
2. List all plants
3. Update plant details
4. Record watering
5. List watering history
6. Add new category
7. Exit
Enter choice: 1

Plant name: Monstera Deliciosa
Species: Monstera deliciosa
Location: Living Room
Watering frequency (days): 7

--- Categories ---
1. Indoor - Indoor houseplants
2. Outdoor - Garden plants

Category ID: 1
Plant 'Monstera Deliciosa' added successfully!
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🐛 Troubleshooting

### Common Issues

**Database not found**: Run `python run.py` from the backend directory to create the database automatically.

**Module not found**: Ensure you're in the correct virtual environment with `pipenv shell`.

**Port already in use**: Change the port in the frontend package.json or kill the process using the port.

## 🔮 Future Enhancements

- Plant care reminders and notifications
- Photo upload for plants
- Weather integration for outdoor plants
- Plant health tracking
- Export/import functionality
- Mobile app version
