import pandas as pd
import random
import faker

# Create a Faker instance for generating random data
fake = faker.Faker()

# Function to generate random data for each column
def generate_random_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    mobile_number = f"9{random.randint(100000000, 999999999)}"
    aadhaar_number = f"{random.randint(100000000000, 999999999999)}"
    college_name = fake.company()
    roll_number = random.randint(1000, 9999)
    qualification = random.choice(["B.Tech", "M.Tech", "B.Sc", "M.Sc", "BBA", "MBA"])
    experience_type = random.choice(["Full-time", "Part-time", "Internship"])
    experience = random.randint(0, 10)  # Years of experience
    technologies = random.choice(["Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Ruby"])

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "mobile_number": mobile_number,
        "adhaar_number": aadhaar_number,
        "college_name": college_name,
        "roll_number": roll_number,
        "qualification": qualification,
        "experience_type": experience_type,
        "experience": experience,
        "technologies": technologies,
    }

# Generate data for 20 users
data = [generate_random_data() for _ in range(20)]

# Create DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
file_path = r'C:\Users\Dinesh Kumar Reddy\OneDrive - Sparity INC\Desktop\ExamPortal\Test\data\test_users.csv'
df.to_csv(file_path, index=False)
print("Data Inserted Succesfully!!")