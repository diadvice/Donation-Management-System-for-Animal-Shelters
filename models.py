from django.db import models


# Model for Plans
class Plan(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
    name = models.CharField(max_length=255)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    promocode = models.CharField(max_length=100, blank=True, null=True) 


    def __str__(self):
        return self.name


# Model for Bonuses
class Bonus(models.Model):
    bonus_id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
    plan=models.ForeignKey(Plan,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    expiration_date = models.DateTimeField(blank=True, null=True) 
    
    def __str__(self):
        return f"{self.description} by {self.company_name}"


# Model for Shelters
class Shelter(models.Model):
    shelter_id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
    shelter_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    telegram_username = models.CharField(max_length=100)
    shelter_description=models.TextField()
    shelter_bank_link=models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.shelter_name} in {self.city}"


# Model for Users
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    selected_shelter = models.ForeignKey(Shelter, on_delete=models.SET_NULL, null=True)  # Foreign key to shelter
    donation_goal = models.DecimalField(max_digits=10, decimal_places=2)
    current_total_donations_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    plan_start_date = models.DateTimeField(null=True)
    selected_bonus = models.ForeignKey(Bonus, null=True, blank=True, on_delete=models.SET_NULL)  # Foreign key to Bonus
    #receipt_uploaded = models.CharField(max_length=255, blank=True, null=True)
    #city=models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


#Model for donation
class Donations(models.Model):
    donation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)
    receipt_uploaded = models.CharField(max_length=255, blank=True, null=True)  # This stores the path or URL to the receipt
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Donation {self.donation_id} by {self.user.username}"






    

# class Shelter(models.Model):
#     shelter_id=models.IntegerField(unique=True)
#     city = models.CharField(max_length=100)
#     shelter_name = models.CharField(max_length=100)
#     telegram_username=models.CharField(max_lengt=100)
#     #shelter_id INTEGER PRIMARY KEY,
        
#     def __str__(self):
#         return self.shelter_name

# class Plan(models.Model):
#     shelter_id=models.IntegerField(unique=True)
#     description = models.CharField(max_length=255)
#     is_claimed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.description


# class Bonus(models.Model):
#     shelter_id=models.IntegerField(unique=True)
#     description = models.CharField(max_length=255)
#     is_claimed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.description


# # bot/models.py

# # bot/models.py

# # Model for Bonuses
# class Bonus(models.Model):
#     id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
#     description = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     link = models.URLField(max_length=200)

#     def __str__(self):
#         return f"{self.description} by {self.company_name}"

# # Model for Shelters
# class Shelter(models.Model):
#     id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
#     shelter_name = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     telegram_username = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.shelter_name} in {self.city}"

# # Model for Plans
# class Plan(models.Model):
#     id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
#     name = models.CharField(max_length=255)
#     goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     bonuses = models.ManyToManyField(Bonus, related_name="plans")  # Many-to-Many relationship with Bonus

#     def __str__(self):
#         return self.name


# cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
#         user_id INTEGER PRIMARY KEY,
#         username TEXT,
#         first_name TEXT,
#         last_name TEXT,
#         plan_id INTEGER,
#         selected_shelter TEXT,
#         donation_goal REAL,
#         donations REAL DEFAULT 0.0,
#         plan_start_date TEXT
#     )''')

#     cursor.execute('''CREATE TABLE IF NOT EXISTS Plans (
#         plan_id INTEGER PRIMARY KEY,
#         name TEXT,
#         goal_amount REAL,
#         bonuses TEXT
#     )''')


#  # Таблица приютов
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Shelters (
#         shelter_id INTEGER PRIMARY KEY,
#         shelter_name TEXT,
#         city TEXT,
#         telegram_username TEXT
#     )''')

#     # Таблица донатов
#     cursor.execute('''CREATE TABLE IF NOT EXISTS Donations (
#         donation_id INTEGER PRIMARY KEY,
#         user_id INTEGER,
#         shelter_id INTEGER,
#         donation_amount REAL,
#         donation_date TEXT,
#         verified BOOLEAN DEFAULT 0,
#         FOREIGN KEY(user_id) REFERENCES Users(user_id),
#         FOREIGN KEY(shelter_id) REFERENCES Shelters(shelter_id)
#     )''')

#     conn.commit()
#     conn.close()
