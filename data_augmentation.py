import pandas as pd
import numpy as np

# Đọc dữ liệu từ file CSV gốc
df = pd.read_csv('dataset_full.csv')

# Nhân bản mỗi mẫu dữ liệu một lần
df_repeated = df.reindex(df.index.repeat(100)).reset_index(drop=True)

#__________________________________________________________________________
# Tạo cột "profit" và "city" với giá trị ngẫu nhiên cho cả dữ liệu gốc và dữ liệu đã nhân bản
df['profit'] = np.random.randint(1, 1000, len(df))
df['city'] = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], len(df))
df_repeated['profit'] = np.random.randint(1, 1000, len(df_repeated))
df_repeated['city'] = np.random.choice(['Abilene-Sweetwater', 'Albany, GA', 'Albany, NY', 'Albuquerque', 'Alexandria', 'Alpena', 'Amarillo', 'Anchorage', 'Atlanta', 'Augusta', 'Austin', 'Bakersfield', 'Baltimore', 'Bangor', 'Baton Rouge', 'Beaumont', 'Bend', 'Billings', 'Biloxi', 'Binghamton', 'Birmingham', 'Bismarck-Minot', 'Bluefield-Beckley', 'Boise', 'Boston', 'Bowling Green', 'Buffalo', 'Burlington', 'Butte', 'Casper', 'Cedar Rapids', 'Champaign', 'Charleston, SC', 'Charleston, WV', 'Charlotte', 'Charlottesville', 'Chattanooga', 'Cheyenne', 'Chicago', 'Chico-Redding', 'Cincinnati', 'Clarksburg', 'Cleveland', 'Colorado Springs', 'Columbia, MO', 'Columbia, SC', 'Columbus, GA', 'Columbus, OH', 'Columbus/Tupelo', 'Corpus Christi', 'Dallas', 'Davenport', 'Dayton', 'Denver', 'Des Moines', 'Detroit', 'Dothan', 'Duluth', 'El Paso', 'Elmira', 'Erie', 'Eugene', 'Eureka', 'Evansville', 'Fairbanks', 'Fargo', 'Flint', 'Fort Smith', 'Fresno', 'Ft. Myers', 'Ft. Wayne', 'Gainesville', 'Glendive', 'Grand Junction', 'Grand Rapids', 'Great Falls', 'Green Bay', 'Greensboro', 'Greenville, NC', 'Greenville, SC', 'Greenwood', 'Harlingen', 'Harrisburg', 'Harrisonburg', 'Hartford', 'Hattiesburg-Laurel', 'Helena', 'Honolulu', 'Houston', 'Huntsville', 'Idaho Falls-Pocatello', 'Indianapolis', 'Jackson, MS', 'Jackson, TN', 'Jacksonville', 'Johnstown', 'Jonesboro', 'Joplin', 'Juneau', 'Kansas City', 'Knoxville', 'La Crosse', 'Lafayette, IN', 'Lafayette, LA', 'Lake Charles', 'Lansing', 'Laredo', 'Las Vegas', 'Lexington', 'Lima', 'Lincoln', 'Little Rock', 'Los Angeles', 'Louisville', 'Lubbock', 'Macon', 'Madison', 'Manchester, NH', 'Mankato', 'Marquette', 'Medford-Klamath Falls', 'Memphis', 'Meridian', 'Miami', 'Milwaukee', 'Minneapolis', 'Missoula', 'Mobile', 'Monroe', 'Monterey', 'Montgomery', 'Myrtle Beach', 'Nashville', 'National Cable', 'National Network', 'New Orleans', 'New York', 'Norfolk', 'North Platte', 'Odessa/Midland', 'Oklahoma City', 'Omaha', 'Orlando', 'Ottumwa', 'Paducah', 'Palm Springs', 'Panama City', 'Parkersburg', 'Peoria', 'Philadelphia', 'Phoenix', 'Pittsburgh', 'Portland, ME', 'Portland, OR', 'Presque Isle', 'Providence', 'Quincy', 'Raleigh', 'Rapid City', 'Reno', 'Richmond', 'Roanoke', 'Rochester, MN', 'Rochester, NY', 'Rockford', 'Sacramento', 'Salisbury', 'Salt Lake City', 'San Angelo', 'San Antonio', 'San Diego', 'San Francisco', 'Santa Barbara', 'Savannah', 'Seattle', 'Sherman', 'Shreveport', 'Sioux City', 'Sioux Falls', 'South Bend', 'Spokane', 'Springfield, MA', 'Springfield, MO', 'St Louis', 'St. Joseph', 'Syracuse', 'Tallahassee', 'Tampa', 'Terre Haute', 'Toledo', 'Topeka', 'Traverse City', 'Tri-Cities', 'Tucson', 'Tulsa', 'Twin Falls', 'Tyler', 'Utica', 'Victoria', 'Waco', 'Washington DC', 'Watertown', 'Wausau', 'West Palm Beach', 'Wheeling-Steubenville', 'Wichita', 'Wichita Falls', 'Wilkes Barre', 'Wilmington', 'Yakima', 'Youngstown', 'Yuma-El Centro', 'Zanesville'], len(df_repeated))
#___________________________________________________________________________________________________

# Thay đổi cột "id" và "id_by_category" để đảm bảo tính duy nhất
df_repeated['id'] = df_repeated.index + len(df)
df_repeated['id_by_category'] = df_repeated.groupby('sub_category').cumcount() + df['id_by_category'].max()

# Kết hợp dữ liệu gốc và dữ liệu đã tăng cường
combined_df = pd.concat([df, df_repeated], ignore_index=True)

# Xuất dữ liệu đã tăng cường ra file CSV
combined_df.to_csv('dataset_full_augmented.csv', index=False)

