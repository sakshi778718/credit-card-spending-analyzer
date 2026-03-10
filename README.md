
# Credit Card Spending Analyzer

A financial analytics web application that analyzes credit card transaction data and generates spending insights. Users can upload their transaction CSV files to see total spending, largest transaction, and category-wise spending breakdown.

--- 
## Features
- Upload transaction CSV file
- Calculate total spending
- Identify largest transaction
- Category-wise spending analysis
- Simple and clean dashboard

---
## Tech Stack
- Python
- Flask
- Pandas
- HTML/CSS

---
## Project Structure
credit-card-spending-analyzer  
│  
├── app.py           # Main Python Flask app  
├── transactions.csv # Sample CSV dataset  
├── requirements.txt # Python dependencies  
└── README.md        # This file

---
## Installation & Running
1. Clone the repository:  
git clone https://github.com/sakshi778718/credit-card-spending-analyzer.git

2. Navigate to the project folder:  
cd credit-card-spending-analyzer

3. Install dependencies:  
pip install -r requirements.txt

4. Run the application:  
python app.py

5. Open your browser and go to:  
http://127.0.0.1:5000

---
## Example CSV Dataset
Date,Category,Amount  
2024-01-02,Food,450  
2024-01-03,Transport,200  
2024-01-04,Shopping,1500  
2024-01-05,Food,300  
2024-01-06,Bills,1200

---
## Future Improvements
- Add data visualization (charts for spending trends)  
- Monthly budget alerts  
- Fraud detection integration  
- Export report as PDF

---
## Author
Smita Singh  
GitHub: https://github.com/sakshi778718
