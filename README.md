## 🔹 1-DARAJA (Asosiy tushunchalarni mustahkamlash)

### 1. Foydali sonlarni ajratish

Berilgan ro'yxatdan musbat sonlarni `filter()` yordamida ajrating.

```python
numbers = [4, -2, 0, 7, -9, 3, -1, 5]
```

### 2. Har bir sonni kvadratga oshiring

`map()` yordamida quyidagi ro'yxatdagi har bir sonni kvadratga oshiring.

```python
nums = [1, 2, 3, 4, 5]
```

### 3. Eng kichik va eng katta

`min()` va `max()` yordamida quyidagi ro'yxatdan eng kichik va eng katta sonni toping.

```python
numbers = [18, 29, 3, 45, 7, 12]
```

### 4. Alfavit tartibida saralash

`sorted()` yordamida ismlarni alfavit tartibida saralang.

```python
names = ["Zafar", "Ali", "Sami", "Bekzod"]
```

### 5. `lambda` bilan ko'paytirish

Har bir elementni 5 ga ko'paytirish uchun `map()` va `lambda`dan foydalaning.

```python
nums = [2, 4, 6, 8]
```

---

## 🔹 2-DARAJA (Oraliq daraja, real hayotga yaqinlashtirish)

### 6. Email domenlarini ajratish

Quyidagi email ro’yxatidan faqat `gmail.com` domeniga tegishlilarni ajrating.

```python
emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
```

### 7. Narxlarni \$ belgisiz olish

Quyidagi narxlar ro’yxatidan `$` belgisiz faqat raqamlarni ajrating (lambda bilan).

```python
prices = ["$120", "$340", "$50", "$90"]
```

### 8. Yoshi bo'yicha sortlash

Quyidagi lug’atdagi odamlarni yosh bo’yicha o’sish tartibida saralang.

```python
people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]
```

### 9. Eng uzoq ismni toping

`max()` va `lambda` yordamida eng uzun ismni toping:

```python
names = ["Ali", "Valijon", "Sami", "Diyorbek"]
```

---

## 🔹 3-DARAJA (Chuqur tushunish, funksional yondashuv)

### 10. Matndan raqamlarni ajratish

Berilgan matndan faqat sonlarni ajrating:

```python
text = ["apple", "34", "banana", "100", "abc", "75"]
```

> Natija: `['34', '100', '75']`

### 11. Juft sonlarning kvadratlari

Faqat juft sonlarni tanlab, ularning kvadratlarini `filter()` + `map()` bilan hisoblang.

```python
nums = list(range(1, 21))
```

### 12. Talabalarni baho bo‘yicha tartiblang

Baholar bo‘yicha saralash (kichikdan katta):

```python
students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]
```

### 13. Top 3 eng uzun so‘z

Matndagi eng uzun 3 ta so‘zni toping:

```python
sentence = "Functional programming in Python is very powerful and elegant"
```

> Foydalaning: `sorted()`, `lambda`, `split()`, `[:3]`

### 14. list.sort bilan joyida o'zgartirish

Quyidagi ro’yxatni uzunlik bo‘yicha joyida sort qiling:

```python
words = ["sun", "mountain", "a", "apple"]
```

> `list.sort(key=lambda ...)` ishlatilishi kerak.

---

## 🔹 4-DARAJA (Chuqur tahlil va kompozitsiya)

### 15. Tanlovlar ro'yxatidan eng ko'p ovoz olganini topish

Har bir tanlovda necha ovoz borligini bilgan holda eng ko'p ovoz olgan variantni aniqlang.

```python
votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
```

> `max(..., key=lambda x: x["votes"])`

### 16. `lambda` bilan ro'yxatni qisqartirish

Berilgan ro’yxatdagi faqat string va uzunligi 5 dan katta bo‘lganlarni ajrating:

```python
data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
```

---


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

