## 🧪 **Dictionary Amaliy Tasks - Advanced Practice**

---

### **1. `get_full_names(data)`**

🔍 **Vazifa**: Har bir foydalanuvchining to‘liq ismini `"First Last"` formatida ro‘yxatga joylashtiring.

📥 **Input**: `randomuser_data`
📤 **Output**: `["Atilla Bennink", "Stefanus Hilgersom", ...]`
🎯 **Maqsad**: Nested dictionary ichidan ma’lumot olishni mashq qilish.

---

### **2. `get_users_by_country(data, country_name)`**

🔍 **Vazifa**: Faqat `country_name` bo‘yicha yashovchi foydalanuvchilarni filtrlang va ularning full name va email’larini qaytaring.

📥 **Input**: `"India"`
📤 **Output**: `[{"name": "Suhasini Bhardwaj", "email": "suhasini.bhardwaj@example.com"}, ...]`
🎯 **Maqsad**: Filtering va list comprehensionni mustahkamlash.

---

### **3. `count_users_by_gender(data)`**

🔍 **Vazifa**: Foydalanuvchilarni jinsi bo‘yicha sanang va dictda qaytaring.

📤 **Output**: `{'male': 6, 'female': 4}`
🎯 **Maqsad**: Counting values in list + dictionary manipulyatsiyasi.

---

### **4. `get_emails_of_older_than(data, age)`**

🔍 **Vazifa**: Belgilangan yoshi katta bo‘lgan userlarning email ro‘yxatini qaytaring.

📥 **Input**: `age = 60`
📤 **Output**: `["molly.king@example.com", ...]`
🎯 **Maqsad**: If orqali filter qilish + list yaratish.

---

### **5. `sort_users_by_age(data, descending=False)`**

🔍 **Vazifa**: Foydalanuvchilarni yoshiga qarab o‘sish yoki kamayish tartibida sortlab, full name va yoshini chiqaring.

📤 **Output**: `[{name: "Alison Berry", age: 54}, ...]`
🎯 **Maqsad**: `sorted()` funksiyasi va `lambda`dan foydalanishni o‘rganish.

---

### **6. `get_usernames_starting_with(data, letter)`**

🔍 **Vazifa**: Login bo‘yicha `letter` harfi bilan boshlanuvchi username’larni toping.

📥 **Input**: `"g"`
📤 **Output**: `["goldenbutterfly464", "goldenzebra713", ...]`
🎯 **Maqsad**: String bilan ishlash + filtering skills.

---

### **7. `get_average_age(data)`**

🔍 **Vazifa**: Foydalanuvchilar orasidagi o‘rtacha yoshni hisoblang, natijani `float` qilib qaytaring.

📤 **Output**: `56.4`
🎯 **Maqsad**: Loop + matematik hisob-kitob.

---

### **8. `group_users_by_nationality(data)`**

🔍 **Vazifa**: Foydalanuvchilarni `nat` (nationality) bo‘yicha guruhlab, sonini hisoblang.

📤 **Output**: `{"NL": 3, "IN": 2, "IE": 2, ...}`
🎯 **Maqsad**: Dictionary bilan `grouping` va `counting`.

---

### **9. `get_all_coordinates(data)`**

🔍 **Vazifa**: Har bir userning koordinatalarini tuple shaklida ro‘yxatda qaytaring.

📤 **Output**: `[("36.7507", "-169.1103"), ...]`
🎯 **Maqsad**: Nested dictionarylardan qiymat olish.

---

### **10. `get_oldest_user(data)`**

🔍 **Vazifa**: Eng katta yoshdagi foydalanuvchining `name`, `age`, va `email`ini dictionaryda qaytaring.

📤 **Output**: `{"name": "Molly King", "age": 80, "email": "molly.king@example.com"}`
🎯 **Maqsad**: `max()` funksiyasini o‘rganish.

---

### 🧠 **BONUS — KREATIV TASKLAR**

---

### **11. `find_users_in_timezone(data, offset)`**

🔍 **Vazifa**: `"timezone.offset"` qiymati `+5:30` bo‘lgan userlarni full name va city bilan qaytaring.

📤 **Output**: `[{"name": "Gregory Reid", "city": "Clane"}, ...]`

---

### **12. `get_registered_before_year(data, year)`**

🔍 **Vazifa**: Belgilangan yildan avval ro‘yxatdan o‘tgan userlarni chiqaring.

📥 **Input**: `2010`
📤 **Output**: `[{"name": "Doeke Krikke", "registered": "2004-06-29"}, ...]`

---

